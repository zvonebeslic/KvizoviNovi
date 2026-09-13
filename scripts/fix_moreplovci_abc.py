import json, random, re
p='Moreplovci.json'
d=json.load(open(p,encoding='utf-8'))

pools={
'person_pt':['Afonso de Noronha','Duarte de Meneses','Gonçalo de Ataíde','Lourenço de Almeida','Simão de Miranda','António de Saldanha','Manuel de Sousa','Rui de Sequeira','Fernão de Andrade','Estêvão da Gama','João de Serpa'],
'person_es':['Alonso de Córdoba','Diego de Valderrama','Hernando de Villalba','Rodrigo de Salazar','Gonzalo de Montalvo','Martín de Quesada','Álvaro de Sotomayor','Juan de Escalante','Pedro de Alarcón','Francisco de Villaseñor','Sebastián de Aranda','Tomás de Villacorta','Mateo de Villalobos'],
'person_fr':['Étienne Moreau','Jacques de Villeneuve','Pierre de Montfort','Louis de Keradec','René de Beaumont','Claude de Marigny','Henri de Rochefort','Nicolas de Varenne','Henri de Montreuil'],
'person_en':['Thomas Cavendish','Martin Frobisher','John Hawkins','Humphrey Gilbert','Richard Grenville','William Dampier','George Anson','Edward Fenton','John Davis','Henry Every','Robert Harcourt','Edward Blackwell','Richard Hargreaves'],
'person_nl':['Willem Barentsz','Jacob Roggeveen','Willem Schouten','Cornelis de Houtman','Jacob van Heemskerck','Joris van Spilbergen','Pieter de Carpentier','Pieter van der Meer'],
'person_generic':['Lorenzo de Acosta','João de Serpa','Nicolas de Beaumont','Mateo de Villalobos','Sebastián de Aranda','Edward Blackwell','Pieter van der Meer','Henri de Montreuil','Richard Hargreaves','Tomás de Villacorta'],
'women':['Anne Bonny','Grace O’Malley','Charlotte de Berry','Jacquotte Delahaye','Sayyida al Hurra','Ching Shih','Rachel Wall','Mary Critchett','Anne Dieu-le-Veut'],
'ships':['Adventure','Resolution','Endeavour','Providence','Golden Hind','Revenge','Sea Venture','Dreadnought','Mercury','Royal Fortune','São Gabriel','Victoria','Trinidad','Santiago','San Antonio','Dauphin','Pelican','HMS Pandora','Fancy'],
'islands':['Madeira','Tenerife','Curaçao','Martinique','Guadeloupe','Barbados','Dominika','Samoa','Tahiti','Guam','Cebu','Borneo','Timor','Mauricijus','Réunion','Socotra','Zanzibar','Rhode Island','Vanikoro'],
'cities':['Cartagena','Havana','Veracruz','San Juan','Santo Domingo','Lisabon','Sevilla','Cádiz','Porto','Nantes','Bristol','Plymouth','Amsterdam','Malacca','Goa','Acapulco','Calicut','Nassau','Ciudad de México','Lepant'],
'countries':['Portugal','Španjolska','Engleska','Francuska','Nizozemska','Italija','Danska','Norveška'],
'continents':['Afrika','Azija','Europa','Sjeverna Amerika','Južna Amerika','Australija'],
'waters':['Atlantski ocean','Tihi ocean','Indijski ocean','Arktički ocean','Sredozemno more','Karipsko more','Crveno more','Hudsonov zaljev','Zaljev Chesapeake'],
'places':['Rt Dobre nade','Magellanov prolaz','Hormuški tjesnac','Gibraltarski tjesnac','Mozambički kanal','Biskajski zaljev','Hudsonov zaljev','La Manche','Torresov prolaz','Drakeov prolaz','Hormuz','Thule'],
'canals':['Panamski kanal','Sueski kanal','Kielski kanal','Korintski kanal'],
'spices':['Cimet','Muškatni oraščić','Klinčić','Šafran','Kardamom','Đumbir','Piment'],
'nautical':['Pramac','Kobilica','Paluba','Jarbol','Kormilo','Sidro','Oputa','Kormilarnica','Nadgrađe','Bok','Krma'],
'groups':['Flota','Eskadra','Konvoj','Armada','Posada','Eskadrila'],
'concepts':['Rekonkvista','Merkantilizam','Kolonijalizam','Kaperstvo','Piratstvo','Kartografija','Navigacija','Trgovinski monopol','Pomorska blokada'],
'dynasties':['Ming','Qing','Yuan','Song','Tang'],
'animals':['Konj','Deva','Mazga','Slon','Pas'],
'objects':['Dalekozor','Sekstant','Astrolab','Kompas','Kronometar'],
'roles':['Navigator','Kormilar','Kartograf','Kapetan','Pilot'],
'wars':['Osamdesetogodišnji','Sedmogodišnji','Tridesetogodišnji','Stogodišnji'],
'depths':['Challengerova dubina','Sirena Deep','Horizon Deep','Brownson Deep'],
'woods':['Pau brasil','Mahagonij','Ebanovina','Tikovina','Palisandar'],
'directions':['Sjever','Jug','Istok','Zapad'],
}

