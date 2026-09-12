import json
from pathlib import Path
d=json.loads(Path('Glazba.json').read_text(encoding='utf-8'))
out=[]
for i,q in enumerate(d[50:100],51):
 out.append({'index':i,'question':q['question'],'answers':q['answers'],'correct_answer':q['correct_answer']})
Path('GLAZBA_51_100_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('total',len(d),'exported',len(out))
