import json
from pathlib import Path

p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))

items=[
("Koja je porodica iz reda primata, endemična za otok Madagaskar?","Lemuri",["Loriji","Galagosi"]),
("Koja afrička država ima najdužu obalu na Sredozemnom Moru?","Libija",["Egipat","Tunis"]),
("Otoci Mahe, Praslin i La Digue se nalaze u sastavu koje otočne države u Indijskom Oceanu?","Sejšela",["Mauricijusa","Komora"]),
("Koja je službena valuta u Papua Novoj Gvineji, a njeno ime biste mogli lako vidjeti na hrvatskom izdanju zemljovida Azije?","Kina",["Tala","Vatu"]),
("Kako se zove glavni grad Lihtenštajna?","Vaduz",["Bern","Luxembourg"]),
("Koja država kao svoj internetski nastavak koristi 'de'","Njemačka",["Danska","Austrija"]),
("Koja se dva slova, za službeni internetski nastavak, koriste u državi Lesoto?","Ls",["Sz","Bw"]),
("Kako se zove glavni grad Gvineje Bisau?","Bissau",["Conakry","Banjul"]),
("Osim u Kaliforniji, planinski lanac Sierra Nevada na kartama možemo još pronaći i u kojoj europskoj državi?","Španjolskoj",["Portugalu","Francuskoj"]),
("Laraha ili gorka naranča je voće koje se može vidjeti i na grbu koje malene karipske države?","Curacao",["Arube","Barbadosa"]),
("Kruna sv. Stjepana se nalazi na grbu koje europske države?","Mađarske",["Slovačke","Hrvatske"]),
("Kako se zove velika morska luka u Ateni?","Pirejska Luka",["Rafina","Lavrio"]),
("Koja je službena valuta u Gani?","Cedi",["Naira","Dalasi"]),
("Koji prolaz dijeli Maleziju od Indonezijske Sumatre?","Malajski",["Sundski","Makassarski"]),
("Koji je glavni grad Saudijske Arabije?","Riyad",["Jeddah","Mecca"]),
("'bj' je nacionalna internetska domena za koju državu?","Benin",["Burundi","Burkina Faso"]),
("Singapur je glavni grad koje države?","Singapura",["Bruneja","Malezije"]),
("Ringit je službeno sredstvo plaćanja u kojoj državi?","Maleziji",["Indoneziji","Bruneju"]),
("Oresundski Most povezuje Kopenhagen u Danskoj sa kojim gradom u Švedskoj?","Malmo",["Göteborg","Helsingborg"]),
("'Teba' je bila beotska grad-država na području koje današnje države?","Grčke",["Turske","Albanije"]),
("'Lo Stivale' je pojam kojim se opisuje koji poluotok?","Apeninski",["Iberski","Balkanski"]),
("Koji uski prolaz u središnjoj grčkoj najčešće vežemo uz Leonidu i Kserksa?","Termopil",["Korintski prolaz","Tempe"]),
("Najveći dio toka Nila prolazi kroz koju državu?","Sudan",["Egipat","Etiopiju"]),
("Koja je najzapadnija država Afrike ako teritorijalno uračunamo i sve afričke otoke?","Zelenorski Otoci",["Senegal","Gambija"]),
("Panamski kanal se nalazi unutar granica koje države?","Paname",["Kostarike","Kolumbije"]),
("Države San Marino i Vatikan potpuno su omeđeni granicama koje države?","Italije",["Francuske","Švicarske"]),
("Koji naziv se koristio za rezervate dodijeljene crnačkom domorodačkom stanovništvu za vrijeme Apartheida po nekadašnjoj Južnoafričkoj Uniji i Namibiji?","Bantustan",["Protektorat","Rezervat"]),
("Mala karipska država Antigva i Barbuda se sastoji od 3 otoka. Prva dva se nalaze u imenu države, a koji je treći, najmanji i nenaseljen otok, vulkanskog porijekla?","Redonda",["Montserrat","Anguilla"]),
("Kojom današnjom državom je vladao komunistički pokret Crveni Kmeri?","Kambodžom",["Laosom","Vijetnamom"]),
("Kako se zove glavni grad Mađarske?","Budimpešta",["Bratislava","Bukurešt"]),
]

seen=set()
for question,correct,wrong in items:
    matches=[q for q in d if q.get('question')==question]
    assert len(matches)==1,(question,len(matches))
    q=matches[0]
    key=q['correct_answer']
    assert q['answers'][key]==correct,(question,key,q['answers'][key],correct)
    it=iter(wrong)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3
    seen.add(question)
assert len(seen)==30
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed',len(items),'questions 191-220')
