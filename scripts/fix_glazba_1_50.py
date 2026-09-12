import json
from pathlib import Path
p=Path('Glazba.json'); d=json.loads(p.read_text(encoding='utf-8'))
fix={
1:{'A':'Mjesecom','B':'Suncem','C':'Marsom'},
2:{'A':'Britannicu','B':'Titaniku','C':'Olympicu'},
3:{'A':'Dr. Dre','B':'Eazy-E','C':'Ice Cube'},
4:{'A':'Violinu','B':'Violončelo','C':'Flautu'},
5:{'A':'Gudok','B':'Gusle','C':'Liru'},
6:{'A':'Sting','B':'Freddie Mercury','C':'George Michael'},
7:{'A':'Queen','B':'Led Zeppelin','C':'Pink Floyd'},
8:{'A':'Bono','B':'Chris Martin','C':'Brandon Flowers'},
9:{'A':'Duffy','B':'Amy Winehouse','C':'Adele'},
10:{'A':'Prince','B':'David Bowie','C':'Lenny Kravitz'},
11:{'A':'Crne Gore','B':'Srbije','C':'Sjeverne Makedonije'},
12:{'A':'Selena Gomez','B':'Dua Lipa','C':'Ariana Grande'},
13:{'A':'Klavir','B':'Gitara','C':'Saksofon'},
14:{'A':'Magdalena','B':'Nadalina','C':'Lucija'},
15:{'A':'Zlatna arena','B':'Vladimir Nazor','C':'Porin'},
16:{'A':'Journey','B':'Foreigner','C':'Boston'},
17:{'A':'Frenkie','B':'Edo Maajka','C':'Marčelo'},
18:{'A':'Violinu','B':'Klavir','C':'Čelo'},
19:{'A':'Mick Jagger','B':'Robert Plant','C':'Steven Tyler'},
20:{'A':'Hans Zimmer','B':'John Williams','C':'Ennio Morricone'},
21:{'A':'Georg Friedrich Händel','B':'Georg Philipp Telemann','C':'Johann Sebastian Bach'},
22:{'A':'Miley Cyrus','B':'Dua Lipa','C':'Ariana Grande'},
23:{'A':'Charlie Watts','B':'Ringo Starr','C':'Roger Taylor'},
24:{'A':'Ariana Grande','B':'Miley Cyrus','C':'Dua Lipa'},
25:{'A':'Divljih Jagoda','B':'Bijelog Dugmeta','C':'Parnog Valjka'},
26:{'A':'Bruno Mars','B':'Ed Sheeran','C':'The Weeknd'},
27:{'A':'Slim Shady','B':'Sasha Fierce','C':'Ziggy Stardust'},
28:{'A':'Thom Yorke','B':'Matt Bellamy','C':'Chris Martin'},
29:{'A':'Crvene jabuke','B':'Bijelog Dugmeta','C':'Divljih Jagoda'},
30:{'A':'Johann Sebastian Bach','B':'Georg Friedrich Händel','C':'Antonio Vivaldi'},
31:{'A':'Oasis','B':'Blur','C':'Pulp'},
32:{'A':'Partitura','B':'Libreto','C':'Sinopsis'},
33:{'A':'Violina','B':'Klavir','C':'Gitara'},
34:{'A':'Alex Turner','B':'Julian Casablancas','C':'Brandon Flowers'},
35:{'A':'Renaissance','B':'Cowboy Carter','C':'Lemonade'},
36:{'A':'Lorde','B':'Dua Lipa','C':'Billie Eilish'},
37:{'A':'Švedska','B':'Norveška','C':'Danska'},
38:{'A':'Katy Perry','B':'Lady Gaga','C':'Rihanna'},
39:{'A':'Zadra','B':'Dubrovnika','C':'Splita'},
40:{'A':'Nirvani','B':'Pearl Jamu','C':'Soundgardenu'},
41:{'A':'Toxic','B':'Baby One More Time','C':'Oops!... I Did It Again'},
42:{'A':'Jay-Z','B':'50 Cent','C':'Eminem'},
43:{'A':'Fleetwood Mac','B':'Eagles','C':'Bee Gees'},
44:{'A':'Jay-Z','B':'Kanye West','C':'Nas'},
45:{'A':'Rihanna','B':'Alicia Keys','C':'Beyonce'},
46:{'A':'Dubrovački Trubaduri','B':'Pro arte','C':'Indexi'},
47:{'A':'Tom Petty','B':'Bruce Springsteen','C':'Billy Joel'},
48:{'A':'Adele','B':'Madonna','C':'Taylor Swift'},
49:{'A':'Gitara','B':'Bas-gitara','C':'Klavir'},
50:{'A':'Norveške','B':'Švedske','C':'Danske'}
}
# Originalni točni odgovori iz verzije prije prvog uređivanja 1-50.
original_correct={33:'Gitara',34:'Alex Turner',35:'Cowboy Carter',36:'Billie Eilish',37:'Švedska',38:'Lady Gaga',39:'Splita',40:'Nirvani',41:'Baby One More Time',42:'Eminem',43:'Fleetwood Mac',44:'Kanye West',45:'Beyonce',46:'Dubrovački Trubaduri',47:'Bruce Springsteen',48:'Taylor Swift',49:'Gitara',50:'Švedske'}
for i,a in fix.items():
 q=d[i-1]
 q['answers']=a
 if i in original_correct:
  assert q['answers'][q['correct_answer']] == original_correct[i], (i,q['correct_answer'],q['answers'][q['correct_answer']],original_correct[i])
assert all(set(q['answers'])=={'A','B','C'} and len(set(q['answers'].values()))==3 for q in d[:50])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed',len(fix))
