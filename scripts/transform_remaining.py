import json, re, unicodedata, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://raw.githubusercontent.com/zvonebeslic/balkanska_pub_prica/main/'
FILES = [
 'AmerickiPredsjednici.json','AntickiRim.json','Gaming.json','Glazba.json',
 'Knjizevnost.json','Moreplovci.json','Nogomet.json','Sport.json','Svastara.json','Zemljopis.json'
]

def norm(s):
    s = str(s).strip().lower()
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+',' ',s).strip()

def first_answer(q):
    a=q.get('answers')
    if isinstance(a,list) and a: return str(a[0]).strip()
    raise ValueError('Nema izvornog odgovora')

# Kategorije su namjerno uske: cilj je da distraktori budu iste vrste kao točan odgovor.
def category(q, ans):
    x=norm(q.get('question','')); a=norm(ans)
    if a in {'da','ne','tocno','netocno','istina','laz','true','false'}: return 'binary'
    if re.fullmatch(r'\d{4}\.?', a): return 'year'
    if re.fullmatch(r'\d+(?:[.,]\d+)?(?:\s*%|\s*(?:km|m|cm|mm|kg|g|l|ml|h|min|sek|s|eura?|dolara?|bodova?|poena?))?', a): return 'number'
    tests=[
      ('person',r'\b(tko|koj[iae] (?:glumac|glumica|redatelj|redateljica|pisac|spisateljica|autor|autorica|predsjednik|predsjednica|kralj|kraljica|car|carica|papa|znanstvenik|znanstvenica|skladatelj|pjevac|pjevacica|igrac|igracica|nogometas|sportas|trener|general|vojskovoda|moreplovac|istrazivac|umjetnik|slikar)|kako se zove (?:covjek|osoba)|ime i prezime|ciji lik|cijeg .* trazimo)\b'),
      ('country',r'\b(koje drzave|kojoj drzavi|koja drzava|koju drzavu|iz koje zemlje|u kojoj zemlji|koje zemlje|kojoj zemlji|koja zemlja|drzavljanin koje|nacionalnost)\b'),
      ('city',r'\b(koji grad|kojem gradu|kojeg grada|kojem .* gradu|u kojem gradu|glavni grad|prijestolnica|metropola|grad[au] .* zove)\b'),
      ('place',r'\b(gdje se|na kojem otoku|koji otok|kojem otoku|koja planina|kojoj planini|koje more|kojem moru|koji ocean|kojem oceanu|koja rijeka|kojoj rijeci|koje jezero|kojem jezeru|koji zaljev|kojem zaljevu|koji kontinent|kojem kontinentu|koja pokrajina|kojoj pokrajini|koji poluotok|kojem poluotoku|koje mjesto|kojem mjestu|koja regija|kojoj regiji)\b'),
      ('award',r'\b(koju nagradu|koje nagrade|koja nagrada|nobel|oscar|oscara|grammy|zlatn[ui] .*|palme d.or|nagrada)\b'),
      ('book',r'\b(koje djelo|koji roman|koja knjiga|koju knjigu|naslov knjige|knjizevno djelo|ep|pjesnicka zbirka|pripovijetka|drama|tragedija|komedija .* djelo)\b'),
      ('film',r'\b(koji film|kojem filmu|kojeg filma|filmski naslov|serijal filmova|koja serija|kojoj seriji|tv serija)\b'),
      ('song',r'\b(koja pjesma|koju pjesmu|koje pjesme|naziv pjesme|singl|skladba)\b'),
      ('album',r'\b(koji album|kojem albumu|kojeg albuma)\b'),
      ('music_artist',r'\b(koji bend|koja grupa|glazbena grupa|sastav|izvodac|pjevac|pjevacica)\b'),
      ('language',r'\b(koji jezik|kojem jeziku|kojeg jezika|na kojem jeziku|kako se .* jeziku)\b'),
      ('sport',r'\b(koji sport|kojem sportu|kojeg sporta|disciplina|sportskoj disciplini)\b'),
      ('club',r'\b(koji klub|kojem klubu|kojeg kluba|nogometni klub|kosarkaski klub|momcad|reprezentacija|za koji klub)\b'),
      ('game',r'\b(koja igra|koju igru|koje igre|videoigra|video igra|igrica|game|kojem serijalu igara)\b'),
      ('character',r'\b(kako se zove (?:lik|junak|junakinja|zlikovac|protagonist|antagonist|princeza|kralj u)|ime lika|fiktivni lik|koji lik)\b'),
      ('animal',r'\b(koja zivotinja|koju zivotinju|koje zivotinje|kojoj zivotinji|koja ptica|koju pticu|koja riba|koju ribu|koja zmija|pasmina|sisavac|gmaz|vodozemac|kukac)\b'),
      ('plant',r'\b(koja biljka|koju biljku|koje biljke|koje drvo|kojeg drveta|koji cvijet|kojeg cvijeta|koje voce|koji plod)\b'),
      ('war',r'\b(koji rat|kojem ratu|kojeg rata|bitka|koja bitka|kojoj bitki|koje ratove)\b'),
      ('dynasty',r'\b(koja dinastija|kojoj dinastiji|koje dinastije)\b'),
      ('religion',r'\b(koja religija|kojoj religiji|koje religije|vjera)\b'),
      ('currency',r'\b(koja valuta|koju valutu|novcana jedinica|valuta)\b'),
      ('organization',r'\b(koja organizacija|koju organizaciju|udruzenje|savez|agencija|institucija|tvrtka|kompanija)\b'),
      ('title',r'\b(kako se zove|kako nazivamo|koji naziv|koje ime|koji pojam|kratica|oznaka)\b'),
    ]
    for cat,pat in tests:
        if re.search(pat,x): return cat
    # odgovori s dvije ili tri riječi i velikim početnim slovima često su osobna imena; samo kao zadnja rezerva
    raw=str(ans).strip()
    if re.fullmatch(r"[A-ZČĆŽŠĐ][^0-9,;:!?]{1,30}\s+[A-ZČĆŽŠĐ][^0-9,;:!?]{1,30}(?:\s+[A-ZČĆŽŠĐ][^0-9,;:!?]{1,30})?", raw): return 'personlike'
    return 'other'

