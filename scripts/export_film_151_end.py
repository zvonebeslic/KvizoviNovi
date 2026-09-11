import json
from pathlib import Path
data=json.loads(Path('Film.json').read_text(encoding='utf-8'))
out=[]
for i,q in enumerate(data[150:],151):
    out.append({'index':i,'question':q['question'],'answers':q['answers'],'correct_answer':q['correct_answer']})
Path('FILM_151_END_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('total',len(data),'remaining',len(out))
