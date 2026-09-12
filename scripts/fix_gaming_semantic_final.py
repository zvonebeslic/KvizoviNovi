import json
p='Gaming.json'
with open(p,encoding='utf-8') as f: data=json.load(f)
# Only distractors are changed. Original question text, original correct-answer text and correct_answer letters stay untouched.
fixes={
8:{'A':'Jeanne de Clisson','C':'Marie Marvingt'},
63:{'A':'Marshall Law','B':'Bryan Fury'},
95:{'A':'Gamepires','C':'Nanobit'},
133:{'B':'Godrick','C':'Rennala'},
182:{'A':'Space Invaders','C':'Phoenix'},
216:{'A':'Nova Terra','B':'Selendis'},
218:{'A':'King Boo','C':'Wario'},
219:{'A':'Božić','B':'Duhovi'},
220:{'B':'Aperture Science','C':'Umbrella Laboratory'},
224:{'A':'Mephisto','C':'Azmodan'},
225:{'A':'Empire Bay','B':'Liberty City'},
229:{'B':'Toadette','C':'Goomba'},
230:{'A':'Lisa','C':'Homer'},
232:{'B':'Snow Bros.','C':'Tumble Pop'},
234:{'A':'Cole Phelps','B':'Wei Shen'},
236:{'A':'Pobunjenici','C':'Plaćenici'},
240:{'A':'Lordran','B':'Drangleic'},
241:{'B':'Force Feedback','C':'Haptic Feedback'},
242:{'A':'Dual Analog','C':'Sixaxis'},
243:{'A':'Aviona','B':'Brodova'},
244:{'B':'Drugi svjetski rat','C':'Vijetnamski rat'},
246:{'A':'Fygar','B':'Taizo Hori'},
249:{'A':'Little Sisters','B':'Splicers'},
250:{'B':'Vice City','C':'Liberty City'},
253:{'B':'Nemesis','C':'Mr. X'},
255:{'A':'Galaxian','B':'Xevious'},
288:{'A':'Konstrukti','B':'Sinteti'},
316:{'B':'Stealth Boy','C':'RobCo Fun'},
317:{'A':'Zerg','C':'Terran'},
318:{'A':'Alexey Pajitnov','B':'Vadim Gerasimov'},
321:{'A':'Gume','B':'Bačvice'},
323:{'A':'Daisy','C':'Rosalina'},
326:{'A':'Puran','C':'Patka'},
330:{'A':'Questor','B':'Merlin'},
332:{'A':'Košarka','C':'Hokej'},
337:{'B':'Ripto','C':'Red'},
339:{'A':'Altered Beast','B':'Gauntlet'},
342:{'A':'Naughty Dog','B':'Sucker Punch Productions'},
344:{'A':'R-9 Arrowhead','C':'Silver Hawk'},
345:{'A':'Stormbird','B':'Rockbreaker'},
347:{'A':'Ciglu','C':'Beton'},
348:{'A':'Pandemonium','B':'Westmarch'},
349:{'B':'ROG Ally','C':'Legion Go'},
350:{'A':'Walter Raleigh','C':'James Cook'},
351:{'A':'Grčkoj','B':'Rimskoj'},
354:{'A':'Colorado','B':'Wyoming'},
362:{'A':'Guild Wars 2','C':'The Elder Scrolls Online'},
398:{'A':'Hogan’s Alley','C':'Wild Gunman'},
442:{'B':'Tommy Angelo','C':'Lincoln Clay'}
}
for n,repl in fixes.items():
    x=data[n-1]
    ca=x['correct_answer']; original=x['answers'][ca]
    for k,v in repl.items():
        if k!=ca: x['answers'][k]=v
    assert x['answers'][ca]==original, (n,original,x['answers'][ca])
    assert len({x['answers'][k].casefold() for k in 'ABC'})==3, n
assert len(data)==444
with open(p,'w',encoding='utf-8') as f: json.dump(data,f,ensure_ascii=False,indent=2); f.write('\n')
print('Fixed',len(fixes),'Gaming answer sets; original correct answers preserved.')
