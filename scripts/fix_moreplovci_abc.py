import json, random, re
p='Moreplovci.json'
d=json.load(open(p,encoding='utf-8'))

pools={
'person_pt':['Afonso de Noronha','Duarte de Meneses','Gonçalo de Ataíde','Lourenço de Almeida','Simão de Miranda','António de Saldanha','Manuel de Sousa','Rui de Sequeira','Fernão de Andrade','Estêvão da Gama','João de Caminha','Gaspar de Lemos'],
'person_es':['Alonso de Córdoba','Diego de Valderrama','Hernando de Villalba','Rodrigo de Salazar','Gonzalo de Montalvo','Martín de Quesada','Álvaro de Sotomayor','Juan de Escalante','Pedro de Alarcón','Francisco de Villaseñor','Diego de Mendoza','Hernán de Rojas'],
'person_fr':['Étienne Moreau','Jacques de Villeneuve','Pierre de Montfort','Louis de Keradec','René de Beaumont','Claude de Marigny','Henri de Rochefort','Nicolas de Varenne','Jean de Bréval','Antoine Delacroix'],
'person_en':['Thomas Cavendish','Martin Frobisher','John Hawkins','Humphrey Gilbert','Richard Grenville','William Dampier','George Anson','Edward Fenton','John Davis','Henry Every','Thomas Button','Robert Harcourt'],
'person_nl':['Willem Barentsz','Jacob Roggeveen','Willem Schouten','Cornelis de Houtman','Jacob van Heemskerck','Joris van Spilbergen','Pieter de Carpentier','Jan Huygen van Linschoten'],
'person_generic':['Sebastián de Aranda','Tomás de Villacorta','Henri de Montreuil','Edward Blackwell','Pieter van der Meer','Lorenzo de Acosta','João de Serpa','Nicolas de Beaumont','Richard Hargreaves','Mateo de Villalobos'],
'women':['Anne Bonny','Grace O’Malley','Charlotte de Berry','Jacquotte Delahaye','Sayyida al Hurra','Ching Shih','Rachel Wall','Mary Critchett','Anne Dieu-le-Veut'],
'ships':['Adventure','Resolution','Endeavour','Providence','Golden Hind','Revenge','Sea Venture','Mercury','Royal Fortune','São Gabriel','Victoria','Trinidad','Santiago','San Antonio','Dauphin','Pelican','Hopewell','Lion','Elizabeth'],
'islands':['Madeira','Tenerife','Curaçao','Martinique','Guadeloupe','Barbados','Dominika','Samoa','Tahiti','Guam','Cebu','Borneo','Timor','Mauricijus','Réunion','Socotra','Zanzibar','Mindanao','Palawan'],
'continents':['Azija','Afrika','Južna Amerika','Sjeverna Amerika','Europa','Australija'],
'cities':['Cartagena','Havana','Veracruz','San Juan','Santo Domingo','Lisabon','Sevilla','Cádiz','Porto','Nantes','Bristol','Plymouth','Amsterdam','Malacca','Goa','Acapulco','Manila'],
'waterways':['Rt Dobre nade','Magellanov prolaz','Hormuški tjesnac','Gibraltarski tjesnac','Mozambički kanal','Biskajski zaljev','Hudsonov zaljev','La Manche','Torresov prolaz','Drakeov prolaz','Malajski prolaz'],
'spices':['Cimet','Muškatni oraščić','Klinčić','Šafran','Kardamom','Đumbir','Piment'],
'nautical_parts':['Pramac','Krma','Kobilica','Paluba','Jarbol','Kormilo','Sidro','Oputa','Kormilarnica','Nadgrađe','Bok','Pramčani kaštel'],
'groups':['Flota','Eskadra','Konvoj','Armada','Posada','Eskadrila'],
'concepts':['Rekonkvista','Merkantilizam','Kolonijalizam','Kaperstvo','Piratstvo','Kartografija','Navigacija','Trgovinski monopol','Pomorska blokada'],
'woods':['Mahagonij','Ebanovina','Tikovina','Sandalovina','Cedrovina'],
'weapons':['Arkebuza','Mušketa','Samostrel','Kremenjača','Top'],
'directions':['Sjever','Jug','Istok','Zapad'],
}

