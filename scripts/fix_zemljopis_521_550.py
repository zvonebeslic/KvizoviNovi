import json
from pathlib import Path
p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))
anchor='U kojoj je državi službeno sredstvo plaćanja valuta Paanga?'
starts=[i for i,q in enumerate(d) if q.get('question')==anchor]
assert len(starts)==1,starts
start=starts[0]
wrong=[
['Fidžiju','Samoau'],
['Švedska','Norveška'],
['Belfast','Edinburgh'],
['Montana','Idaho'],
['Prešov','Žilina'],
['Sardinija','Sicilija'],
['Kingstown','Georgetown'],
['Phnom Penh','Hanoi'],
['Veksilologija','Sfragistika'],
['Grčke','Sjeverne Makedonije'],
['Sveti Toma i Princip','Komori'],
['Kingstown','Castries'],
['Kazbek','Dykh-Tau'],
['Okavango','Kunene'],
['Austriji','Njemačkoj'],
['Finski zaljev','Riški zaljev'],
['Aralsko jezero','Issyk-Kul'],
['Crno More','Crveno More'],
['Lima','Bogota'],
['Uzbekistana','Tadžikistana'],
['Melaneziju','Mikroneziju'],
['Sofija','Tirana'],
['Vientiane','Yangon'],
['Ostrobotnija','Kainuu'],
['Maleziji','Filipinima'],
['Annobón','Corisco'],
['Doha','Manama'],
['Planina Oku','Planina Manengouba'],
['Katar','Kuvajt'],
['Siriji','Jordanu']
]
assert len(wrong)==30
for off,pair in enumerate(wrong):
    q=d[start+off]
    key=q['correct_answer']
    correct=q['answers'][key]
    assert correct not in pair,(521+off,q['question'],correct,pair)
    it=iter(pair)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed 30 questions 521-550')