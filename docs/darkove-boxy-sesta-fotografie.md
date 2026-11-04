# Dárkové boxy: šestá fotografie vedle šesti piktogramů

Na zadání Pavla se úvodní fotografie vedle benefitových piktogramů bere ze **šesté fotografie galerie daného produktu**, nikoli z hlavní / první fotografie. Platí pro Beauty, Hormonal, Longevity, Slim a UFIRST; aktualizovány jsou dlouhé HTML v `web/` i jejich varianty v `shoptet/` (10 souborů). Krátké popisy se nemění.

## Chování
- Pořadí určuje nativní galerie produktu, ne číselná přípona v názvu souboru ani aktuálně vybraný snímek. Duplikáty různých velikostí a klonované snímky se nepočítají znovu.
- Nový skript `assets/giftbox-sixth-gallery-photo.js` je rovnou vložen i do dodávaných HTML. Není potřeba připojovat nový vzdálený skript.
- Každý úvodní IMG má vlastní ověřené ID produktu v `data-gl-gallery-product-id`. Původní ID a rozhodování nákupního tlačítka se nemění.
- V samostatném náhledu zůstává ověřený snímek šesté fotografie téhož boxu. Při cizím hostitelském produktu nebo méně než šesti fotografiích v přítomné galerii se úvodní obrázek skryje, nikoli přepne na první fotografii.
- Nákupní blok si ponechává hlavní fotografii a karta dárkového balení druhou fotografii. Oddělení CTA synchronizace zabraňuje tomu, aby změna úvodu nechtěně změnila i spodní snímek. Původní obsluha nákupu/ceny je beze změny mimo odebrání úvodního IMG z fotografie-synchronizačního selektoru.
- Barvy, šestice ikon, texty, pořadí produktových karet a načítání detailů se nemění. Přesné reverzní nahrazení v každém HTML vrací původní soubor bajtově shodně.

## Ověření
Chromium/Playwright načetl pět skutečně stažených veřejných produktových stránek s lokálně nahrazeným dlouhým popisem. Skripty dodaného HTML proběhly při normálním načtení celé stránky; nešlo o neaktivní vložení přes innerHTML.

Všech pět boxů prošlo při šířkách 1440, 390 a 320 px (15 případů): načtená správná šestá fotografie a šest původních piktogramů. Ověřena hlavní fotografie CTA a druhá fotografie dárkového balení, nezávislost na výběru hlavního snímku, ignorování duplikátu, skrytí při chybějící šesté fotografii a odmítnutí nesouhlasícího nativního ID. Bez JavaScriptových chyb v těchto pěti testovacích stránkách. Každý vložený skript všech 10 HTML prošel `node --check`. Test neodesílal košík, formuláře ani zprávy. Overlaye se skrývaly jen v testovacím prohlížeči pro čistší výřezy.

Podrobnosti: `tests/giftbox-sixth-gallery-photo-results.json`; ověřené veřejné adresy a ID: `config/giftbox-hero-gallery-photo.json`.

## Stav a zdroje
Zápis pouze do Git main na přímý pokyn, **nikoli do živého CMS Shoptetu**. Pro nasazení je potřeba převzít aktualizované dlouhé HTML produktu.

Podklady: vzdálená větev main `pavel489/goldenlife-web` (výchozí commit `726f53522fc46501d409a785ad5e1a89d604ac88`), pět aktuálních veřejných galerií, `brand/RULES.md`, přímé zadání. Provedení: model GPT-6.1, Python/BeautifulSoup, Chromium/Playwright a Node.js. Bez placeného generování obrázků; cena modelového provozu nebyla vyčíslena.

Původní zdravotní formulace u piktogramů nebyly měněny ani nově právně schváleny; tato oprava se týká výhradně výběru fotografie.
