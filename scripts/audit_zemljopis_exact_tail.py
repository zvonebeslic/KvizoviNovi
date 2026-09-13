import json
from pathlib import Path

p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))

fixes={
'Zemlja Franje Josipa je otočje koje pripada kojoj državi?':['Norveškoj','Kanadi'],
'Na koje manje sredozemno more gledaju gradovi Genova i San Remo?':['Tirensko More','Jadransko More'],
'Koji je glavni grad Bocvane?':['Windhoek','Lusaka'],
'Kako se zove glavni grad Libanona?':['Amman','Damask'],
'Koji je glavni grad nazvan po jednoj božici iz grčke mitologije?':['Rim','Nikozija'],
'Kako se zove glavni grad Nikaragve?':['Tegucigalpa','San Salvador'],
'Sa kojim otokom Trinidad tvori suvremenu državu?':['Grenada','Barbados'],
'Koja se država dijeli na tri povijesne regije, Cireniku, Fezan i Tripolitaniju?':['Egipat','Tunis'],
'Koji je najjužniji glavni grad latinske Amerike?':['Buenos Aires','Santiago'],
'Koja europska država ima nacionalnu zastavu vrlo sličnu onoj od Haitija?':['Luksemburg','San Marino'],
'Koje otočje uz obalu Afrike pripada Španjolskoj?':['Zelenortski Otoci','Madeira'],
'Najveći kip na svijetu sačinjen u potpunosti od zlata je 5,5 tona težak kip Bude koji se čuva u hramu Wat Traimit, u kojoj državi?':['Mjanmar','Kambodža'],
'S kojom državom Sjeverna Irska ima kopnenu granicu?':['Škotskom','Walesom'],
'Colombo je glavni grad koje države?':['Indije','Maldiva'],
"Koja država za internetski nastavak ima slova 'sz'?":['Lesoto','Bocvana'],
"Koju državu njeni žitelji zapisuju kao 'Magyarország'":['Slovačku','Rumunjsku'],
'Kako se zove glavni grad Litve?':['Riga','Tallinn'],
'Kako se zove glavni grad Grenade?':['Castries','Kingstown'],
'Azerski jezik, kojim govori više od 23 milijuna ljudi, službeni je jezik koje države?':['Turske','Turkmenistana'],
'Koja se nagrada u bivšem SSSR-u dodijeljivala planinarima koji su ispenjali svih 5 vrhova iznad 7000m na području Sovjetskog Saveza?':['Zlatni cepin','Majstor sporta SSSR-a'],
'Kako se zove glavni grad Crne Gore?':['Sarajevo','Skoplje'],
"Kada napišemo 'China', svima nam na pamet prvo dođe Kina, ali ovaj put tražimo jedan mali grad tog imena, koji se nalazi u sklopu otočja Amami, koje pripada kojoj državi?":['Južnoj Koreji','Kini'],
'U koji se ocean ulijeva rijeka Jangce?':['Indijski Ocean','Atlantski Ocean'],
'Na kojem kontinentu se nalazi država Gvajana?':['Sjeverna Amerika','Afrika'],
'Koja velika afrička rijeka, unutar svog toka, ima više od 4 000 otoka?':['Niger','Zambezi'],
'Koju rijeku tražimo, ako znamo da postoji Crvena, Bijela i Crna, čije se vode slijevaju u jezero, koje se također zove kao i rijeka, te se na kraju, sva ta voda ulijeva u Atlantik kod Gvinejskog Zaljeva?':['Niger','Senegal'],
"Ime kojeg glavnog grada, a i same države, u sebi 'redom' nosi ime jednog oskarovca te plod hrasta i bukve?":['Tunis','Rabat'],
'Palacio de los Lopez je palača u kojoj se nalazi predsjednik koje države?':['Urugvaja','Bolivije'],
'Ako se razvojem drevnog Tai Kadai (Kra Dai) jezika u jugoistočnoj Aziji, u Tajlandu danas govori Thai, onda je logično da se u Laosu govri koji jezik?':['Khmer','Burmanski'],
'Koji je glavni grad Curacaa, najvećeg otoka Karipske Nizozenske?':['Oranjestad','Kralendijk']
}

index={q.get('question'):q for q in d}
changed=0
for question,pair in fixes.items():
    assert question in index, question
    q=index[question]
    key=q['correct_answer']
    correct=q['answers'][key]
    assert correct not in pair,(question,correct,pair)
    it=iter(pair)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3,(question,q['answers'])
    changed+=1

p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed exact tail questions',changed)
