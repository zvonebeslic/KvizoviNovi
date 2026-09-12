import json, collections
from pathlib import Path
p=Path('Glazba.json')
d=json.loads(p.read_text(encoding='utf-8'))
assert len(d)==133, f'Expected 133, got {len(d)}'
issues=[]
counts=collections.Counter()
seen_q={}
for i,q in enumerate(d,1):
    if q.get('question') in seen_q:
        issues.append(f'DUPLICATE QUESTION {seen_q[q["question"]]} & {i}')
    else:
        seen_q[q.get('question')]=i
    a=q.get('answers',{})
    if set(a.keys())!={'A','B','C'}: issues.append(f'{i}: bad answer keys {list(a)}')
    if len(set(a.values()))!=3: issues.append(f'{i}: duplicate answer text')
    c=q.get('correct_answer')
    if c not in ('A','B','C'): issues.append(f'{i}: invalid correct_answer {c}')
    else: counts[c]+=1
    if not q.get('question','').strip(): issues.append(f'{i}: empty question')
    if any(not str(v).strip() for v in a.values()): issues.append(f'{i}: empty answer')
    if q.get('topic')!='Glazba': issues.append(f'{i}: topic={q.get("topic")}')
report={
 'total':len(d),
 'correct_distribution':dict(counts),
 'difference_max_min':max(counts.values())-min(counts.values()),
 'issues':issues
}
Path('GLAZBA_FINAL_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if any(x for x in issues if not x.startswith('DUPLICATE QUESTION')):
    raise SystemExit(1)
