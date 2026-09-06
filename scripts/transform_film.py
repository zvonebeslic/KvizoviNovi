import json
import urllib.request
from pathlib import Path

SOURCE = "https://raw.githubusercontent.com/zvonebeslic/balkanska_pub_prica/main/Film.json"
ROOT = Path(__file__).resolve().parents[1]

with urllib.request.urlopen(SOURCE, timeout=30) as r:
    source = json.loads(r.read().decode("utf-8"))

wrong = []
for n in (1, 2, 3):
    with open(ROOT / "scripts" / f"film_distractors_{n}.json", encoding="utf-8") as f:
        wrong.extend(json.load(f))

if len(source) != len(wrong):
    raise SystemExit(f"Broj pitanja i distraktora se ne poklapa: source={len(source)}, distractors={len(wrong)}")

out = []
letters = "ABC"
for i, (src, pair) in enumerate(zip(source, wrong)):
    if not isinstance(src.get("answers"), list) or not src["answers"]:
        raise SystemExit(f"Pitanje {i+1} nema izvorni točan odgovor")
    if not isinstance(pair, list) or len(pair) != 2:
        raise SystemExit(f"Pitanje {i+1} nema točno dva distraktora")

    correct = src["answers"][0]
    if correct in pair or pair[0] == pair[1]:
        raise SystemExit(f"Neispravni distraktori na pitanju {i+1}")

    pos = i % 3
    values = []
    wi = iter(pair)
    for p in range(3):
        values.append(correct if p == pos else next(wi))

    item = dict(src)
    item["answers"] = {"A": values[0], "B": values[1], "C": values[2]}
    item["correct_answer"] = letters[pos]
    out.append(item)

counts = {l: sum(q["correct_answer"] == l for q in out) for l in letters}
if max(counts.values()) - min(counts.values()) > 1:
    raise SystemExit(f"Neuravnotežena raspodjela: {counts}")

with open(ROOT / "Film.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Film.json: {len(out)} pitanja; raspodjela {counts}")
# workflow trigger
