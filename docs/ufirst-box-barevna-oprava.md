# Dárkový box UFIRST — sjednocení barev

## Co se mění
- Pouze UFIRST: tyrkysová `#5BCFDE`, tmavá tyrkysová `#1F9CAD`, žluté nákupní tlačítko `#EDFF00` a černý text. Světlé plochy zůstávají tyrkysovým odstínem `#E6F8FA`.
- Doplněná explicitní hranice barevných proměnných na dlouhém i krátkém popisu. Ostatní boxy se nepřebarvují.
- Konkrétně reprodukovaná růžová byla v otevřeném detailu USB míchátka: `.usb-prod` a `.usb-prod-name` měly inline růžová pozadí, rámečky a názvy doporučených nápojů. Oprava je pouze v izolovaném vloženém detailu uvnitř UFIRST boxu. Samostatná stránka míchátka ani obaly na fotografiích se nemění.
- Malý bootstrap je uložený jako čitelný zdroj `assets/giftbox-ufirst-reader-colors.js` a vložený přímo v obou dlouhých HTML. Nevyžaduje další externí JS import. Při přepínání detailů obnoví izolovaný styl a nevkládá ho opakovaně do stejného kořene.

## Předání
Dlouhý CMS fragment: `shoptet/ufirst.html`. Krátký CMS fragment: `shoptet/ufirst-kratky.html`. Plné odpovídající dokumenty jsou v `web/Golden Life Darkovy box UFIRST/`.

Všechny čtyři HTML importují nové, bajtově ověřené společné CSS na neměnné revizi `8f9db974966408eba8bdfdb66fc4f35e376a709c`. Veřejná CDN odpověděla HTTP 200. Ostatní boxy mají původní CSS pin a jejich pravidla zůstala nezměněná.

Jde o publikaci návrhových souborů do Gitu podle zavedeného předání, nikoli uložení do administrace Shoptetu. Teprve import celých CMS fragmentů a následné ověření skutečné stránky znamená nasazení.

## Skutečně provedené kontroly
- Čtyři HTML: textové uzly, atributy obrázků a všechny původní inline skripty zachovány. Navíc jen nový UFIRST bootstrap ve dvou dlouhých dokumentech a změna CSS pinu.
- Osm izolovaných vykreslení: dlouhý/krátký popis při 320, 390, 768 a 1280 px; bez horizontálního přetékání a bez růžových computed barev.
- Dvanáct ověřených pointer otevření/přepnutí: všech pět produktů a opětovné otevření USB, při 390 a 1280 px. U každého kliknutí ověřen skutečný aktivní productId, titulek a existující ShadowRoot. Bez růžové v textu, pozadí, rámečcích a stínech otevřených detailů. Originální produktové fotografie se netestují jako CSS barvy a nepřebarvují se.
- Závěrečný test použil skutečné publikované CSS importy a aktuální veřejné produktové zdroje ve stejném původu golden-life.cz; hostitelské HTML bylo dočasně nahrazené testovaným dokumentem. Pozdní newsletter/chat překryvy byly potlačené pouze v testovací kartě. Není to screenshot uložené CMS změny. FAQ se kliknutím otevřelo; žádná operace košíku neproběhla.
- Vizuálně zkontrolovaný desktopový náhled hlavního popisu a vloženého USB detailu.

## Původní omezení mimo barevnou opravu
V náhledu se nenačítá původní hero `/user/documents/upload/mockup/darkovy-box-ufirst.png` a v USB doporučeních původní miniatura `https://cdn.myshoptet.com/usr/www.golden-life.cz/user/documents/upload/mockup/UFIRST-all-in-one.png`. URL ani fotografie nebyly touto barevnou úpravou nahrazovány. Rozsah tohoto zadání není změna produktové galerie ani doporučených produktů.

Zdravotní texty nebyly přepisovány ani tímto vizuálním zásahem nově schváleny.

## Zdroje a náklady
Aktuální vzdálené soubory z `pavel489/goldenlife-web`, veřejný UFIRST box a všechny jeho vložené detaily, veřejné `golden-life-produkt.css`, `brand/RULES.md`, `brand/ufirst/manual/README.md`, manuál U F1RST v1.0 a `brand/ufirst/creative-memory.md`.

Model GPT-6.1-sol; Python, Chromium a existující Composio GitHub spojení ověřené jako bot `goldie-golden-life`. Žádná placená generace obrázků/videí. Přesná cena modelu a konektoru není poskytovaná.
