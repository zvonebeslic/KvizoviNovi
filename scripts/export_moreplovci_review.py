import json, os
p='Moreplovci.json'
d=json.load(open(p,encoding='utf-8'))
os.makedirs('review_moreplovci',exist_ok=True)
size=50
for start in range(0,len(d),size):
    end=min(start+size,len(d))
    lines=[]
    for i in range(start,end):
        q=d[i]; a=q['answers']; c=q['correct_answer']
        lines.append(f"{i+1}. Q: {q['question']}\n   A: {a['A']} | B: {a['B']} | C: {a['C']} | CORRECT: {c}={a[c]}\n")
    fn=f'review_moreplovci/{start+1:03d}_{end:03d}.txt'
    open(fn,'w',encoding='utf-8').write('\n'.join(lines))
print('TOTAL',len(d),'CHUNKS',(len(d)+size-1)//size)
