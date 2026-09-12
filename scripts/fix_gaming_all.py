import json, hashlib, re
from pathlib import Path
p=Path('Gaming.json')
data=json.loads(p.read_text(encoding='utf-8'))

POOLS={
'company':['Nintendo','Sega','Konami','Capcom','Namco','Atari','Taito','Electronic Arts','Ubisoft','Valve','Blizzard Entertainment','Sony','Microsoft','Rockstar Games','Naughty Dog','Bethesda Game Studios','id Software','Midway','Williams','Magnavox','Coleco','Niantic','Wargaming'],
'city':['New York','Los Angeles','Chicago','San Francisco','Miami','Seattle','Boston','London','Kopenhagen','Zagreb','Tokyo','Osaka','Seoul'],
'country':['Japan','SAD','Južna Koreja','Finska','Francuska','Njemačka','Švedska','Kanada','Ujedinjeno Kraljevstvo'],
'year':['1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1989','1991','1994','1996','1997','1998','2000','2001','2003','2004','2005','2007','2010','2016','2020'],
'number':['2','3','4','5','6','7','8','9','10','12','15'],
'game':['Pac-Man','Galaga','Frogger','Defender','Joust','Centipede','Asteroids','Contra','Shinobi','Gradius','Diablo','StarCraft','Warcraft','Doom','Quake','Half-Life','Portal','BioShock','Fallout','The Sims','SimCity','Tetris','Minecraft','Fortnite','PUBG','World of Tanks','Need for Speed','Grand Theft Auto','Tekken','Street Fighter','Resident Evil','Crash Bandicoot','Spyro the Dragon','Prince of Persia','God of War','The Legend of Zelda','Metroid'],
'character':['Mario','Luigi','Sonic','Lara Croft','Samus Aran','Solid Snake','Nathan Drake','Kratos','Master Chief','Ryu','Jill Valentine','Leon S. Kennedy','Arthur Morgan','Niko Bellic','CJ','Aloy','Geralt','Steve','Kirby','Pikachu','Crash Bandicoot','Spyro','Jim Raynor','Deckard Cain','Gordon Freeman'],
'person':['Shigeru Miyamoto','Will Wright','John Carmack','Sid Meier','Hideo Kojima','Gabe Newell','Toru Iwatani','Tomohiro Nishikado','Chris Sawyer','Dona Bailey','Ed Logg','Alexey Pajitnov'],
'place':['Hyrule','Lordran','Raccoon City','Liberty City','Vice City','San Andreas','Empire Bay','Bayview','Stormwind','Tristram','Azeroth','Piggy Island'],
'weapon':['Hidden Blade','BFG 9000','Crowbar','Master Sword','Energy Sword','Lancer','Portal Gun','Gravity Gun'],
'item':['Memory Card','Gamepad','Kaciga','Shield','PokéStop','Nuka Cola','Souls','Dragulje','Zlato','Kocka','Avion'],
'creature':['Creeper','Cacodemon','Ender Dragon','Nemesis','Mighty Eagle','King Pig','Boo','Zerg','Vukodlak'],
'sport':['Tenis','Nogomet','Košarka','Stolni tenis','Hokej','Bejzbol'],
'color':['Crvene','Plave','Zelene','Žute','Crne','Bijele'],
}

