import json, subprocess

# Always rebuild from the last stable Gaming version before later edits corrupted answers.
raw = subprocess.check_output(['git','show','8f2f142:Gaming.json'], text=True)
data = json.loads(raw)
assert len(data) == 444

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

# Ambiguous or too-close alternatives.
set_wrongs('BioShock omogućuje genetske modifikacije', 'EVE', 'Salts')
set_wrongs('povijesna francuska junakinja ima vlastitu kampanju', 'Jeanne Hachette', 'Jeanne de Clisson')
set_wrongs('američki borac iz serijala videoigara Tekken, prepoznatljiv po izrazito visokoj plavoj frizuri', 'Marshall Law', 'Bryan Fury')
set_wrongs('izmišljena droga koja ima važnu ulogu u priči prve videoigre Max Payne', 'Joy', 'Spank')
set_wrongs('hrvatski studio razvio serijal videoigara Serious Sam', 'Gamepires', 'Nanobit')
set_wrongs('čuva pristup dvorcu Stormveil', 'Godrick', 'Rennala')
set_wrongs('zajednički nazivaju robotska stvorenja koja nastanjuju svijet serijala videoigara Horizon', 'Konstrukti', 'Sinteti')

# Games/titles should be compared with games/titles.
set_wrongs('arkadnu igru kompanija Gremlin objavila 1976.g.', 'Nibbler', 'Surround')
set_wrongs('arkadna videoigra iz 1986.g. u kojoj zmajevi Bub i Bob', 'Snow Bros.', 'Tumble Pop')
set_wrongs('serijal pucačkih videoigara otvorenog svijeta', 'Just Cause', 'Crysis')
set_wrongs('kultnoj igri iz 1984.g. pas doslovno ismijavao igrača', "Hogan's Alley", 'Wild Gunman')

# Characters should be compared with characters of the same kind/franchise where practical.
set_wrongs('jedna od najpoznatijih protagonistica videoigre StarCraft', 'Nova Terra', 'Selendis')
set_wrongs('veliki kralj Koopa koji je desetljećima jedan od glavnih protivnika Super Marija', 'King Boo', 'Wario')
set_wrongs('tajni istraživački kompleks u kojem na početku prve videoigre Half-Life', 'Aperture Science', 'Blackwing Research Facility')
set_wrongs('Uz Buba, kako se zove još jedan zmaj', 'Nick', 'Tom')
set_wrongs('Donkey Kongov manji prijatelj i česti partner', 'Dixie Kong', 'Tiny Kong')
set_wrongs('njujorški policajac i protagonist serijala videoigara Max Payne', 'Cole Phelps', 'Wei Shen')
set_wrongs('yordle iz League of Legendsa koji nosi zelenu kapu', 'Tristana', 'Veigar')
set_wrongs('crveni okruglasti neprijatelj s velikim naočalama u arkadnoj videoigri Dig Dug', 'Fygar', 'Pooka Jr.')
set_wrongs('golemi zaštitnici u ronilačkim odijelima koji čuvaju Little Sisters', 'Big Sisters', 'Splicers')
set_wrongs('glavni antagonist videoigre Prince of Persia: The Sands of Time', 'Dahaka', 'Kaileena')
set_wrongs('čudovište s velikom metalnom piramidalnom kacigom', 'Nemesis', 'Mr. X')
set_wrongs('neprijatelj iz serijala Serious Sam koji bez glave trči', 'Kleer', 'Gnaar')
set_wrongs('djevojka koju je spašavao od Donkey Konga', 'Princess Daisy', 'Rosalina')
set_wrongs('glavni protagonist prve videoigre Mafia, taksist', 'Vito Scaletta', 'Lincoln Clay')
set_wrongs('popularnim nadimkom poznat protagonist novijih videoigara Doom', 'Master Chief', 'Gordon Freeman')
set_wrongs('ratnik iz arkadne videoigre Gauntlet koji predstavlja crvenu boju', 'Questor', 'Merlin')
set_wrongs('glavni antagonist originalne videoigre Spyro the Dragon', 'Ripto', 'Red')
set_wrongs('plavo odjeveni borac iz Mortal Kombata', 'Scorpion', 'Reptile')
set_wrongs('pravo ime CJ-ja', 'Tommy Vercetti', 'Niko Bellic')
set_wrongs('protagonist videoigre Mafia II', 'Tommy Angelo', 'Lincoln Clay')
set_wrongs('stariji prijatelj i mentor Nathana Drakea', 'Sam Drake', 'Charlie Cutter')

