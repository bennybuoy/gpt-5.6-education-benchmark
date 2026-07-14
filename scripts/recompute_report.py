#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import csv,io,json,statistics
ROOT=Path(__file__).resolve().parent.parent
DATA=ROOT/'data'
EFF=['none','low','medium','high','xhigh','max']; MODELS=['gpt-5.6-sol','gpt-5.6-terra','gpt-5.6-luna']; CONDS=[(m,e) for m in MODELS for e in EFF]
LABEL=lambda c:f"{c[0].removeprefix('gpt-5.6-').title()}/{c[1]}"
tasks={p.stem:json.loads(p.read_text()) for p in (ROOT/'tasks').glob('T*.json')}

def load_phase(prefix):
 gen=json.loads((DATA/f'{prefix}-generation-results.json').read_text()); jud=json.loads((DATA/f'{prefix}-judge-results.json').read_text()); ids=json.loads((DATA/f'{prefix}-identity-key.json').read_text())
 grows={(r['task_id'],r['model_requested'],r['effort']):r for r in gen['results']}
 jr={}
 for call in jud['calls']:
  if call.get('status')!='completed' or not call.get('parsed'):continue
  tid=call['task_id']; judge=call['judge']; scores={x['candidate']:float(x.get('capped_score',x.get('raw_score',0))) for x in call['parsed']['scores']}; ranks={x['candidate']:int(x['rank']) for x in call['parsed']['ranking']}
  for cid,ident in ids[tid].items():
   if cid in scores and cid in ranks:jr[(tid,ident['model'],ident['effort'],judge)]={'score':scores[cid],'rank':ranks[cid]}
 return gen,jud,grows,jr

def majority_task(tid,conditions,jr,failures_as_losses=False):
 judges=sorted({k[3] for k in jr if k[0]==tid}); points={c:0.0 for c in conditions}; details={c:[0,0,0] for c in conditions}
 for i,a in enumerate(conditions):
  for b in conditions[i+1:]:
   av=[]
   for j in judges:
    ka=(tid,*a,j);kb=(tid,*b,j)
    if ka in jr and kb in jr: av.append((jr[ka]['rank'],jr[kb]['rank']))
   if av:
    aw=sum(x<y for x,y in av);bw=sum(y<x for x,y in av)
    if aw>bw:points[a]+=1;details[a][0]+=1;details[b][1]+=1
    elif bw>aw:points[b]+=1;details[b][0]+=1;details[a][1]+=1
    else:points[a]+=.5;points[b]+=.5;details[a][2]+=1;details[b][2]+=1
   elif failures_as_losses:
    aok=any((tid,*a,j) in jr for j in judges);bok=any((tid,*b,j) in jr for j in judges)
    if aok and not bok:points[a]+=1;details[a][0]+=1;details[b][1]+=1
    elif bok and not aok:points[b]+=1;details[b][0]+=1;details[a][1]+=1
    else:points[a]+=.5;points[b]+=.5;details[a][2]+=1;details[b][2]+=1
 return points,details

def summarise(prefix,conditions,include_failures=False):
 gen,jud,grows,jr=load_phase(prefix); agg={c:defaultdict(list) for c in conditions}; task_tables={}
 for tid in sorted(tasks):
  pts,det=majority_task(tid,conditions,jr,include_failures); rows=[]
  for c in conditions:
   g=grows.get((tid,*c)); vals=[v for k,v in jr.items() if k[:3]==(tid,*c)]; ranks=[v['rank'] for v in vals];scores=[v['score'] for v in vals]; n=max([v['rank'] for k,v in jr.items() if k[0]==tid] or [len(conditions)])
   success=bool(g and g.get('status')=='completed'); checks=(g or {}).get('deterministic_checks') or []; passrate=(sum(bool(x.get('pass')) for x in checks)/len(checks)*100) if checks else None
   row={'condition':c,'success':success,'score':statistics.mean(scores) if scores else None,'ranks':ranks,'points':pts[c],'wlt':det[c],'latency':g.get('elapsed_seconds') if success else None,'cost':g.get('public_api_equivalent_usd_uncached') if success else None,'tokens':g.get('output_tokens') if success else None,'check':passrate}
   rows.append(row);agg[c]['task_points'].append(pts[c]/(len(conditions)-1)*100);agg[c]['success'].append(success)
   if scores:agg[c]['scores'].extend(scores)
   if ranks:
    agg[c]['normranks'].extend([(n-r)/(n-1)*100 if n>1 else 100 for r in ranks]);agg[c]['spreads'].append(max(ranks)-min(ranks))
   if success:agg[c]['latency'].append(g['elapsed_seconds']);agg[c]['cost'].append(g.get('public_api_equivalent_usd_uncached') or 0);agg[c]['tokens'].append(g.get('output_tokens') or 0)
   if passrate is not None:agg[c]['checks'].append(passrate)
  rows.sort(key=lambda r:(-r['points'],-(r['score'] if r['score'] is not None else -1),LABEL(r['condition'])));task_tables[tid]=rows
 overall=[]
 for c,a in agg.items():
  overall.append({'condition':c,'pairwise':statistics.mean(a['task_points']),'score':statistics.mean(a['scores']) if a['scores'] else None,'rankpct':statistics.mean(a['normranks']) if a['normranks'] else None,'success':sum(a['success']),'latency':statistics.median(a['latency']) if a['latency'] else None,'cost':sum(a['cost']),'tokens':statistics.mean(a['tokens']) if a['tokens'] else None,'spread':statistics.mean(a['spreads']) if a['spreads'] else None,'check':statistics.mean(a['checks']) if a['checks'] else None,'firsts':sum(rows[0]['condition']==c for rows in task_tables.values())})
 overall.sort(key=lambda r:(-r['pairwise'],-r['success'],-(r['score'] or 0),r['latency'] or 1e9));return gen,jud,overall,task_tables

