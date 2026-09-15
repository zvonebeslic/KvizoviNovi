import json
from pathlib import Path
p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))
fixes={
"Koju državu stanovnici Paragvaja poznaju kao 'Pindorama'?":['Argentina','Bolivija'],
"Angkor Wat je najveći religijski objekat na svijetu. Prostire se na 1,6km² i djeluje kao cijeli grad. Ponos je tog naroda, pa se tako našao i na nacionalnoj zastavi koje države?":['Tajlanda','Laosa'],
"Koji se planinski lanac Karpata, najviše prostire na području Slovačke?":['Beskidi','Fatra'],
"Koji kanal prolazi između Madagaskara i afričkog kopna?":['Zanzibarski kanal','Pemba kanal'],
"Koja azijska država nema ni jednu susjednu zemlju sa izlazom na more?":['Mongolija','Nepal'],
"Državu Trinidad i Tobago čine dva otoka, a veći je koji?":['Tobago','Grenada'],
"Japan se sastoji od tisuća otoka a četiri najveća su Hokkaido, Honshu, Shikoku i koji još?":['Okinawa','Sado'],
"Turizam koje države je procvao nakon Gospodara Prstenova?":['Australije','Islanda'],
"Peru se danas smatra domovinom kojeg drevnog latinskog naroda?":['Maja','Asteka'],
"Pont Neuf,  Pont au Change, Pont au Double i Petit Pont su mostovi koji povezuju koji europski grad?":['Lyon','Toulouse'],
"Kako se zove glavni grad Iraka?":['Damask','Amman'],
"Ime koje se rijeke, koja najvećim dijelom protječe kroz Malavi, može pronaći i na karti Međuzemlja, J. R. R. Tolkien?":['Anduin','Brandywine'],
"Najviši vulkan u Europi pripada Španjolskoj, nalazi se na Kanarima, visok je 3718m a zove se kako?":['Etna','Stromboli'],
"Apia je glavni grad koje države?":['Tonga','Fidži'],
"Organizacija CARICOM je zajednica 15 karipskih naroda sa sjedištem u kojoj državi?":['Barbadosu','Trinidadu i Tobagu'],
"Koju državu možemo pronaći i na popisu parafina?":['Propan','Pentan'],
"Kojom rijekom su povezani Managua i Nikaragva, dva najveća jezera države Nikaragve?":['San Juan','Escondido'],
"Koja velika rijeka čini granicu između Lihtenštajna i Švicarske?":['Dunav','Inn'],
"Koje more su 'zarobili' tjesnaci Bospor i Dardaneli?":['Crno More','Egejsko More'],
"Keren, Teseney i Assab su gradovi koje države?":['Etiopije','Džibutija'],
"Koji se morski tjesnac nalazi u blizini Bospora?":['Kerčki tjesnac','Otrantska vrata'],
"U kojem zaljevu, Benin ima izlaz na Atlantski ocean?":['Beninskom','Biafranskom']
}
idx={q.get('question'):q for q in d}
for text,wrong in fixes.items():
    assert text in idx,text
    q=idx[text]; key=q['correct_answer']; correct=q['answers'][key]
    assert correct not in wrong,(text,correct,wrong)
    it=iter(wrong)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3,(text,q['answers'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed',len(fixes),'exact tail questions')
