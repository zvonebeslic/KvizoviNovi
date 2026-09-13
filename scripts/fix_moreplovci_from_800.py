import json
p='Moreplovci.json'
d=json.load(open(p,encoding='utf-8'))
# Manual cleanup of distractors in the section beginning around source line 800.
# Correct answer strings and question strings are never changed.
fix={
"Kako se zvala tajanstvena krajnja sjeverna zemlja koju je grčki istraživač Piteja iz Masalije opisao oko 325. godine prije Krista?": ["Ultima Thule","Hyperboreja"],
"Koju je važnu trgovačku luku na Malajskom poluotoku Afonso de Albuquerque osvojio 1511.g., čime je Portugal stekao nadzor nad ključnim prolazom prema \"Otocima začina\"?": ["Kedah","Johor"],
"Koji tjesnac nosi ime moreplovca čija je ekspedicija 1520.g. kroz krajnji jug Južne Amerike pronašla prolaz iz Atlantika u ocean koji je potom nazvao 'mirnim'?": ["Drakeov prolaz","Torresov tjesnac"],
"Koje su otočje, za tadašnju Europu jako daleko, portugalci otkrili 1456.g.?": ["Azore","Madeiru"],
"Koji je portugalski kralj poslao Vasca da Gamu na putovanje koje je 1498.g. otvorilo pomorski put iz Europe do Indije?": ["Ivan II.","Afonso V."],
"Koji je arapski moreplovac i pisac iz 15. stoljeća, poznat pod nadimkom Lav mora, napisao važne priručnike o plovidbi Indijskim oceanom?": ["Ibn Battuta","Sulayman al-Mahri"],
"Nakon što je brod Endurance uništen u antarktičkom ledu, Ernest Shackleton je ostavio većinu svojih ljudi na Elephant Islandu te s petoricom članova posade krenuo malim čamcem preko više od 1.300 km otvorenog mora kako bi pronašao pomoć a uspio je doploviti do kojeg udaljenog otoka?": ["Falklandski otoci","Južni Orkney"],
"Kako se naziva portugalska navigacijska tehnika u kojoj se jedrenjak udaljava od afričke ili europske obale i pravi širok luk preko Atlantika kako bi iskoristio povoljnije vjetrove i morske struje?": ["Volta da costa","Rota do vento"],
"Koji je grad na otoku New Providence na Bahamima početkom 18. stoljeća postao glavno gusarsko utočište i središte takozvane Gusarske republike?": ["Freeport","Port Royal"],
"Vasco da Gama nije stigao u Indiju na područje današnjeg Mumbaija ili Goe, nego u luku kojeg grada na obali Kerale?": ["Cochin","Kannur"],
"U kojem je američkom zaljevu francuska flota 1781.g. spriječila britanske brodove da pomognu vojsci kod Yorktowna i tako snažno utjecala na ishod Američkog rata za neovisnost?": ["Zaljev Delaware","Zaljev Massachusetts"],
"Koje su otočje portugalci otkrili 1419.g., danas autonomnu portugalsku regiju?": ["Azore","Zelenortske Otoke"],
"Koji je japanski samuraj predvodio diplomatsku misiju koja je od 1613.g. preko Tihog oceana, Meksika i Atlantika stigla sve do Španjolske i Rima?": ["Date Masamune","Sanada Yukimura"],
"Kako se naziva najveća vrsta slanog vodenog prostranstva na Zemlji?": ["More","Zaljev"],
"Kako se naziva kopno koje je sa svih strana okruženo vodom?": ["Poluotok","Atol"],
"Koji ocean moraju prijeći brodovi koji iz Europe plove izravno prema Americi?": ["Tihi ocean","Indijski ocean"],
"Kako se naziva istaknuti dio kopna koji duboko ulazi u more?": ["Poluotok","Prevaka"],
"Koje su otočje u atlantskom oceanu 1427.g. otkrili portugalci?": ["Madeiru","Zelenortske Otoke"],
"Portugalski je moreplovac Bartolomeu Dias, prolazeći uz južne obale Afrike 1488.g. doživio olujno nevrijeme uz jedan rt kojeg je kasnije nazvao Rt Oluja, no taj naziv je portugalski kraj Joao II. promijenio u koje ime koje stoji i danas, a tada je simboliziralo nadu da će se pomorski put prema Aziji ipak pronaći?": ["Rt Agulhas","Rt Svetog Vincenta"],
"Koji je norveški istraživač 1911.g. prvi stigao na Južni pol, pobijedivši britansku ekspediciju Roberta Falcona Scotta u jednoj od najpoznatijih polarnih utrka u povijesti?": ["Fridtjof Nansen","Otto Sverdrup"],
"Arheološki dokaz nordijskog boravka u Sjevernoj Americi pronađen je u L'Anse aux Meadowsu a to nalazište je danas na kojem kanadskom otoku?": ["Baffinov otok","Otok Cape Breton"],
"Magellanu se pripisuje ime jednog oceana, ali tijekom njegova prelaska posada nije imala pojma koliko je taj ocean golem. Koji je to ocean?": ["Atlantski ocean","Indijski ocean"],
"Koji je norveški istraživač namjerno dopustio da njegov brod Fram ostane zarobljen u arktičkom ledu, računajući da će ga morske struje zajedno s ledom odnijeti bliže Sjevernom polu?": ["Roald Amundsen","Otto Sverdrup"],
"Koji se tjesnac između japanskog otoka Hokkaida i ruskog Sahalina zove po francuskom istraživaču koji ga je kartirao 1787.g.?": ["Beringov tjesnac","Tsugaru tjesnac"],
}
count=0
for q in d:
    if q['question'] not in fix: continue
    correct=q['answers'][q['correct_answer']]
    wrong=fix[q['question']]
    vals=[]; wi=iter(wrong)
    for k in 'ABC':
        vals.append(correct if k==q['correct_answer'] else next(wi))
    q['answers']=dict(zip('ABC',vals)); count+=1
assert count==len(fix),(count,len(fix))
for q in d:
    a=q['answers']; assert set(a)==set('ABC') and q['correct_answer'] in a and len(set(a.values()))==3
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
open(p,'a',encoding='utf-8').write('\n')
print('fixed',count)
