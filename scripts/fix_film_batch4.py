import json
from pathlib import Path

p = Path('Film.json')
data = json.loads(p.read_text(encoding='utf-8'))

fixes = {
    "U filmu 'Amélie', u kojem dijelu Pariza živi i radi glavna junakinja Amelie Poulain?": {
        "A": "Le Maraisu",
        "B": "Latinskoj četvrti",
        "C": "Montmartreu"
    },
    "Koji je američki gluhi glumac dobio oscara za ulogu u filmu 'Coda', igrajući ulogu Franka, gluhog oca obitelji Rossi?": {
        "A": "Russell Harvard",
        "B": "Daniel Durant",
        "C": "Troy Kotsur"
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
