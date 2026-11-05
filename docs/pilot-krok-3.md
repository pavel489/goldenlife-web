# Krok 3 – tři pilotní produktové šablony

## Stav a rozsah
Dokončená pracovní příprava tří produktů, vždy českého krátkého i dlouhého popisu. Není to nasazení na e-shop. Veřejná CSS ani CMS pole, ceny, zákaznická a objednávková data se neměnily.

Zdrojový Git: `6bca09f6f6afe310d4572910766502a9de97d023`. Referenční produkt: Slim GLP-1 Activator s Berberinem, nativní ID 476. Použity skutečné veřejné popisy a nativní galerie přesně těchto SKU:

- **Beauty Star (ID 351)**: `web/Golden Life Beauty Star/Golden-Life-Beauty-Star-cz.html` a `web/Golden Life Beauty Star/maly/Golden-Life-Beauty-Star-maly-cz.html`. Vlastní téma `user/documents/upload/css/golden-life-barvy-beauty-star.css`. Dialogy: 5; tabulky: 1.
- **Slim Extreme Collagen box s příchutí ananasu (ID 383)**: `web/Golden Life Slim Extreme Collagen box ananas/Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html` a `web/Golden Life Slim Extreme Collagen box ananas/maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-maly-cz.html`. Vlastní téma `user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-box-ananas.css`. Dialogy: 6; tabulky: 2.
- **Beauty Longevity NAD+ (ID 544)**: `web/Golden Life Beauty Longevity NAD+ dóza/Golden-Life-Beauty-Longevity-NAD-doza-cz.html` a `web/Golden Life Beauty Longevity NAD+ dóza/maly/Golden-Life-Beauty-Longevity-NAD-doza-maly-cz.html`. Vlastní téma `user/documents/upload/css/golden-life-barvy-beauty-longevity.css`. Dialogy: 6; tabulky: 3.

## Co je převedeno
- Jednotný modulární banner, hero, vysvětlující karty, přehled, vlastní ingredient teasery a úplné + dialogy, FAQ, CTA, užívání, upozornění a původní tabulky.
- Každé pole má jeden malý style blok se dvěma importy (framework a vlastní téma), vlastní ID a samostatné označení layoutu a tématu. Původní vložené layoutové CSS bylo odstraněno.
- Vlastní produktové texty se nezkracovaly na opakované dávkové údaje. Beauty Star má obnovený původní úvod, devět benefitových vysvětlení, zvláštní odstavec o biotinu i pět plných ingredient vysvětlení. Ananas zachovává šest vlastních vysvětlení. Beauty Longevity zachovává všech šest ingredient vysvětlení, příběh, graf, FAQ, užívání a další původní odstavce.
- Nativní fotografie se v heru a CTA synchronizuje pouze při správném ID; jinak zůstává vlastní ověřený fallback. Nejsou použity fotografie GLP-1 reference ani generované obaly.
- Staré pevné cenové/skladové CTA snapshoty byly odstraněny. CTA míří k vlastnímu nativnímu nákupnímu bloku, bez automatického vložení do košíku. U Beauty Star byly souhrny založeny na vlastním krátkém popisu (gumové hvězdičky), nikoli rozporném starém CTA slově „tobolky“.
- Tři osiřelé SEO-like titulkové odstavce byly odstraněny z nového těla: Beauty Star, chybný „Slim Extreme Collagen Mango“ v ananasovém poli a „Beauty Longevity NAD+ | Kolagen, NAD+ a komplex pro krásu a vitalitu | Golden Life“. Původní veřejné zálohy zůstaly nezměněné; nejde o zkrácení produktového vysvětlení.

## CSS a sourozenci
Společný `golden-life-produkt.css` je byte-identický se zdrojovým Gitem a nezměnil se. Témata Beauty Star a ananas jsou beze změny oproti kroku 2. Pouze `golden-life-barvy-beauty-longevity.css` má lokální dodatek pro `data-gl-theme="beauty-longevity"` + `data-gl-product-id="544"`: chybějící tokeny aktuálních mobilních/krátkých komponent a zalamování pěti ikon a metadat. Původní obsah tématu zůstává byte-identickým prefixem; pravidla dodatku nemíří na jiný produkt. Jediný zděděný inline styl (černá barva odkazu ke studii) je přesunutý do téhož lokálního tématu se zachováním barvy.

