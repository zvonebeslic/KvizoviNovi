import json, glob, os, random

ROOT='AmerickiPredsjednici.json'
with open(ROOT,encoding='utf-8') as f:
    root=json.load(f)

qmap={}
for i,q in enumerate(root):
    qmap.setdefault(q.get('question'),[]).append(i)

files=[]
base='redo/AmerickiPredsjednici.json'
if os.path.exists(base): files.append(base)
files += sorted(p for p in glob.glob('redo/AmerickiPredsjednici_*.json')
                if '_source_index' not in p and '_manual_audit' not in p)
files += sorted(glob.glob('redo/manual/AmerickiPredsjednici_*.json'))

applied=set()
for path in files:
    try:
        with open(path,encoding='utf-8') as f: data=json.load(f)
    except Exception:
        continue
    if not isinstance(data,list):
        continue
    for item in data:
        if not isinstance(item,dict) or 'question' not in item or 'answers' not in item or 'correct_answer' not in item:
            continue
        matches=qmap.get(item['question'],[])
        if len(matches)!=1:
            continue
        i=matches[0]
        root[i]['answers']=item['answers']
        root[i]['correct_answer']=item['correct_answer']
        applied.add(i)

custom={
"Prezime kojeg američkog predsjednika se piše kao ime jednog glumca koji je utjelovio agenta 007?": ({'A':'Pierce','B':'Ford','C':'Carter'},'A'),
"Američki Senat je 9. travnja (aprila) 1867.g. ratificirao sporazum kojim je od rusije za 7,2mil. dolara kupljen koji teritorij?": ({'A':'Louisiana','B':'Aljaska','C':'Florida'},'B'),
"Tko nedostaje Washingtonu, Rooseveltu i Lincolnu, na planini Rushmore?": ({'A':'John Adams','B':'James Buchanan','C':'Thomas Jefferson'},'C'),
"Tko je bio treći predsjednik SAD-a?": ({'A':'Thomas Jefferson','B':'John Adams','C':'James Madison'},'A'),
"Godine 1800. Johna Adamsa je na predsjedničkim izborima porazio tko?": ({'A':'James Madison','B':'Thomas Jefferson','C':'James Monroe'},'B'),
"Kako se zvao prvi rat koji su Sjedinjene Američke Države vodile na stranom tlu?": ({'A':'Meksičko-američki rat','B':'Drugi berberski rat','C':'Prvi berberski rat'},'C'),
"Tko je bio prvi američki predsjednik koji je za vrijeme svog predsjedničkog mandata boravio u rezidenciji koja će kasnije postati poznata pod nazivom Bijela Kuća?": ({'A':'John Adams','B':'Thomas Jefferson','C':'James Madison'},'A'),
"Odbor za izradu američke deklaracije neovisnosti se naziva i odborom petorice, a od tih pet članova, koliko ih je postalo američkim predsjednicima?": ({'A':'Jedan','B':'Dva','C':'Tri'},'B'),
"Koje je ime Thomas Jefferson dao svom imanju u Charlottesvilleu na kojem se i danas nalazi vila, na 260m visokom brdu?": ({'A':'Mount Vernon','B':'Montpelier','C':'Monticello'},'C'),
"Od koje godine je u uporabi Veliki pečat Sjedinjenih Američkih Država (Great Seal of the US)?": ({'A':'1782.','B':'1778 .','C':'1786 .'},'A'),
}
for q,(answers,correct) in custom.items():
    m=qmap.get(q,[])
    if len(m)==1:
        i=m[0]; root[i]['answers']=answers; root[i]['correct_answer']=correct; applied.add(i)

# Build an exactly balanced, well-mixed A/B/C target sequence with no runs of 3.
n=len(root)
remaining={'A':n//3,'B':n//3,'C':n//3}
for k in ['A','B','C'][:n%3]:
    remaining[k]+=1
rng=random.Random(20260910)
pool=[]
for i in range(n):
    banned = pool[-1] if len(pool)>=2 and pool[-1]==pool[-2] else None
    choices=[k for k in 'ABC' if remaining[k]>0 and k!=banned]
    max_left=max(remaining[k] for k in choices)
    best=[k for k in choices if remaining[k]>=max_left-1]
    pick=rng.choice(best)
    pool.append(pick)
    remaining[pick]-=1
assert sum(remaining.values())==0
assert all(not (pool[i]==pool[i-1]==pool[i-2]) for i in range(2,n))

for i,item in enumerate(root):
    old=item['answers']
    cur=item['correct_answer']
    correct_text=old[cur]
    wrong=[old[k] for k in ['A','B','C'] if k!=cur]
    target=pool[i]
    other=[k for k in ['A','B','C'] if k!=target]
    remapped={target:correct_text, other[0]:wrong[0], other[1]:wrong[1]}
    item['answers']={k:remapped[k] for k in ['A','B','C']}
    item['correct_answer']=target

assert len(root)==n
assert all(set(x['answers'])=={'A','B','C'} for x in root)
assert all(x['correct_answer'] in x['answers'] for x in root)
final_counts={k:sum(x['correct_answer']==k for x in root) for k in 'ABC'}
assert max(final_counts.values())-min(final_counts.values())<=1
assert all(not (root[i]['correct_answer']==root[i-1]['correct_answer']==root[i-2]['correct_answer']) for i in range(2,n))

with open(ROOT,'w',encoding='utf-8') as f:
    json.dump(root,f,ensure_ascii=False,indent=2)
    f.write('\n')
print('questions',n,'reviewed answer sets applied',len(applied),'distribution',final_counts)
