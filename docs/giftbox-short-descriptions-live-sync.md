# Krátké popisy boxů — synchronizace podle živého webu

Na výslovné zadání Pavla byly aktualizovány soubory pěti krátkých popisů v adresářích `maly/`. Zdrojem jsou aktuálně načtené veřejné produktové stránky, nikoli starší místní kopie. Ověřena jejich nativní productId:

- Beauty, 656: https://www.golden-life.cz/darkovy-box-collagen-beauty/
- Hormonal, 668: https://www.golden-life.cz/golden-life-darkovy-box-hormonal-balance/
- Longevity, 662: https://www.golden-life.cz/golden-life-darkovy-box-longevity/
- Slim, 659: https://www.golden-life.cz/golden-life-darkovy-box-collagen-slim/
- UFIRST, 665: https://www.golden-life.cz/ufirst-darkovy-box/

Převzat celý zdrojový editorový fragment uvnitř `.p-short-description`, bez vnějšího obalu šablony. Obsahuje současný úvodní odstavec, původních pět ikon, rozbalovací obsah boxu i aktuální vánoční blok s informací o balení a doručení. Texty a obsah jsou shodné se zdrojem; marketingové formulace ani zdravotní účinky nebyly nově vymýšleny. Věty o osobním rituálu, balení a doručení nepřisuzují doplňkům zdravotní účinek. Názvy produktů jsou převzaty jako identifikace. Značková pravidla byla načtena z brand/RULES.md; samostatný brand/NOT-ALLOWED.md nebyl nalezen. Tato synchronizace není právním schválením původních názvů.

Nejde o přepis dlouhých popisů: jejich předchozí nové pořadí produktových karet zůstává nedotčeno. Nebyla změněna žádná cena, sklad, košík, tracking ani administrace Shoptetu.

## Ověření

- Zpětně porovnány všechny textové uzly s přesným převzatým fragmentem.
- Chromium/Playwright: fragment vložen pouze v testovacím prohlížeči do skutečného nativního hostitele na příslušné veřejné produktové stránce.
- Všech pět produktů při 1440, 390 a 320 px, rozbaleno i sbaleno: 30 kontrol bez vnitřního vodorovného přetoku; pět ikon, pět položek a vánoční blok zachovány.
- Ověřeno otevření i zavření nativního rozbalovacího obsahu. Náhledy skrývají pouze v testovacím prohlížeči chat/cookie překryvy; nejde o změnu webu.
- Všechny kopírované fragmenty jsou bez skriptů, iframe, formulářů a nákupních ovládacích prvků.

Podklady: aktuální veřejný web, současné vzdálené soubory GitHub main a brand/RULES.md. Provedení GPT-6.1, Python, HTMLParser, BeautifulSoup a Playwright/Chromium. Bez placeného generování; cenu agentového a konektorového provozu nemáme vyčíslenou.

Publikace pouze do Gitu. Živý web se nepřepisoval — tentokrát je naopak zdrojem pro Git.