def numeric_wrongs(ans, cat):
    raw=str(ans).strip(); m=re.search(r'-?\d+(?:[.,]\d+)?', raw)
    if not m: return None
    val=float(m.group(0).replace(',','.'))
    if cat=='year':
        y=int(val); vals=[y-4,y+4] if y>1000 else [y-1,y+1]
    else:
        if val==0: vals=[1,2]
        elif abs(val)<10: vals=[val-1 if val>1 else val+1,val+1 if val>1 else val+2]
        elif abs(val)<100: vals=[val-5,val+5]
        else: vals=[val-10,val+10]
    out=[]
    for v in vals:
        s=str(int(v)) if float(v).is_integer() else str(v).replace('.',',')
        # zadrži osnovnu jedinicu ako postoji
        suffix=(raw[m.end():]).strip()
        out.append(s + ((' '+suffix) if suffix else ''))
    if norm(out[0])==norm(raw) or norm(out[1])==norm(raw) or norm(out[0])==norm(out[1]): return None
    return out

def compatible(cat, ans):
    a=str(ans).strip(); n=norm(a)
    if not n: return False
    if cat in {'year','number','binary'}: return True
    if cat in {'person','personlike'}:
        return not re.fullmatch(r'\d+', n) and len(a)<=70
    return len(a)<=90

