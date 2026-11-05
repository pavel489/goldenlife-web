# Collagen Beauty — předání dodaných českých textů

## Co je hotové

Pracovní implementace celého Pavlem dodaného znění do stávajícího českého dlouhého a krátkého popisu. Jde o stejnou Git cestu jako u předchozích boxů, nikoli uložení do živého Shoptetu. Texty se stylisticky nepřepisovaly; `&amp;` se vykresluje jako `&`.

- Dlouhý popis: `shoptet/beauty.html`.
- Krátký popis: `shoptet/beauty-kratky.html`.
- Aktualizované i oba odpovídající české soubory v `web/Golden Life Darkovy box Beauty/`; ostatní jazyky zůstávají beze změny.
- Název produktu, SEO titulek a meta description: přesné hodnoty v `config/beauty-darkovy-box-texty-cz.json`. Jsou to samostatná pole administrace; vložením dlouhého HTML se název ani SEO produktu samy nezmění. Samostatný webový dokument má aktualizované také TITLE, description a OG texty.
- Úplný dodaný text: `docs/beauty-darkovy-box-dodane-texty.md`.
- Identita: existující `productId=656`, kanonický odkaz z uloženého veřejného snímku `https://www.golden-life.cz/darkovy-box-collagen-beauty/`.

Zachováno všech pět původních detailových tlačítek, jejich produktová ID/URL, všechny původní SCRIPT a STYLE obsahy byte-for-byte a původní identita/režim košíku. Karty jsou v dodaném pořadí: Slim Extreme Collagen, Slim & Detox Power, Good Sleep, láhev, míchátko, balení. Celkem je šest karet, protože dárkové balení není šestý produkt. FAQ obsahuje sedm dodaných otázek.

Zachované vazby fotografií: šestá galerie v úvodu, druhá u dárkového balení, hlavní fotografie v nákupním bloku. Žádné fotografie se nepřekreslovaly nebo nenahrazovaly jiným SKU. Trvalý text „5 produktů v dárkové krabici“ je samostatně mimo `.gl-packaging-note`, kterou galerie může přepisovat nebo skrývat. Dodané „Do košíku“ je ve zdroji; původní skript smí bezpečně použít jiný stav při nedostupném nativním nákupu či v samostatném náhledu. Cena ani sklad se tímto Git krokem nemění.

## Piktogramy přesně ve stylu nynějšího Longevity

Referencí jsou skutečné vzdálené bajty `shoptet/longevity.html` z výchozího commitu uvedeného v testech, nikoli paměť starší varianty. Zachována konstrukce 64 × 64, síla tahu 3.5, zaoblené konce i spoje a stejný způsob vykreslení barevnou maskou. Na obrazovce je stejná stávající boxová červená RGB 217, 8, 23. Žádná změna sdíleného CSS.

- Kolagen, kapsle, láhev a míchátko používají totožné SVG kresby jako Longevity.
- Sáček má nově ananasový motiv; symbol vitaminu C a zinku je nová obsahová kresba ve stejném systému. Nejde o oficiální dodaný piktogram ani o chemický strukturní vzorec zinku.
- Šestice je stejná v dlouhém i krátkém popisu a má přesně dodané obsahové popisky. Staré účinkové popisky typu „Redukce vrásek“ byly v těchto blocích nahrazeny podle zadání.
- Editovatelné SVG: `assets/beauty-giftbox-line-icons/`. Jejich vložené kopie v HTML byly dekódovány a porovnány s mistry.
- Náhledy v `nahledy/beauty-darkovy-box-piktogramy.png` a `nahledy/beauty-darkovy-box-kratky-mobil.png` jsou offline vykreslení skutečných dodaných bloků, ne screenshot nasazeného e-shopu.

## Otevřené věcné body — neměněné potichu

