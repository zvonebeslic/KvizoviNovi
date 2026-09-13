import json
from pathlib import Path

p = Path('Zemljopis.json')
d = json.loads(p.read_text(encoding='utf-8'))

# Ručno uređeni distraktori za Zemljopis 74-127.
# Izvorni točan odgovor ostaje netaknut; mijenjaju se samo dva netočna odgovora.
distractors = {
    74: ['Rona', 'Seina'],
    75: ['Kijev', 'Vilnius'],
    76: ['San Marino', 'Monako'],
    77: ['Baku', 'Erevan'],
    78: ['Senegala', 'Volte'],
    79: ['Johannesburg', 'Durban'],
    80: ['Jezera', 'Planine'],
    81: ['Kaduna', 'Sokoto'],
    82: ['Sudana', 'Libije'],
    83: ['Lusaka', 'Harare'],
    84: ['Rodos', 'Eubeja'],
    85: ['Jadransko More', 'Crno More'],
    86: ['Magreb', 'Kalahari'],
    87: ['Maliju', 'Nigeru'],
    88: ['Uzbekistanom', 'Turkmenistanom'],
    89: ['Surabaya', 'Bandung'],
    90: ['Drakeov', 'Beagleov'],
    91: ['Gvajana', 'Brazil'],
    92: ['Jordan', 'Oront'],
    93: ['Gruzije', 'Etiopije'],
    94: ['Srbijom', 'Albanijom'],
    95: ['Etiopije', 'Kenije'],
    96: ['Won', 'Yuan'],
    97: ['Apeninskom', 'Balkanskom'],
    98: ['Dnjepar', 'Don'],
    99: ['Libreville', 'Luanda'],
    100: ['Gurke', 'Tuarezi'],
    101: ['Pas-de-Calais', 'Golfe de Gascogne'],
    102: ['New York', 'Philadelphia'],
    103: ['Pole Pole', 'Jambo Sana'],
    104: ['Indijski Ocean', 'Tihi Ocean'],
    105: ['Jenisej', 'Lena'],
    106: ['Boliviji', 'Čileu'],
    107: ['Kuvajt', 'Sirija'],
    108: ['Lahore', 'Karachi'],
    109: ['San Salvador', 'Managua'],
    110: ['Zürich', 'Ženeva'],
    111: ['Canary Wharf', 'Porta Nuova'],
    112: ['Zambije', 'Bocvane'],
    113: ['Kampala', 'Dodoma'],
    114: ['Srbiju', 'Austriju'],
    115: ['Senegala', 'Tanzanije'],
    116: ['Grenada', 'Sveta Lucija'],
    117: ['Kenijom', 'Somalijom'],
    118: ['Danskom', 'Belgijskim'],
    119: ['Riga', 'Tallinn'],
    120: ['Huang He', 'Mekong'],
    121: ['Španjolskoj', 'Irskoj'],
    122: ['Salomonovi Otoci', 'Vanuatu'],
    123: ['Gvineji', 'Senegalu'],
    124: ['Olimp', 'Helikon'],
    125: ['Laosom', 'Kambodžom'],
    126: ['Salalah', 'Sohar'],
    127: ['Azija', 'Južna Amerika'],
}

original_correct = {
    74: 'Loire', 75: 'Minsk', 76: 'Vatikan', 77: 'Tbilisi', 78: 'Gambije',
    79: 'Bloemfontein', 80: 'Rijeke', 81: 'Benue', 82: 'Egipta', 83: 'Lilongwe',
    84: 'Kreta', 85: 'Baltičko More', 86: 'Sahel', 87: 'Burkini Faso', 88: 'Kazahstanom',
    89: 'Jakarta', 90: 'Mageljanov', 91: 'Surinam', 92: 'Tigris', 93: 'Armenije',
    94: 'Bosnom', 95: 'Somalije', 96: 'Jen', 97: 'Pirinejskom', 98: 'Volga',
    99: 'Kinshasa', 100: 'Sherpe', 101: 'La Manche', 102: 'Washington DC', 103: 'Hakuna Matata',
    104: 'Atlantski Ocean', 105: 'Ob', 106: 'Peruu', 107: 'Irak', 108: 'Islamabad',
    109: 'Tegucigalpa', 110: 'Bern', 111: 'La Defensa', 112: 'Zimbabvea', 113: 'Nairobi',
    114: 'Bosna I Hercegovina', 115: 'Madagaskara', 116: 'Dominika', 117: 'Etiopijom', 118: 'Nizozemskom',
    119: 'Vilnius', 120: 'Jangce', 121: 'Portugalu', 122: 'Papua Nova Gvineja', 123: 'Mali',
    124: 'Parnas', 125: 'Mjanmarom', 126: 'Muscat', 127: 'Afrika',
}

for i in range(74, 128):
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

# Uredničke napomene: izvorni odgovor ne mijenjamo bez zasebne odluke.
d[106]['qa_note'] = 'Pitanje navodi da se Eufrat ulijeva u Indijski ocean; preciznije, Eufrat s Tigrisom tvori Šat al-Arab koji utječe u Perzijski zaljev. Izvorni točan odgovor Irak ostavljen je netaknut.'
d[110]['qa_note'] = 'Naziv pariške poslovne četvrti standardno se piše La Défense; izvorni odgovor "La Defensa" ostavljen je netaknut prema pravilu očuvanja izvornog točnog odgovora.'

assert all(set(q['answers']) == {'A','B','C'} and len(set(q['answers'].values())) == 3 for q in d[73:127])
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('fixed', len(distractors), 'questions 74-127')
