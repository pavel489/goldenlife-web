# Hormonal Balance — předání českého dárkového boxu

## Rozsah
- Git podklad pro pavel489/goldenlife-web, nikoli uložení nebo publikace v Shoptetu.
- Dlouhý a krátký český popis v shoptet/ a odpovídající český pár web/Golden Life Darkovy box Hormonal/.
- Úvod malého popisu je doslova aktuálně dodané „Darujte krásu, pohodu a chvíli jen pro sebe!…“. Úvod velkého popisu je doslova aktuálně dodané „Dárek, který potěší každou ženu 40+…“. Starší, odlišné intro z minulé iterace není novým zadáním a nebylo přeneseno zpět. Tvoje aktuální znění se redakčně nepřepisovalo.
- Všechny nové odstavce, příběhy, šest karet, sedm FAQ, závěrečný blok a upozornění jsou zahrnuté; kontrolují se celé odstavce, ne jen klíčová slova.
- Název a SEO jsou v config/hormonal-darkovy-box-texty-cz.json pro samostatná pole administrace. HTML popis jejich uložením tato nativní pole nezmění.
- Současná vazba na 6. galerijní fotku produktu 668, foto CTA, balení, čtečka a košíková bezpečnost zůstaly zachované. Kořenové data-gl-product-id zůstalo prázdné jako v originálu; záměrně se nemění režim nákupu.

## Piktogramy
Šestice: večerní višňový nápoj, 30 sáčků, vitamin D3 a K2, 8 rostlinných extraktů, láhev Golden Life, USB-C míchátko. Shodné v obou popisech. Převzatý styl Longevity: viewBox 64 × 64, 2,6px tah, zaoblené konce a spoje, červená #d90817. Čtyři nové kresby, láhev a míchátko mají totožné SVG předlohy s Longevity. Žádné kreslení generativním obrazovým modelem.

HTML i CSS masky odkazují na stejné průhledné PNG 512 × 512 přes HTTPS, připnuté k neměnnému commitu; žádné vložené SVG v IMG. SVG zůstávají jen jako editovatelné předlohy. Každé veřejné PNG bylo stažené s HTTP200, image/png a CORS *, porovnané byte-for-byte a dekódované. V prohlížeči se testovaly skutečné síťové PNG v obou sestavách, nejen lokální náhražka.

## Ověření
- 1440, 390 a 360 px: oba popisy bez horizontálního přetékání, 12 IMG dekódovaných, popisky zachované.
- Sedm FAQ: pointer otevření/zavření, první též klávesnicí Enter. Krátký obsah boxu se rozbaluje/zavírá.
- Všech pět skutečných produktových detailů: otevření/zavření, první znovuotevření, správné tituly a netriviální obsah, žádné importované skripty. Použitý aktuálně připnutý loader, skutečné archivované produktové zdroje.
- Původní skripty, styly, produktové URL, galerijní atributy a košíková logika porovnané se snapshotem Gitu.
- Vizuálně prohlédnuté finální gridy a mobil, také samostatné kresby při 64, 48 a 40 px.
- Živý e-shop v tomto běhu vrátil HTTP403 Access temporarily blocked. Další požadavky na obchod nebyly prováděné. Fotografie a živá cena/dostupnost nejsou nově ověřené; náhled není screenshot nasazeného e-shopu. Původní produkční fotografie ani jejich URL nebyly nahrazovány.

## Před zveřejněním — konkrétní otevřené věci
1. [DOPLŇ DATUM] zůstává viditelně v pracovním HTML. Potvrď skutečnou vánoční uzávěrku; datum nevymýšlíme.
2. Cena 3 950 Kč, původní 4 600 Kč a úspora 650 Kč jsou dodané veřejné nabídkové údaje. Výpočet ověřený; aktuální platnost nabídky se kvůli HTTP403 nepotvrdila. Skript načítání nativní ceny nebyl měněn.
3. „Zákaznice box hodnotí 5,0 z 5…“ a citace: doložená v dřívějším veřejném snapshotu produktu 668; nejde o aktuální revalidaci ani nový doklad souhlasu s marketingovým užitím recenze.
4. Děti/těhotné/kojící, hormonální léčba a alergeny zůstávají dle dodaného textu. Před zveřejněním porovnat s nejnovějšími etiketami všech tří doplňků. Historický zdroj 635 uvádí „Vhodné pro děti od 8 let“, zatímco dodaná FAQ celý box určuje jen dospělým; opatrnější určení celé kombinace nepřepisujeme. U červeného jetele a sóji je vhodné ponechat konzultaci při hormonální léčbě. Nejde o společný návod současného dávkování všech doplňků.

## Zdravotní formulace — pracovní znění, nikoli právní schválení
brand/RULES.md přečtený. brand/NOT-ALLOWED.md chybí. Samostatný aktuální schválený info.md k nápoji Dark Cherry a Woman Hormonal Balance v dostupném brand/product nebyl nalezen. Veřejné produktové HTML není samo o sobě právní schválení. Tvrzení proto nebyla označená jako schválená ani potichu přepisovaná.

### Dodané znění
Tento nádherný vánoční box je ideálním dárkem pro ženy 40+, které chtějí pečovat o pleť, vlasy i kosti, dopřát si každý večer klidný rituál a cítit se skvěle v každém věku.

