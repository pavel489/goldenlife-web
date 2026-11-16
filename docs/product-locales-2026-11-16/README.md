# Chybějící jazykové mutace jednotlivých produktů

## Výsledek a rozsah
- Zdroj: aktuální spárované české dlouhé a krátké fragmenty z `pavel489/goldenlife-web`, pin `f401c4e725c6cf22c895821f64e7efd581d48f16`, `brand/RULES.md`, produktové podklady citované v přiložených ledgerech.
- Inventář: 27 jednotlivých variant. Doplněno 18 produktů × SK/EN/DE × dlouhý/krátký popis = 108 nových HTML souborů. Devět dalších produktů má překlady již v aktuálním main, z toho šest bylo doplněno souběžnou prací během tohoto úkolu. Jejich 36 nových souborů bylo ponecháno beze změny; jejich kvalita se touto dávkou znovu neschvaluje.
- Jde o **interní pracovní překlady zdrojového obsahu, nikoli texty právně schválené pro živou publikaci**. Git handoff je požadovaný cíl, nikoli nasazení do Shoptetu. GitHub může zobrazovat veřejné zdrojové soubory; zákaznický web ani nativní jazyková pole se tím nemění.
- Balíčky, Double, dárkové boxy, láhve a samostatná řada U F1RST nejsou součástí původního inventáře 27 jednotlivých variant. Slim Extreme Collagen boxy jsou vlastní jednotlivé sáčkové SKU, nikoli vícesložkové dárkové balíčky.
- České originály, stávající překlady, obrázky, CSS, sdílené JS a veškeré jiné dříve sledované soubory zůstávají beze změny.

## Co je přeloženo
Plné odstavce a ingredienční dialogy, tabulkové popisky, bezpečnostní informace, ALT/ARIA a skutečné mobilní runtime řetězce včetně párovacích nadpisových regulárních výrazů. Zdroje jsou HTML fragmenty bez samostatných SEO/OG/JSON-LD polí; nativní metadata se nevymýšlela ani neupravovala. URL obrázků/odkazů a technické identifikátory zůstávají původní.

## Ověření přesných výstupů
- 108/108 nových souborů; syntaxe 255 skutečných vložených skriptů přes `node --check`; všechny kontroly prošly.
- Osm skupinových statických testů rodičem znovu spuštěno na úplných původních překladech: úplná reverzibilita inventarizovaných změn, textové pokrytí, chráněné atributy, CSS a čísla/tabulkové buňky. Před zápisem byla zachycena souběžná aktualizace main. Šest již doplněných produktů nebylo přepsáno; zbývající překlady byly napojeny na nové beze-kruhové ikony přes přesnou reverzibilní URL-only transformaci. Obsah českých zdrojů byl jinak bajtově shodný s původním pinem. Finální struktura, čísla, CSS, script syntax a Chromium byly testovány znovu proti novému pinu.
- Nezávislé strukturální porovnání všech 108 souborů vyhovuje po přesně evidovaných přesunech interních poznámek do ledgeru a doplnění chybějících bezpečnostních vět. Nejde o tvrzení, že každý původní tag zůstal beze změny; viz `explicit-structure-exceptions.json`.
- Rodičovský Chromium běh: 162 párovaných scénářů (18 produktů × 3 jazyky × 375/768/1200 px), 159 otevření/zavření mobilních ovladačů s ARIA. Žádná JS page error, žádný naměřený vodorovný přesah dokumentu. Vedle toho podrobné skupinové kontroly každého ingredienčního dialogu a responzivních návratů.
- Jde o izolovaný runtime/geometry test s autentickými repo CSS/JS. Externí fotografie, videa a fonty bez lokálních kopií byly blokovány, nikoli nahrazeny falešným úspěchem. Není to kompletní vizuální schválení s fotografiemi, kontrola dnešního živého shopu, cen/skladu ani nativního nákupu. Chybějící obrázek může v testu zobrazovat ALT a zkreslovat ikonový proužek.
- Po Git zápisu je samostatně ověřena přesná množina změněných blobů a všechny vzdálené bajty; doklad zůstává v pracovním úkolu, tento soubor jeho výsledek nepředjímá.

## Explicitní úzké výjimky
Interní draft/review poznámky a archivní konfliktní panely nejsou zákaznickým textem: odstraněny jen z nových jazykových souborů a zachovány v oddělených ledgerech. Doplněna chybějící obecná upozornění, u 357 opraven nezavřený zdrojový komentář pouze v nových překladech. Některé dlouhé německé složeniny mají jazykové měkké dělení. Nezměněno dávkování, formule, gramáže ani původní konfliktní číselné hodnoty. Žádná zdravotní účinková část nebyla potichu nahrazena dávkovacím boilerplatem.

## Tvrzení a otevřené rozpory
Přejatá tvrzení nejsou tímto schválena. Přiložené `group-*-claims*` a `group-*-CLAIMS.md` obsahují přesné zdrojové věty, překlady/odkazy, rizika a skutečně dohledané produktové formulace tam, kde existují; chybějící podklady nejsou doplněny odhadem. Týká se zejména spalování tuku, hormonálních/GLP-1, omlazujících a léčebných slibů. K rozhodnutí zůstávají rozpory balení/dávek, allergenů a CFU, některé věkové/těhotenské údaje. `brand/NOT-ALLOWED.md` nebyl dostupný. Pro živé nasazení je potřeba samostatná obsahová a jazyková finální kontrola těchto položek; není tím blokováno toto požadované dokončení pracovních podkladů.

## Inventář a původ práce
- `new-files.csv`: všech 108 cest s jazykem, SKU a SHA-256.
- `static-audit.json`, `group-static-rerun.json`, `browser-final-cases.json`: skutečné výsledky.
- Model: GPT-6.1-sol, textové překlady a Python/Node/Chromium kontroly. Bez placené obrazové generace a bez placeného externího překladového API; cenu modelového provozu nástroje nevyčíslily.
