# Golden Life — piktogramy bez vnějších koleček

## Stav
Připravené a otestované soubory pro web. Git publikace není uložení do Shoptetu. V tomto úkolu nebyly změněny živé CMS popisy ani nahrány tři CSS soubory do správce souborů.

## Rozsah
- Prohledáno všech 167 produkčních HTML souborů v `web/` a `shoptet/` v aktuálním snapshotu `c23e3022f9dea036ed8dbcf9bb458d36bfec9133`, včetně právě doplněných jazykových mutací.
- 80 krátkých/dlouhých HTML popisů: 446 přesných výměn obrazových URL. Texty, tabulky, skripty, fotografie a ostatní bajty beze změny.
- 72 původních URL převedeno na 61 deduplikovaných transparentních PNG. Nové PNG jsou již dostupné na neměnných HTTPS adresách revize `bb751e31b25b03355205706aebdf460db0d65d98`.
- 3 CSS soubory, 5 úzce cílených pravidel: bez kruhového orámování a pozadí `.nad-ico` a dekorativních šipek `.gl-ingredient-cta-arrow`.
- Historické náhledy a staré QA snapshoty nebyly přepsány. Nejde o tvrzení, že repozitář obsahuje každou stránku či aktuální jazykovou verzi celého živého obchodu.

## Co zůstalo zachováno
Vlastní kontury původních symbolů, jejich barvy a proporce. Oddělené vnější PNG kruhy jsou odstraněny jako komponenty alfa kanálu včetně drobných antialiasových zbytků; vnitřní glyph pixely zůstaly nezměněny. U propojeného přeškrtnutí zůstala původní úhlopříčka, odstraněn jen obvodový kruh. Kruhové české vlajky byly nahrazeny existujícími obdélníkovými vlajkami stejné barevné řady; pouhé odstranění kruhu by zanechalo nečitelný symbol. Jedna původní růžová CZ URL vracela 404 a je nahrazena stejným ověřeným motivem.

Hodiny, významové oblouky a tečkovaný mechanismus uvolňování uvnitř vlastního symbolu nejsou dekorativní rámečky. Funkční ovladače, tlačítka zavření/přehrávání, galerie, zaoblené obdélníkové karty a datové body grafů zůstaly beze změny. Nejde o globální mazání všech kruhových tvarů.

## Soubory pro nasazení
- Každý upravený dlouhý/krátký popis je uveden v `manifest.json` → `changedHtmlFiles`; jde o celé soubory, ne CSS přilepené přes starou grafiku.
- Nahrajte tyto přesné CSS soubory na jejich stávající adresy:
  - `user/documents/upload/css/golden-life-produkt.css`
  - `user/documents/upload/css/golden-life-barvy-slim-sos-fat-burner.css`
  - `user/documents/upload/css/golden-life-barvy-double-slim-sos-burner.css`
- PNG není potřeba ručně vkládat do všech popisů: upravené HTML již používá ověřené neměnné HTTPS adresy.
- Před živou výměnou zkontrolujte případné novější změny CMS proti tomuto snapshotu a po uložení načtěte přesné veřejné cíle; až pak lze potvrdit živé nasazení. Pokud má CMS novější copy než Git, zachovejte ji a aplikujte jen mapované URL.

## Kontrola
- Každý z 61 HTTPS PNG načten, HTTP 200 a image/png, bajty SHA-256 porovnány s lokálním výsledkem.
- 72 variant v samostatném Chromium náhledu: obrázky dekódovány, masky mají skutečný zdroj, mobil 390 a desktop 1280 bez horizontálního přetečení. Masky jsou synteticky zabarvené pouze v kontrolním náhledu, nikoli přebarvené produktové fotografie.
- Vizuálně zkontrolovány všechny obrazové zdroje na kontaktních listech a všechny výsledné páry před/po. Ověřeno zachování nepřepsaných pixelů originálních glyfů.
- Lokální CSS regrese: 56 Chromium případů, 88 kontrol cílových ikon a 656 porovnání stylů funkčních ovladačů; mobil/desktop a light/dark. Omezení: záměrně blokované obrázky a externí ikonový font v této dílčí CSS fixture.
- Veřejný Vitamin C: jen lokální záměna 12 IMG URL pro náhled. Obrázky načteny na desktopu i mobilu. Nejde o uložení CMS ani test kompletního nového HTML na celé produkci.
- Konečné HTML je bajtově přesně rekonstruováno z aktuálního zdroje a inventarizovaných URL náhrad; každý výsledný IMG zdroj je navíc zkontrolován jako celá URL. Absolutní adresy jsou nahrazovány před relativními, aby nevznikl slepený CDN+HTTPS zdroj.

## Náhledy a důkazy
- `nahled-pred-po.jpg`: stručný vizuální přehled.
- `vsechny-piktogramy-1.jpg`, `vsechny-piktogramy-2.jpg`: všechny skutečné původní/upravené dvojice.
- `kontrolni-nahled.html`: samostatný offline kontrolní náhled všech 72 zdrojových variant.
- `manifest.json`, `zmeny-html.json`, `mapovani-piktogramu.json`, `https-qa.json`, `png-browser-qa.json`, `css-qa.json`, `css-audit.md`: inventář, přesné náhrady a výsledky.

## Podklady, model, cena a obsah
Podklady: `brand/RULES.md`, pracovní `brand/golden-life/visual-identity.md`, skutečná původní PNG, aktuální Git a veřejný produktový náhled. Pokyn bez vnějších koleček nahrazuje starší webovou grafiku s kruhy; původní lidský manuál a pravidla nebyly přepisovány.

Model GPT-6.1-sol; Pillow, SciPy a Chromium. Bez placeného obrazového generování — 0 za generovací služby. Cena agentového/modelového provozu zde není vyčíslena.

Původní účinkové popisky nebyly upravovány ani právně schvalovány. Tato grafická úprava není revizí zdravotních tvrzení.
