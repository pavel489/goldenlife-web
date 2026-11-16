# Svačinky Slim GLP-1 Shake — SK / EN / DE

**18 dokončených HTML, interní pracovní překlad; bez právního schválení a bez nasazení.**

## Výstup
- `out/<původní repo cesta>`: pro ID **547 cappuccino**, **470 kokos–bílá čokoláda**, **458 vanilka–jahoda** vždy dlouhý a krátký popis v SK, EN, DE. Krátké popisy zůstávají v `maly/`; přípona `-cz` je nahrazena jazykem.
- `manifest.json`: přesných 18 relativních cest, SHA-256, testy, zdroje a omezení.
- `analysis/translations.json`: úplný zdrojový a překladový inventář 294 jedinečných textových segmentů. Čistě číselné segmenty a skutečné názvy značek zůstávají beze změny; vysvětlující zkratky RHP/KJT jsou lokalizovány bez převodu množství.
- `analysis/edits.json`: všechny přesné změny se zdrojovými a cílovými offsety; jejich obrácení obnoví celý původní soubor. Žádná celodokumentová HTML normalizace.
- `analysis/claims-ledger.json`: přesné původní rizikové věty / celé odstavce a související překlady, neutrální věcné alternativy v CZ/SK/EN/DE a jejich doslovný podklad z konkrétního produktového `info.md`. Nejde o povolené ekvivalentní zdravotní tvrzení.
- `analysis/screenshots/`: skutečné Chromium snímky výsledných souborů, včetně produktových fotografií a otevřených dialogů.

## Zachováno a přeloženo
Úplné úvody, dlouhé vysvětlení, všech devět originálních dialogů v každé dlouhé jazykové verzi, tabulky, alergeny, skladování, upozornění, všechny alt/aria texty a zákaznické JavaScriptové popisky. Přeloženy jsou i regexy pro rozpoznání obou mobilních nadpisů. Každé SKU si zachovává vlastní příchuť, obrázky, recepturu i mapování surovin: cappuccino má např. syrovátkový protein tam, kde kokosová varianta uvádí chrom. Technická ID, odkazy, CSS a logika zůstávají zachovány.

Jediná typografická úprava nad rámec běžného překladu: německé `Schokoladen­geschmack` obsahuje měkký spojovník, aby nadpis při zachovaném CSS nebyl na telefonu uříznutý. Je zahrnut v inventáři i v reverzibilních editech.

## Reálné testy
- `analysis/static-tests.json`: všech 18 HTML; shoda stromu tagů, chráněných atributů, CSS, URL, technických kotev, číselných buněk i všech číselných hodnot v textových segmentech; úplnost inventáře a počty odstavců dialogů; jedinečná ID.
- **45 skutečně vytažených vykonatelných skriptů prošlo `node --check`.** `analysis/scripts/` obsahuje testované znění.
- `analysis/runtime-tests.json`: všech 18 HTML v jsdom; porovnání skutečného AST přes Acorn dovoluje pouze inventarizované zákaznické literály a regex. Spuštěno všech 45 skriptů; 27 mobilních přepínačů, 81 stavů dialogů a mobil–desktop–mobil cleanup. Jde o logický fixture, nikoli vizuální důkaz.
- `analysis/browser-tests.json`: **36/36 skutečných Chromium scénářů**, všech 18 souborů při 1280 a 390 px; **162 otevření devíti dialogů pointerem a zavření Escape**, informační dialogy, 27 mobilních přepínačů a responsive round trip. Všechny IMG se dekódovaly; bez chyb JS, horizontálního přetečení dokumentu a přetékajících popisků piktogramů.
- `analysis/responsive-tests.json`: **99 dalších layout scénářů**; dlouhé při 320, 360, 767, 768, 820, 1024 px včetně tabletů 768×1024, 820×1180 a 1024×768; krátké při šířce hostitele 280, 300, 320, 360, 420 px. Bez zjištěného přetečení sledovaných nadpisů/popisků či dokumentu. Navíc všech 9 dlouhých HTML bez JS: **81 otevření/zavření původních CSS-target dialogů skutečným kliknutím**.
- `analysis/asset-tests.json`: všech **35 různých zděděných IMG URL reálně staženo s HTTP 200**, uloženy skutečné bajty a hashe. Tyto skutečné odpovědi byly použity pro opakovatelný prohlížečový test; žádné náhradní nebo syntetické fotografie. Produkční URL zůstávají doslovně stejné.
- `analysis/source-tests.json`: všech šest CZ zdrojů porovnáno bajtově s uvedeným commitem. Výstupy nepřepisují zdrojové soubory.