FG,FJ,overall,tables=summarise('full',CONDS,True)
BCONDS=[('gpt-5.6-sol','low'),('gpt-5.6-sol','high'),('gpt-5.6-terra','xhigh')];BG,BJ,bover,btables=summarise('phase-b',BCONDS,False)
# Pareto on pairwise quality (higher), latency/cost (lower), requiring 8/8 success.
valid=[r for r in overall if r['success']==8]
pareto=[]
for r in valid:
 if not any((q['pairwise']>=r['pairwise'] and q['latency']<=r['latency'] and q['cost']<=r['cost'] and (q['pairwise']>r['pairwise'] or q['latency']<r['latency'] or q['cost']<r['cost'])) for q in valid):pareto.append(r['condition'])
lines=['# GPT-5.6 Education Benchmark — Final Eight-Task Report','',f"Full first-pass matrix: **{FG['successful']}/144 artifacts produced**. Phase B repeats: **{BG['successful']}/24**. Full blind judgements: **{FJ['successful']}/32**; Phase B: **{BJ['successful']}/32**.",'',f"Generation public-list equivalent: **${FG['public_equivalent_usd']:.5f}** first pass + **${BG['public_equivalent_usd']:.5f}** Phase B = **${FG['public_equivalent_usd']+BG['public_equivalent_usd']:.5f}**. Actual Codex OAuth charge: N/A.",'','## Bottom line','', 'The only route that remained strong across all three views was **Sol/high**: it led the original six-condition screen, led those same six outputs when re-ranked inside the full matrix, and led the Phase B repeat. The rest of the ordering was unstable enough that this benchmark does **not** justify permanent default-route changes without a human pilot. Luna/xhigh led the 18-condition first pass, but it was not repeated and had a 269-second median latency. `max` is not operationally viable: all three model families failed to return a T8/max artifact after repeated 15-minute streams.','', '## Overall first-pass ordering','', '| Order | Condition | Pairwise quality | Mean judge score | Success | Task firsts | Median latency | Total cost | Mean output tokens | Judge rank spread | Deterministic checks |','|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
for i,r in enumerate(overall,1):
 check_text=f"{r['check']:.1f}%" if r['check'] is not None else 'N/A'
 lines.append(f"| {i} | {LABEL(r['condition'])} | {r['pairwise']:.1f} | {r['score']:.2f} | {r['success']}/8 | {r['firsts']} | {r['latency']:.1f}s | ${r['cost']:.5f} | {r['tokens']:.0f} | {r['spread']:.2f} | {check_text} |")
lines += ['','Pairwise quality is the mean task-level Copeland share: each condition receives one point for a pairwise-majority win and half for a tie, then is normalised within each task. It is ordinal, not a cardinal quality percentage. Missing T8/max artifacts lose to produced artifacts and tie one another.','', 'Pareto frontier among routes with 8/8 successful artifacts: **'+', '.join(LABEL(c) for c in pareto)+'**.','', '## Phase B repeat — finalists','', '| Condition | Repeat pairwise quality | Repeat score | Repeat task firsts | Median latency | Repeat cost |','|---|---:|---:|---:|---:|---:|']
for r in bover:lines.append(f"| {LABEL(r['condition'])} | {r['pairwise']:.1f} | {r['score']:.2f} | {r['firsts']} | {r['latency']:.1f}s | ${r['cost']:.5f} |")
lines += ['','Phase B is a fresh second sample of the three Phase A finalists. Its role is variance checking, not replacing the broader 18-condition comparison.','','## Ranking stability warning','','The ranking changed materially when the same six Phase A artifacts were judged beside twelve additional candidates. Original six-condition order: **Sol/high, Sol/low, Terra/xhigh, Terra/high, Luna/high, Luna/none**. Full-panel ranks restricted back to those same six artifacts: **Sol/high, Luna/none, Luna/high, Terra/xhigh, Sol/low, Terra/high**. This is a candidate-set/judge-context effect, not generation variance. Therefore the full-matrix Copeland table is evidence, not a sufficiently stable deployment oracle.','','Phase B again ranked **Sol/high, Sol/low, Terra/xhigh**. Sol/high is the only condition robustly first across the original screen, the restricted full-panel comparison and the repeat.','', '## Task-level results']
judge_order=['claude-opus-4.8','gpt-5.6-sol','glm-5.2','grok-4.5']
_,_,_,fulljr=load_phase('full')
for tid in sorted(tasks):
 lines += ['',f"### {tid} — {tasks[tid]['title']}",'', '| Order | Condition | Score | Judge ranks | Pairwise W–L–T | Latency | Cost |','|---:|---|---:|---|---:|---:|---:|']
 for i,r in enumerate(tables[tid],1):
  c=r['condition']; rankmap={j:next((v['rank'] for k,v in fulljr.items() if k==(tid,*c,j)),None) for j in judge_order}; rs=' / '.join(str(rankmap[j]) if rankmap[j] is not None else '—' for j in judge_order);score=f"{r['score']:.2f}" if r['score'] is not None else 'N/A';lat=f"{r['latency']:.1f}s" if r['latency'] is not None else 'TIMEOUT';cost=f"${r['cost']:.5f}" if r['cost'] is not None else 'N/A';w,l,t=r['wlt'];lines.append(f"| {i} | {LABEL(c)} | {score} | {rs} | {w}–{l}–{t} | {lat} | {cost} |")
lines += ['','Judge-rank order: Opus / Sol / GLM / Grok. For T1 and T4, GLM scored each candidate independently and the rank was derived from those scores because its all-18 prompt repeatedly exhausted the response budget. Other GLM tasks used joint within-task ranking.','','## Routing decision','','- **High-consequence planning, assessment, scientific synthesis and final review:** **Sol/high** is the defensible default. It was the only route robustly first across all three comparison views.','- **Routine production:** keep **Sol/low** as a provisional fast route, not a settled winner. It placed second in the original screen and repeat but fell sharply when judged in the 18-candidate context. Validate it against a small set of real Susan/Marie jobs before changing defaults.','- **Economy experiment:** **Luna/none** is extremely fast and cheap and scored well in the full-panel context, but it was last in the original six-condition screen. Treat it as a candidate for a targeted repeat, not an approved bulk route.','- **Ceiling experiment:** **Luna/xhigh** led the full first pass but took a 269-second median and received no repeat sample. It needs a direct repeat against Sol/high before any routing change.','- **Asynchronous challenger:** Terra/xhigh did not survive the repeat strongly enough to justify broad default use. Retain it only where task-specific evidence shows an advantage.','- **Exact consistency and compliance:** prefer deterministic code; more reasoning was not reliably better for source-of-truth repair.','- **Max effort:** reject operationally. It was extremely slow and all three families failed to return the T8 artifact.','','## Important limitations','','- No human blind survival/approval decisions were collected. Model-judge scores are proxies, not measured teacher repair minutes.','- Deterministic checks were implemented only where fixtures supplied machine-readable checks; `N/A` does not mean compliant.','- T1 and T4 GLM rankings were derived from 18 independent candidate scores rather than one joint ranking; this reduces prompt-size failure but changes the comparison method.','- Public-list costs omit unreported token use from failed streams and are comparative only; Codex OAuth reported no actual route charge.','- One first-pass sample per condition is noisy. Only the three finalists received a fresh Phase B sample.','- Forced within-task rank measures relative preference, not absolute classroom readiness.','', '## Reproducibility artifacts','','- `full-generation-results.json` — 144-seat generation manifest, including three recorded failures','- `full-identity-key.json` and `full-blind-pack.json` — anonymisation artifacts','- `full-judge-results.json` — raw four-family judge calls','- `phase-b-generation-results.json` and `phase-b-judge-results.json` — fresh finalist repeats','- `FINAL-SUMMARY.csv` — machine-readable overall table']
(ROOT/'FINAL-REPORT.md').write_text('\n'.join(lines)+'\n')
buf=io.StringIO();w=csv.DictWriter(buf,fieldnames=['order','condition','pairwise_quality','mean_score','success_tasks','task_firsts','median_latency_s','total_cost_usd','mean_output_tokens','judge_rank_spread','deterministic_check_pct','pareto']);w.writeheader()
for i,r in enumerate(overall,1):w.writerow({'order':i,'condition':LABEL(r['condition']),'pairwise_quality':round(r['pairwise'],3),'mean_score':round(r['score'],3),'success_tasks':r['success'],'task_firsts':r['firsts'],'median_latency_s':round(r['latency'],3),'total_cost_usd':round(r['cost'],6),'mean_output_tokens':round(r['tokens'],1),'judge_rank_spread':round(r['spread'],3),'deterministic_check_pct':round(r['check'],2) if r['check'] is not None else '','pareto':r['condition'] in pareto})
(ROOT/'FINAL-SUMMARY.csv').write_text(buf.getvalue());print(json.dumps({'report':str(ROOT/'FINAL-REPORT.md'),'summary':str(ROOT/'FINAL-SUMMARY.csv'),'top5':[LABEL(r['condition']) for r in overall[:5]],'phase_b':[LABEL(r['condition']) for r in bover],'pareto':[LABEL(c) for c in pareto]},indent=2))
