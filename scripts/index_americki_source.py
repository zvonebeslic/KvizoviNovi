import json, urllib.request
from pathlib import Path

url='https://raw.githubusercontent.com/zvonebeslic/balkanska_pub_prica/main/AmerickiPredsjednici.json'
with urllib.request.urlopen(url, timeout=60) as r:
    src=json.loads(r.read().decode('utf-8'))
rows=[]
for i,q in enumerate(src,1):
    answers=q.get('answers') or []
    first=answers[0] if isinstance(answers,list) and answers else ''
    rows.append({'index':i,'question':q.get('question',''),'correct':first,'type':q.get('type'),'difficulty':q.get('difficulty'),'topic':q.get('topic'),'rarity':q.get('rarity'),'image':q.get('image')})
out=Path('redo/AmerickiPredsjednici_source_index.json')
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('indexed',len(rows))
