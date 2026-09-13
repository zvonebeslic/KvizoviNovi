import json,re,random
P='Moreplovci.json'
raw=open(P,encoding='utf-8').read().splitlines()
data=json.loads('\n'.join(raw))
# Map each question to its approximate source start line.
starts=[]
for i,line in enumerate(raw,1):
    if '"question":' in line: starts.append(i)
assert len(starts)==len(data)

pools={
'portugalac':['Duarte de Meneses','Tomé de Alvarenga','Rui de Noronha','Álvaro de Sequeira','Gaspar de Távora','Lourenço de Ataíde','Simão de Faria','António de Mascarenhas','João de Alvim','Diogo de Noronha'],
'spanjolac':['Diego de Villacorta','Rodrigo de Alarcón','Hernando de Sotomayor','Gonzalo de Valcárcel','Juan de Villaseca','Martín de Arriaga','Pedro de Salcedo','Alonso de Benavides','Francisco de Montalvo','Luis de Cárdenas'],
'englez':['Thomas Wycliffe','Edmund Harcourt','Richard Ashcombe','William Fenwick','George Blackthorne','Henry Walsingham','Arthur Redgrave','Edward Langford','John Haverford','Charles Whitmore'],
'francuz':['Étienne de Villeneuve','Jean-Baptiste Delorme','Pierre de Montreuil','François de Chastel','Louis de Varenne','Claude de Rochefort','Nicolas de Bréval','Antoine de Marigny','Jacques de Valcourt','Henri de Beaumont'],
'nizozemac':['Pieter van Aelst','Hendrik van Roon','Willem de Graaf','Cornelis van Houten','Jan van der Velde','Dirk van Meeren','Maarten de Wit','Adriaan van Loen','Gerrit van Dijk','Joost van Brederode'],
'italijan':['Lorenzo Bellandi','Marco Ventresca','Giovanni Almerigo','Pietro Valdieri','Antonio Serravalle','Niccolò Ferretti','Matteo Corsini','Giulio Varano','Francesco Malaspina','Andrea Bellori'],
'norvezanin':['Eirik Solberg','Lars Haldorsen','Knut Eide','Sverre Nygaard','Olav Torgersen','Bjørn Halvorsen','Anders Vik','Leif Rønning'],
'arap':['Yusuf ibn Rashid','Hassan al-Bahrani','Umar ibn Khalaf','Salim al-Masri','Ibrahim al-Qadiri','Khalid ibn Nasser','Mansur al-Hadrami','Farid al-Basri'],
'kinez':['Li Wenhai','Zhao Mingyuan','Chen Haifeng','Wang Shun','Liu Zhenhai','Xu Guanglin','Sun Weiming','Guo Haoran'],
'korejac':['Kim Seong-ho','Park Gyeong-su','Choe Min-jun','Yi Dong-hyeon','Jeong Tae-su','Han Seung-min','Seo Jin-ho','Kang Mu-yeol'],
'osoba':['Adrian Mercer','Nicolás Ferraro','Étienne Valmont','Henrik Dahl','Matteo Serani','João Valente','Pieter Roeland','Edmund Carver','Lucien Moreau','Diego Santillán'],
'tjesnac':['Hudsonov tjesnac','Davisov tjesnac','Sundski tjesnac','Lombokški tjesnac','Makassarski tjesnac','Mesinski tjesnac','Beringov tjesnac','Torresov tjesnac','Danski tjesnac','Tjesnac Juan de Fuca'],
'rt':['Rt Leeuwin','Rt Comorin','Rt Guardafui','Rt Wrath','Rt Farewell','Rt York','Rt Horn','Rt Agulhas','Rt Bojador','Rt Finisterre'],
'otok':['Madeira','Socotra','Tenerife','Réunion','Mauricijus','Samoa','Guam','Tahiti','Cipar','Bermuda','Sardinija','Korzika','Tasmanija','Mindanao','Cebu','Borneo'],
'otocje':['Azori','Kanarski otoci','Marijanski otoci','Aleutski otoci','Molučki otoci','Sejšeli','Maldivi','Bahami','Hebridi','Kurilski otoci','Farski otoci','Andamani'],
'grad':['Cartagena','Cádiz','Lisabon','Sevilla','Havana','Goa','Malacca','Calicut','Nassau','Portsmouth','Brest','Antwerpen','Macau','Manila','Batavia','Valparaíso'],
'zaljev':['Biskajski zaljev','Hudsonov zaljev','Gvinejski zaljev','Bengalski zaljev','Adenski zaljev','Omanski zaljev','Kalifornijski zaljev','Zaljev Fundy','Botnički zaljev','Karpentarijski zaljev'],
'more':['Koraljno more','Arapsko more','Sargaško more','Tasmanovo more','Beringovo more','Andamansko more','Labradorsko more','Timorsko more','Javansko more','Celebesko more'],
'ocean':['Atlantski ocean','Tihi ocean','Indijski ocean','Južni ocean','Arktički ocean'],
'brod':['Sea Venture','Golden Hind','Discovery','Resolution','Adventure','Providence','Royal Fortune','São Gabriel','Victoria','Trinidad','Duyfken','Batavia','Endurance','Terra Nova','Santa Catarina','Esperança','San Telmo','Mercury','North Star','Belle Étoile'],
'dinastija':['Ming','Tang','Song','Yuan','Qing','Han','Sui','Jin'],
'zivotinja':['Konj','Mazga','Deva','Magarac','Vol','Bivol','Lama','Slon'],
'zacin':['Papar','Klinčić','Muškatni oraščić','Cimet','Đumbir','Kardamom','Šafran','Piment'],
'drzava':['Portugal','Španjolska','Francuska','Engleska','Nizozemska','Danska','Norveška','Italija','Maroko','Oman'],
}

