# GPT-5.6 Education Pipeline Benchmark Suite v1

Status: approved for Phase A execution by [TEACHER] on 13 July 2026; eight frozen task fixtures authored and hashed  
Owner: Susan  
Date: 13 July 2026

## Decision this suite must support

Choose model/effort routes for materially different education-pipeline workloads. The suite must not produce one universal league table. It must identify the best quality/latency/cost trade-off for each lane:

1. high-volume drafting;
2. specialist planning;
3. scientific and curriculum audit;
4. assessment design;
5. resource transformation and consistency repair;
6. creative lesson ideation;
7. critical orchestration and final adjudication.

## Correction to interpretation of the first benchmark

The existing forced rank is quality-only. Rankers were explicitly told not to consider model cost, latency or token use. Averaging two ordinal ranks gives a rough comparative-quality ordering, not a value score. No value conclusion should be drawn until quality, severity-weighted errors, latency and cost are combined under a declared deployment policy.

The current lesson-design result places these conditions on the useful operational frontier:

- Sol/low: strong fast candidate generation;
- Sol/high: strongest practical quality-first default;
- Terra/xhigh: slower deep challenger;
- Luna/none: cheapest high-volume baseline;
- max routes: quality ceiling checks, not defaults.

OpenAI does not publish parameter counts for Sol, Terra and Luna in the available model guidance. Do not use assumed parameter count as evidence. Test disciplinary knowledge directly.

## Candidate configurations — Phase A

Run six conditions on every task:

- `gpt-5.6-sol / low`
- `gpt-5.6-sol / high`
- `gpt-5.6-terra / high`
- `gpt-5.6-terra / xhigh`
- `gpt-5.6-luna / none`
- `gpt-5.6-luna / high`

Rationale:

- Sol/low and Sol/high are the leading practical candidates from the first task.
- Terra/high tests the claimed workhorse lane; Terra/xhigh tests deep asynchronous review.
- Luna/none tests the economy lane; Luna/high tests whether extra Luna reasoning helps on tasks unlike the first benchmark.
- Exclude max from the broad screen because its latency is operationally unrealistic. Use max only as a ceiling condition on two selected high-stakes tasks after Phase A.

## Eight benchmark tasks

### T1 — Source-grounded unit sequence planning

Workload: unit-plan generation.

Self-contained input:

- a compact authoritative syllabus extract;
- class and room profile;
- timetable and assessment constraints;
- practical minimum and equipment limits.

Output:

- 8–10 lesson sequence;
- prerequisite chain;
- practical placement;
- formative-assessment cadence;
- explicit deferrals and risks.

Measures:

- curriculum fidelity;
- sequence coherence;
- realistic pacing;
- practical feasibility;
- ability to resolve competing constraints.

### T2 — Lesson pedagogical core

Workload: lesson architecture.

Use the corrected Year 8 Change task from the existing benchmark as the anchor case. Retain it unchanged so results remain comparable.

Measures:

- scientific precision;
- build–test–revise pedagogy;
- assessment validity;
- ADHD-supportive structure;
- operational feasibility;
- instruction following.

### T3 — Assessment architecture and moderation

Workload: formal assessment design.

Self-contained case:

- Year 8 depth-study portfolio;
- group practical plus individual evidence;
- absence and authenticity constraints;
- 30-mark ceiling;
- moderation and adjustment requirements.

Output:

- task architecture;
- construct-to-evidence map;
- marking allocation;
- checkpoints;
- absence/authenticity controls;
- blocking decisions.

Measures:

- construct validity;
- individual attribution;
- marking reliability;
- workload realism;
- fairness and moderation readiness.

### T4 — Scientific misconception and safety audit

Workload: adversarial review.

Provide a deliberately flawed Year 10 chemical-reactions lesson containing subtle and obvious errors, for example:

- indicators treated as proof;
- mass-conservation ambiguity;
- activation-energy misconception;
- unsafe or impractical method details;
- weak observation/inference separation.