def choose_pair(i, cat, source, cats):
    correct=first_answer(source[i]); nc=norm(correct)
    if cat=='binary':
        n=norm(correct)
        if n in {'da','tocno','istina','true'}: return ['Ne']
        return ['Da']
    if cat in {'year','number'}:
        z=numeric_wrongs(correct,cat)
        if z: return z

    # Prioritet: ista kategorija + blizina u izvornom dokumentu. Pitanja su u bazama često tematski grupirana,
    # pa bliski odgovori iste vrste daju znatno prirodnije distraktore od nasumičnog globalnog izbora.
    candidates=[]
    for distance in range(1, len(source)):
        for j in (i-distance, i+distance):
            if 0<=j<len(source) and cats[j]==cat:
                a=first_answer(source[j])
                if norm(a)!=nc and compatible(cat,a) and all(norm(a)!=norm(x) for x in candidates):
                    candidates.append(a)
                    if len(candidates)==2: return candidates
    # srodne rezervne kategorije, nikad potpuno nasumični tipovi
    related={
      'person':['personlike'],'personlike':['person'],'city':['place'],'place':['city','country'],
      'country':['place'],'film':['book','game'],'book':['film'],'song':['album'],'album':['song'],
      'club':['organization'],'organization':['club'],'character':['personlike','person'],
      'title':['other'],'other':['title']
    }.get(cat,[])
    for rc in related:
        for distance in range(1,len(source)):
            for j in (i-distance,i+distance):
                if 0<=j<len(source) and cats[j]==rc:
                    a=first_answer(source[j])
                    if norm(a)!=nc and compatible(rc,a) and all(norm(a)!=norm(x) for x in candidates):
                        candidates.append(a)
                        if len(candidates)==2: return candidates
    # Posljednja rezerva: ručno neutralne alternative prema tipu.
    defaults={
      'country':['Francuska','Italija'],'city':['Rim','Pariz'],'place':['Europa','Azija'],
      'award':['Pulitzerova nagrada','Zlatni globus'],'language':['Francuski','Talijanski'],
      'sport':['Tenis','Košarka'],'animal':['Lav','Tigar'],'plant':['Hrast','Maslina'],
      'currency':['Euro','Dolar'],'religion':['Budizam','Hinduizam'],'war':['Prvi svjetski rat','Drugi svjetski rat'],
      'dynasty':['Dinastija Han','Dinastija Ming'],'game':['Minecraft','The Legend of Zelda'],
      'film':['Kum','Casablanca'],'book':['Odiseja','Božanstvena komedija'],
      'song':['Imagine','Yesterday'],'album':['Abbey Road','Thriller'],
      'music_artist':['The Beatles','Queen'],'club':['Real Madrid','Barcelona'],
      'organization':['UNESCO','UNICEF'],'character':['Hamlet','Odisej'],'person':['Albert Einstein','Isaac Newton'],
      'personlike':['Albert Einstein','Isaac Newton'],'title':['Alfa','Omega'],'other':['Prvi','Drugi']
    }.get(cat,['Prvi','Drugi'])
    for a in defaults:
        if norm(a)!=nc and all(norm(a)!=norm(x) for x in candidates): candidates.append(a)
        if len(candidates)==2: break
    return candidates[:2]

def transform(name):
    with urllib.request.urlopen(BASE+name, timeout=60) as r:
        src=json.loads(r.read().decode('utf-8'))
    cats=[category(q,first_answer(q)) for q in src]
    out=[]; letters='ABC'; counts={'A':0,'B':0,'C':0}; binary=0
    for i,q in enumerate(src):
        correct=first_answer(q); cat=cats[i]; pair=choose_pair(i,cat,src,cats)
        item=dict(q)
        if cat=='binary':
            # dvije opcije; balansiraj A/B po redoslijedu binarnih pitanja
            pos=binary%2; binary+=1
            vals=[None,None]; vals[pos]=correct; vals[1-pos]=pair[0]
            item['answers']={'A':vals[0],'B':vals[1]}
            item['correct_answer']='AB'[pos]
            counts[item['correct_answer']]+=1
        else:
            if len(pair)!=2 or norm(pair[0])==norm(pair[1]) or norm(correct) in {norm(pair[0]),norm(pair[1])}:
                raise SystemExit(f'{name} pitanje {i+1}: loši distraktori {pair}')
            pos=i%3; vals=[]; it=iter(pair)
            for p in range(3): vals.append(correct if p==pos else next(it))
            item['answers']={'A':vals[0],'B':vals[1],'C':vals[2]}
            item['correct_answer']=letters[pos]; counts[letters[pos]]+=1
        out.append(item)
    with open(ROOT/name,'w',encoding='utf-8') as f:
        json.dump(out,f,ensure_ascii=False,indent=2); f.write('\n')
    # stroga strukturalna provjera
    check=json.load(open(ROOT/name,encoding='utf-8'))
    assert len(check)==len(src)
    for i,(a,b) in enumerate(zip(src,check)):
        assert a['question']==b['question']
        assert first_answer(a) in b['answers'].values()
        assert b['answers'][b['correct_answer']]==first_answer(a)
    print(f'{name}: {len(out)} pitanja, ABC={counts}, binary={binary}')

for fn in FILES:
    transform(fn)
print('SVE PREOSTALE BAZE GOTOVE')