## Děděná omezení a předání k revizi
1. Produktové `info.md` všech tří SKU výslovně **neuvádějí schválená EFSA tvrzení**. Původní účinkové věty jsou na výslovný pokyn úplně a věrně přeloženy do tohoto interního návrhu, nikoli schváleny pro publikaci. Zejména GLP-1 aktivace, potlačení chuti, spalování tuku, 27 %, omlazení, probiotika/imunita, buněčná hydratace a konkurenční srovnání vyžadují revizi; ledger nedoporučuje schválit je jen kvůli překladu.
2. Původní text uvádí **8,9 mld. CFU**, ale tabulka dávky uvádí **0,75 mld. KJT / 50 mg**. Čísla jsou ponechána, nikoli sjednocena nebo dopočítána.
3. Původní piktogram **„Bez cukru“** je v konfliktu s tabulkou **8 g cukrů / 100 g, 2,4 g / dávka**. Původní **„Bez přídatných látek“** vyžaduje revizi vůči seznamu sladidel, aromat a dalších přídatných látek. Ani obrázky, ani data nebyly přepsány.
4. Kokosový seznam surovin uvádí rybí kolagen a alergeny mléko/ryby/kokos/stopy sóji; cappuccino a vanilka uvádějí hovězí kolagen a jiná alergenová znění. Obecné upozornění na mléko/sóju a piktogramy si se seznamy nemusí plně odpovídat. Jsou zachovány vlastní zdrojové varianty, žádné převzetí receptury z jiného SKU.
5. Tabulka zdědila L-karnitin tartrát **1 g / 100 g** a **0,33 g / 30 g**; přepočet ani oprava není součástí zadání. Vanilkové úplné složení užívá `OPTIDIGEST®`, ostatní pasáže `OPTI7DIGEST®`; tato zdrojová odlišnost zůstává.
6. Původní upozornění a skladování jsou přeložena celá. U krátkých HTML chybí samostatný povinný blok upozornění; v dlouhém znění zdroj mluví o pestré stravě, ne výslovně o pestré **a vyvážené** stravě. Jde o děděný redakční/compliance úkol, ne o právní souhlas s existujícím zněním.
7. `brand/NOT-ALLOWED.md` v poskytnutém workspace neexistuje. Použita dostupná `RULES.md` a skutečné produktové `info.md`; žádné schválení nebylo domyšleno.
8. Jde o samostatné HTML fragmenty pro existující Shoptet stránku. Odkaz `#product-detail-form` vyžaduje nativní rodičovský nákupní formulář. Nativní košík, živá synchronizace s celou produktovou stránkou, nasazení CSS/JS a aktuální stav CMS nebyly tímto izolovaným testem ověřovány.
9. Prohlížečový fixture použil přesné CSS/JS z připnutého repozitáře, nikoli prohlášení o aktuálních veřejných CSS. Externí Google font byl v offline testu blokován. Fotografie/grafiky jsou původní, včetně případného česky zapečeného textu na obalech; zadání zachovat fotografie neumožňuje jeho přemalování.
10. Zdroj neobsahuje nabídky s natvrdo zapsanou cenou, skladovostí či recenzemi; pouze neutrální odkaz na aktuální nákupní sekci. Žádné měnové přepočty, nové recenze, ceny ani stav zásob nebyly vytvořeny. Historické ceny z `info.md` se do HTML nepřenášely.

**Žádný commit, push, CMS zápis ani publikace.** Výstup je pouze v přidělené `group4/`; ostatní skupiny a zdroje se neměnily.

## Opakování
Ze složky `analysis/`:
```
python3 inventory.py
python3 translations3.py
python3 build.py
python3 test_static.py
node test_runtime.cjs
node test_browser.cjs
node test_responsive.cjs
python3 claims_ledger.py
python3 finalize.py
```
Node závislosti jsou připraveny izolovaně v `analysis/runtime/`. Prohlížečový test používá přítomný Chromium uvedený ve skriptu. `fetch_assets.py` je pouze volitelná nová veřejná kontrola zdrojů; opakované QA používá již stažené autentické bajty.
