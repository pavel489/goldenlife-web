# Automatická fotografie v dolním CTA

Úprava všech pěti dárkových boxů: Beauty, Hormonal, Longevity, Slim a U F1RST. Dolní CTA nyní přebírá skutečně načtenou úvodní fotografii `.heroimg` ze stejného boxu. Nemá vlastní ručně udržovaný odkaz ani si nestahuje další produktovou stránku.

## Chování
- První zobrazení až po úspěšném načtení úvodního obrázku.
- Přebírá se aktuální `currentSrc` (včetně responzivního výběru), případně `src`, a alternativní text úvodního obrázku.
- Sleduje změnu URL, `srcset`, velikost okna i nahrazení celého úvodního obrazového elementu.
- Při chybějící či nefunkční fotografii nebo placeholderu se obrázek v CTA skryje; CTA text a nákupní ovládání zůstávají.
- Po pozdějším doplnění fotografie se obrázek obnoví automaticky.
- Původní synchronizace úvodu z hlavní galerie Shoptetu zůstává zachovaná. Stejně tak původní ověření produktového ID, cena, dostupnost a nákupní napojení.
- Šestá karta dárkového balení ani pět produktových karet se touto změnou nepřepisují.

## Soubory
`assets/giftbox-cta-photo.js` je čitelný zdroj. Jeho kompaktní kopie je vložená do pěti dlouhých CMS popisů v `shoptet/` a odpovídajících pěti plných dokumentů v `web/`. Žádný nový externí skript nebo placená služba se nenačítá. Krátké popisy jsou beze změny.

## Ověření
Playwright/Chromium: všech pět boxů, čtyři šířky 320/390/768/1440 px, změna a nahrazení úvodního obrázku, `srcset`/`currentSrc`, HTTP404 a obnova, odmítnutí SVG placeholderu, původní hlavní galerie a cena, šest karet a stále pět produktových akcí. Obrazové scénáře používají výslovně syntetické 32px PNG testovací podklady, nikoli vymyšlené fotografie skutečných boxů. Odpovídající plná HTML a CMS fragmenty mají shodný nový skript i obrazový element.

Regrese všech 25 produktových tlačítek nad skutečnými uloženými produktovými HTML: 20 dostupných popisů a pět správných hlášek chybějícího popisu téže láhve. Bez JavaScriptových chyb. Tabulky, cache, opakování chyby, odmítnutí nesprávného SKU a nebezpečného obsahu, rychlé přepínání a zavření během načítání prošly. Výsledky jsou v `tests/giftbox-cta-photo-results.json`.

## Hranice
Základ úpravy je main / `93bd99e2bcb2f1219cf110f3f09481d17d2e7c6d`. Jde o pokračování úprav repozitáře; konkrétní publikovaný commit ověř v historii main. Shoptet v rámci tohoto kroku nebyl změněný a nevznikla testovací objednávka. Skutečně uložené HTML po případném nasazení do administrace bude potřeba ověřit: předchozí editor měl problém s uříznutím velkého kódu a jeho přesný limit není doložený. Automatické přebírání fotografie nenahrazuje chybějící fotografii v úvodu a samo neověřuje správnost či schválení dané fotografie.

Podklady: aktuální Git main, jeho úvodní/CTA elementy a původní nákupní skript, `brand/RULES.md`. Zpracování: gpt-6.1-sol, HTML/CSS/JavaScript, Python/BeautifulSoup a Playwright/Chromium. Bez placeného generování obrázků; cenu modelových a konektorových volání nemám vyčíslenou. Původní produktové a účinkové texty zůstávají beze změny; tato technická úprava je právně neschvaluje.