# exact correct-answer type hints, used before question wording
answer_type={
 'Krma':'nautical','Paluba':'nautical','Jarbol':'nautical','Flota':'groups','Afrika':'continents',
 'La Manche':'places','Kuba':'islands','Vanikoro':'islands','St. Augustine':'cities','Rekonkvista':'concepts',
 'Papar':'spices','Pau brasil':'woods','Discovery':'ships','Fancy':'ships','São Gabriel':'ships',
 'Španjolska':'countries','Portugal':'countries','Tihi ocean':'waters','Panamski kanal':'canals',
 'Dalekozor':'objects','Hormuz':'places','Thule':'places','Nassau':'cities','Calicut':'cities',
 'Konj':'animals','Zaljev Chesapeake':'waters','Ming':'dynasties','Navigator':'roles',
 'Osamdesetogodišnji':'wars','Rhode Island':'islands','Lepant':'cities','HMS Pandora':'ships',
 'Madiera':'islands','Challengerova dubina':'depths','Ocean':'waters','Zapad':'directions'
}

def classify(q,c):
 ql=q.lower(); cl=c.lower()
 if c in answer_type: return answer_type[c]
 # Strong question-shape rules first
 if 'koji se kontinent' in ql or 'kojem kontinent' in ql: return 'continents'
 if 'iz koje je europske zemlje' in ql or 'koja je europska kraljevina' in ql or 'iz koje zemlje' in ql: return 'countries'
 if 'koji ocean' in ql or 'koje more' in ql or 'kojem zaljevu' in ql or 'koji zaljev' in ql: return 'waters'
 if 'koji je grad' in ql or 'kojeg grada' in ql or 'koja se metropola' in ql or 'koja luka' in ql or 'koju je važnu trgovačku luku' in ql: return 'cities'
 if 'koji kanal' in ql or 'plovni put' in ql: return 'canals'
 if 'koji je brod' in ql or 'kako se zvao brod' in ql or 'kako se zvao glavni brod' in ql or 'gusarski brod' in ql: return 'ships'
 if 'koji optički predmet' in ql or 'koji predmet' in ql: return 'objects'
 if 'koja je životinja' in ql: return 'animals'
 if 'koja je kineska dinastija' in ql: return 'dynasties'
 if 'kako se naziva osoba' in ql: return 'roles'
 if 'u kojem dugotrajnom ratu' in ql or 'u kojem ratu' in ql: return 'wars'
 if 'najdublja poznata točka' in ql: return 'depths'
 if 'prema kojoj je strani svijeta' in ql: return 'directions'
 if 'po kojem je crvenkastom drvu' in ql: return 'woods'
 if 'kako se naziva stražnji dio broda' in ql or 'površina broda' in ql or 'stup na brodu' in ql: return 'nautical'
 if 'velika skupina brodova' in ql: return 'groups'
 if 'otok' in ql or 'otočje' in ql: return 'islands'
 if any(x in ql for x in ['prolaz','tjesnac','rt ','ulazu u perzijski zaljev']): return 'places'
 if 'začin' in ql: return 'spices'
 if any(x in ql for x in ['žena','gusarica','botaničarka','kći erika crvenog','zapovjednica']): return 'women'
 # Nationality/person rules
 if any(x in ql for x in ['portugalski','portugalac']): return 'person_pt'
 if any(x in ql for x in ['španjolski','konkvistador']): return 'person_es'
 if any(x in ql for x in ['francuski','francuz']): return 'person_fr'
 if any(x in ql for x in ['nizozemski','nizozemac','flamanski']): return 'person_nl'
 if any(x in ql for x in ['engleski','britanski','škotski','velški']): return 'person_en'
 if any(x in ql for x in ['moreplovac','istraživač','pomorac','kapetan','gusar','admiral','zapovjednik','kartograf','matematičar','kozmograf','franjevac','potkralj','samuraj','sudionik']): return 'person_generic'
 if any(x in ql for x in ['kako se naziva','popularno nazivala','popularan naziv']): return 'concepts'
 return 'concepts'

rng=random.Random(73193)
used={k:0 for k in pools}
for i,x in enumerate(d):
 ca=x['correct_answer']; correct=x['answers'][ca]
 k=classify(x['question'],correct)
 cand=[z for z in pools[k] if z.casefold()!=correct.casefold()]
 start=(used[k]*2+i)%len(cand); used[k]+=1
 wrong=[]
 for j in range(len(cand)):
  z=cand[(start+j)%len(cand)]
  if z.casefold()!=correct.casefold() and z not in wrong: wrong.append(z)
  if len(wrong)==2: break
 for letter,z in zip([a for a in 'ABC' if a!=ca],wrong): x['answers'][letter]=z
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
open(p,'a',encoding='utf-8').write('\n')
print('processed',len(d))
