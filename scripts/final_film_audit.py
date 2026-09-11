import json
from pathlib import Path
from collections import Counter
p=Path('Film.json')
data=json.loads(p.read_text(encoding='utf-8'))
assert len(data)==177, len(data)
errors=[]
for i,q in enumerate(data,1):
    if set(q.get('answers',{})) != {'A','B','C'}: errors.append((i,'ABC'))
    if q.get('correct_answer') not in {'A','B','C'}: errors.append((i,'correct'))
    if len(set(q.get('answers',{}).values())) != 3: errors.append((i,'duplicate answers'))
# Targeted language/grammar corrections found in the final human review.
# Do not alter question text or the identity of the correct answer.
fixes={
3:{'A':'Maraisu','B':'Latinskoj četvrti','C':'Montmartreu'},
}
for idx,ans in fixes.items():
    q=data[idx-1]
    old=q['answers'][q['correct_answer']]
    q['answers']=ans
    assert q['answers'][q['correct_answer']]==old
# final structural pass
for i,q in enumerate(data,1):
    assert set(q['answers'])=={'A','B','C'}
    assert q['correct_answer'] in q['answers']
    assert len(set(q['answers'].values()))==3
print('questions',len(data),'distribution',Counter(q['correct_answer'] for q in data),'initial_errors',errors,'fixes',list(fixes))
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
