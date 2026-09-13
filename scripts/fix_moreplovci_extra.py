import json

p='Moreplovci.json'
d=json.load(open(p,encoding='utf-8'))

# Dodatne rucne korekcije nakon ponovnog citanja pitanja.
# Vrijednosti su samo dva NETOCNA odgovora; tocni odgovor se ne dira.
fix={
    1:['Pramac','Bok'],
    2:['Azija','Europa'],
    3:['Gibraltarski tjesnac','Skagerrak'],
    4:['Potpalublje','Nadgrađe'],
    6:['Amerigo Vespucci','Alonso de Ojeda'],
    7:['Bum','Rah'],
    8:['Eskadra','Konvoj'],
    12:['Benjamin Hornigold','Henry Jennings'],
    14:['Hispaniola','Portoriko'],
    15:['Tonga','Samoa'],
    16:['Pensacola','Santa Fe'],
    18:['Conquista','Repoblación'],
    20:['Cimet','Klinčić'],
    22:['Half Moon','Hopewell'],
}

for n,wrongs in fix.items():
    q=d[n-1]
    ca=q['correct_answer']
    correct=q['answers'][ca]
    if correct in wrongs or len(set(wrongs+[correct])) != 3:
        raise SystemExit(f'duplicate/bad mapping {n}')
    it=iter(wrongs)
    for L in 'ABC':
        if L != ca:
            q['answers'][L]=next(it)

for i,q in enumerate(d,1):
    a=q['answers']; c=q['correct_answer']
    assert set(a)==set('ABC'), i
    assert c in a, i
    assert len(set(a.values()))==3, i
    assert all(str(a[k]).strip() for k in 'ABC'), i

json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
open(p,'a',encoding='utf-8').write('\n')
print('extra fixed',len(fix),'questions')
