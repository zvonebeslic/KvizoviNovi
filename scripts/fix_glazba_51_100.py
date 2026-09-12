import json
from pathlib import Path
p=Path('Glazba.json'); d=json.loads(p.read_text(encoding='utf-8'))
# Završni audit: zadržavamo originalni točan odgovor Beethoven,
# ali uklanjamo Mozarta jer i on ima Simfoniju br. 9.
q=d[85]
assert q['correct_answer']=='B'
assert q['answers']['B']=='Ludwig van Beethoven'
q['answers']={'A':'Antonio Vivaldi','B':'Ludwig van Beethoven','C':'Johannes Brahms'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('final fixed Q86')