Output:

- severity-ranked findings;
- exact correction;
- classroom consequence;
- acceptance test.

Measures:

- disciplinary knowledge not supplied in the candidate prompt;
- error detection recall and precision;
- causal explanation;
- safety judgement;
- resistance to false positives.

Authoritative answer key must be prepared from syllabus and scientific sources before generation.

### T5 — Stage 6 Biology knowledge and exam reasoning

Workload: HSC-level disciplinary explanation and assessment.

Self-contained case from Module 3 or 4 requiring:

- analysis of unfamiliar data;
- causal biological explanation;
- one extended-response item;
- marking criteria and common-error diagnosis.

Measures:

- advanced biological knowledge;
- data interpretation;
- command-verb alignment;
- marking discriminability;
- precision without overclaiming.

Use an authoritative hidden answer key. Do not rely on model memory for syllabus wording.

### T6 — Cross-document consistency repair

Workload: pipeline cross-check.

Input:

- approved lesson-plan extract as source of truth;
- worksheet extract;
- slide outline;
- deliberately planted mismatches in learning intention, success criteria, worked example, timing and exit ticket.

Output:

- structured mismatch ledger;
- resource-side repairs only;
- no unauthorised plan changes.

Measures:

- recall across documents;
- exactness;
- obedience to source-of-truth policy;
- false-positive rate;
- minimal repair quality.

This task should have a deterministic gold set and therefore needs little LLM judging.

### T7 — Student-resource transformation

Workload: resource creation and transformation.

Input:

- an approved lesson plan;
- precise content propositions;
- required student artifact;
- constraints against graveyard worksheets and answers in student materials.

Output:

- compact student worksheet specification or text artifact;
- separate teacher-answer transformation.

Measures:

- content fidelity;
- answer separation;
- build-don’t-fill quality;
- cognitive progression;
- implementability;
- transformation consistency.

### T8 — Creative lesson concepts and earned spectacle

Workload: divergent lesson ideation.

Use a frozen science brief with room, class and sequence constraints. Ask for three genuinely different central mechanisms, not polished full lessons.

Measures:

- originality of the scientific mechanism;
- conceptual payoff;
- memorability;
- feasibility;
- evidence application;
- resistance to gimmickry;
- proportion of ideas surviving human review.

Human blind review is essential for this task; a single forced rank is insufficient.

## Knowledge versus source use

The suite must separate two constructs:

1. **Source-grounded fidelity** — tasks T1, T2, T3, T6 and T7 provide the authoritative content needed. These test whether the model can use supplied sources reliably.
2. **Disciplinary knowledge and transfer** — tasks T4 and T5 withhold selected scientific answers from candidates but use an authoritative hidden answer key. These test whether a purportedly larger or more capable model actually knows and applies more science.

Do not infer knowledge from parameter count. Parameter count, active parameters, training mixture and retrieval-like memorisation are not published sufficiently to support that claim.

## Experimental design

### Phase A — breadth screen

- 8 tasks × 6 model/effort conditions = 48 generation seats.
- One frozen prompt per task.
- Equal-condition calls run concurrently where account quotas permit.
- Preserve requested and returned model, profile, route, latency, TTFT, token use and public-equivalent cost.
- Use deterministic grading wherever a gold set is possible.
- Use two blind judges for pedagogical and assessment quality.
- Do not force one 48-output global rank. Rank within each task only.

### Phase B — variance check

Select the best three operational conditions after Phase A and repeat every task once:

- expected candidates: Sol/low, Sol/high and the best economy/challenger route;
- 8 tasks × 3 conditions = 24 additional generation seats;
- use a new deterministic seed or fresh backend sample without changing prompts;
- compare error rates and rank stability, not only means.

### Optional ceiling check

Run Sol/max, Terra/max and Luna/max only on T3 and T5 if Phase A shows that a material quality gain could justify the latency.

## Scoring model

### Independent judge panel

