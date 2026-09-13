import json, subprocess

# Rebuild from the last stable Gaming version before later semantic edits corrupted some answers.
raw = subprocess.check_output(['git','show','8f2f142:Gaming.json'], text=True)
data = json.loads(raw)
assert len(data) == 444

# Never change question text, correct_answer letters, or the original correct-answer text.
def set_wrongs(fragment, wrong1, wrong2):
    matches=[x for x in data if fragment in x['question']]
    assert len(matches)==1, (fragment, len(matches))
    x=matches[0]
    ca=x['correct_answer']
    original=x['answers'][ca]
    wrong=[k for k in 'ABC' if k!=ca]
    x['answers'][wrong[0]]=wrong1
    x['answers'][wrong[1]]=wrong2
    assert x['answers'][ca] == original
    assert len({x['answers'][k].casefold().strip() for k in 'ABC'}) == 3

# Ambiguity / same-identity / weak-category fixes.
set_wrongs('BioShock omogućuje genetske modifikacije', 'EVE', 'Salts')
set_wrongs('povijesna francuska junakinja ima vlastitu kampanju', 'Jeanne de Clisson', 'Marie Marvingt')
set_wrongs("čuva pristup dvorcu Stormveil", 'Godrick', 'Rennala')
set_wrongs('hrvatski studio razvio serijal videoigara Serious Sam', 'Gamepires', 'Nanobit')
set_wrongs('izmišljena droga koja ima važnu ulogu u priči prve videoigre Max Payne', 'Joy', 'Spank')
set_wrongs('zajednički nazivaju robotska stvorenja koja nastanjuju svijet serijala videoigara Horizon', 'Konstrukti', 'Sinteti')

# Obvious category-mismatch fixes.
set_wrongs('arkadnu igru kompanija Gremlin objavila 1976.g.', 'Nibbler', 'Surround')
set_wrongs('američkom sveučilištu 1972.g. održano natjecanje u videoigri Spacewar!', 'MIT', 'Harvard')
set_wrongs('životinju jaše glavni junak u Williamsovoj arkadnoj videoigri Joust', 'Emu', 'Kondor')
set_wrongs('neprijatelj iz serijala Serious Sam koji bez glave trči', 'Kleer', 'Gnaar')
set_wrongs("Xbox-ov dodatak koji igračima omogućuje igranje i upravljanje pokretima", 'PlayStation Move', 'Wii MotionPlus')
set_wrongs('finski studio razvio prve dvije videoigre Max Payne', 'Housemarque', 'Bugbear Entertainment')
set_wrongs('planetu nalazi velik dio objekata korporacije UAC', 'Zemlja', 'Venera')
set_wrongs('vrstu namirnice predstavlja predmet koji Mario', 'Cvijet', 'Zvijezda')
set_wrongs("svjetski rat predstavlja povijesnu pozadinu Capcomove arkadne videoigre '1942'", 'Prvi svjetski rat', 'Vijetnamski rat')
set_wrongs('duhovni konj kojeg igrač jaše u videoigri Elden Ring', 'Roach', 'Epona')
set_wrongs('sport simulira u serijalu videoigara koji se nekada zvao FIFA', 'Košarka', 'Hokej')
set_wrongs('ratnik iz arkadne videoigre Gauntlet koji predstavlja crvenu boju', 'Questor', 'Merlin')
set_wrongs('virtualni ljudi kojima igrač upravlja u serijalu videoigara The Sims', 'Likovi', 'Avatari')
set_wrongs('najpoznatija mapa videoigre League of Legends na kojoj se standardno igraju mečevi pet protiv pet', 'Howling Abyss', 'Twisted Treeline')

# Keep the Stanford question fully homogeneous even if it was manually edited later.
# All answers are universities, and the original correct answer from the stable baseline stays untouched.

# Structural guarantees.
for i,x in enumerate(data,1):
    assert set(x['answers']) == set('ABC'), i
    assert x['correct_answer'] in 'ABC', i
    assert all(str(x['answers'][k]).strip() for k in 'ABC'), i
    assert len({x['answers'][k].casefold().strip() for k in 'ABC'}) == 3, i

with open('Gaming.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=2)
    f.write('\n')
print('Gaming rebuilt from stable baseline and curated distractors applied.')
