import json
from pathlib import Path
from collections import Counter
p=Path('Film.json'); data=json.loads(p.read_text(encoding='utf-8'))
assert len(data)==177
# Q172: točan odgovor je hrvatski naslov, pa i oba distraktora moraju biti na hrvatskom.
q=data[171]
assert q['question']=="U kojem filmu iz 2001. igraju George Clooney i Brad Pitt kao pljačkaši kockarnica?"
assert q['correct_answer']=='A'
q['answers']={'A':'Oceanovih 11','B':'Oceanovih 12','C':'Talijanski posao'}
chunk=data[150:]
assert len(chunk)==27
assert all(set(q['answers'])=={'A','B','C'} for q in chunk)
assert all(q['correct_answer'] in q['answers'] for q in chunk)
assert all(len(set(q['answers'].values()))==3 for q in chunk)
print('Film 151-177 OK',Counter(q['correct_answer'] for q in chunk))
print('TOTAL',len(data),Counter(q['correct_answer'] for q in data))
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
