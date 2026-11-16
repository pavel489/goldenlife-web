# Oprava šesti označených piktogramů

Nová grafická revize pouze šesti motivů přeškrtnutých červenými poznámkami v dodaném návrhu: plamen, běžec, postava, pokožka, ochranný štít na dlani a vlasové kořínky. Červené čáry jsou odmítnutí předchozí kresby, nikoli pokyn odstranit přeškrtnutí z dietních piktogramů.

## Co se změnilo
- Vycházíme ze skutečných původních obrazových motivů místo geometrických generických náhrad.
- Plamen a běžec sledují vyhlazené obrysy původních siluet; běžec má opět skutečný zaoblený obrys těla, ne čárkovou postavičku.
- Postava vychází z původních středových křivek, včetně jemnějších boků a existujících šipek.
- Pokožka má původní prohlubeň póru, tři šipky ven a vlnitou vrstvu, ne vrchol či cihlový blok.
- Štít a dlaň drží kompaktnější původní proporce a malé jiskry; vlasům jsou vráceny kořínky a oddělené oblouky folikulu.
- Společná referenční tloušťka zůstává 2 jednotky na ploše 64 × 64, zaoblené konce i spoje, bez dekorativních vnějších koleček. Nejde o pixelově totožné původní soubory, ale o jejich věrnější linkovou adaptaci.

## Výstupy
- Šest editovatelných SVG v `assets/piktogramy/organic-v4/masters/`.
- 22 barevných transparentních PNG v `assets/piktogramy/organic-v4/`.
- `nahled-opravy.jpg`: původní motiv → nová úprava; odmítnutý prostřední návrh není znovu prezentován jako finální volba.
- `kontrolni-nahled.html`: všechny varianty při 64 a 40 px.
- `mapovani.json`, `puvod-kresby.json`, `qa.json`: přesné zdroje, metody, hashe a kontrola rozsahu.

Vlajka, mléko, jiné neoznačené symboly a existující produkční HTML nebyly změněné. Nové grafické podklady zatím nepřepojují staré neměnné URL v popisech a nebyly nasazeny do živého Shoptetu. To odděluje nynější opravu výtvarného návrhu od plošného použití další estetické revize.

## Kontroly a původ
Otevřen skutečný označený screenshot a všech šest původních obrazových předloh. Nové SVG mají shodné parametry čáry, PNG se ověřují proti hashům, nejsou prázdné ani oříznuté. Ověření malých a referenčních velikostí je zapsané v `browser-qa.json`. Vzhled je vizuálně kontrolovaný, ne vydávaný za uživatelem již schválenou variantu.

Podklady: dodaný screenshot pro výběr šesti odmítnutých motivů, původní veřejné PNG, předchozí repo podklady a `brand/RULES.md`. Původní anotovaný screenshot se do veřejného repozitáře nekopíruje. Model GPT-6.1-sol, Pillow/OpenCV/SciPy a SVG/Chromium; bez placeného obrazového generování, cenu modelového provozu zde nemám vyčíslenou. Žádné nové účinkové texty ani změny popisků.
