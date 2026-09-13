import json
from pathlib import Path

p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))
anchor="Koji je glavni grad Austrije?"
starts=[i for i,q in enumerate(d) if q.get('question')==anchor]
assert len(starts)==1, starts
start=starts[0]

correct=[
'Beč','Maršalovi Otoci','Burkine Faso','Bled','Latinskog','Nauru','Somalija','Čehoslovačke','Malim','Peloponeskog Poluotoka',
'Galapagos','Južnoafrička Republika','Estonijom','Tuvalu','Rusija','Juba','Bosna i Hercegovina','Guadalcanal','Senegal','Leone',
'Bospor','Tiber','Amman','Roseau','Kina','Brazzaville','Libije','Sirije','Gitega','Robinson Crusoe',
'Malte','Niger','Natron','Peso','Massai Mara','Banjul','Andorra la Vella','Italije','Transilvanija','Ukrajini',
'Teheran','Rim','Nouakchott','Norveškoj','Albaniji','Perzijskom','Crvene','Libanon','Addis Abeba','Monako',
'Svahili','Abelu Tasmanu','Dong','Rombu','Irske','Guatemala City','Volga','Uganda','Kalahari','Jemena',
'Monrovia','Haiti','Njemački','Kapadokija','Pjongjang','Karipsko','Slovenija','Zapadna Sahara','Filipina','Belize',
'Rusija','Sarajevo','Ukrajine','Odense','Južno Kinesko More','Biškek','Džibuti','Crveno More','Plava','Berlina',
'Angole','Irak','Rusijom','Indiji','Kanade','Praia','El Salvador','Surinam','Mauricijusa','Zelenorski Otoci',
'Oaza','Tongu','Ciudad de Mexico','Hekla','Arapsko More','Mali','Sredozemnom','Iravadi','Senegala','Mount Everest'
]
wrong=[
['Prag','Bratislava'],['Solomonski Otoci','Cookovi Otoci'],['Mali','Niger'],['Bohinj','Cerknica'],['Grčkog','Staroslavenskog'],['Tuvalu','Kiribati'],['Džibuti','Eritreja'],['Austro-Ugarske','Slovačke'],['Velikim','Bahamskim'],['Atičkog Poluotoka','Halkidikija'],
['Juan Fernandez','Revillagigedo'],['Lesoto','Esvatini'],['Latvijom','Švedskom'],['Tonga','Kiribati'],['Kanada','Kina'],['Khartoum','Addis Abeba'],['Slovenija','Mađarska'],['Malaita','Nova Georgia'],['Gambija','Niger'],['Dalasi','Naira'],
['Dardaneli','Kerčki prolaz'],['Arno','Po'],['Beirut','Damask'],['Castries','Kingstown'],['Rusija','Sjedinjene Američke Države'],['Kinshasa','Libreville'],['Tunisa','Alžira'],['Libanona','Jordana'],['Kigali','Bujumbura'],['Lemuel Gulliver','Sinbad'],
['Cipra','Grčke'],['Senegal','Kongo'],['Turkana','Eyasi'],['Quetzal','Sol'],['Amboseli','Tsavo'],['Kunta Kinteh','Janjanbureh'],['Escaldes-Engordany','Encamp'],['Francuske','Španjolske'],['Vlaška','Moldavija'],['Moldaviji','Rumunjskoj'],
['Tabriz','Isfahan'],['Milano','Napulj'],['Nouadhibou','Bamako'],['Švedskoj','Finskoj'],['Srbiji','Sjevernoj Makedoniji'],['Omanskom','Adenskom'],['Zelene','Bijele'],['Jordan','Cipar'],['Asmara','Nairobi'],['Bahrein','Singapur'],
['Arapski','Francuski'],['Jamesu Cooku','Willemu Janszoonu'],['Kip','Baht'],['Trokutu','Kvadratu'],['Islanda','Malte'],['San Salvador','Tegucigalpa'],['Dunav','Dnjepar'],['Ruanda','Kenija'],['Namib','Karoo'],['Omana','Jordana'],
['Freetown','Banjul'],['Honduras','Gvatemala'],['Francuski','Talijanski'],['Likija','Pamfilija'],['Seul','Ulaanbaatar'],['Sargaško','Sredozemno'],['Slovačka','Hrvatska'],['Azawad','Kabinda'],['Indonezije','Malezije'],['Meksiko','Honduras'],
['Bjelorusija','Poljska'],['Skoplje','Podgorica'],['Bjelorusije','Moldavije'],['Kopenhagen','Aarhus'],['Sulu More','Javsko More'],['Taškent','Dušanbe'],['Asmara','Mogadiš'],['Sredozemno More','Adenski Zaljev'],['Zelena','Crvena'],['Beča','Münchena'],
['Namibije','Mozambika'],['Jordan','Iran'],['Švedskom','Norveškom'],['Nepalu','Šri Lanki'],['Sjedinjenih Američkih Država','Rusije'],['Mindelo','Bissau'],['Gvatemala','Honduras'],['Gvajana','Francuska Gvajana'],['Sejšela','Komora'],['Komori','Sveti Toma i Princip'],
['Vadi','Slana ravnica'],['Samoa','Fidži'],['Guadalajara','Monterrey'],['Katla','Grimsvötn'],['Crveno More','Andamansko More'],['Togo','Benin'],['Crvenom Moru','Crnom Moru'],['Salween','Sittaung'],['Mauritanije','Malija'],['Annapurna','Manaslu']
]
assert len(correct)==100 and len(wrong)==100

for off in range(100):
    q=d[start+off]
    key=q['correct_answer']
    cur=q['answers'][key]
    exp=correct[off]
    assert cur==exp,(221+off,q.get('question'),key,cur,exp)
    it=iter(wrong[off])
    q['answers']={k:(exp if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3

# Izvorni odgovor ostaje netaknut, ali bilježimo povijesno/zastarjelo formulirana pitanja.
d[start+5]['qa_note']='Nauru nema službeno proglašen glavni grad; Yaren se u praksi navodi kao de facto sjedište vlade. Izvorni odgovor "Nauru" ostavljen je netaknut.'
d[start+19]['qa_note']='SLL je stara oznaka leonea prije redenominacije 2022.; nova valuta koristi oznaku SLE. Izvorni odgovor "Leone" ostavljen je netaknut.'

p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed 100 questions 221-320')
