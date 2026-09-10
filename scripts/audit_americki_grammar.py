import json,re
from pathlib import Path
p='AmerickiPredsjednici.json'
data=json.load(open(p,encoding='utf-8'))
patterns=re.compile(r'\b(kojeg|kojem|koga|čijeg|u kojem|na kojem|na kojoj|u kojoj|od kojeg|za kojeg|s kojim|sa kojim|koju|koje|kakvom|kakvoj)\b',re.I)
out=[]
for i,x in enumerate(data,1):
    q=x.get('question','')
    if patterns.search(q):
        out.append({'index':i,'question':q,'answers':x.get('answers'),'correct_answer':x.get('correct_answer')})
Path('AMERICKI_GRAMMAR_AUDIT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('candidates',len(out))