Obecné sdělení o péči/kráse a kostech může v kontextu vyznít jako účinek celého boxu. Zdrojová neutrální alternativa z dodaných produktových údajů: „Box spojuje tři doplňky stravy, láhev Golden Life a USB míchátko.“ U kostí je k dispozici v původním dlouhém souboru boxu konkrétnější „Vitamin D v nápoji Dark Cherry přispívá k udržení normálního stavu kostí.“ Ani tento výskyt nenahrazuje schválení produktu.

### Dodané znění
Tento nádherný vánoční box spojuje 5 produktů pro každodenní péči o sebe, krásnou pleť, vlasy i nehty a zdravé kosti.

Obecné sdělení o péči/kráse a kostech může v kontextu vyznít jako účinek celého boxu. Zdrojová neutrální alternativa z dodaných produktových údajů: „Box spojuje tři doplňky stravy, láhev Golden Life a USB míchátko.“ U kostí je k dispozici v původním dlouhém souboru boxu konkrétnější „Vitamin D v nápoji Dark Cherry přispívá k udržení normálního stavu kostí.“ Ani tento výskyt nenahrazuje schválení produktu.

### Dodané znění
Vitamin D a vitamin K přispívají k udržení normálního stavu kostí a zinek k udržení normálního stavu vlasů, nehtů a kůže.

Zdravotní tvrzení se jmenovanou živinou; přesné schválení v produktovém info.md nebylo dostupné. Nelze potvrdit jako schválené. Před publikací ověřit formulaci a podmínky použití pro tento konkrétní produkt; do rozhodnutí lze použít neutrální složení „Nápoj obsahuje vitamin D3, vitamin K2, zinek, chrom a kyselinu listovou.“ Tato alternativa je návrh bez účinku, nikoli tvrzení označené za schválené.

### Dodané znění
Vitamin D a vitamin K přispívají k udržení normálního stavu kostí.

Zdravotní tvrzení se jmenovanou živinou; přesné schválení v produktovém info.md nebylo dostupné. Nelze potvrdit jako schválené. Před publikací ověřit formulaci a podmínky použití pro tento konkrétní produkt; do rozhodnutí lze použít neutrální složení „Nápoj obsahuje vitamin D3, vitamin K2, zinek, chrom a kyselinu listovou.“ Tato alternativa je návrh bez účinku, nikoli tvrzení označené za schválené.

### Dodané znění
Zinek přispívá k udržení normálního stavu vlasů, nehtů a kůže.

Zdravotní tvrzení se jmenovanou živinou; přesné schválení v produktovém info.md nebylo dostupné. Nelze potvrdit jako schválené. Před publikací ověřit formulaci a podmínky použití pro tento konkrétní produkt; do rozhodnutí lze použít neutrální složení „Nápoj obsahuje vitamin D3, vitamin K2, zinek, chrom a kyselinu listovou.“ Tato alternativa je návrh bez účinku, nikoli tvrzení označené za schválené.

### Dodané znění
Vitamin D a zinek přispívají k normální funkci imunitního systému.

Zdravotní tvrzení se jmenovanou živinou; přesné schválení v produktovém info.md nebylo dostupné. Nelze potvrdit jako schválené. Před publikací ověřit formulaci a podmínky použití pro tento konkrétní produkt; do rozhodnutí lze použít neutrální složení „Nápoj obsahuje vitamin D3, vitamin K2, zinek, chrom a kyselinu listovou.“ Tato alternativa je návrh bez účinku, nikoli tvrzení označené za schválené.

### Dodané znění
Chrom přispívá k udržení normální hladiny glukózy v krvi.

Živina je jmenovaná. Historický produktový zdroj 635 má vlastní formulaci „Chrom přispívá k udržení normální hladiny glukózy v krvi“; výskyt na webu nepovažujeme za právní schválení. Ověřit aktuální etiketu/registr.

### Dodané znění
Kyselina listová přispívá ke snížení míry únavy a vyčerpání.

Zdravotní tvrzení se jmenovanou živinou; přesné schválení v produktovém info.md nebylo dostupné. Nelze potvrdit jako schválené. Před publikací ověřit formulaci a podmínky použití pro tento konkrétní produkt; do rozhodnutí lze použít neutrální složení „Nápoj obsahuje vitamin D3, vitamin K2, zinek, chrom a kyselinu listovou.“ Tato alternativa je návrh bez účinku, nikoli tvrzení označené za schválené.

## Zdroje a náklady
- Aktuálně dodaný český text, povolený předchozí Pavelův webový kontext a současné vzdálené soubory v Gitu; konkrétní předloha Longevity včetně editovatelných SVG a PNG.
- Skutečné uložené veřejné HTML produktu 668 a pěti jednotlivých produktů 635,644,550,597,653 z předchozího stejného webového úkolu; nejde o čtení zákaznických exportů, jiné osoby nebo interních financí.
- Model gpt-6.1-sol; kresba a převod kódem/Chromiem. Žádná placená obrazová generace, dodatečný poplatek za obrazové generování 0. Cenu jazykového běhu nemáme k dispozici.
