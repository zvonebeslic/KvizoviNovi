import json
from pathlib import Path

p=Path('AmerickiPredsjednici.json')
data=json.load(open(p,encoding='utf-8'))

patches={
0: ({'A':'Donald Trump','B':'Barack Obama','C':'George W. Bush'},'A'),
1: ({'A':'Thomas Jefferson','B':'Benjamin Franklin','C':'John Adams'},'B'),
2: ({'A':'José de San Martín','B':"Bernardo O'Higgins",'C':'Simon Bolivar'},'C'),
3: ({'A':'Benjamin Franklin','B':'Thomas Jefferson','C':'John Adams'},'A'),
4: ({'A':'George H. W. Bush','B':'Ronald Reagan','C':'Jimmy Carter'},'B'),
5: ({'A':'Florida','B':'Oregon','C':'Louisiana'},'C'),
6: ({'A':'Parizu','B':'Londonu','C':'Ghentu'},'A'),
7: ({'A':'John F. Kennedy','B':'George Herbert Walker Bush','C':'Gerald Ford'},'B'),
8: ({'A':'Gerald Ford','B':'Jimmy Carter','C':'Ronald Reagan'},'C'),
9: ({'A':'Kumrovec','B':'Krapina','C':'Marija Bistrica'},'A'),
10: ({'A':'Võ Nguyên Giáp','B':'Ho Ši Mina','C':'Lê Duẩn'},'B'),
11: ({'A':'Reforger','B':'Autumn Forge','C':'AbleArcher 83'},'C'),
12: ({'A':'Prištini','B':'Prizrenu','C':'Peći'},'A'),
13: ({'A':'Jesse Jackson','B':'Barack Obama','C':'Colin Powell'},'B'),
14: ({'A':'New York','B':'Connecticut','C':'Massachusetts'},'C'),
}

for i,(answers,correct) in patches.items():
    data[i]['answers']=answers
    data[i]['correct_answer']=correct

json.dump(data,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
open(p,'a',encoding='utf-8').write('\n')
print('Rucno popravljeno',len(patches),'pitanja')
