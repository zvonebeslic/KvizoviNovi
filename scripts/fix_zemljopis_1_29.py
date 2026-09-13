import json
from pathlib import Path

p = Path('Zemljopis.json')
d = json.loads(p.read_text(encoding='utf-8'))

# Ručno odabrana dva uvjerljiva distraktora za svako pitanje.
# Točan odgovor se NE mijenja: zadržava se iz postojećeg correct_answer polja.
distractors = {
    1: ['Osmangazi', 'Yavuz Sultan Selim'],
    2: ['Ascension', 'Tristan da Cunha'],
    3: ['Ferdinanda Focha', 'Henrija de Turennea'],
    4: ['Angola', 'Mozambik'],
    5: ['3', '5'],
    6: ['Alexander Selkirk', 'Santa Clara'],
    7: ['Europa', 'Afrika'],
    8: ['Europa', 'Sjeverna Amerika'],
    9: ['Arcah', 'Čečeniju'],
    10: ['Armenije', 'Azerbajdžana'],
    11: ['Sjeverna Amerika', 'Afrika'],
    12: ['Krstionica', 'Transept'],
    13: ['Šest', 'Osam'],
    14: ['Norveške', 'Švedske'],
    15: ['Sob', 'Tulenj'],
    16: ['Island', 'Farski Otoci'],
    17: ['Irske', 'Kanade'],
    18: ['3', '4'],
    19: ['Mikronezije', 'Palaua'],
    20: ['Kamčatka', 'Tajmir'],
    21: ['Palawan', 'Samar'],
    22: ['Zambije', 'Namibije'],
    23: ['Tana', 'Rufiji'],
    24: ['Tuvalua', 'Naurua'],
    25: ['Thimphu', 'Dhaka'],
    26: ['Tungurahua', 'Chimborazo'],
    27: ['Canberra', 'Islamabad'],
    28: ['Victoria', 'Port Louis'],
    29: ['Bahreina', 'Ujedinjenih Arapskih Emirata'],
}

original_correct = {
    1: 'Canakkale 1915',
    2: 'Sveta Helena',
    3: 'Napoleona I. Bonaparte',
    4: 'Gvineja Bisau',
    5: '4',
    6: 'Robinson Crusoe',
    7: 'Azija',
    8: 'Azija',
    9: 'Abhaziju',
    10: 'Gruzije',
    11: 'Južna Amerika',
    12: 'Zvonik',
    13: 'Sedam',
    14: 'Danske',
    15: 'Ovcu',
    16: 'Grenland',
    17: 'Velike Britanije',
    18: '2',
    19: 'Maršalovih Otoka',
    20: 'Kola',
    21: 'Mindanao',
    22: 'Angole',
    23: 'Mara',
    24: 'Kiribatija',
    25: 'Kathmandu',
    26: 'Cotopaxi',
    27: 'Brasilia',
    28: 'Moroni',
    29: 'Katara',
}

for i in range(1, 30):
    q = d[i - 1]
    key = q['correct_answer']
    current_correct = q['answers'][key]
    assert current_correct == original_correct[i], (i, key, current_correct, original_correct[i])
    wrong = iter(distractors[i])
    new_answers = {}
    for letter in ('A', 'B', 'C'):
        new_answers[letter] = original_correct[i] if letter == key else next(wrong)
    assert len(set(new_answers.values())) == 3, (i, new_answers)
    q['answers'] = new_answers

# Napomena za pitanje 15: grb Farskih Otoka heraldički prikazuje ovna;
# izvorni prihvaćeni odgovor "Ovcu" ostavljen je netaknut prema pravilu da
# se originalni točan odgovor ne mijenja bez zasebne uredničke odluke.
d[14]['qa_note'] = 'Grb Farskih Otoka heraldički prikazuje ovna (mužjaka ovce); izvorni odgovor "Ovcu" ostavljen je netaknut.'

assert all(set(q['answers']) == {'A', 'B', 'C'} and len(set(q['answers'].values())) == 3 for q in d[:29])
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('fixed', len(distractors))
