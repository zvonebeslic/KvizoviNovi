import json
from pathlib import Path
p=Path('Film.json')
data=json.loads(p.read_text(encoding='utf-8'))
fixes={
"Kako se zove robot pratitelj Lukea Skywalkera?": {"A":"K-2SO","B":"BB-8","C":"R2-D2"},
"U kojem filmu Bill Murray proživljava isti dan iznova?": {"A":"Izgubljeni u prijevodu","B":"Istjerivači duhova","C":"Beskrajni dan"},
"Radnja kojeg filma se odvija na fiktivnom mjesecu Pandora u zvjezdanom sustavu Alpha Centauri?": {"A":"Dune","B":"Interstellar","C":"Avatar"},
"Kako se zove medvjed u filmu 'Knjiga o džungli'?": {"A":"Kenai","B":"Baloo","C":"Koda"},
"Kako se zove kći Morticije i Gomeza Addams iz filma 'Obitelji Addams' (The Addams Family)?": {"A":"Debbie","B":"Ophelia","C":"Wednesday"},
"Koji glumac igra ulogu tiranina Immortan Joea u filmu 'Pobješnjeli Max: Divlja cesta' (Mad Max: Fury Road)?": {"A":"Tom Hardy","B":"Nicholas Hoult","C":"Hugh Keays-Byrne"},
"Mladog Potrku je glumio Stjepan Puljić. Tko je glumio odraslog Matana?": {"A":"Rade Šerbedžija","B":"Boris Dvornik","C":"Fabijan Šovagović"}
}
seen=set()
for q in data:
    if q.get('question') in fixes:
        q['answers']=fixes[q['question']]
        seen.add(q['question'])
missing=set(fixes)-seen
if missing: raise SystemExit('Missing: '+repr(sorted(missing)))
assert all(set(q['answers'])=={'A','B','C'} and q['correct_answer'] in {'A','B','C'} for q in data)
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed',len(seen),'total',len(data))
