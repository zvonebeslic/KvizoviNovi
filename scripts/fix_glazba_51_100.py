import json
from pathlib import Path
p=Path('Glazba.json'); d=json.loads(p.read_text(encoding='utf-8'))
fix={
51:{'A':'Goran Bare','B':'Davorin Bogović','C':'Davor Gobac'},
52:{'A':'The Kid Laroi','B':'Post Malone','C':'Shawn Mendes'},
53:{'A':'Saksofon','B':'Trubu','C':'Klavir'},
54:{'A':'Brandon Flowers','B':'Chris Martin','C':'Adam Levine'},
55:{'A':'Aretha Franklin','B':'Diana Ross','C':'Tina Turner'},
56:{'A':'Billie Eilish','B':'Olivia Rodrigo','C':'Sabrina Carpenter'},
57:{'A':'True Blue','B':'Erotica','C':'Like a Virgin'},
58:{'A':'Flautu','B':'Violinu','C':'Klarinet'},
59:{'A':'Bee Gees','B':'ABBA','C':'Boney M.'},
60:{'A':'TLC','B':'Destiny’s Child','C':'Spice Girls'},
61:{'A':'Ed Sheeran','B':'Sam Smith','C':'Shawn Mendes'},
62:{'A':'Gitare','B':'Bubnjeve','C':'Klavijature'},
63:{'A':'Tri baritona','B':'Tri soprana','C':'Tri tenora'},
64:{'A':'Guns N’ Roses','B':'Aerosmith','C':'Bon Jovi'},
65:{'A':'Katy Perry','B':'Lady Gaga','C':'Pink'},
66:{'A':'Agnes','B':'Alice','C':'Adele'},
67:{'A':'Riblja čorba','B':'Električni orgazam','C':'Idoli'},
68:{'A':'Pearl Jam','B':'Nirvana','C':'Soundgarden'},
69:{'A':'Henrika II.','B':'Franju II.','C':'Karla IX.'},
70:{'A':'Gitaru','B':'Bas-gitaru','C':'Bubnjeve'},
71:{'A':'John Williams','B':'Hans Zimmer','C':'James Horner'},
72:{'A':'Whitney Houston','B':'Céline Dion','C':'Mariah Carey'},
73:{'A':'Trubu','B':'Saksofon','C':'Trombon'},
74:{'A':'Dr. Dre','B':'Snoop Dogg','C':'Ice Cube'},
75:{'A':'Beyoncé','B':'Jennifer Lopez','C':'Shakira'},
76:{'A':'Dubrovniku','B':'Splitu','C':'Zadru'},
77:{'A':'Milano','B':'Cremona','C':'Brescia'},
78:{'A':'Ava Max','B':'Rita Ora','C':'Dua Lipa'},
79:{'A':'Christina Aguilera','B':'Britney Spears','C':'Jessica Simpson'},
80:{'A':'Minnesängera','B':'Trubadura','C':'Goliarda'},
81:{'A':'50 Cent','B':'Jay-Z','C':'Eminem'},
82:{'A':'Bruce Springsteen','B':'Billy Joel','C':'Tom Petty'},
83:{'A':'Manchester','B':'Liverpool','C':'Birmingham'},
84:{'A':'Lollapalooza','B':'Bonnaroo','C':'Coachella'},
85:{'A':'Jim Morrison','B':'Roger Daltrey','C':'Robert Plant'},
86:{'A':'Wolfgang Amadeus Mozart','B':'Ludwig van Beethoven','C':'Johannes Brahms'},
87:{'A':'Niall Horan','B':'Zayn Malik','C':'Harry Styles'},
88:{'A':'Lana Del Rey','B':'Florence Welch','C':'Marina Diamandis'},
89:{'A':'Eddie Vedder','B':'Dave Grohl','C':'Chris Cornell'},
90:{'A':'Elton John','B':'Freddie Mercury','C':'David Bowie'},
91:{'A':'Pink Floyd','B':'Genesis','C':'Yes'},
92:{'A':'Aerosmith','B':'Guns N’ Roses','C':'Bon Jovi'},
93:{'A':'The Weeknd','B':'Justin Timberlake','C':'Bruno Mars'},
94:{'A':'The Weeknd','B':'Post Malone','C':'Bruno Mars'},
95:{'A':'Beyoncé','B':'Rihanna','C':'Alicia Keys'},
96:{'A':'Italije','B':'Belgije','C':'Francuske'},
97:{'A':'Bono','B':'Michael Stipe','C':'Michael Hutchence'},
98:{'A':'Prince','B':'Michael Jackson','C':'Stevie Wonder'},
99:{'A':'Kanye West','B':'Drake','C':'Jay-Z'},
100:{'A':'Jimi Hendrix','B':'Eric Clapton','C':'Jimmy Page'}
}
for i,a in fix.items():
 q=d[i-1]
 assert len(set(a.values()))==3,(i,a)
 q['answers']=a
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed',len(fix))
