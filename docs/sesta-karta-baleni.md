# Šestá karta dárkových boxů — pracovní návrh

## Co je hotové
- Beauty, Hormonal, Longevity, Slim a U F1RST: pět původních produktových karet plus šestá informační karta „Dárkové balení“.
- Dva úplné řádky po třech na šířkách 768, 1024 a 1440 px; mobilní rozložení při 320 a 390 px bez vodorovného přetékání.
- Text: „Pět produktů společně v jedné elegantní dárkové krabici.“ Viditelný štítek BALENÍ a doplnění „5 produktů + dárková krabice“. Nejde o šestý produkt ani novou položku košíku.
- Původních pět karet, jejich obsah, zdroje popisů, fotografie, FAQ, nákupní napojení a krátké popisy nejsou touto úpravou přepisované.

## Chybějící fotografie — nezaměňovat za hotovou fotografii
Všechny původní URL fotografií celého boxu (`/user/documents/upload/mockup/darkovy-box*.png`, podle konkrétní varianty) při ověření vrátily HTTP 404. Schválená fotografie jednotlivých přesných celých boxů není v tomto návrhu dosazená. Šestá karta zatím používá jednoduchý SVG symbol dárku: UI ikonu, ne vymyšlenou fotografii nebo skutečnou podobu balení. Fotografie láhve nadále chybí a v přenosném náhledu je tato mezera výslovně označená.

Tlačítko „Prohlédnout celý box“ je připravené, ale bez fotografie zůstává skryté. Neukazuje se nefunkční tlačítko.

## Doplnění skutečné fotografie
1. Ověř, že fotografie ukazuje přesný konkrétní box a správný obsah, a nahraj ji do schváleného úložiště e-shopu.
2. U šesté karty nastav `data-gl-packaging-src="https://www.golden-life.cz/..."` na její skutečnou URL. Totéž proveď v odpovídajícím plném HTML z `web/`. Mapovací `config/giftbox-packaging-card.json` je evidence, kterou také aktualizuj; prohlížeč tento soubor sám nestahuje.
3. Povolena je vlastní HTTPS doména nebo `www.golden-life.cz` / `cdn.myshoptet.com`. Původní HTTP404 adresy zatím nepoužívej.
4. Po úspěšném načtení skutečného obrázku se symbol skryje a zpřístupní se fotografie i tlačítko. Tlačítko otevře její zvětšení v nativním dialogu. Zavření tlačítkem nebo Escape vrací fokus ke spouštěči. Selhání obrázku ponechá symbol a srozumitelnou zprávu bez nefunkční akce.

## Soubory
- `shoptet/*.html`: pět samostatných dlouhých popisů pro CMS.
- `web/*/*.html`: odpovídající plné HTML dokumenty. Krátké popisy nejsou v této změně upravované.
- `config/giftbox-packaging-card.json`: stav fotografií a postup zapojení.
- `tests/giftbox-packaging-results.json`: skutečné výsledky nové sady i regrese.
- Samostatná příloha `darkove-boxy-sesta-karta.html`: přepínatelný přenosný náhled všech pěti variant. Otevři jej v moderním prohlížeči, nikoli v náhledu textu ve Slacku.

Náhled obsahuje zabalené původní produktové fotografie a uložené produktové popisy. Není to živý e-shop; nákup nemá zapojený. Doplňkové externí obrázky a ikonové fonty uvnitř starších produktových detailů mohou chybět; CSP blokuje jejich síťové načítání. Hlavní šestikartový návrh funguje bez těchto zdrojů.

## Ověření
Playwright/Chromium: všech pět boxů a páry plného HTML/CMS; počet šesti karet a stále pěti produktových akcí; pět šířek; dvě plné desktopové řady; žádné horizontální přetékání; skryté tlačítko při chybějící fotografii. Úspěch, HTTP404, nebezpečné URL, dialog, Escape a návrat fokusu prověřené explicitní syntetickou 1px obrazovou fixture — nejde o zkoušku skutečné fotografie boxu.

Regrese: všech 25 produktových tlačítek proti uloženým skutečným HTML; 20 načtených popisů a pět správných hlášek chybějícího popisu téže láhve. Cache, opakování chyby, nesprávné SKU, sanitizace, přepínání a zavření během načítání prošly. Bez JavaScriptových chyb. Ověřený byl i dodaný přenosný náhled, přepínání všech variant a otevírání uložených detailů. Screenshoty Beauty a U F1RST v desktopu a mobilní karty byly vizuálně zkontrolované. Nejde o test fyzického iPhonu/Safari ani uloženého živého Shoptet HTML.

## Stav a omezení
Pracovní zdroj: `design/gift-packaging-card`, vychází z ověřeného vzdáleného `main` / `d9a5a7fe7bf405ffee9d1627739b5a93b178ddef`. Pavel v pracovním vlákně výslovně schválil nahrání této šestikartové verze do `main`. Konkrétní publikovaný commit ověř v historii Gitu. Nasazení v Shoptetu není součástí tohoto kroku a Shoptet nebyl změněný. Příznaky `main_changed: false` v podkladech testů zachycují stav při místním testování před touto publikací. Před vložením do administrace je nutná kontrola zachování celého kódu: CMS fragmenty touto verzí narostly přibližně na 38 kB; dřívější editor měl problém s uříznutím velkých skriptů a přesný limit není ověřený. Lokální test neověřuje transformace editoru.

Původní účinkové texty zůstaly na výslovně zachovaných produktových kartách a v importovaných zdrojích. Tato vizuální změna je právně ani produktově neschvaluje. Nová karta balení žádné zdravotní tvrzení nepřidává.

## Podklady, model a náklady
Podklady: skutečný Git main uvedený výše, `brand/RULES.md`, existující text o dárkovém balení, předchozí inventář produktových fotografií a uložené kanonické produktové HTML. Zpracování: gpt-6.1-sol; Python, BeautifulSoup, Playwright/Chromium a SVG/HTML/CSS/JS. Bez placeného generování fotografií nebo videa a bez nového nákupu služby. Cenu modelových volání nemám vyčíslenou.
