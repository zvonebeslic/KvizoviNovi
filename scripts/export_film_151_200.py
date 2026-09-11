import json
from pathlib import Path
data=json.loads(Path('Film.json').read_text(encoding='utf-8'))
out=[]
for i,q in enumerate(data[150:200],151):
    out.append({'index':i,'question':q['question'],'answers':q['answers'],'correct_answer':q['correct_answer']})
Path('FILM_151_200_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('exported',len(out),'of total',len(data))
