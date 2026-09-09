import json
from pathlib import Path
src=json.load(open('Film.json',encoding='utf-8'))
out=[]
for i,q in enumerate(src,1):
    out.append({'index':i,'question':q.get('question'),'source_correct':q.get('answers',{}).get(q.get('correct_answer'))})
Path('redo/Film_source_index.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('FILM_TOTAL',len(out))
