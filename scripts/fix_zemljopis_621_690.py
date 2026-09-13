import json
from pathlib import Path

p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))
anchor='Koju se državu često naziva i Letonijom?'
starts=[i for i,q in enumerate(d) if q.get('question')==anchor]
assert len(starts)==1,starts
start=starts[0]
wrong=[
['Litva','Estonija'],
['Prespansko','Skadarsko'],
['Ljubljana','Beograd'],
['Niger','Gambija'],
['Kiribatija','Samoa'],
['Kizilkum','Taklamakan'],
['Sultanat','Kalifat'],
['1','3'],
['Osaka','Kyoto'],
['Zaljev','Estuarij'],
['Medina','Rijad'],
['Plava','Crna'],
['Lyon','Marseille'],
['Kina','Turkmenistan'],
['Albertovog jezera','jezera Tana'],
['Rabat','Nikozija'],
['Uzbekistana','Kirgistana'],
['Hron','Nitra'],
['Castries','Roseau'],
['Kirgistanu','Kazahstanu'],
['Surinam','Gabon'],
['Port Vila','Apia'],
['Peruu','Ekvadoru'],
['Canberra','Brasilia'],
['Islam','Budizam'],
['Manat','Som'],
['Belgije','Nizozemske'],
['Douala','Libreville'],
['Monarhija','Federacija'],
['Mauricijusu','Komorima'],
['Baht','Kip'],
['Malta','Kreta'],
['La Paz','Quito'],
['Bahami','Barbados'],
['Ahu','Tiki'],
['Kolumbije','Ekvadora'],
['Sueski Kanal','Kielski Kanal'],
['Namibija','Zambija'],
['Okcident','Levanta'],
['Poljskom','Češkom'],
['Kolduny','Babka'],
['Öland','Saaremaa'],
['Dar','Deh'],
['3','5'],
['Kublaj-kana','Timura'],
['Azori','Kanarski Otoci'],
['Odra','Varta'],
['Ngorongoro','Tarangire'],
['Brno','Bratislava'],
['Latviji','Litvi'],
['Santiago de Cuba','Camagüey'],
['Lastovo','Vis'],
['Dominiki','Svetoj Luciji'],
['Kumasi','Lomé'],
['Španjolske','Italije'],
['Obala Bjelokosti','Togo'],
['Malabo','São Tomé'],
['Kina','Južna Koreja'],
['Estuarij','Delta'],
['Mauricijus','Komori'],
['Fidžija','Samoe'],
['Slovačke','Češke'],
['Petra','Wadi Mujib'],
['Čad','Tanganjika'],
['Amerigo Vespucci','Vasco da Gama'],
['Grčke','Malte'],
['Rusije','Uzbekistana'],
['Novom Zelandu','Ujedinjenom Kraljevstvu'],
['Lagos','Kano'],
['Norveška','Finska']
]
assert len(wrong)==70,len(wrong)
for off,pair in enumerate(wrong):
    q=d[start+off]
    key=q['correct_answer']
    correct=q['answers'][key]
    assert correct not in pair,(621+off,q['question'],correct,pair)
    it=iter(pair)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3,(621+off,q['question'],q['answers'])

p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed 70 questions 621-690')