1. **Vánoční doručení:** ve FAQ zůstává `[DOPLŇ DATUM]`. Datum musí potvrdit odpovědný člověk před živou publikací.
2. **Good Sleep — zlatobýl versus řimbaba:** dodaná věta „Kapsle spojují mučenku, meduňku, kozlík, chmel a hloh s garcinií kambodžskou, zlatobýlem a mořskou řasou wakame.“ se liší od `brand/product/good-sleep-night-burn/info.md` a uloženého veřejného detailu produktu 57, kde je **řimbaba obecná**. Zdrojově podložená alternativa: **„Kapsle spojují mučenku, meduňku, kozlík, chmel a hloh s garcinií kambodžskou, řimbabou obecnou a mořskou řasou wakame.“** V pracovním podkladu zůstalo dodané znění; potvrď oproti aktuální etiketě před zveřejněním.
3. **Nabídka a recenze:** uložený veřejný snímek stejného produktu 656 obsahuje 3 790 Kč, srovnávací cenu 4 400 Kč, hodnocení 5,0 z 5 a recenze k dárku pro maminku, krásnému balení a chuti „naprostá špička“. Rozdíl 610 Kč je spočítaný v Pythonu. Nejde o nové živé ověření nabídky. Do textu se nepřenášelo zdravotní tvrzení z plné zákaznické recenze ani jména zákaznic.
4. **Dávkování a upozornění:** dodané texty byly porovnány s produktovými soubory a uloženými veřejnými detaily 383, 174 a 57. Potvrzují 30 sáčků a 200–300 ml vody, 90 tobolek/45 dní u obou kapslí, kofein a omezení při forskolinu a konzultaci u Good Sleep při lécích na tlak nebo sedativech. Nenahrazuje to aktuální schválené etikety; každá receptura má vlastní dávkování. Hodnoty v tabulkách historického produktového souboru vykazují i jiné nejasnosti, nejsou novým analytickým certifikátem.

## Zdravotní tvrzení — oddělená kontrola

Následující věty jsou tvrzení o účinku a v dodaném pracovním znění zůstaly. Jejich implementace není právní schválení:

- „Vitamin C přispívá k normální tvorbě kolagenu pro normální funkci kůže a zinek k udržení normálního stavu vlasů a nehtů.“ — úvod.
- „Slim & Detox Power je zaměřený na aktivní dopoledne, zatímco Good Sleep & Night Burn na večerní zklidnění s mučenkou, meduňkou a chmelem.“ — konkrétně část o **večerním zklidnění** je botanický účinkový claim. Neutrální alternativa: „Slim & Detox Power doplňuje dopolední rutinu, Good Sleep & Night Burn je večerní receptura s mučenkou, meduňkou a chmelem.“ Tato alternativa je popis, nikoli schválené zdravotní tvrzení.
- „Vitamin C přispívá k normální tvorbě kolagenu pro normální funkci kůže.“ — pod ikonami a v kartě nápoje.
- „Biotin a zinek přispívají k udržení normálního stavu vlasů a kůže.“
- „Zinek přispívá k udržení normálního stavu nehtů.“
- „Kyselina pantothenová, vitamin B12 a vitamin C přispívají ke snížení míry únavy a vyčerpání.“
- „Vitamin C, vitamin E a zinek přispívají k ochraně buněk před oxidativním stresem.“

Nutrientové věty jmenují nosné živiny, avšak dostupný vlastní soubor přesného ananasového produktu `brand/product/slim-extreme-collagen-box-s-prichuti-ananasu/info.md` **nemá doslovně schválené zdravotní tvrzení**. U Slim & Detox a Good Sleep jejich soubory také uvádějí, že žádné EFSA claims nejsou zapsané. Proto zde nelze nabídnout skutečnou produktově schválenou účinkovou alternativu: v těchto zdrojích není. Nevypůjčovala se formulace od varianty ananas–mango ani od jiného SKU. Aktuální individuální ověření registru EU a podmínek použití nebylo součástí této implementace; nelze běžnou formulaci automaticky vydávat za produktově právně schválenou.

