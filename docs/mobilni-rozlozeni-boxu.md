# Mobilní rozložení pěti dárkových boxů

## Úpravy
- Krátké popisy Beauty, Hormonal, Longevity, Slim a U F1RST: všech pět piktogramů v jediné řadě, včetně úzkého sloupce detailu produktu. Popisky se mohou zalomit pod svou ikonou; ikony samy nepřecházejí do druhé řady.
- Kompaktnější mezery u piktogramů a přehledu obsahu. Žádná osamocená pátá ikona a prázdná druhá řada.
- Dlouhé popisy: do šířky 767 px fotografie nad názvem, popisem a tlačítkem. Na telefonu do 599 px jedna karta v řádku, mezi 600–767 px dvě karty, každá s obrázkem nad textem.
- Větší, sjednocená plocha pro packshoty; `object-fit: contain` zachovává celý produkt a jeho etiketu bez ořezu.
- Dárkové balení používá stejnou svislou kartu. Šestá karta zůstává balením, nikoli šestým produktem. Symbol dárku není fotografie krabice.
- Od 768 px zachováno původní rozložení šesti karet 3 + 3.

## Rozsah
Pouze CSS v pěti krátkých a deseti dlouhých souborech (pět úplných dokumentů a pět CMS fragmentů). Texty, pořadí a složení produktů, jejich fotografie a 25 produktových tlačítek, čtečka detailů, synchronizace CTA fotografie i stránka láhve včetně objemu 0,5 l zůstávají beze změny.

CSS je vložené přímo do každého popisu. Referenční samostatné soubory: `assets/giftbox-mobile-short.css` a `assets/giftbox-mobile-cards.css`. Není potřeba načítat další CSS přes CDN.

## Ověření
- Skutečný Chromium render pěti variant v 12 šířkách: 280, 320, 360, 375, 390, 414, 599, 600, 767, 768, 1024 a 1440 px, celkem 60 kombinací.
- Souřadnice všech pěti ikon v jedné řadě, žádný vodorovný přesah; navíc krátký popis v samostatném 260px sloupci.
- Na mobilu každá fotografie nad textem, všechny packshoty načtené, zachovaný poměr stran, neříznutý celý produkt.
- Desktopové rozměry karet porovnány přímo s původní verzí: beze změny.
- Zachování a otevírání/zavírání všech 25 produktových tlačítek. U láhve uložený starší snímek zdroje obsahuje hlášení o chybějícím popisu; čtečka správně ukazuje tuto existující situaci. Živý e-shop vždy čte aktuální zdrojovou stránku.
- Ověřen konkrétní offline soubor se všemi pěti variantami; žádné HTTP požadavky ani JS chyby. Originální packshoty pocházejí z dříve ověřené produktové galerie; doprovodná média, která nejsou v uložených podkladech, se v offline detailech nenačítají. Ikonový font je vložen jako skutečný stažený podmnožinový soubor Google Fonts, nikoli simulovaný font.
- Náhled zachycuje jen upravované části, nikoli celý vzhled e-shopu. Při nedostupném Metropolis používá deklarovanou náhradu Arial.

## Nasazení a soubory pro PC
GitHub `main` je publikační cíl této úpravy. Shoptet nebyl zapisován. V dodaném ZIPu jsou vedle kompletního repozitáře zjednodušené soubory `DO-SHOPTETU/<box>-KRATKY-POPIS.html` a `<box>-DLOUHY-POPIS.html`; vkládej celý obsah příslušného souboru do HTML režimu krátkého či dlouhého popisu správného boxu. Soubor `DARKOVE-BOXY-MOBIL-NAHLED.html` je pouze offline náhled, ne popis do Shoptetu.

## Zdroje a náklady
Základ: commit `b2c75962580e499099b4b5df88331ef10cdd7b8a`; `/root/workspace/brand/RULES.md`, původní HTML/CSS, uložené originální fotografie a zdrojové produktové stránky. Model GPT‑6.1‑sol. Úprava HTML/CSS a skutečné browserové screenshoty, bez AI obrazové generace a bez placeného generačního API (0 Kč za obrazovou generaci; běžné náklady na model tím nejsou vyčíslené).
