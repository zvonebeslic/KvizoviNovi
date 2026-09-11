import json
from pathlib import Path
from collections import Counter

p=Path('Film.json')
data=json.loads(p.read_text(encoding='utf-8'))
assert len(data) >= 100

# Q56: odgovori gramatički odgovaraju pitanju "u kojoj trilogiji"
q=data[55]
assert q['question']=="U kojoj trilogiji je hobbit Bilbo Baggins, glavni lik?"
q['answers']={
    'A':'Gospodaru prstenova',
    'B':'Hobitu',
    'C':'Kronikama iz Narnije'
}
q['correct_answer']='B'

# Q57: standardizacija zapisa imena
q=data[56]
assert q['question']=="Koji glumac glumi Sherlocka Holmesa u filmovima Guyja Ritchieja?"
q['answers']={
    'A':'Benedict Cumberbatch',
    'B':'Jude Law',
    'C':'Robert Downey Jr.'
}
q['correct_answer']='C'

# Q91: usporedivi naslovi domaćih serija
q=data[90]
assert q['question']=="U kojoj seriji susrećemo Pučanstvo, policajca i trgovca sličica sa svecima?"
q['answers']={
    'A':'Velo misto',
    'B':'Naše malo misto',
    'C':'Prosjaci i sinovi'
}
q['correct_answer']='A'

chunk=data[50:100]
assert len(chunk)==50
assert all(set(x['answers'])=={'A','B','C'} for x in chunk)
assert all(x['correct_answer'] in x['answers'] for x in chunk)
assert all(len(set(x['answers'].values()))==3 for x in chunk)
print('Film 51-100 OK', Counter(x['correct_answer'] for x in chunk))

p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
