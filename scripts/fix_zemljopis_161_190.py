import json
from pathlib import Path

p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))

items=[
('Koja rijeka, sa sjevera prema jugu, protječe kroz gotovo cijeli Pakistan?','Ind',['Ganges','Brahmaputra']),
('Koja država od 2023.g. nosi titulu najmnogoljudnije na svijetu?','Indija',['Kina','Indonezija']),
('Sa kojom državom Papua Nova Gvineja ima kopnenu granicu?','Indonezijom',['Australijom','Malezijom']),
('Koji grad je od nedavno zamijenio Malabo na mjestu glavnog grada Ekvatorijalne Gvineje?','Ciudad de la Paz',['Bata','Mongomo']),
('Koja država,jednim dijelom graniči i sa Slovenijom te Lihtenštajnom?','Austrija',['Švicarska','Italija']),
('Koja je valuta službeno sredstvo plaćanja u Moldaviji?','Lej',['Lev','Lari']),
('Najveći sustav podzemnih tunela, galerija i dvorana u Sloveniji, nastao prirodnim putem, dug je 24,12km a nalazi se u blizini kojeg grada, po kojem je i dobio ime?','Postojne',['Škocjana','Kranja']),
('Bolivijano je valuta koje države?','Bolivije',['Perua','Paragvaja']),
('Koju državu su stvorili Tanganjika i Zanzibar?','Tanzaniju',['Keniju','Mozambik']),
('Koja država graniči sa Nikaragvom i Panamom?','Kostarika',['Honduras','Salvador']),
('Pingvini se, iako poznati po staništima na Antartici te hladnim predjelima Čilea i Argentine, mogu pronaći i na kojem otočju u blizini zemljina ekvatora?','Galapagosa',['Falklanda','Juan Fernándeza']),
('U kojoj afričkoj državi se nalaze gradovi Ruiru, Nakuru i Eldoret?','Keniji',['Ugandi','Tanzaniji']),
('Prema legendi, na području koje današnje države je rođen Buda?','Nepala',['Indije','Butana']),
('Kako se zove glavni grad Haitija?','Port au Prince',['Santo Domingo','Kingston']),
('Koji je planinski vrh, sada u Sloveniji, bio najviši vrh bivše Jugoslavije?','Triglav',['Mangart','Grintovec']),
('Koja je planina kao dio Anda, sa 6 267m nadmorske visine, najviši vrh Ekvadora?','Chimborazo',['Cotopaxi','Cayambe']),
('Kojom državom je u potpunosti okružen Monako?','Francuskom',['Italijom','Španjolskom']),
('Tugrik je službena valuta koje države?','Mongolije',['Kazahstana','Kirgistana']),
('Koji je glavni grad Burkine Faso?','Ouagadougou',['Bamako','Niamey']),
('Koja rijeka izvire kod Krkonoša, protječe kroz Spindlerov Mlin i Dresden, te se iza Hamburga ulijeva u Sjeverno More?','Laba',['Odra','Rajna']),
('Republika Kongo svoj izlaz na more ima na koji ocean?','Atlantski Ocean',['Indijski Ocean','Tihi Ocean']),
('Koji je najmnogoljudniji grad u Kazahstanu, a nekada je bio i glavni grad te države?','Almati',['Astana','Šimkent']),
('Kojim imenom nazivamo tamnoputa plemena niskog rasta koja žive u tropskim šumama srednje Afrike?','Pigmeji',['Masaji','Tuarezi']),
('Koji je glavni grad Eswatinija?','Mbabane',['Maseru','Gaborone']),
('Kako se zove glavni grad Norveške?','Oslo',['Stockholm','Kopenhagen']),
('Koliko krakova ima zvijezda na zastavi Somalije?','5',['4','6']),
('São Tomé je glavni grad koje države?','Sveti Toma i Princip',['Zelenortski Otoci','Komori']),
('Kojim Antilima pripada Barbados?','Malim',['Velikim','Zavjetrinskim']),
('Port Vila je glavni grad koje države?','Vanuatua',['Fidžija','Samoae']),
('Koji je svetac, svoje mjesto pronašao i u imenu glavnog grada Antigve i Barbude?','Sveti Ivan',['Sveti Juraj','Sveti Petar']),
]

index={q['question']:q for q in d}
for question,correct,wrongs in items:
    assert question in index, question
    q=index[question]
    key=q['correct_answer']
    current=q['answers'][key]
    assert current==correct,(question,current,correct)
    it=iter(wrongs)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3

p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed',len(items),'questions 161-190 by question text')
