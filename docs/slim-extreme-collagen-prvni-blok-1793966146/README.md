# Slim Extreme Collagen ID168 — doplnění prvního bloku

## Co chybělo
Ve zdrojovém českém dlouhém popisu a nových překladech ID168 nebyl úvodní `.nad-banner` + `.nad-info`, který připravený box ID383 má. Živá SK stránka také neměla ani jednu z těchto komponent. Nejde o doloženou chybu Opery: blok nebyl v HTML. Předchozí překlady tento strukturální nedostatek českého zdroje zachovaly.

## Oprava
Na začátek dlouhého popisu vložen stejný komponentový strom z aktuální Git verze boxu ID383. Obsah odpovídá dóze ID168: 240 g, 30 denních dávek po 8 g, dávkování odměrkou. Žádné tvrzení o sáčcích ani boxové fotografii se nepřenáší. Tlačítko otevírá podrobnosti a funguje i bez JavaScriptu.

Změněny pouze 4 dlouhé HTML: CZ, SK, EN, DE. Původní obsah, skripty, tabulky, krátké popisy, produktové fotografie a společné CSS/JS zůstaly beze změny. Odebrání jediného vloženého bloku vrací každý soubor přesně na zdrojové bajty.

## Kompletní dlouhé popisy k nahrazení
Pro nasazení nahraďte celý dosavadní dlouhý popis odpovídajícím souborem níže; krátký popis se nemění. Stáhněte přes Download raw file, nikoli kopírováním GitHub náhledu. Prvni-blok-*.html je samostatný výřez pro kontrolu, nikoli náhrada celého popisu.
- DE: [Golden Life Slim Extreme Collagen-de.html](https://github.com/pavel489/goldenlife-web/blob/main/web/Golden%20Life%20Slim%20Extreme%20Collagen/Golden%20Life%20Slim%20Extreme%20Collagen-de.html)
- EN: [Golden Life Slim Extreme Collagen-en.html](https://github.com/pavel489/goldenlife-web/blob/main/web/Golden%20Life%20Slim%20Extreme%20Collagen/Golden%20Life%20Slim%20Extreme%20Collagen-en.html)
- SK: [Golden Life Slim Extreme Collagen-sk.html](https://github.com/pavel489/goldenlife-web/blob/main/web/Golden%20Life%20Slim%20Extreme%20Collagen/Golden%20Life%20Slim%20Extreme%20Collagen-sk.html)
- CS: [Golden Life Slim Extreme Collagen.html](https://github.com/pavel489/goldenlife-web/blob/main/web/Golden%20Life%20Slim%20Extreme%20Collagen/Golden%20Life%20Slim%20Extreme%20Collagen.html)

## Ověření
- 32/32 scénářů: CZ/SK/EN/DE × šířky 390, 768, 820, 1280 px × světlé/tmavé okolí. Systémová preference byla vždy opačná než okolí.
- 224 otevření/zavření: nový informační blok a všech šest původních ingredienčních dialogů v každém scénáři; ověřena klávesa Escape a ARIA.
- Nový informační blok otestován bez JS ve všech čtyřech jazycích.
- Bez horizontálního přetečení banneru i dokumentu; v izolovaných kontrolách žádné chybějící obrázky, JS chyby ani externí požadavky.
- Na reálné SK stránce proběhlo dočasné vložení pouze do DOM testovacího prohlížeče; existující stylování a informační dialog se aktivovaly. Žádná změna CMS.
- Vizuálně zkontrolován tabletový náhled. Testovací engine Chromium/Linux, nikoli fyzická Opera/macOS.

## Náhled a hranice
[Samostatný offline SK náhled](nahled-prvni-blok-sk.html) otevřete po stažení. Obsahuje skutečné předchozí fotografie a fonty zabalené pro náhled; fotografie jsou pouze pro náhled zmenšené bez ořezu a komprimované do WebP. Vyžaduje JavaScript, neodesílá košík ani nesynchronizuje nativní cenu. Stažený soubor otestován při 390, 820 a 1280 px včetně 21 otevření/zavření informačních a ingredienčních dialogů. Není určen pro vložení do administrace.

V novém banneru jsou pouze produktové a balicí údaje, bez nových účinkových zdravotních tvrzení. Již označená zděděná tvrzení a rozpory ve stávajícím dávkování/tabulkách zůstávají k revizi; nejde o právní schválení nebo kompletní migraci ostatních sekcí.

Zdrojový commit: `6eaf61830e4de826942cc742df4f03ec1aa78002`. Model: gpt-6.1-sol; bez generování obrazu či videa a bez dalšího placeného generačního volání. Samostatnou cenu modelového běhu nástroje neposkytují.

**Dodání do Gitu není živé nasazení. E-shop nebyl změněn.**