Use model-family diversity rather than two GPT-5.6 judges as the final authority:

- Claude Opus 4.8 through a pinned model slug as the primary independent pedagogical/assessment judge;
- GPT-5.6 Sol/high as a second blind judge;
- one non-OpenAI/non-Anthropic route such as a strong DeepSeek or Qwen model as an adversarial third judge where available;
- deterministic validators and authoritative answer keys override judge preference on factual compliance;
- [TEACHER]/Susan adjudicate high-stakes disagreements.

Do not use an unversioned `opus-latest` alias in a reproducible benchmark. Preserve judge model, provider, prompt hash, candidate order and returned usage. Opus should supplement rather than replace deterministic grading and human moderation.

Aggregate three ordinal rankings through pairwise majority wins or a clearly labelled Borda/Copeland table, and publish judge disagreement. Do not present the arithmetic mean of ranks as a cardinal value score.

Current route status:

- Claude Opus 4.8 is verified through Susan's direct Anthropic provider credential pool (`provider=anthropic`, returned model `claude-opus-4-8`). Do not route it through OpenRouter.
- GLM-5.2 is verified directly through LlamaHerd.
- Grok 4.5 is verified directly through Susan's xAI OAuth Responses route.

Use Opus + Sol/high + GLM-5.2 + Grok 4.5 for diverse blind review where the stakes justify four model families, with deterministic gold checks and human adjudication.

Do not collapse results immediately into one rank.

For each condition and task report:

1. deterministic compliance pass/fail;
2. critical scientific or curriculum errors;
3. blind rubric score;
4. blind comparative rank within that task;
5. human survival/approval decision;
6. latency and TTFT;
7. input, output and reasoning tokens;
8. public-equivalent cost;
9. actual route charge, or `N/A` if absent.

### Severity-weighted quality score

Use a 0–100 task rubric, then apply explicit penalties:

- critical factual/safety/curriculum error: task score capped at 50;
- major validity or source-of-truth violation: cap at 70;
- missing required individual assessment or output: cap at 80;
- deterministic formatting/length failure: fixed small penalty, not an evaluator impression.

### Value views — report several, not one

- **Quality-first:** highest severity-weighted quality subject to acceptable latency.
- **Fast-production:** highest quality under a 60-second wall-time ceiling.
- **Economy:** highest quality under a declared cost ceiling.
- **Pareto frontier:** conditions not dominated simultaneously on quality, latency and cost.
- **Human-adjusted:** approved artifacts per dollar and per minute of teacher repair.

The production decision should privilege teacher repair time and critical-error avoidance over token cost. A ten-cent model call is cheap if it prevents five minutes of teacher correction.

## Expected decision policy

The current provisional hypothesis to test is:

- Sol/high for high-consequence planning, assessment and final synthesis;
- Sol/low for most routine lesson/resource generation and rapid alternatives;
- Luna/none for genuinely high-volume, low-stakes transformations;
- Terra/xhigh for asynchronous adversarial challenge if it remains model-diverse and competitive;
- deterministic code for consistency and compliance checks;
- max only when a repeated, high-stakes gain is measured.

## Estimated scale

Using the first task’s returned token usage as a rough proxy:

- Phase A generation: about $2.62 public-list equivalent;
- Phase B generation: about $1.29 if Sol/low, Sol/high and Luna/none advance;
- blind evaluation and ranking: roughly $5.19 by proportional extrapolation;
- rough combined estimate: about $9.09 public-list equivalent.

This is not the actual OAuth charge. The route currently reports no monetary charge, so actual charge remains `N/A`. Longer source-grounded tasks may materially increase token use.

## Approval gate before execution

Before running the suite, Susan will provide:

- eight frozen candidate prompts;
- eight hidden rubrics/answer keys;
- deterministic validators;
- exact candidate matrix;
- estimated maximum call count and latency;
- source and prompt hashes.

[TEACHER] approves the suite once, then execution proceeds without changing prompts mid-run.
