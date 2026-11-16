# Další rodina piktogramů — jednotná zaoblená linka

Navazuje na přijatý styl předchozí dávky, nikoli na obnovení starých kruhových rámečků. Nové konkrétní kresby jsou další adaptací tohoto stylu, ne tvrzením o jejich dřívějším individuálním schválení.

## Výsledek

- **46 původních obrazových variant** rodiny `piktogramy-bez` převedeno na **30 editovatelných motivů / 45 barevných PNG**. Dvě původní adresy nyní záměrně sdílejí stejný motiv/barvu.
- Linka 2 jednotky při konstrukci 64 × 64, zaoblené konce i spoje, průhledný podklad, bez dekorativního vnějšího rámování.
- Vedle benefitů zahrnuje skutečné dosavadní faktické symboly kalendáře, dávkování, hmotnosti, tobolky, sáčku a obou odměrek. Kruhový ciferník hodin, vlasová cibulka nebo chemický skelet NAD+ jsou součástí samotného motivu, ne dekorativní obal.
- **991 přesných výměn IMG v 152 HTML:** 150 souborů `web/`, 2 pomocné podklady `shoptet/`. Aktuální hlavní soubory pocházejí z 24 produktových složek a zahrnují CZ / SK / EN / DE, krátké i dlouhé popisy podle výskytu původních ikon.
- Po skenu 341 aktuálních produkčních HTML nezůstal v těchto podkladech žádný odkaz na `/piktogramy/piktogramy-bez/`. Není to tvrzení o jiných ikonových rodinách nebo o živém e-shopu.

## Zachování obsahu

V každém změněném souboru jsou stejné zákaznické texty, popisky a přiřazení motivů, tabulky, vložené skripty i CSS a ostatní obrázky. Změna je pouze inventarizovaná výměna obrazových adres. Některé historické názvy souborů/motivy jsou s popisky významově nezvyklé, například běžec u textu o sytosti nebo kostky u BioPerine; párování nebylo svévolně měněné. Zdravotní tvrzení jsou převzaté, nikoli schválené tímto úkolem; viz `TVRZENI.md`.

Barevné varianty používají jednu skutečnou dominantní barvu viditelné kresby původního PNG. Nejde o nový oficiální vzorník; původní gradientní rastr je pro jednotnou linku převeden na tuto jednu inkoustovou barvu. Kontury jsou zdrojově vedená vektorová adaptace, místy s ručním vyčištěním spojů a obličejových detailů, nikoli tvrzení o pixelové identitě.

## Kontrola

- 30 SVG masterů: shodná geometrická plocha, šířka, zaoblení, žádná vyplněná silueta nebo individuální transformace čáry.
- 45 PNG: platné 256 × 256, průhlednost, neprázdná a neoříznutá kresba; všechny shodné s veřejnými neměnnými HTTPS soubory.
- Kalibrační čára skutečně renderovaná při 20, 40, 64, 85 a 256 px. Při menším zobrazení se poměrně ztenčuje, neslibujeme stejné fyzické 2 CSS px při libovolné velikosti.
- **608 Chromium scénářů** nad všemi 152 změněnými HTML: 390/1280 px × světlá/tmavá CSS větev. Každý obsahuje srovnání skutečných starých a nových obrazových bajtů. Dekódování, nezměněná viditelnost, bez obnovených kartiček a nejvýše 0,1875 px rozdílu rozměru obrazu v těchto testech. Ověřeno 3964 výskytů ikon v těchto scénářích.
- Samostatný HTML náhled všech 30 motivů při 20/40/64 px skutečně otevřen v prohlížeči; 90 IMG se načetlo.
- Vizuálně otevřené všechny originály na kontaktu, všechny tři porovnávací listy, jednotlivé obličejové/vlasové předlohy a konečný přehled. Automatická vektorizace byla před dodáním ručně dočištěná.

Statické prohlížečové testy záměrně blokují skripty, externí fotografie a fonty; nejsou testem nativního nákupu, všech dialogů nebo celého živého Shoptetu. Přerušení prvního delšího běhu bylo obnoveno z uložených výsledků a konečný počet zkontrolovaný, ne odhadnutý.

## Nahrání

Gitová předávka není publikace do Shoptetu. HTML používá neměnné veřejné PNG adresy z asset commitu `c8aab36a83be76909a314f648e9c59740412913a`. Při ručním přenosu porovnejte případné novější nativní úpravy CMS a zachovejte je. Tento úkol sám žádný CMS popis ani živé CSS neukládal.

Pro vzhled bez kartiček používejte také aktuální společné a produktové CSS z předchozí dávky. ZIP proto obsahuje nezměněné potřebné CSS jako závislosti; nejsou nové změny tohoto commitu. Staré rodiny některých boxových ikon a historické screenshoty nejsou touto dávkou přepracované.

## Reprodukce a původ

Z kořene repozitáře: `python3 docs/piktogramy-dalsi-jednotna-linka/regeneruj.py` s Pillow a CairoSVG. Z uložených SVG a mapování znovu vytvoří přesných 45 PNG a ověří jejich SHA-256. Skutečně spuštěno před předáním.

Zdroje: veřejné původní PNG z rodiny `piktogramy-bez`; aktuální Git `e0c68c37e017e312decff0c9bb2c7dbf2c9b06b6`; předchozí přijatá monoline sada a obrysový plamen; `brand/RULES.md`; pracovní vizuální identita Golden Life a text kapitoly Ikonografie originálního manuálu. Staré kruhové rámování v manuálu je pro toto webové zadání nahrazené výslovným požadavkem bez rámů; lidské pravidlové soubory se neupravovaly.

Model GPT‑6.1‑sol. SVG / Pillow / CairoSVG / OpenCV / scikit-image / Chromium; bez placeného generování obrázků. Cena modelového provozu není vyčíslena.