Obecné sliby krásy, krásné pleti/vlasů/nehtů a klidných večerů v krátkém i dlouhém úvodu patří do stejné předpublikační kontroly v kontextu celého sdělení. Povinné upozornění je zachované přesně podle dodaného znění. Dynamicky importované detaily jsou samostatný obsah původního obchodu; toto předání je nijak právně neschvaluje.

Přečteno `brand/RULES.md` i pracovní vizuální identita. `brand/NOT-ALLOWED.md` na dostupné cestě není.

## Co se skutečně testovalo a co ne

- Oba dlouhé soubory: úplné znění všech **59** očekávaných textových položek. Oba krátké: **7** položek (celý odstavec + šest popisků).
- Bajtově shodné obsahy všech původních SCRIPT a STYLE bloků, zachované ID/URL čteček, hero atributy a původní root `data-gl-product-id=656`.
- Chromium, izolovaná offline stránka s produkčním HTML a skutečně vykonanými dodanými skripty. Neměnily se shopové účty ani konfigurace.
- Šířky **1440, 390 a 360 px**: bez horizontálního přetékání obou bloků, všech 12 vložených SVG načtených, stejná šestice popisků, správné pořadí šesti karet a sedm FAQ.
- Na každé šířce kliknutím otevřeno/zavřeno všech sedm FAQ i krátký obsah. Všech pět čteček otevřeno/zavřeno a první znovu otevřena; správné nadpisy a podstatný obsah v Shadow DOM, žádné importované SCRIPT prvky. Čtečky používaly **skutečné uložené veřejné snímky**, nikoli současné síťové odpovědi. Ověřeno i ovládání první FAQ Enterem. Žádná zachycená JS chyba.
- Všechny síťové požadavky v testovacím prohlížeči byly zachyceny: povolené zdroje byly dodané ze skutečných uložených bajtů, ostatní zablokované. Zablokované fotografie nejsou počítané jako úspěšně načtené. Chybějící fotografie se nevyráběly ani nenahrazovaly domnělými odpověďmi. Nativní nákup byl nefunkční fixture; neproběhlo odeslání do košíku.
- Závislosti: přesný čtečkový pin `45c603ef2f6582495668bbb0c02d81a761bf2344`, přesný boxový CSS pin `b28871724fad59acc0c53dc1ddeef1015472ce50`, sdílený framework z ověřeného výchozího Gitu a reálný Google Material Symbols font. Náhled nemá kompletní nativní šablonu ani všechny její fonty; není pixelovým testem živého e-shopu.
- **Živý obchod:** přesná kanonická stránka vrátila HTTP 403 „Access temporarily blocked“ s informací o dočasném IP bloku. Další přístupy na Shoptet byly zastavené, nikoli obcházené jiným prohlížečem nebo IP. Nelze proto potvrdit současnou nabídku, načtení fotografií ani úplnou živou integraci. Git dokončení tím blokované není.
- Piktogramový blok a mobilní krátký popis byly skutečně vizuálně prohlédnuté. Výsledky: `tests/beauty-darkovy-box-texty-results.json`.

## Zdroje, model, náklady

Vstupy: celý Pavlův text v tomto vlákně; ověřený vzdálený `pavel489/goldenlife-web`, aktuální referenční Longevity, existující české Beauty soubory; uložené veřejné snímky boxu 656 a složek 383/174/57/597/653 z předchozího webového testu tohoto zadavatele; vlastní tři produktové soubory, `brand/RULES.md` a pracovní vizuální identita.

Model **gpt-6.1-sol**. HTML a dva doplňkové SVG symboly připravené kódem; ostatní čtyři kresby převzaté beze změny z existujícího Longevity. **Bez placeného obrazového/video generování.** Cenu modelového běhu a případné konektorové účtování toto rozhraní nezpřístupňuje, proto nelze tvrdit celkové nulové náklady.
