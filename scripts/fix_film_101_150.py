import json
from pathlib import Path
from collections import Counter
p=Path('Film.json'); data=json.loads(p.read_text(encoding='utf-8'))
assert len(data)>=150
fixes={
127:{'A':'Robert Downey Jr.','B':'Johnny Depp','C':'Adrien Brody'},
}
for idx,answers in fixes.items():
    q=data[idx-1]
    old_correct=q['answers'][q['correct_answer']]
    q['answers']=answers
    assert q['answers'][q['correct_answer']].rstrip('.')==old_correct.rstrip('.')
chunk=data[100:150]
assert len(chunk)==50
assert all(set(q['answers'])=={'A','B','C'} for q in chunk)
assert all(q['correct_answer'] in q['answers'] for q in chunk)
assert all(len(set(q['answers'].values()))==3 for q in chunk)
print('Film 101-150 OK',Counter(q['correct_answer'] for q in chunk))
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
