#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
R=Path(__file__).resolve().parent.parent
f=json.loads((R/'data/full-generation-results.json').read_text());j=json.loads((R/'data/full-judge-results.json').read_text());b=json.loads((R/'data/phase-b-generation-results.json').read_text());bj=json.loads((R/'data/phase-b-judge-results.json').read_text())
assert (f['successful'],f['total'])==(141,144)
assert (j['successful'],j['total'])==(32,32)
assert (b['successful'],b['total'])==(24,24)
assert (bj['successful'],bj['total'])==(32,32)
pat=re.compile(r'(sk-[A-Za-z0-9_-]{12,}|access_token|refresh_token|/home/ben|benkamholtz@gmail|ben@whetstone|100\.(?:64|69|123)\.)',re.I)
hits=[]
for p in R.rglob('*'):
 if p.is_file() and '.git' not in p.parts and p.name!='verify_dataset.py':
  try:
   if pat.search(p.read_text()):hits.append(str(p.relative_to(R)))
  except UnicodeDecodeError:pass
assert not hits,hits
print('PASS: counts verified; sensitive-pattern scan clean')
