import json
from pathlib import Path

p=Path('Film.json')
data=json.loads(p.read_text(encoding='utf-8'))
assert len(data) >= 100

# Q57: standardizacija zapisa imena
q=data[56]
assert q['question']=="Koji glumac glumi Sherlocka Holmesa u filmovima Guyja Ritchieja?"
assert q['correct_answer']=='C'
q['answers']={
    'A':'Benedict Cumberbatch',
    'B':'Jude Law',
    'C':'Robert Downey Jr.'
}

# Q91: sva tri odgovora neka budu stvarni, usporedivi naslovi domaćih serija
q=data[90]
assert q['question']=="U kojoj seriji susrećemo Pučanstvo, policajca i trgovca sličica sa svecima?"
assert q['correct_answer']=='A'
q['answers']={
    'A':'Velo misto',
    'B':'Naše malo misto',
    'C':'Prosjaci i sinovi'
}

# Strukturna provjera baš paketa 51-100
chunk=data[50:100]
assert len(chunk)==50
assert all(set(x['answers'])=={'A','B','C'} for x in chunk)
assert all(x['correct_answer'] in x['answers'] for x in chunk)
assert all(len(set(x['answers'].values()))==3 for x in chunk)

from collections import Counter
counts=Counter(x['correct_answer'] for x in chunk)
print('Film 51-100 OK', counts)

p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