def cat(q):
 s=q.lower()
 # explicit requested entity beats incidental words elsewhere in stem
 if re.search(r'koji (se )?tjesnac|kojeg tjesnaca|kroz koji tjesnac',s): return 'tjesnac'
 if re.search(r'koji rt|kojeg rta|na kojem rtu|kako se zove rt',s): return 'rt'
 if re.search(r'koje otočje|koja otočja|kojeg otočja',s): return 'otocje'
 if re.search(r'koji otok|kojeg otoka|na kojem otoku|s kojeg .*otoka|do kojeg .*otoka',s): return 'otok'
 if re.search(r'koji grad|kojeg grada|u kojem .*gradu|luku kojeg grada|koju .*luku|koja .*luka',s): return 'grad'
 if re.search(r'koji zaljev|kojem .*zaljevu|kojeg zaljeva',s): return 'zaljev'
 if re.search(r'koje more|kojem moru|kojeg mora',s): return 'more'
 if re.search(r'koji ocean|kojem oceanu|kojeg oceana',s): return 'ocean'
 if re.search(r'kako se zvao brod|koji .*brod|ime broda|naziv broda|kojim brodom|brod zvao',s): return 'brod'
 if 'dinastij' in s and re.search(r'koja|koju|koje',s): return 'dinastija'
 if re.search(r'koja .*životinja|koju .*životinju',s): return 'zivotinja'
 if re.search(r'koji .*začin|kojeg .*začina',s): return 'zacin'
 if re.search(r'koja država|koje države|koju državu',s): return 'drzava'
 # people, with nationality-aware invented names
 if re.search(r'koji|koja|tko|kako se zvao|kako se zvala|ime .*moreplov',s):
  if 'portugal' in s: return 'portugalac'
  if 'španjol' in s or 'spanjol' in s: return 'spanjolac'
  if 'englesk' in s or 'britan' in s: return 'englez'
  if 'francusk' in s: return 'francuz'
  if 'nizozem' in s or 'flamansk' in s: return 'nizozemac'
  if 'talijan' in s or 'venecij' in s or 'genove' in s: return 'italijan'
  if 'norve' in s: return 'norvezanin'
  if 'arapsk' in s: return 'arap'
  if 'kinesk' in s: return 'kinez'
  if 'korej' in s: return 'korejac'
  # only classify as generic person when the stem explicitly asks for a person/title
  if re.search(r'koji je .*?(moreplovac|istraživač|pomorac|kapetan|gus(ar|arica)|konkvistador|kartograf|redovnik|zapovjednik|kralj|kraljica|pustolov|navigator)|koja je .*?(žena|kraljica|botaničarka|gusarica)|tko je ',s): return 'osoba'
 return None

used={k:0 for k in pools}
changed=0
for idx,q in enumerate(data):
 if starts[idx] < 800: continue
 c=cat(q['question'])
 if not c: continue
 correct=q['answers'][q['correct_answer']]
 candidates=[x for x in pools[c] if x.casefold()!=str(correct).casefold()]
 if len(candidates)<2: continue
 # varied deterministic rotation; avoid the same pair over and over
 off=(idx*2+used[c])%len(candidates); used[c]+=1
 wrong=[]
 for j in range(len(candidates)):
  x=candidates[(off+j)%len(candidates)]
  if x not in wrong: wrong.append(x)
  if len(wrong)==2: break
 for letter in 'ABC':
  if letter!=q['correct_answer']:
   q['answers'][letter]=wrong.pop(0)
 changed+=1
# hard sanity checks
for i,q in enumerate(data,1):
 a=q['answers']; c=q['correct_answer']
 assert set(a)==set('ABC') and c in a and len({str(v).casefold() for v in a.values()})==3,(i,q)
open(P,'w',encoding='utf-8').write(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('REWORKED_FROM_LINE_800',changed,'OF',len(data))
