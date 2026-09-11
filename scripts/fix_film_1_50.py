import json
from pathlib import Path
p=Path('Film.json')
data=json.loads(p.read_text(encoding='utf-8'))
assert len(data)>=50
for q in data[:50]:
    text=q.get('question','')
    a=q.get('answers',{})
    if text=="U kojoj seriji Borisa Dvornika poznamo kao Dimnjačara?" and a.get('C')=='Kapelski Kresovi':
        a['C']='Kapelski kresovi'
    if text=="Koji glumac glumi Sherlocka Holmesa u filmovima Guyja Ritchieja?" and a.get('C')=='Robert Downey Jr':
        a['C']='Robert Downey Jr.'
for i,q in enumerate(data[:50],1):
    assert set(q['answers'])=={'A','B','C'}, i
    assert q['correct_answer'] in {'A','B','C'}, i
    assert len(set(q['answers'].values()))==3, i
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('FILM 1-50 OK')
