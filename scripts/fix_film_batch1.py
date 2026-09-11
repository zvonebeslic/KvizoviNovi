import json
from pathlib import Path

p = Path('Film.json')
data = json.loads(p.read_text(encoding='utf-8'))

fixes = {
"Koji je film 1994. godine pobijedio 'Pakleni šund' u utrci za najbolji film?": {
    "A": "The Shawshank Redemption", "B": "Four Weddings and a Funeral", "C": "Forrest Gump"
},
"U kojoj državi se odvija radnja filma 'Casablanca' iz 1942.?": {
    "A": "Maroku", "B": "Alžiru", "C": "Tunisu"
},
"U kojem gradu žive 'Prijatelji' (Friends)?": {
    "A": "Chicagu", "B": "Bostonu", "C": "New Yorku"
},
"Koji je film 1929. prvi osvojio Oscara za najbolji film?": {
    "A": "Krila", "B": "Izlazak sunca", "C": "Pjevač jazza"
},
"Iz koje je zemlje redatelj Bong Joon-ho, redatelj filma 'Parazit'?": {
    "A": "Južne Koreje", "B": "Japana", "C": "Kine"
},
"Koji je prvi dugometražni animirani film Walta Disneyja?": {
    "A": "Pinokio", "B": "Fantazija", "C": "Snjeguljica i sedam patuljaka"
},
"U Velom Mistu je bio Jozo, u Jelenku je bio Mate, u Prosjacima i sinovima je bio Divac. Kojeg glumca tražimo?": {
    "A": "Borisa Dvornika", "B": "Špiru Guberinu", "C": "Ivicu Vidovića"
},
"U kojem zatvoru završava Andy Dufresne nakon što ubije svoju suprugu i njenog ljubavnika?": {
    "A": "Alcatrazu", "B": "Sing Singu", "C": "Shawshanku"
},
"Koji film prati povijest stvaranja Facebooka?": {
    "A": "Steve Jobs", "B": "Osnivač", "C": "Društvena mreža"
},
"Koji je film poznat po rečenici: 'Life is like a box of chocolates'?": {
    "A": "The Green Mile", "B": "Forrest Gump", "C": "The Terminal"
},
"Koji je film prvi u povijesti zaradio više od 2 milijarde dolara?": {
    "A": "Titanic", "B": "Avengers: Endgame", "C": "Avatar"
},
"Koji je film poznat po rečenici: 'E.T. phone home'?": {
    "A": "Close Encounters of the Third Kind", "B": "Gremlins", "C": "E.T."
},
"U filmu 'Joker', u kojoj četvrti New Yorka Arthur Fleck pleše stepenicama, koje su kasnije postale turistička atrakcija?": {
    "A": "Queensu", "B": "Brooklynu", "C": "Bronxu"
}
}

seen = set()
for q in data:
    question = q.get('question')
    if question in fixes:
        q['answers'] = fixes[question]
        seen.add(question)

missing = set(fixes) - seen
if missing:
    raise SystemExit('Missing questions: ' + repr(sorted(missing)))

# structural safety
assert all(set(q.get('answers',{})) == {'A','B','C'} for q in data)
assert all(q.get('correct_answer') in {'A','B','C'} for q in data)

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('fixed', len(seen), 'questions; total', len(data))