RELATED={
'Will Wright':['Sid Meier','Peter Molyneux'], 'Valve':['Blizzard Entertainment','Epic Games'], 'Nexus':['Inhibitor','Turret'], 'Adam':['EVE','Plasmid'],
'New York':['Chicago','Boston'], 'Animus':['Helix','Memory Corridor'], 'Samus Aran':['Lara Croft','Jill Valentine'], 'Ivana Orleanska':['Saladin','William Wallace'],
'Gandhi':['Abraham Lincoln','Julius Caesar'], 'Lara Croft':['Jill Valentine','Aloy'], 'Mental':['Ugh-Zan III','Mordekai'], 'Sonic':['Tails','Knuckles'],
'Leon S. Kennedy':['Chris Redfield','Carlos Oliveira'], 'Ancient':['Barracks','Fountain'], 'King Pig':['Foreman Pig','Chef Pig'], 'Hidden Blade':['Phantom Blade','Hookblade'],
'Mighty Eagle':['Mighty Dragon','Terence'], 'Ralph':['George','Lizzie'], 'Bayview':['Rockport','Palmont'], 'Alliance':['Horde','Scourge'], 'Memory Card':['Expansion Pak','Rumble Pak'],
'Sony':['Nintendo','Sega'], 'Atari':['Coleco','Mattel'], 'Luigi':['Wario','Waluigi'], 'Steve':['Alex','Herobrine'], 'Nuka Cola':['Sunset Sarsaparilla','Vim!'],
'Taito':['Namco','Konami'], 'Piggy Island':['Bird Island','Golden Island'], 'Captain Price':['Soap MacTavish','Gaz'], 'Crash Bandicoot':['Spyro','Rayman'],
'Need for Speed':['Burnout','Midnight Club'], 'Solid Snake':['Sam Fisher','Agent 47'], 'Arthur Morgan':['John Marston','Dutch van der Linde'], 'Sega':['Nintendo','NEC'],
'Shredder':['Krang','Baxter Stockman'], 'Kornjače':['Krokodili','Vidre'], 'Prin Prin':['Princess Peach','Princess Daphne'], 'Glados':['SHODAN','Cortana'],
"Eden's Gate":['The Project at Eden’s Gate','Children of Atom'], 'Gwyn':['Artorias','Ornstein'], 'Neo Cortex':['N. Gin','N. Tropy'], 'Tarnished':['Chosen Undead','Bearer of the Curse'],
'Spy Hunter':['RoadBlasters','Out Run'], 'Sue':['Clyde','Blinky'], 'Boo':['Dry Bones','Shy Guy'], 'Olly':['Dimentio','Count Bleck'], 'CJ':['Tommy Vercetti','Niko Bellic'],
'PUBG':['H1Z1','Fortnite'], 'Modern Warfare':['Black Ops','World at War'], 'Empire Bay':['Liberty City','Lost Heaven'], 'Namco':['Konami','Taito'],
'Aloy':['Kassandra','Jesse Faden'], 'Mona Sax':['Nicole Horne','Michelle Payne'], 'Kazuya Mishima':['Jin Kazama','Heihachi Mishima'], 'Microsoft':['Sony','Nintendo'],
'Zombies':['Spec Ops','Survival'], 'Origami':['Kirigami','Papercraft'], 'Williams':['Midway','Atari'], 'Liberty City':['Vice City','Los Santos'], 'Južna Koreja':['Japan','Kina'],
'Heihachi Mishima':['Jinpachi Mishima','Kazuya Mishima'], 'Razor':['Ronnie','Bull'], 'PlayStation 5':['PlayStation 4','PlayStation 3'], 'Frogger':['Q*bert','Dig Dug'],
'Souls':['Humanity','Titanite'], 'Sony Interactive Entertainment':['Nintendo','Microsoft'], 'Nora':['Carja','Oseram'], 'Magnavox':['Coleco','Atari'], 'Naughty Dog':['Insomniac Games','Sucker Punch'],
'Dust II':['Inferno','Mirage'], 'Coleco':['Mattel','Magnavox'], 'Philips':['De Santa','Townley'], 'Valkyr':['V','Chronos'], 'Splinter':['Shredder','Baxter Stockman'],
'Dragulje':['Kristale','Novčiće'], 'Croteam':['CroTeam Games','Nanobit'], 'Zelene':['Crvene','Plave'], 'PlayStation 2':['PlayStation 3','PlayStation 1'], 'Bob Omb':['Goomba','Koopa Troopa'],
'Tristram':['Westmarch','Lut Gholein'], 'StarCraft':['Command & Conquer','Total Annihilation'], 'Hyrule':['Termina','Lorule'], 'Kaciga':['Prsluk','Ruksak'], 'FUT':['MUT','MyTEAM'],
'Snijeg':['Led','Voda'], 'Electronic Arts':['Activision','Ubisoft'], 'Chris Sawyer':['Sid Meier','Peter Molyneux'], 'Most Wanted':['Carbon','Underground'], 'Margit':['Godrick','Morgott'],
'Thrall':['Grom Hellscream','Orgrim Doomhammer'], 'Pro Evolution Soccer':['FIFA','Virtua Striker'], 'Stormwind':['Ironforge','Darnassus'], 'Kuma':['Panda','Roger Jr.'], 'Peter Pepper':['Mr. Do','Dig Dug'],
'Cacodemon':['Pain Elemental','Mancubus'], 'The Combine':['Xen','Race X'], 'Pac Man':['Galaga','Dig Dug'], 'George':['Lizzie','Ralph'], 'Stolar':['Vodoinstalater','Građevinar'],
'Šest':['Pet','Sedam'], 'Dona Bailey':['Carol Shaw','Roberta Williams'], 'Bomb':['Chuck','Terence'], 'Zerg':['Protoss','Terran'], 'Konami':['Capcom','Namco'], 'Finske':['Švedske','Norveške'],
'Call of Duty':['Medal of Honor','Battlefield'], 'Ender Dragon':['Wither','Warden'], 'Blizzard Entertainment':['BioWare','Bethesda Game Studios'], 'Tomohiro Nishikado':['Toru Iwatani','Shigeru Miyamoto'],
'PokéStop':['Gym','PokéCenter'], 'Farah':['Kaileena','Elika'], 'Aku Aku':['Uka Uka','Lani-Loli'], 'King':['Armor King','Marduk'], 'Diablo':['Baal','Mephisto'],
'Tenis':['Stolni tenis','Badminton'], 'Creeper':['Zombie','Skeleton'], 'Zmaj':['Grifon','Feniks'], 'Zagreb':['Split','Rijeka'], 'Arkada':['Platformer','Avantura'], 'Nathan Drake':['Victor Sullivan','Sam Drake'],
'PlayStation 1':['Nintendo 64','Sega Saturn'], 'BMW':['Porsche','Mercedes-Benz'], 'Zlato':['Drvo','Kamen'], 'Kratos':['Ares','Deimos'], 'Avion':['Helikopter','Brod'], 'Niko Bellic':['Johnny Klebitz','Luis Lopez'],
'Nintendo':['Sega','Sony'], 'Jim Raynor':['Arcturus Mengsk','Tychus Findlay'], 'Pagan Min':['Vaas Montenegro','Joseph Seed'], 'Umbrella':['Tricell','WilPharma'], 'Tetromine':['Pentomine','Tromine'],
'Jin Kazama':['Hwoarang','Lee Chaolan'], 'Roach':['Kelpie','Bucephalus'], 'Contra':['Metal Slug','Gunstar Heroes'], 'Master Chief':['Marcus Fenix','Doom Slayer'], 'Usisavačem':['Metlom','Tavom'],
'Simlish':['Hylian','Al Bhed'], 'Bally Midway':['Atari','Williams'], 'E Football':['FIFA','UFL'], 'Vault Boy':['Pip-Boy','Nuka-Girl'], 'The Lich King':['Deathwing','Kil’jaeden'],
'Nemesis':['Mr. X','Birkin'], 'Žabu':['Kornjaču','Guštera'], 'Vukodlak':['Medvjed','Zmaj'], 'Ryu':['Ken','Akuma'], 'Niantic':['Zynga','Supercell'],
'World of Tanks':['War Thunder','Armored Warfare'], 'Pikachu':['Raichu','Jolteon'], 'G Man':['Barney Calhoun','Eli Vance'], 'Battle Royale':['Team Rumble','Save the World'], 'Shield':['Armor','Barrier'],
'Raccoon City':['Silent Hill','Ravenholm'], 'Lordran':['Drangleic','Boletaria'], 'Deckard Cain':['Adria','Tyrael'], 'Shinobi':['Shadow Dancer','Ninja Gaiden'], 'Koko':['Tawna','Nina Cortex'], 'Gradius':['R-Type','Darius']
}

