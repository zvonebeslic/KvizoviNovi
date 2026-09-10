import json, glob
from pathlib import Path

source=json.load(open('redo/AntickiRim_source_index.json',encoding='utf-8'))
items={}
for fn in sorted(glob.glob('redo/AntickiRim*.json')):
    if fn.endswith('_source_index.json') or fn.endswith('_manual_audit.json'):
        continue
    data=json.load(open(fn,encoding='utf-8'))
    if not isinstance(data,list):
        continue
    for q in data:
        idx=q.get('index')
        if isinstance(idx,int):
            items[idx]=q

missing=[i for i in range(1,len(source)+1) if i not in items]
if missing:
    raise SystemExit(f'Missing indexes: {missing[:20]} total={len(missing)}')

out=[]
for i in range(1,len(source)+1):
    q=items[i]
    if q.get('question') != source[i-1]['question']:
        raise SystemExit(f'Question mismatch at {i}')
    clean={}
    for k in ('type','rarity','difficulty','topic','question','answers','image','correct_answer'):
        if k in q:
            clean[k]=q[k]
    out.append(clean)

Path('AntickiRim.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('MERGED',len(out))