# Places/regions/countries/cities.
set_wrongs('izmišljena himalajska država u kojoj se odvija radnja videoigre Far Cry 4', 'Yara', 'Medici')
set_wrongs('područje u kojem se odvija radnja videoigre Elden Ring', 'Lordran', 'Drangleic')
set_wrongs('izmišljeni kalifornijski grad, snažno inspiriran Los Angelesom', 'Vice City', 'Liberty City')
set_wrongs('svijet smrtnika smješten između High Heavensa i Burning Hellsa', 'Pandemonium', 'Westmarch')
set_wrongs('američkoj saveznoj državi nalazi izmišljeni Hope County', 'Colorado', 'Wyoming')
set_wrongs('drevnoj civilizaciji i među njezinim hramovima i piramidama', 'Grčkoj', 'Rimskoj')
set_wrongs('američkom sveučilištu 1972.g. održano natjecanje u videoigri Spacewar!', 'MIT', 'Yale')

# Devices, terms and control concepts.
set_wrongs('engleskim gaming izrazom naziva vibracija kontrolera', 'Haptic', 'Force Feedback')
set_wrongs('poznati PlayStationov kontroler predstavljen 1997.g.', 'Dual Analog', 'Sixaxis')
set_wrongs('najčešće naziva kontroler koji igrač drži objema rukama', 'Joystick', 'Arcade Stick')
set_wrongs("Xbox-ov dodatak koji igračima omogućuje igranje i upravljanje pokretima", 'PlayStation Move', 'Wii MotionPlus')
set_wrongs('prijenosno računalo koje se nosi na podlaktici', 'Stealth Boy', 'RobCo Fun')
set_wrongs('Valveov prijenosni uređaj za igranje PC videoigara', 'ROG Ally', 'Legion Go')

# Factions/races/groups.
set_wrongs('Uz protuteroriste koja još suprotstavljena strana', 'Pobunjenici', 'Plaćenici')
set_wrongs('tradicionalno pripadaju orci, taureni i trolovi', 'Alliance', 'Scourge')
set_wrongs('ljudska rasa odnosno frakcija kojom igrač može upravljati uz Zerg i Protoss', "Xel'Naga", 'Hybrid')
set_wrongs('tehnološki napredna izvanzemaljska rasa iz videoigre StarCraft', 'Zerg', 'Terran')

# Concrete semantic categories.
set_wrongs('voće koje glavni protagonist videoigre Crash Bandicoot skuplja', 'Mango', 'Papaja')
set_wrongs('boje ptica koja je glavni i najprepoznatljiviji lik serijala videoigara Angry Birds', 'Žute', 'Crne')
set_wrongs('Svijet kojih ratnih strojeva je kompanija Wargaming', 'Aviona', 'Brodova')
set_wrongs('velikom povijesnom sukobu smještena radnja videoigre Battlefield 1', 'Drugi svjetski rat', 'Vijetnamski rat')
set_wrongs('Namcova arkadna videoigra iz 1981. u kojoj igrač upravlja svemirskim lovcem', 'Galaxian', 'Xevious')
set_wrongs('životinju jaše glavni junak u Williamsovoj arkadnoj videoigri Joust', 'Emu', 'Kondor')
set_wrongs('predmet Donkey Kong u originalnoj arkadnoj igri kotrlja', 'Sanduke', 'Gume')
set_wrongs('životinja spominje u poznatoj frazi PUBG-ja', 'Puran', 'Patka')
set_wrongs('finski studio razvio prve dvije videoigre Max Payne', 'Housemarque', 'Bugbear Entertainment')
set_wrongs('sport simulira u serijalu videoigara koji se nekada zvao FIFA', 'Košarka', 'Hokej')
set_wrongs('planetu nalazi velik dio objekata korporacije UAC', 'Zemlja', 'Venera')
set_wrongs('vrstu namirnice predstavlja predmet koji Mario', 'Jabuka', 'Mrkva')
set_wrongs("svjetski rat predstavlja povijesnu pozadinu Capcomove arkadne videoigre '1942'", 'Prvi svjetski rat', 'Vijetnamski rat')
set_wrongs('duhovni konj kojeg igrač jaše u videoigri Elden Ring', 'Roach', 'Epona')
set_wrongs('građevinski resurs, uz drvo i metal', 'Staklo', 'Plastika')
set_wrongs('povijesnom engleskom moreplovcu protagonist videoigre Uncharted', 'Walter Raleigh', 'James Cook')

# Easter/holiday question: keep all options as holidays.
set_wrongs('kršćanskim blagdanom povezan naziv', 'Božić', 'Duhovi')

# Keep original correct answers and balanced correct letters exactly as in the stable source.
for i,x in enumerate(data,1):
    assert set(x['answers']) == set('ABC'), i
    assert x['correct_answer'] in 'ABC', i
    assert all(str(x['answers'][k]).strip() for k in 'ABC'), i
    assert len({x['answers'][k].casefold().strip() for k in 'ABC'}) == 3, i

from collections import Counter
c=Counter(x['correct_answer'] for x in data)
assert c == {'A':148,'B':148,'C':148}, c

with open('Gaming.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=2)
    f.write('\n')
print('Gaming rebuilt and curated. Distribution:', c)
