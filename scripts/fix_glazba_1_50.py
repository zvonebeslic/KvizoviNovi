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
13:{'A':'Klavir','B':'Gitaru','C':'Saksofon'},
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
27:{'A':'The Thin White Duke','B':'Major Tom','C':'Ziggy Stardust'},
28:{'A':'Thom Yorke','B':'Matt Bellamy','C':'Chris Martin'},
29:{'A':'Crvene jabuke','B':'Bijelog Dugmeta','C':'Divljih Jagoda'},
30:{'A':'Johann Sebastian Bach','B':'Georg Friedrich Händel','C':'Antonio Vivaldi'},
31:{'A':'Oasis','B':'Blur','C':'Pulp'},
32:{'A':'Partitura','B':'Libreto','C':'Sinopsis'},
33:{'A':'Gitara','B':'Violina','C':'Klavir'},
34:{'A':'Norveška','B':'Švedska','C':'Danska'},
35:{'A':'Taylor Swift','B':'Adele','C':'Beyoncé'},
36:{'A':'Marimba','B':'Ksilofon','C':'Vibrafon'},
37:{'A':'Bob Dylan','B':'Neil Young','C':'Bruce Springsteen'},
38:{'A':'Nirvana','B':'Pearl Jam','C':'Soundgarden'},
39:{'A':'Wolfgang Amadeus Mozart','B':'Ludwig van Beethoven','C':'Joseph Haydn'},
40:{'A':'Madonna','B':'Cyndi Lauper','C':'Cher'},
41:{'A':'ABBA','B':'Roxette','C':'Ace of Base'},
42:{'A':'Freddie Mercury','B':'David Bowie','C':'Elton John'},
43:{'A':'Metallica','B':'Megadeth','C':'Slayer'},
44:{'A':'Whitney Houston','B':'Mariah Carey','C':'Céline Dion'},
45:{'A':'The Beatles','B':'The Rolling Stones','C':'The Who'},
46:{'A':'Aretha Franklin','B':'Tina Turner','C':'Diana Ross'},
47:{'A':'U2','B':'R.E.M.','C':'INXS'},
48:{'A':'Elvis Presley','B':'Johnny Cash','C':'Roy Orbison'},
49:{'A':'Guns N’ Roses','B':'Bon Jovi','C':'Aerosmith'},
50:{'A':'Stevie Wonder','B':'Ray Charles','C':'Marvin Gaye'}
}
for i,a in fix.items():
 q=d[i-1]; old=q['answers'][q['correct_answer']]; q['answers']=a
 if q['answers'][q['correct_answer']] != old: print('WARNING',i,old,'->',q['answers'][q['correct_answer']])
assert all(set(q['answers'])=={'A','B','C'} and len(set(q['answers'].values()))==3 for q in d[:50])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed',len(fix))
