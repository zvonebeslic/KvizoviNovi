import json
from pathlib import Path

p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))
anchor='U kojoj državi se nalazi grad Tripoli?'
starts=[i for i,q in enumerate(d) if q.get('question')==anchor]
assert len(starts)==1,starts
start=starts[0]
wrong=[
['Siriji','Jordanu'],
['Majuro','Tarawa'],
['Almaty','Biškek'],
['Aso','Ontake'],
['Sudan','Somalija'],
['Ubangi','Kasai'],
['Bayuda pustinja','Libijska pustinja'],
['Polineziji','Mikroneziji'],
['Athi-Galana-Sabaki','Ewaso Ng\'iro'],
['Stockholm','Riga'],
['Mauricijusa','Komora'],
['Addis Abeba','Džibuti'],
['Tiraspol','Bukurešt'],
['Mana','Aloha'],
['Niamey','Bangui'],
['Kazahstana','Kirgistana'],
['Maliju','Nigeru'],
['Oulu','Kemi'],
['Togu','Obali Bjelokosti'],
['Hadrijanov zid','Berlinski zid'],
['Bosni i Hercegovini','Albaniji'],
['Limpopo','Kafue'],
['Victoria','Moroni'],
['Madagaskara','Réuniona'],
['Samoa','Tuvalu'],
['Češke','Slovačke'],
['Tanzanija','Mozambik'],
['Tikal','Palenque'],
['Baja California','Nicoya'],
['Naira','Kwacha'],
['Watzmann','Brocken'],
['Dinar','Dirham'],
['Ural','Taurus'],
['Bože pravde','Zdravljica'],
['Poopó','Junín'],
['Jordana','Libanona'],
['Urugvaj','Čile'],
['Brahmaputra','Meghna'],
['Atena','Tirana'],
['Monarhija','Federacija'],
['Marija Petković','Žarka Ivasić'],
['Alajuela','Heredia'],
['Gvajana','Francuska Gvajana'],
['Laosa','Kambodže'],
['Pakistan','Bangladeš'],
['Belgija','Danska'],
['Kuba','Puerto Rico'],
['Bayon','Banteay Srei'],
['Saint-Barthélemy','Anguilla'],
['Australije','Ujedinjenog Kraljevstva'],
['Bandung','Surabaya'],
['Malezije','Indonezije'],
['Gaborone','Lusaka'],
['Sueski Kanal','Korintski Kanal'],
['Jonsko','Jadransko'],
['Gobi','Taklamakan'],
['Somalija','Eritreja'],
['Armenije','Azerbajdžana'],
['Basutoland','Bechuanaland'],
['San Marina','Monaka'],
['Kina','Laos'],
['3','5'],
['Filipinsko More','Molučko More'],
['Beringovo More','Japansko More'],
['Samoe','Fidžija'],
['Zimbabvea','Malavija'],
['Ekoturizam','Trekking'],
['Leone','Cedi'],
['Taškent','Biškek'],
['Apia','Nukuʻalofa']
]
assert len(wrong)==70,len(wrong)
for off,pair in enumerate(wrong):
    q=d[start+off]
    key=q['correct_answer']
    correct=q['answers'][key]
    assert correct not in pair,(551+off,q['question'],correct,pair)
    it=iter(pair)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3,(551+off,q['question'],q['answers'])

notes={
0:'Pitanje je dvosmisleno jer postoje gradovi Tripoli i u Libanonu i u Libiji; izvorni odgovor "Libanonu" ostavljen je netaknut.',
16:'Mauritanija je afrička, a ne azijska država; izvorni odgovor ostavljen je netaknut.',
47:'Filmske scene iz Tomb Raidera snažno se povezuju s hramom Ta Prohm unutar kompleksa Angkor; izvorni odgovor "Angkor Wat" ostavljen je netaknut.'
}
for off,note in notes.items():
    d[start+off]['qa_note']=note

p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed 70 questions 551-620')
