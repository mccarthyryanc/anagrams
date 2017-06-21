# Anagrams

A script to generate lists of anagrams by using Python dicts and the Fundamental Theorem of Arithmetic. To keep output simple, anagrams with words that are at least 4 letters long and at least as many anagrams as there are letters are output.


## Algorithm

Via the Fundamental Theorem of Arithmetic, we know that any integer can be uniquely factored into primes. An integer can be constructed from a word by representing each letter in an alphabet as a prime and then multiplying these letters. Because multiplication is order independent, words that are formed with the same letters will have the same unique integer representation: This creates a unique key for an anagram set. This is use to find anagrams based off an input dictionary of words.

## Dependencies

  * Python 3.5 or greater
  * Prime number list, included as `primes-to-100k.txt`. Sorry, I was too lazy to write code to generate primes...

## Usage

This was tested on Ubuntu 16.04 using dictionaries found in `/usr/share/dict`. Because it pulls all characters from the Unicode 'Ll' category, it should work many different languages.

By default output uses english:

```bash
./anagrams.py
```

Should output:

```
abet, bate, beat, beta
rues, ruse, sure, user
ores, roes, rose, sore
eons, noes, nose, ones
bast, bats, stab, tabs
dale, deal, lade, lead
gnus, guns, snug, sung
amen, mane, mean, name
pars, raps, rasp, spar
leap, pale, peal, plea
huts, shut, thus, tush
acts, cast, cats, scat
ales, leas, sale, seal
opts, post, pots, spot, stop, tops
oils, silo, soil, soli
mate, meat, tame, team
part, rapt, tarp, trap
pare, pear, rape, reap
emit, item, mite, time
evil, live, veil, vile
last, lats, salt, slat
ares, ears, eras, sear, sera
bust, buts, stub, tubs
asps, pass, saps, spas
lair, liar, lira, rail
nips, pins, snip, spin
past, pats, spat, taps
diet, edit, tide, tied
arts, rats, star, tars, tsar
east, eats, sate, seat, teas
naps, pans, snap, span
nope, open, peon, pone
nest, nets, sent, tens
bares, baser, bears, saber, sabre
hares, hears, rheas, share, shear
reins, resin, rinse, risen, siren
ester, reset, steer, terse, trees
lapse, leaps, pales, peals, pleas, sepal
pares, parse, pears, rapes, reaps, spare, spear
abets, baste, bates, beast, beats, betas
pores, poser, prose, ropes, spore
emits, items, mites, smite, times
least, slate, stale, steal, tales, teals
parts, sprat, strap, tarps, traps
aster, rates, stare, tares, tears
mates, meats, steam, tames, teams
skate, stake, steak, takes, teaks
arced, cadre, cared, cedar, raced
caret, cater, crate, react, recta, trace
paste, pates, septa, spate, tapes
drapes, padres, parsed, rasped, spared, spread
carets, caster, caters, crates, reacts, recast, traces
palest, pastel, petals, plates, pleats, staple
```

Also if you have other languages' dictionaries installed you can find anagrams in them too! **WARNING**: I only speak English so I have no idea what any of these words mean :-)

```bash
./anagrams.py -d /usr/share/dict/danish -w 7
```

will output:

```txt
agerens, agrenes, gaserne, reagens, sagerne, sangere, sargene
ankrets, kanters, knaster, kranset, skarnet, skrante, tankers
krattes, retsakt, skatter, skratte, strakte, takster, takters, trasket
nistret, nitters, rittens, snitter, strinte, tinters, trinets
erantis, inserat, retsina, satiner, satiren, sitaren, stearin
kortest, kortets, skortet, skotter, skrotte, storket, torsket
dyrenes, dyserne, snydere, syndere, syrende, yderens, ydernes, ynderes
genlæst, lægtens, længste, længtes, slægten, slænget, stængel
akternes, ankerets, enakters, karetens, kasterne, sekanter, taskerne, trakeens
ankernes, ankrenes, annekser, kanernes, kasernen, kransene, skannere, skarnene
ankredes, danskere, dekaners, eskadren, rankedes, skaderne, skandere, skarende
dynernes, snyderen, snyderne, synderen, synderne, syrnende, ynderens, yndernes
avlerens, avlernes, lavernes, relevans, salverne, slaveren, slaverne, svalerne, valenser, velarens, versalen
ringeste, signeret, signeter, sigterne, stenrige, stigerne, tigerens, tigrenes
ferniser, finerers, firerens, firernes, firserne, frierens, friernes, friserne
```

Or if the file uses a different encoding:

```bash
./anagrams.py -d /usr/share/dict/portuguese -e iso-8859-1 -w 10
```

Which outputs:

```txt
acarreteis, acertareis, carreteais, carreteias, catarreeis, catarreies, estarrecia, recatareis, receitaras, recetarias, secretaria, secretaria
acordantes, acordantes, cantadores, coentradas, consertada, recontadas, descontara, encartados, encastrado, encrostada, estroncada
amarroteis, amostrarei, atiraremos, atrairemos, estoiraram, maroteiras, retomarias, retraiamos, sorteariam, tesoiraram
adentarmos, adentramos, adormentas, amedrontas, amestrando, amontardes, antedarmos, atendarmos, mastreando, desmontara, remontadas
amestrarei, arremateis, arremetais, arremetias, estreariam, estremaria, mastrearei, rematareis, reteimaras, retesariam
```

Wow! Looks like Portuguese has lots of anagrams! TODO: compare different languages for the distribution of anagram counts over word length.