## Skutečně provedené společné testy
- Všech 6 dodaných HTML polí, jedna style dvojice importů a správná nativní identita; 6 bootstrap skriptů prošlo Node vm.Script a všechny 4 potřebné CSS soubory prošly tinycss2 1.5.1.
- Multiset původních podstatných odstavců/listových bodů 31 / 25 / 54 (bez tří osiřelých SEO titulků a výslovně nahrazených starých CTA) bez ztraceného výskytu; přesná shoda vnitřního HTML původních vysvětlujících odstavců všech 17 ingredient dialogů.
- **6 tabulek / 202 buněk**: nezměněné vnitřní HTML buněk proti původním veřejným polím. Čísla ani jednotky se neopravovaly odhadem.
- Celostránkový veřejný shop snapshot na reálném originu, se skutečnými shopovými skripty a obrázky; jen lokálně nahrazené CMS fragmenty a CSS odpovědi. Desktop 1440 px a mobil 390 px, všech 6 scénářů prošlo.
- **34 pointer testů dialogů**: všech 17 unikátních ingredient dialogů otevřeno a zavřeno na obou šířkách. Všechny měly podstatný plný text a vešly se do šířky viewportu.
- **10 mobilních přepínačů** otevřeno/zavřeno skutečným pointerem, první přepínač každého produktu navíc klávesnicí. Voliče se testovaly stabilní třídou/indexem, nikoli měnícím se textem tlačítka.
- U všech tří SKU v plném shop runtime skutečná změna na druhou načtenou fotografii stejného SKU a odmítnutí galerie při cizím nativním ID. Tím je doplněná původní izolovaná zkouška 544.
- CTA skutečně kliknuto na obou šířkách; vedlo na správný nativní formulář a nevznikl požadavek na Cart endpoint. Všechny ne-GET požadavky byly v testu blokovány.
- Nulové změřené horizontální přetékání rootu a krátkého hostu, textové range všech tabulek uvnitř buněk, pět krátkých ikon v jedné řadě, žádné nenahrané obrázky dlouhých popisů, responsive roundtrip a skutečně přesunutý root mimo `.basic-description`.
- Dvě cizí Seznam tracking chyby `Failed to fetch` v každém scénáři byly doloženy stackem `l.seznam.cz/static/js/sem.js` a souvisejí s blokovanými zápisy v testu. Výsledek neprohlašuje čistotu všech cizích integračních skriptů.

## Offline pracovní náhled
`pilotni-sablony-offline.html` je předávaná samostatná příloha, nikoli další živá stránka. Obsahuje přepínání všech tří produktů a mobilní/desktopovou šířku, skutečné vložené obrázky a fonty. Obrázky jsou pro velikost náhledu zmenšené a převedené do WebP bez ořezu; originály a produkční URL se neměnily. Krátký host je zjednodušený, font Nunito je vložen podle skutečného hostu; ověření produkčního vzhledu vychází z celostránkových shop testů, ne z této náhrady okolí.

V náhledu jsou vypnuté nákup, externí odkazy, síťové připojení a nativní synchronizátor galerie (neexistuje tam skutečný shopový host). Plný mobilní skript a CSS dialogy fungují. Skutečný finální soubor byl otevřen přes file://, opakovaně přepnuty všechny varianty; všechny dialogy na obou šířkách i přepínače prošly, žádná JS chyba ani externí request.

## Co zbývá rozhodnout před nasazením
**Historické copy není automaticky schválené.** Přesné citace a zdrojové alternativy jsou v `docs/pilot-krok-3-obsahove-vyhrady.md`. Zejména:
- Beauty Star: 30 g v krátkém popisu proti 65 g v dlouhém návodu, gumové hvězdičky proti tabletám/tobolkám a účinkové věty o akné, hormonech a vlasech.
- Ananas: box se sáčky proti zmínce o odměrce, číselné rozpory původní tabulky a spalovací/zeštíhlující tvrzení.
- Beauty Longevity: historický adresář „dóza“ proti vlastní nativní fotografii krabičky se sáčkem; původní informace o vhodnosti pro děti od 8 let, tříměsíční kúře a štípání v krku; neověřená longevity a účinková tvrzení. Nové souhrny „dózu“ netvrdí.

Tyto rozpory nebyly tiše opravené ani nově odborně posouzené. Pilot je dokončená **technická a vizuální pracovní verze**, ne souhlas k živému publikování copy.

## Předání a cena
Editovatelné HTML/CSS a dokumentace v tomto repozitáři; tři označené kontaktní náhledy v `nahledy/`; samostatný offline HTML přiložený ve Slacku. Před skutečným importem jsou potřeba čerstvé raw zálohy editoru, kontrola nahraných CSS a následné veřejné ověření. Toto předání je v Gitu, nikoli Shoptetu.

Zpracování: GPT-6.1-Sol (včetně nezávisle ověřené dílčí práce na 544), Python/BeautifulSoup, CSS parser a Chromium/Playwright. Bez placeného obrazového generování; cenu modelového/connectorového běhu zde nemám vyčíslenou.