def kind(q,c):
    l=q.lower()
    if re.fullmatch(r'\d{4}', str(c)): return 'year'
    if str(c).isdigit() or c in ['Šest','Pet','Sedam']: return 'number'
    if 'koje boje' in l or 'koja boja' in l: return 'color'
    if 'kompanij' in l or 'studio ' in l or 'tvrtk' in l: return 'company'
    if 'koje godine' in l or 'koja se godina' in l: return 'year'
    if 'koliko' in l: return 'number'
    if 'u kojoj je državi' in l or 'iz koje je države' in l: return 'country'
    if 'u kojem se američkom gradu' in l or 'iz kojeg je hrvatskog grada' in l: return 'city'
    if 'koji sport' in l: return 'sport'
    if 'kako se zove grad' in l or 'kako se zove kraljevstvo' in l or 'kako se zove otok' in l or 'izmišljeni grad' in l or 'glavni grad' in l: return 'place'
    if 'dizajner' in l or 'programer' in l or 'povijesna ličnost' in l or 'povijesna francuska' in l or 'dizajnerica' in l: return 'person'
    if 'kako se zove serijal' in l or 'kako se zove arkadna videoigra' in l or 'koju je arkadnu' in l or 'koja je znanstveno-fantastična strateška igra' in l or 'koji se nastavak' in l or 'kako se zove nastavak' in l: return 'game'
    if 'oružj' in l: return 'weapon'
    if 'životinj' in l or 'mitskog bića' in l or 'zvijer' in l: return 'creature'
    if any(x in l for x in ['protagonist','junak','lik','princeza','policajac','vojnik','antagonist','neprijatelj','gospodar','borac','kralj','orao','vukodlak','duh','kuhar','medvjed','štakor','maskirani','odmetnik','demon','zmaj','ptica']): return 'character'
    if any(x in l for x in ['predmet','resurs','tvar','kartica','zaštita','droga','piće','građevina','frakcija','uređaj','jezik','umjetnost','pleme','način igranja','kraticom','kratica']): return 'item'
    return 'game'

def choose(q,c):
    if c in RELATED: return RELATED[c][:2]
    pool=POOLS[kind(q,c)]
    opts=[x for x in pool if x.casefold()!=str(c).casefold()]
    seed=int(hashlib.sha256((q+'|'+str(c)).encode()).hexdigest()[:12],16)
    a=opts[seed%len(opts)]; b=opts[(seed//len(opts)+7)%len(opts)]
    if b==a: b=opts[(opts.index(a)+1)%len(opts)]
    return [a,b]

for item in data:
    ca=item['correct_answer']; ans=item['answers']; correct=ans[ca]
    wrong=choose(item['question'],correct)
    letters=[x for x in 'ABC' if x!=ca]
    ans[letters[0]]=wrong[0]; ans[letters[1]]=wrong[1]
    assert ans[ca]==correct
    assert len(set(ans.values()))==3

p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Gaming questions fixed:',len(data))
print('Questions unchanged; original correct answer strings preserved at their original correct_answer letters.')
