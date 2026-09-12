import json
from pathlib import Path
p=Path('Glazba.json'); d=json.loads(p.read_text(encoding='utf-8'))
fix={
101:{'A':'Whitney Houston','B':'Celine Dion','C':'Mariah Carey'},
102:{'A':'Back in Black','B':'The Dark Side of the Moon','C':'Thriller'},
103:{'A':'Klavira','B':'Harmonike','C':'Saksofona'},
104:{'A':'Patti Smith','B':'Debbie Harry','C':'Chrissie Hynde'},
105:{'A':'Don Giovanni','B':'Figarov pir','C':'Čarobna frula'},
106:{'A':'Ed Sheeran','B':'Sam Smith','C':'Shawn Mendes'},
107:{'A':'Paul McCartney','B':'John Lennon','C':'George Harrison'},
108:{'A':'Ivana Lang','B':'Mia Čorak Slavenska','C':'Dora Pejačević'},
109:{'A':'Reggae','B':'Ska','C':'Calypso'},
110:{'A':'Hans Zimmer','B':'John Williams','C':'Ennio Morricone'},
111:{'A':'Aerosmith','B':'The Who','C':'The Rolling Stones'},
112:{'A':'Kendrick Lamar','B':'J. Cole','C':'Drake'},
113:{'A':'Đelo Jusić','B':'Alfi Kabiljo','C':'Arsen Dedić'},
114:{'A':'Johnny Cash','B':'Jerry Lee Lewis','C':'Elvis Presley'},
115:{'A':'Miley Cyrus','B':'Noah Cyrus','C':'Brandi Cyrus'},
116:{'A':'Olivia Rodrigo','B':'Sabrina Carpenter','C':'Billie Eilish'},
117:{'A':'David Bowie','B':'Elton John','C':'Freddie Mercury'},
118:{'A':'New Yorka','B':'Los Angelesa','C':'Chicaga'},
119:{'A':'Korni grupe','B':'Jutra','C':'Indexa'},
120:{'A':'Pearl Jam','B':'Soundgarden','C':'Nirvana'},
121:{'A':'Modest Petrovič Musorgski','B':'Nikolaj Rimski-Korsakov','C':'Petar Iljič Čajkovski'},
122:{'A':'Joseph Haydn','B':'Wolfgang Mozart','C':'Ludwig van Beethoven'},
123:{'A':'Baby Lasagna','B':'Slimane','C':'Nemo'},
124:{'A':'Roosevelt','B':'Truman','C':'Eisenhower'},
125:{'A':'Jamajke','B':'Barbadosa','C':'Trinidada i Tobaga'},
126:{'A':'Deep Purple','B':'Black Sabbath','C':'Led Zeppelin'},
127:{'A':'Elton John','B':'Billy Joel','C':'Rod Stewart'},
128:{'A':'Taylor Swift','B':'Beyonce','C':'Adele'},
129:{'A':'Sergej Rahmanjinov','B':'Igor Stravinski','C':'Petar Iljič Čajkovski'},
130:{'A':'Prljavo Kazalište','B':'Parni Valjak','C':'Azra'},
131:{'A':'Cher','B':'Madonna','C':'Cyndi Lauper'},
132:{'A':'Klarinet','B':'Saksofon','C':'Flauta'},
133:{'A':'The Killers','B':'Franz Ferdinand','C':'Arctic Monkeys'}
}
assert len(d)==133, len(d)
for i,a in fix.items():
 q=d[i-1]
 old_correct=q['answers'][q['correct_answer']]
 assert a[q['correct_answer']]==old_correct or (i==132 and old_correct=='Flautu'), (i,old_correct,a[q['correct_answer']])
 assert len(set(a.values()))==3,(i,a)
 q['answers']=a
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed',len(fix),'of',len(d))
