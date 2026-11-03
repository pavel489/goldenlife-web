# Šest oblých piktogramů v barvě dárkového boxu

Oprava výslovného zadání: **šest**, ne pět. Beauty, Hormonal, Longevity a Slim přebírají červenou `--gl-color-primary: #d90817`; UFIRST přebírá vlastní modrou/tyrkysovou `#5bcfde`. Barvy jsou převzaté z dosavadního boxového tématu, nikoli z barev jednotlivých komponent.

Ve všech 20 dlouhých/krátkých HTML (`web/` a CMS protějšky `shoptet/`) je šest skutečných původních oblých PNG motivů. CSS maska použije původní alfa kanál PNG a vybarví kresbu přesně proměnnou boxu, bez barevné aproximace filtrem a bez změny fotografií. V prohlížeči nepodporujícím masky zůstává původní PNG jako fallback (v jeho původní barvě).

Šestý piktogram: Beauty — Zpevnění nehtů; Hormonal — Metabolická rovnováha; Longevity — Podpora zdravého stárnutí; Slim — Zvýšený pocit sytosti; UFIRST — Hydratuje. Jde o existující párování skutečně obsažených produktů, ne generický symbol krabice/lahve. Souřadná provenience všech šesti je v `config/giftbox-benefit-pictograms.json`.

Dlouhá mřížka používá 3×2 na širokém zobrazení a 2×3 na mobilu. Krátká řada má šest sloupců na širokém zobrazení, na telefonu 3×2 pro čitelnost. Zrušeno roztažení poslední kartičky přes dvě buňky. Názvy, fotografie, produktové detaily, galerie, původní skripty a dřívější uživatelovy UFIRST CSS/JS zůstávají mimo ikonový blok beze změny. Jediná další HTML změna je připnutí nové verze sdíleného CSS.

## Skutečná kontrola
- 21 unikátních originálních PNG: HTTP 200, dekódování a ověřený průhledný alfa kanál.
- 30 skutečných renderů Chromium: pět boxů × dlouhý/krátký × 320, 390 a 1280 px. V každém šest načtených motivů, správná vypočtená barva a žádné horizontální přetékání stránky nebo popisků.
- Na 390 px samostatná kontrola reálně vykreslených barevných pixelů všech 60 motivů; porovnání zohledňuje alfa antialiasing vůči bílému podkladu. Nešlo pouze o kontrolu deklarace masky.
- Pět krátkých seznamů produktů otevřeno i zavřeno skutečným kliknutím.
- Zachování mimo ikonový blok ověřeno přesnou reverzibilitou. Finální vzdálené soubory se čtou zpět po každé Git publikaci.

Testy jsou izolované vizuální fixture se skutečnými veřejnými závislostmi; nepředstírají kompletní nativní Shoptet checkout. Původní shop bootstrapy jsou ve fixture vynechané a v dodaných HTML zachované. První kontrola přes browser helper narazila na screenshot timeout; úspěšné renderové/pixelové testy byly dokončené samostatným Chromium přes Playwright. Původní test vyžadující plně sytý pixel neprošel u tenké antialiasované kresby; opravená kontrola měří barvu po alfa kompozici a byla znovu spuštěna nad všemi motivy.

## Stav a zdroje
Grafický pracovní návrh na Gitu, **nikoli živé uložení do Shoptetu**. Popisky účinků nejsou tímto vzhledovým zadáním právně schválené; všechny včetně nově doplněných jsou evidované v `docs/darkove-boxy-claims-piktogramy.md`.

Zdroje: aktuální vzdálený snapshot autorizovaného repozitáře; jeho boxová témata; původní produktové PNG a doložená veřejná párování; `brand/RULES.md` a vlastní produktový soubor UFIRST. Model GPT-6.1-sol, Python/Pillow a Chromium/Playwright, existující Composio GitHub spojení jako Goldie. Bez placené generace obrázků/videí; cenu modelu a konektoru runtime neposkytuje.