# exact known answer types have priority
def exact_type(c):
    cf=c.casefold()
    for k,vals in pools.items():
        if any(cf==v.casefold() for v in vals): return k
    return None

def person_pool(q):
    s=q.lower()
    if 'portugal' in s: return 'person_pt'
    if 'španjol' in s or 'spanjol' in s: return 'person_es'
    if 'francusk' in s or 'francuz' in s: return 'person_fr'
    if 'nizozem' in s: return 'person_nl'
    if 'englesk' in s or 'britansk' in s or 'škotsk' in s: return 'person_en'
    return 'person_generic'

def classify(q,c):
    ql=q.lower(); cl=c.lower()
    et=exact_type(c)
    if et: return et

    # what the question is actually asking for
    if re.search(r'koji se kontinent|kojem kontinentu|koji kontinent', ql): return 'continents'
    if re.search(r'kako se zvao brod|kako se zvala karavela|ime broda|koji brod|kojeg broda|jedrenjak', ql): return 'ships'
    if re.search(r's kojeg .*otoka|na kojem .*otoku|kod kojeg .*otoka|koji .*otok|kojem .*otoku|otočj', ql): return 'islands'
    if re.search(r'koji grad|kojem gradu|kojeg grada|koja luka|kojoj luci|iz kojeg grada', ql): return 'cities'
    if re.search(r'prolaz|tjesnac|zaljev|rtu | rt |kanal', ql): return 'waterways'
    if re.search(r'koji začin|kojeg začina|začin', ql): return 'spices'
    if re.search(r'koje drvo|kojem drvu|po kojem .*drvu', ql): return 'woods'
    if re.search(r'koje oružje|kojim oružjem', ql): return 'weapons'
    if re.search(r'koji smjer|u kojem smjeru|strana svijeta', ql): return 'directions'
    if re.search(r'koja .*žena|koja je .*botaničarka|koja .*gusarica|kako se zvala .*žena', ql): return 'women'
    if re.search(r'koji je .*?(moreplovac|istraživač|pomorac|kapetan|gusarski kapetan|guverner|franjevac|potkralj|konkvistador|kralj|vođa|admiral)', ql) or re.search(r'kako se zvao .*?(moreplovac|istraživač|pomorac|kapetan|vođa|vladar|tlatoani)', ql):
        return person_pool(q)
    if re.search(r'kako se naziva .*?(dio broda|površina broda|stup na brodu)|stražnji dio broda|prednji dio broda', ql): return 'nautical_parts'
    if re.search(r'skupina brodova|velika skupina brodova|brodovi koji zajedno|pomorska formacija', ql): return 'groups'
    if re.search(r'kako se .*naziv|popularan naziv|koji pojam|naziva se kako|sustav|politika', ql): return 'concepts'

    # fallback from shape/content of correct answer
    if any(x in cl for x in ['otok','island']): return 'islands'
    if len(c.split())>=2 and c[0].isupper() and not c.isupper(): return person_pool(q)
    return 'concepts'

rng=random.Random(73193)
used={k:0 for k in pools}
for i,x in enumerate(d):
    ca=x['correct_answer']; correct=x['answers'][ca]
    k=classify(x['question'],correct)
    candidates=[z for z in pools[k] if z.casefold()!=correct.casefold()]
    start=(used[k]*3+i)%len(candidates); used[k]+=1
    wrong=[]
    for j in range(len(candidates)):
        z=candidates[(start+j)%len(candidates)]
        if z.casefold()!=correct.casefold() and z not in wrong:
            wrong.append(z)
        if len(wrong)==2: break
    wi=iter(wrong)
    for letter in 'ABC':
        if letter!=ca:
            x['answers'][letter]=next(wi)

json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
open(p,'a',encoding='utf-8').write('\n')
print('processed',len(d))
