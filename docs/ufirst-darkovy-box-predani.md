# UFIRST dárkový box — předání textů do Gitu

## Stav

Dodané české znění je zapracované do obou existujících párů HTML pro UFIRST dárkový box. Jde pouze o Git podklad k importu, ne o uložení nebo publikaci v živém Shoptetu. Ceny, dostupnost, nastavení košíku ani jiné produkty se neměnily.

- Dlouhý popis pro import: `shoptet/ufirst.html`.
- Krátký popis pro import: `shoptet/ufirst-kratky.html`.
- Samostatná webová verze: `web/Golden Life Darkovy box UFIRST/Golden_Life_Darkovy_box_UFIRST_cz.html` a její stávající soubor v `maly/`.
- Název produktu, SEO titulek a meta description jsou samostatná pole CMS. Jejich přesné hodnoty jsou v `config/ufirst-darkovy-box-texty-cz.json`. Samotné vložení dlouhého popisu tato pole v Shoptetu nezmění. Samostatný webový dokument má zároveň aktualizovaný title, description a OG texty.
- Kompletní editorský podklad: `docs/ufirst-darkovy-box-dodane-texty.md`.

Text se stylisticky nepřepisoval. HTML entity `&amp;` se vykreslují jako `&`. Obě varianty dlouhého popisu mají karty v dodaném pořadí: Brain & Focus, All-in-One, Care Free, láhev, míchátko, dárkové balení. Šest původních účinkových symbolů je nahrazeno zaoblenými obsahovými symboly odpovídajícími výslovně dodaným šesti popiskům; shodně v krátkém i dlouhém popisu, ve stávající tyrkysové barvě. Jsou vložené přímo v HTML, bez nového externího souboru.

## Co ještě potřebuje rozhodnutí před živou publikací

- Ve FAQ zůstává doslovný pracovní údaj **`[DOPLŇ DATUM]`**. Potřebujeme potvrzený vánoční objednávkový termín. Běžná aktuální dodací lhůta na webu není doklad vánoční garance; žádný datum se nevymýšlel.
- Hodnocení a cenová nabídka jsou časově proměnlivé údaje. Při tomto předání veřejná stránka produktu s nativním `productId=665` uváděla 3 290 Kč, srovnávací cenu 3 780 Kč a hodnocení 5,0 z pěti hodnocení. Veřejná stránka TRIO (`productId=605`) uváděla 3 190 Kč. Rozdíly 490 Kč a 100 Kč byly spočítané a ověřené. Před pozdějším zveřejněním tyto údaje ověř znovu.
- Poslední upozornění v dodaném textu je obecné. Vlastní produktové zdroje Care Free a Brain & Focus uvádějí navíc omezení pro děti, těhotné a kojící a upozornění pro užívání některých léků; Brain & Focus obsahuje sóju. Text zadání se potichu nerozšiřoval. Úplná produktová upozornění zachovej na etiketách a v dostupných detailech jednotlivých produktů a před publikací potvrď rozsah upozornění u celého setu.

## Zdravotní tvrzení — oddělené od implementace

Dodané věty byly ponechány; Git zápis není nové právní schválení.

1. **All-in-One:** „Vitaminy B2, B3 a B5 obsažené v All-in-One přispívají k normálnímu energetickému metabolismu a ke snížení míry únavy a vyčerpání.“
   - Je to zdravotní tvrzení navázané na uvedené vitaminy.
   - Zdroj `brand/product/ufirst-all-in-one-drink-/info.md` uvádí širší znění: „Vitaminy B1, B2, B3, B5, B6, B12 a vitamin C přispívají k normálnímu energetickému metabolismu a ke snížení míry únavy a vyčerpání.“
   - Dodaná věta není doslovně totožná s tímto záznamem: vybírá jen B2, B3 a B5. Ponechána jako dodaný pracovní text; samostatné nové schválení v registru EU ani posouzení zdrojového širšího seskupení se neprovádělo. Nepřebírej širší seznam automaticky jako novou právně prověřenou alternativu.
2. **Care Free pod ikonami:** „Hořčík a vitamin B6 obsažené v Care Free přispívají k normální psychické činnosti a k normální činnosti nervové soustavy.“
   - Zdravotní tvrzení; nosné živiny i produkt jsou pojmenované.
   - Doslovné produktové zdrojové znění vedle něj: **„Hořčík a vitamin B6 přispívají k normální psychické činnosti a k normální činnosti nervové soustavy.“** (`brand/product/care-free/info.md`). Rozdíl je doplnění informace „obsažené v Care Free“.
3. **Care Free v kartě:** „Hořčík a vitamin B6 přispívají k normální psychické činnosti a k normální činnosti nervové soustavy.“
   - Doslovná shoda se zdrojovým zněním výše.

Ostatní dodané věty popisují složení, balení, manipulaci, publikum či veřejnou nabídku, nikoli léčbu nemocí. Věty o Brain & Focus neprezentují účinek bylin a hub jako zdravotní fakt. Vizuální symboly také nepřidávají účinkové tvrzení. Obecná pravidla přečtena z `brand/RULES.md`; `brand/NOT-ALLOWED.md` v dostupné složce neexistoval, proto nešlo ověřit případná dodatečná stanoviska z tohoto souboru.

## Ověření

- Porovnání všech dodaných nadpisů a plných odstavců s výsledným HTML, včetně všech šesti FAQ a šesti karet.
- Původní obsah všech SCRIPT a STYLE bloků zachován byte-for-byte; nezměněné cíle detailových tlačítek a vazba fotografie na nativní produkt 665, hlavní fotografii a šestou galerijní fotografii.
- Krátký text pod dárkovým balením má samostatný viditelný odstavec, aby jej původní skript galerie neschoval nebo nenahradil technickou hláškou.
- Skutečný Chromium na šířkách 1440 a 390 px: testovací přepsání HTML odpovědi stejné veřejné stránky, původní shopové skripty i dodané bootstrapy běžely z HTML. Žádné uložení CMS. Žádné odeslání do košíku.
- Na obou šířkách prošlo otevření a zavření všech šesti FAQ a rozbalovacího krátkého obsahu, otevření a zavření všech pěti vložených produktových detailů; každý měl vlastní správný název a obsah v Shadow DOM, bez importovaných scriptů. Bez horizontálního přetékání dlouhého a krátkého bloku a bez zachycené JS chyby.
- Zachována bezpečná původní obsluha nákupního tlačítka: zdroj má dodané „Do košíku“, původní skript v samostatném náhledu nebo při přechodu k hlavnímu nákupu popisek přizpůsobuje dostupnému nativnímu stavu. Nic se kvůli textu nenutí do aktivního nákupu.
- Newsletter/chat/sticky překryvy byly skryté jen v testovacím prohlížeči. První překrytý screenshot nebyl použit jako finální vizuální doklad; byly zkontrolované čisté náhledy. JSON výsledky jsou v `tests/ufirst-darkovy-box-texty-results.json`.

## Vstupy, model a náklady

Vstupy: Pavlovo zadání v aktuálním vlákně, aktuální čtyři soubory autorizovaného Git repozitáře, veřejné stránky `https://www.golden-life.cz/ufirst-darkovy-box/` a `https://www.golden-life.cz/ufirst-trio/`, produktové soubory All-in-One, Care Free a Brain & Focus, `brand/RULES.md`.

Model: `gpt-6.1-sol`. Úpravy HTML a vložené jednoduché symboly vznikly kódem; bez placeného obrazového nebo video generování. Nebyl spuštěn žádný placený generátor. Skutečnou cenu jazykového běhu platforma v tomto úkolu neposkytla.
