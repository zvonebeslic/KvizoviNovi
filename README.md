# KvizoviNovi

Ovaj repozitorij sadrži ABC verzije pitanja iz repozitorija `balkanska_pub_prica`.

## Pravila pretvorbe

- Tekst pitanja ostaje nepromijenjen.
- Prvi odgovor iz izvornog polja `answers` smatra se jedinim točnim odgovorom.
- Ostale izvorne varijante pisanja/izgovora ne koriste se kao ponuđeni odgovori.
- Za svako pitanje izrađuju se dva semantički smislena netočna odgovora iste vrste kao točan odgovor.
- Kod prirodno binarnih pitanja koriste se samo A i B.
- Točni odgovori raspoređuju se približno ravnomjerno između A, B i C.
- Svaki zapis ima polje `correct_answer` s vrijednošću `A`, `B` ili `C`.

Format:

```json
{
  "type": "blitz",
  "difficulty": 3,
  "topic": "Film",
  "question": "...",
  "answers": {
    "A": "...",
    "B": "...",
    "C": "..."
  },
  "correct_answer": "B",
  "image": null
}
```
