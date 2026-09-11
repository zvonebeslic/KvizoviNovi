import json
from pathlib import Path

p = Path('Film.json')
data = json.loads(p.read_text(encoding='utf-8'))

fixes = {
    "Koji je film 1929. prvi osvojio Oscara za najbolji film?": {
        "A": "Krila", "B": "Izlazak sunca", "C": "Pjevač jazza"
    },
    "U kojem gradu žive 'Prijatelji' (Friends)?": {
        "A": "Chicagu", "B": "Bostonu", "C": "New Yorku"
    },
    "Iz koje je zemlje redatelj Bong Joon-ho, redatelj filma 'Parazit'?": {
        "A": "Južne Koreje", "B": "Japana", "C": "Kine"
    },
    "U Velom Mistu je bio Jozo, u Jelenku je bio Mate, u Prosjacima i sinovima je bio Divac. Kojeg glumca tražimo?": {
        "A": "Borisa Dvornika", "B": "Špiru Guberinu", "C": "Ivicu Vidovića"
    },
    "Koji film prati povijest stvaranja Facebooka?": {
        "A": "Pirati Silicijske doline", "B": "Osnivač", "C": "Društvena mreža"
    },
    "Koji je film poznat po rečenici: 'Life is like a box of chocolates'?": {
        "A": "The Green Mile", "B": "Forrest Gump", "C": "The Terminal"
    },
    "Koji je film prvi u povijesti zaradio više od 2 milijarde dolara?": {
        "A": "Titanic", "B": "Avengers: Endgame", "C": "Avatar"
    },
    "U filmu 'Joker', u kojoj četvrti New Yorka Arthur Fleck pleše stepenicama, koje su kasnije postale turistička atrakcija?": {
        "A": "Queensu", "B": "Brooklynu", "C": "Bronxu"
    },
    "Koji je prvi dugometražni animirani film Walta Disneyja?": {
        "A": "Pinokio", "B": "Fantazija", "C": "Snjeguljica i sedam patuljaka"
    }
}

changed = 0
for item in data:
    q = item.get('question')
    if q in fixes:
        old_correct = item['correct_answer']
        item['answers'] = fixes[q]
        assert old_correct in item['answers']
        changed += 1

assert changed == len(fixes), (changed, len(fixes))
assert all(set(x['answers']) == {'A','B','C'} for x in data)
assert all(x['correct_answer'] in x['answers'] for x in data)

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('changed', changed, 'questions', len(data))
