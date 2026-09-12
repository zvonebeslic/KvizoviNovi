import json
from pathlib import Path

p = Path('FloraFauna.json')
data = json.loads(p.read_text(encoding='utf-8'))

fixes = {
    "Koja životinja na sebi ima kućicu?": {
        "answers": {"A": "Glista", "B": "Puž", "C": "Jež"},
        "correct_answer": "B",
    },
    "Koji se austrijski zoolog i nobelovac smarta jednim od osnivača moderne etologije?": {
        "answers": {"A": "Konrad Lorenz", "B": "Desmond Morris", "C": "Nikolaas Tinbergen"},
        "correct_answer": "A",
    },
    "Pas Lajka je jedno od prvih živih bića u svemiru, ali i pas lutalica iz kojeg grada?": {
        "answers": {"A": "Lenjingrada", "B": "Moskve", "C": "Kijeva"},
        "correct_answer": "B",
    },
    "Budistički tekstovi pisani Gandhārskim pismom su jedni od najstarijih sačuvanih budističkih rukopisa uopće, a pisani su na kori kojeg drveta?": {
        "answers": {"A": "Cedra", "B": "Breze", "C": "Bora"},
        "correct_answer": "B",
    },
    "Koja životinja u Kini simbolizira dug život?": {
        "answers": {"A": "Panda", "B": "Kornjača", "C": "Tigar"},
        "correct_answer": "B",
    },
    "Napoleon, Old Major, Squealer, Snowball, Minimus i Pinkeye su svi redom koja životinja?": {
        "answers": {"A": "Konj", "B": "Svinja", "C": "Pas"},
        "correct_answer": "B",
    },
    "Koji cvijet stoji na grbu glavnog grada talijanske pokrajine Toskane?": {
        "answers": {"A": "Ruža", "B": "Ljiljan", "C": "Karanfil"},
        "correct_answer": "B",
    },
}

seen = set()
for q in data:
    qt = q.get('question')
    if qt in fixes:
        old_correct = q['answers'][q['correct_answer']]
        f = fixes[qt]
        new_correct = f['answers'][f['correct_answer']]
        # Preserve the intended original correct answer semantically; case-only correction allowed for Moscow/birch.
        allowed = {
            ('Moskvi', 'Moskve'),
            ('Breza', 'Breze'),
        }
        assert old_correct == new_correct or (old_correct, new_correct) in allowed, (qt, old_correct, new_correct)
        q['answers'] = f['answers']
        q['correct_answer'] = f['correct_answer']
        assert len(set(q['answers'].values())) == 3
        seen.add(qt)

assert seen == set(fixes), (set(fixes) - seen)
assert len(data) == 172, len(data)

# Structural final audit.
for i, q in enumerate(data, 1):
    assert q['correct_answer'] in ('A','B','C'), i
    assert set(q['answers']) == {'A','B','C'}, i
    assert len(set(q['answers'].values())) == 3, i
    assert q['answers'][q['correct_answer']], i

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('FloraFauna final fixes:', len(fixes), 'questions:', len(data))
