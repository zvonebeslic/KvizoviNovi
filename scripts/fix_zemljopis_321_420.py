import json
from pathlib import Path

p=Path('Zemljopis.json')
d=json.loads(p.read_text(encoding='utf-8'))
anchor="Čija linija razdvaja Pakistan od Afganistana?"
starts=[i for i,q in enumerate(d) if q.get('question')==anchor]
assert len(starts)==1,starts
start=starts[0]
wrong=[
['Radcliffeova','McMahonova'],['Davisov','Danski'],['Irak','Irska'],['Bijela','Zelena'],['Bodensko Jezero','Jezero Maggiore'],['Arktičkom','Indijskom'],['Niger','Mali'],['Gruzije','Kazahstana'],['Alžira','Libije'],['Latvije','Litve'],['Bahrein','Ujedinjeni Arapski Emirati'],['Surinam','Venezuela'],['Tahiti','Pitcairn'],['Bugarske','Mađarske'],['Lamanai','Caracol'],['Pileus','Tricorne'],['Novom Muzeju','Bodeovu Muzeju'],['Sudanu','Etiopiji'],['Tajlanda','Nepala'],['Limpopo','Zambezi'],['Kolumbija','Bolivija'],['Kamerun','Republika Kongo'],['Sveta Lucija','Grenada'],['Kostarike','Nikaragve'],['Bjelorusije','Ukrajine'],['Gambija','Niger'],['Sveta Lucija','Martinique'],['Sardinije','Trentina-Južnog Tirola'],['Aralskog','Crnog'],['Kanarskom Otočju','Pitiuškom Otočju'],['Amsterdamu','Rotterdamu'],['Sumatri','Sulawesiju'],['Abomey','Parakou'],['Koror','Melekeok'],['Austriju','Hrvatsku'],['Kopenhagen','Helsinki'],['Bengazi','Tunis'],['Katanga','Kongo-Léopoldville'],['Nanga Parbat','Gasherbrum I'],['Tbilisi','Erevan'],['Andora','Vatikan'],['Luksemburg','Andora'],['Peru','Bolivija'],['Trinidad i Tobago','Sveta Lucija'],['Azija','Južna Amerika'],['Tadžikistana','Kazahstana'],['Hrvatske','Slovačke'],['Rusiji','Azerbajdžanu'],['Tenge','Manat'],['Češkoj','Slovačkoj'],['Sofija','Vilnius'],['Quetzal','Córdoba'],['Ohridsko Jezero','Prespansko Jezero'],['Mumbai','Kolkata'],['Dalmacije','Istre'],['Karakum','Kumtag'],['Douro','Guadiana'],['Kosovo','Zapadnu Saharu'],['Tarawa','Palikir'],['Andoru','Lihtenštajn'],['Riga','Vilnius'],['Titicaca','Poopó'],['Juan Fernández','Chiloé'],['Portugala','Italije'],['Managua','San Salvador'],['Bahami','Barbados'],['Emalangeni','Pula'],['Lima','Buenos Aires'],['Katla','Hekla'],['Kinshasa','Libreville'],['Australiji','Samoa'],['Sveta Lucija','Barbados'],['Kalahari','Sahara'],['Beira','Nampula'],['Somalija','Mozambik'],['Nepalu','Indiji'],['Tiber','Arno'],['Norveške','Danske'],['Crni Drim','Strumica'],['Butan','Švicarska'],['Rotterdam','Haag'],['Sejšeli','Maršalovi Otoci'],['Kalahari','Namib'],['Čukotka','Tajmir'],['Soufrière Hills','Mount Pelée'],['Choquequirao','Ollantaytambo'],['Rusijom','Kazahstanom'],['Omanu','Somaliji'],['Parnas','Helikon'],['Albanije','Sjeverne Makedonije'],['Tadžikistan','Turkmenistan'],['Polumjesec','Zvijezda'],['Fumarole','Solfatare'],['Peloponez','Halkidiki'],['Kantabrijskim gorjem','Sierra Nevadom'],['Senegala','Gambije'],['Montego Bay','Spanish Town'],['Beninski','Biafranski'],['Lav','Koza'],['Zimbabvea','Zambije']
]
assert len(wrong)==100,len(wrong)
for off,pair in enumerate(wrong):
    q=d[start+off]
    key=q['correct_answer']
    correct=q['answers'][key]
    it=iter(pair)
    q['answers']={k:(correct if k==key else next(it)) for k in ('A','B','C')}
    assert len(set(q['answers'].values()))==3,(321+off,q['question'],q['answers'])

# QA napomene bez mijenjanja izvornog točnog odgovora.
for off,note in {
16:'Pergamski muzej u Berlinu zatvoren je zbog velike obnove; pitanje se odnosi na muzej i njegove zbirke, a izvorni odgovor ostavljen je netaknut.',
57:'Status Palestine i međunarodno priznanje razlikuju se među državama; izvorni odgovor ostavljen je netaknut.',
}.items(): d[start+off]['qa_note']=note

p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('fixed 100 questions 321-420')
