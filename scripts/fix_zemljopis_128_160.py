import json
from pathlib import Path

p = Path('Zemljopis.json')
d = json.loads(p.read_text(encoding='utf-8'))

distractors = {
    128: ['Mikroneziji', 'Melaneziji'],
    129: ['Ouagadougou', 'Lilongwe'],
    130: ['Skoplje', 'Podgorica'],
    131: ['Île-à-Vache', 'Gonâve'],
    132: ['Lesoto', 'Bocvana'],
    133: ['Yangon', 'Mandalay'],
    134: ['Cochabamba', 'Santa Cruz'],
    135: ['Crne Gore', 'Sjeverne Makedonije'],
    136: ['Antigva i Barbuda', 'Dominika'],
    137: ['Sahel', 'Mašrek'],
    138: ['Stockholm', 'Oslo'],
    139: ['Zanzibar', 'Mauricijus'],
    140: ['Belizea', 'Hondurasa'],
    141: ['Maputo', 'Dodoma'],
    142: ['Niamey', 'Conakry'],
    143: ['Manat', 'Dram'],
    144: ['Azerbajdžana', 'Gruzije'],
    145: ['Crnoj Gori', 'Bosni i Hercegovini'],
    146: ['Hoppers', 'Lamprais'],
    147: ['Kathmandu', 'Thimphu'],
    148: ['Sueski Kanal', 'Kielski Kanal'],
    149: ['Bonaire', 'Aruba'],
    150: ['Kamčatka', 'Ural'],
    151: ['Kamerun', 'Gabon'],
    152: ['Tajo', 'Guadiana'],
    153: ['Kathmandu', 'Dhaka'],
    154: ['Sinaj', 'Judejska pustinja'],
    155: ['Sijera Leoneu', 'Gvineji'],
    156: ['Endeavour', 'Resolution'],
    157: ['Ahileju', 'Hektoru'],
    158: ['Tajvan', 'Luzon'],
    159: ['Tambore', 'Merapi'],
    160: ['Putrajaya', 'George Town'],
}

original_correct = {
    128:'Polineziji',129:'Antananarivo',130:'Tirana',131:'Tortuga',132:'Eswatini',
    133:'Naypyidaw',134:'La Paz',135:'Srbije',136:'Sveti Kristofor i Nevis',137:'Magreb',
    138:'Helsinki',139:'Madagaskar',140:'Guatemale',141:'Antananarivo',142:'Bamako',
    143:'Lari',144:'Turske',145:'Srbiji',146:'Kotu',147:'Dhaka',148:'Korintski Kanal',
    149:'Curacao',150:'Sibir',151:'Srednjoafrička Republika',152:'Ebro',153:'Thimphu',
    154:'Negev',155:'Liberiji',156:'Bounty',157:'Diomedu',158:'Hainan',159:'Krakataua',160:'Kuala Lumpur'
}

anchor = "Iako u sastavu Čilea, kojoj 'neziji' tj. otočnoj skupini u Tihom Oceanu, pripada Uskršnji Otok?"
starts = [idx for idx, q in enumerate(d) if q.get('question') == anchor]
assert len(starts) == 1, f'Anchor count: {len(starts)}'
start = starts[0]

for num in range(128,161):
    q = d[start + (num - 128)]
    key = q['correct_answer']
    cur = q['answers'][key]
    assert cur == original_correct[num], (num, q['question'], key, cur, original_correct[num])
    wrong = iter(distractors[num])
    q['answers'] = {letter: (original_correct[num] if letter == key else next(wrong)) for letter in ('A','B','C')}
    assert len(set(q['answers'].values())) == 3
    assert q['answers'][key] == original_correct[num]

p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('fixed', len(distractors), 'questions 128-160 from anchor index', start + 1)
