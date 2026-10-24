#!/usr/bin/env python3
"""Read a specific GEO task by ID from the bundled reference. Offline stdlib only."""
import argparse, pathlib, re
p=argparse.ArgumentParser(description='Show one of the 78 GEO course tasks')
p.add_argument('task_id',help='e.g. 00-01 or 05-07')
a=p.parse_args()
file=pathlib.Path(__file__).resolve().parent.parent/'references'/'curriculum-78.md'
s=file.read_text(encoding='utf-8')
pat=re.compile(r'^#### (?P<id>\d{2}-\d{2})\s*·[^\n]*',re.M)
marks=list(pat.finditer(s))
for i,m in enumerate(marks):
    if m.group('id')==a.task_id:
        print(s[m.start():marks[i+1].start() if i+1<len(marks) else s.find('### ',m.end()) if s.find('### ',m.end())>=0 else len(s)].rstrip())
        break
else:
    p.error('Not found; use IDs in references/curriculum-78.md')
