import json
from pathlib import Path

p=Path('Film.json')
data=json.loads(p.read_text(encoding='utf-8'))
chunk=[]
for i,item in enumerate(data[50:100], start=51):
    chunk.append({
        'index': i,
        'question': item.get('question'),
        'answers': item.get('answers'),
        'correct_answer': item.get('correct_answer')
    })
Path('FILM_51_100_REVIEW.json').write_text(json.dumps(chunk,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('exported',len(chunk))