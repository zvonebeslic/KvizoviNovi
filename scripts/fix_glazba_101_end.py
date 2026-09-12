import json
from pathlib import Path
p=Path('Glazba.json'); d=json.loads(p.read_text(encoding='utf-8'))
# Q108: svi odgovori skladateljice, originalni točan odgovor ostaje Dora Pejačević.
q=d[107]
assert q['correct_answer']=='C' and q['answers']['C']=='Dora Pejačević'
q['answers']={'A':'Ivana Lang','B':'Skladana Atanasijević','C':'Dora Pejačević'}
# Q115: originalni odgovor Miley ostaje. Noah i Brandi su također kćeri Billyja Raya,
# pa ih mijenjamo jednoznačnim lažnim odgovorima.
q=d[114]
assert q['correct_answer']=='A' and q['answers']['A']=='Miley Cyrus'
q['answers']={'A':'Miley Cyrus','B':'Selena Gomez','C':'Demi Lovato'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('final fixed Q108 Q115')
