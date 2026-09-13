import json
from pathlib import Path
p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))
anchor='Koja velika azijska rijeka velikim dijelom čini granicu između Tajlanda i Laosa?'
starts=[i for i,q in enumerate(d) if q.get('question')==anchor]
assert len(starts)==1,starts
start=starts[0]
wrong=[
['Salween','Chao Phraya'],['Tahiti','Pitcairn'],['Južnoafričkoj Republici','Maroku'],['Mbabane','Gaborone'],['Chania','Rethymno'],['Grenade','Dominike'],['Malezije','Filipina'],['Bugarski','Ukrajinski'],['Afganistanu','Pakistanu'],['Japana','Južne Koreje'],['Južnoafričke Republike','Sijera Leonea'],['Irkutskom','Habarovskom'],['Austrije','Mađarske'],['Omanskog','Adenskog'],['Taklamakan','Karakum'],['Japana','Kine'],['Car rapide','Taptap bus'],['Mali','Togo'],['Kikuyu','Amharski'],['Belgije','Luksemburga'],['Eritreji','Somaliji'],['Casablanca','Marrakech'],['Krakatau','Merapi'],['Namibiji','Bocvani'],['Latvija','Litva'],['Mezopotamija','Anatolija'],['Latvija','Litva'],['Daugava','Neman'],['Amharski','Tigrinja'],['Vaduz','Bruxelles'],['Iberski','Balkanski'],['Beču','Pragu'],['Pančen Lama','Karmapa'],['Jednu','Tri'],['Kivi','Kasuari'],['Australiju','Samoa'],['Liffey','Barrow'],['Sparti','Korintu'],['Strasbourg','Luxembourg'],['Tanganjika','Edwardovo jezero'],['Doha','Kuwait City'],['Bospor','Dardaneli'],['Slovačke','Poljske'],['Mjanmar','Kambodža'],['Benina','Gane'],['Won','Jen'],['Sao Tome i Principe','Gvineja Bisau'],['Plava','Žuta'],['Eswatini','Bocvana'],['Kalahari','Namib'],['Gagauzija','Abhazija'],['Port-au-Prince','Havana'],['Hrvatske','Bugarske'],['Bamako','Freetown'],['Eritreja','Somalija'],['Vilnius','Tallinn'],['Rumunjskoj','Grčkoj'],['Kenija','Uganda'],['Juba','Kampala'],['Kairo','Juba'],['San Marina','Lihtenštajna'],['Oslo','Stockholm'],['Tonga','Samoa'],['Bolivije','Ekvadora'],['Armenije','Azerbajdžana'],['Jordana','Tunisa'],['Viktorijino jezero','Jezero Malawi'],['Alpama','Karpatima'],['Sejšele','Mauricijus'],['Kalahari','Namib'],['Abu Dhabi','Sharjah'],['Madeira','Kanarski Otoci'],['Kinom','Mongolijom'],['Nikaragva','Honduras'],['Eswatini','Bocvana'],['Malé','Colombo'],['Maldivi','Madagaskar'],['God Save the King','Hino Nacional Brasileiro'],['Bolivijom','Peruom'],['Amazon','Nil'],['Doha','Muscat'],['Tel Aviv','Amman'],['Sydney','Canberra'],['Finskom','Rusijom'],['Japana','Južne Koreje'],['Panama','Kostarika'],['Bahrein','Katar'],['Shanghai','Guangzhou'],['Italije','Švicarske'],['Auckland','Christchurch'],['Quito','Lima'],['Sarez','Iskanderkul'],['5','6'],['Liberije','Gvineje'],['Bruneja','Indonezije'],['Sol','Boliviano'],['Zambija','Mozambik'],['Azovsko More','Kaspijsko jezero'],['Aralskom jezeru','Urmijskom jezeru'],['Libanon','Karmel']
]
assert len(wrong)==100,len(wrong)
for off,pair in enumerate(wrong):
    q=d[start+off]
    key=q['correct_answer']
    correct=q['answers'][key]
    assert correct not in pair,(421+off,q['question'],correct,pair)
    it=iter(pair)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3,(421+off,q['question'],q['answers'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed 100 questions 421-520')
