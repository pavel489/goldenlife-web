# Další piktogramy bez koleček

Další sada vychází ze skutečných veřejných produktových stránek mimo první připravenou sadu. Zatím jde o Git podklady, nikoli nasazení do živého Shoptetu.

## Co je hotové
- 48 nových transparentních PNG pokrývajících 50 původních obrazových URL; soubory jsou v `assets/piktogramy/bez-kruhu-v2/`.
- Odstraněné vnější kruhy i šest plných růžových disků; skutečná vnitřní kresba zůstala zachovaná. Dva kruhové CZ zdroje jsou nahrazené existující fialovou obdélníkovou vlajkou. Bílé U F1RST symboly zůstaly bílé.
- 51 upravených veřejných HTML fragmentů pro 31 dalších produktů v `shoptet/piktogramy-dalsi/`: pouze 278 přesných výměn `IMG src`, bez přepisování textů, CSS, skriptů, tabulek či fotografií.
- Produkt 461 nebyl přepsán starším veřejným popisem, protože má v hlavním repozitáři novější připravené soubory.
- Pro tuto další sadu bylo ověřeno 84 českých produktových URL ze sitemapu a jejich skutečné nativní productId. Další jazykové verze nejsou touto sadou označené za zkontrolované.

## Jak se v souborech vyznat
- `manifest.json`: přesná vazba produktId, veřejná URL, krátký/dlouhý fragment a jeho hash. Chybějící druhé pole znamená, že v něm nebyla potřebná obrazová změna, ne nedokončený soubor.
- `mapovani-novych-piktogramu.json`: původní a nové HTTPS adresy, způsob odstranění rámu, zdroje a využití.
- `mapovani-vsech-znamych-url.json`: normalizované mapování nové i předchozí sady; mapovací klíče `shop:` jsou interní identifikátory, nikoli URL k otevření.
- `nahled-pred-po.jpg`: stručný přehled. Dva soubory `vsechny-piktogramy-*.jpg` ukazují všechny skutečné dvojice.
- `kontrolni-nahled.html`: samostatný offline přehled všech 50 zdrojových variant.
- `https-png-qa.json`, `png-browser-qa.json`, `html-static-qa.json`: skutečné testy a jejich meze.
- `OBSAH-A-LIMITY.md`: samostatné obsahové výhrady a nezakryté limity zobrazení.

## Před případným živým vložením
HTML pochází z přesného veřejného snapshotu, nikoli z nativního exportu administrace. Zachovává současné veřejné rozložení, nejde o migraci na novou společnou šablonu. Před vložením porovnejte aktuální surové CMS pole a zachovejte veškeré novější opravy; podle mapy lze měnit pouze obrazové zdroje bez návratu staršího copy. Z dlouhého veřejného obalu byl vynechán pouze Shoptetem přidaný nadpis „Detailní popis produktu“.

Všechny nové PNG používají již ověřené neměnné HTTPS adresy revize `a003d4e6437ab85fa71892c88ee992fef4616bf8`. Není nutné je znovu generovat. Po živém uložení je třeba ověřit konkrétní veřejné stránky; Git publikace toto uložení nepotvrzuje.

## Ověření a omezení
Všech 48 HTTPS PNG vrací HTTP 200 / image/png a bajty odpovídají lokálním souborům. Všech 50 zdrojových variant se dekódovalo v Chromium na 390/1280 px. Osm statických scén ověřilo načtení nových ikon ve čtyřech skutečných produktových fragmentech; v sedmi byly i viditelně vykreslené.

Dvě samostatné výhrady nejsou skryté: statický mobilní fragment Slim Extreme Cream přetéká a mobilní řádek U F1RST je v této fixture skrytý. Výměna piktogramů toto rozložení neopravuje; kompletní původní skripty a živý obchod nebyly v této dílčí fixture ověřeny. Podrobnosti jsou v `OBSAH-A-LIMITY.md`.

Původní účinková sdělení zůstala pracovními převzatými texty, ne nově schválenými tvrzeními. Model GPT-6.1-sol; bez placeného generování, cenu modelového provozu zde nemám vyčíslenou.
