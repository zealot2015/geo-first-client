#!/usr/bin/env python3
"""Check shipped skill directory, task count, CSV headers and safety links. Offline."""
from pathlib import Path
import csv,json,re,sys
skill=Path(__file__).resolve().parent.parent
errors=[]
f=skill/'SKILL.md'
if not f.exists():errors.append('missing SKILL.md')
else:
    s=f.read_text(encoding='utf-8')
    if not s.startswith('---\n') or '\n---\n' not in s[4:]:errors.append('invalid YAML frontmatter delimiters')
    for key in ('name: geo-first-client','description:','description_zh:','description_en:','version:'):
        if key not in s:errors.append('missing '+key)
    for link in re.findall(r'\]\(([^)]+)\)',s):
        if not link.startswith('https://') and not (skill/link).exists():errors.append('missing referenced file '+link)
ref=skill/'references'/'curriculum-78.md'
if not ref.exists():errors.append('missing curriculum')
else:
    ids=re.findall(r'^####\s*(\d{2}-\d{2})\s*[·-]',ref.read_text(encoding='utf-8'),re.M)
    if len(ids)!=78 or len(set(ids))!=78: errors.append('expected 78 unique tasks, got '+str(len(ids)))
csvs=list((skill/'assets'/'templates').glob('*.csv'))
if len(csvs)!=13:errors.append(f'expected 13 CSV templates, got {len(csvs)}')
for p in csvs:
    with p.open(encoding='utf-8-sig',newline='') as f:
        if len(next(csv.reader(f),[]))<3:errors.append(f'CSV template missing header columns: {p.name}')
if errors:
    for err in errors:print('ERROR:',err,file=sys.stderr)
    sys.exit(1)
print(f'OK: skill={skill.name}, 78 unique tasks, 13 CSV templates, linked references found')
