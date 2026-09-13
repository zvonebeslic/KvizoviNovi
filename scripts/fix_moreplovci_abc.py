import json, random, re
p='Moreplovci.json'
d=json.load(open(p,encoding='utf-8'))
# Carefully chosen broad pools. We keep every original question and its original correct-answer text.
pools={
'person_pt':['Afonso de Noronha','Duarte de Meneses','Gonçalo de Ataíde','Lourenço de Almeida','Simão de Miranda','António de Saldanha','Manuel de Sousa','Rui de Sequeira','Fernão de Andrade','Estêvão da Gama'],
'person_es':['Alonso de Córdoba','Diego de Valderrama','Hernando de Villalba','Rodrigo de Salazar','Gonzalo de Montalvo','Martín de Quesada','Álvaro de Sotomayor','Juan de Escalante','Pedro de Alarcón','Francisco de Villaseñor'],
'person_fr':['Étienne Moreau','Jacques de Villeneuve','Pierre de Montfort','Louis de Keradec','René de Beaumont','Claude de Marigny','Henri de Rochefort','Nicolas de Varenne'],
'person_en':['Thomas Cavendish','Martin Frobisher','John Hawkins','Humphrey Gilbert','Richard Grenville','William Dampier','George Anson','Edward Fenton','John Davis','Henry Every'],
'person_nl':['Willem Barentsz','Jacob Roggeveen','Willem Schouten','Cornelis de Houtman','Jacob van Heemskerck','Joris van Spilbergen','Pieter de Carpentier'],
'women':['Anne Bonny','Grace O’Malley','Charlotte de Berry','Jacquotte Delahaye','Sayyida al Hurra','Ching Shih','Rachel Wall'],
'ships':['Adventure','Resolution','Endeavour','Providence','Golden Hind','Revenge','Sea Venture','Dreadnought','Mercury','Royal Fortune','São Gabriel','Victoria','Trinidad','Santiago','San Antonio','Dauphin','Pelican'],
'islands':['Madeira','Tenerife','Curaçao','Martinique','Guadeloupe','Barbados','Dominika','Samoa','Tahiti','Guam','Cebu','Borneo','Timor','Mauricijus','Réunion','Socotra','Zanzibar'],
'cities':['Cartagena','Havana','Veracruz','San Juan','Santo Domingo','Lisabon','Sevilla','Cádiz','Porto','Nantes','Bristol','Plymouth','Amsterdam','Malacca','Goa'],
'places':['Rt Dobre nade','Magellanov prolaz','Hormuški tjesnac','Gibraltarski tjesnac','Mozambički kanal','Biskajski zaljev','Hudsonov zaljev','La Manche','Torresov prolaz','Drakeov prolaz'],
'spices':['Cimet','Muškatni oraščić','Klinčić','Šafran','Kardamom','Đumbir','Piment'],
'nautical':['Pramac','Kobilica','Paluba','Jarbol','Kormilo','Sidro','Oputa','Kormilarnica','Nadgrađe','Bok'],
'groups':['Flota','Eskadra','Konvoj','Armada','Posada','Eskadrila'],
'concepts':['Rekonkvista','Merkantilizam','Kolonijalizam','Kaperstvo','Piratstvo','Kartografija','Navigacija'],
}

def cat(q,c):
 s=(q+' '+c).lower()
 if any(x in s for x in ['brod ','broda','brod?','brodove','brodovima','jedrenjak','karavela','galijun']): return 'ships'
 if any(x in s for x in ['otok','otoka','otočj']): return 'islands'
 if any(x in s for x in ['grad ','gradu','grada ','luka ','luci']): return 'cities'
 if any(x in s for x in ['prolaz','tjesnac','zaljev','rt ','kanal ']): return 'places'
 if any(x in s for x in ['začin','začina']): return 'spices'
 if any(x in s for x in ['žena','gusarica','botaničarka']): return 'women'
 if any(x in s for x in ['portugalsk','portugalac']): return 'person_pt'
 if any(x in s for x in ['španjolsk','konkvistador']): return 'person_es'
 if any(x in s for x in ['francusk','francuz']): return 'person_fr'
 if any(x in s for x in ['nizozemsk','nizozemac']): return 'person_nl'
 if any(x in s for x in ['englesk','britansk','škotsk']): return 'person_en'
 if any(x in s for x in ['moreplovac','istraživač','pomorac','kapetan','gusarski kapetan','guverner','franjevac','potkralj','vođa']): return 'person_en'
 if any(x in s for x in ['dio broda','na brodu','mornari','jedra','kormilar']): return 'nautical'
 if any(x in s for x in ['skupina brod','zajednica','armada','flota']): return 'groups'
 return 'concepts'

# For answers that are obviously a geographic/nautical/common-word type, override question heuristic.
def choose_pool(q,c):
 cl=c.lower()
 if c in pools['nautical']: return 'nautical'
 if c in pools['groups']: return 'groups'
 if c in pools['spices']: return 'spices'
 return cat(q,c)

rng=random.Random(73193)
used={k:0 for k in pools}
for i,x in enumerate(d):
 ca=x['correct_answer']; correct=x['answers'][ca]
 k=choose_pool(x['question'],correct)
 candidates=[z for z in pools[k] if z.casefold()!=correct.casefold()]
 # rotate pools rather than repeatedly using the same distractors
 start=(used[k]*2 + i)%len(candidates); used[k]+=1
 wrong=[]
 for j in range(len(candidates)):
  z=candidates[(start+j)%len(candidates)]
  if z not in wrong and z.casefold()!=correct.casefold(): wrong.append(z)
  if len(wrong)==2: break
 # preserve the original correct slot, replace only wrong slots
 wi=iter(wrong)
 for letter in 'ABC':
  if letter!=ca: x['answers'][letter]=next(wi)
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
open(p,'a',encoding='utf-8').write('\n')
print('processed',len(d))
