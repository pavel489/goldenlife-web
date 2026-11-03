# Slim Extreme Collagen – jeden společný přehledový blok

## Aktuální úprava
Dvě původní karty „Jak funguje“ a „Účinky“ jsou nahrazeny jediným blokem. Vlevo je přesná dodaná fotografie `/user/documents/upload/ruzovy-popis/slim-collagen-ctverec-2000.jpg`, vpravo jeden nadpis a dva krátké odstavce shrnující oba původní texty. Na mobilu do 767 px je nejdřív fotografie a pod ní celý text. Žádné rozbalování, žádné zkrácení přes CSS. Fotografie je celá čtvercová bez ořezu obličeje a dózy.

### Text bloku
**Jak funguje Slim Extreme Collagen**

Slim Extreme Collagen spojuje kolagenní peptidy Verisol® a Peptiplus® a kyselinu hyaluronovou s komplexem garcinie, zeleného čaje, synefrinu a enzymů. Je navržený jako součást redukčního režimu a každodenní péče o krásu.

Složení doplňují vitaminy a minerály. Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.

Shrnutí ponechává dvě linie původního sdělení (redukční režim / kolagenová kosmetická linie), složení i podloženou formulaci o únavě. Nepřebírá nepodložené sliby termogeneze, rychlejšího metabolismu, odvodnění, sytosti nebo kloubních účinků. Přesné oddělení obsahových výhrad je v [poznámkách](../../docs/slim-extreme-collagen-obsahove-vyhrady.md).

## Soubory
- [Dlouhý popis](Golden%20Life%20Slim%20Extreme%20Collagen.html)
- [Krátký popis – v této opravě nezměněný](maly/Golden%20Life%20Slim%20Extreme%20Collagen%20maly.html)
- [Barevné téma](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen.css)
- [Desktopový náhled](../../nahledy/slim-extreme-collagen-ucinky.png)
- [Mobilní náhled](../../nahledy/slim-extreme-collagen-prehled-mobil.png)
- [HTML náhled](../../nahledy/slim-extreme-collagen.html) – stáhnout a otevřít v prohlížeči, fotografie/fonty vyžadují internet. Bez nákupního formuláře.
- [Testy aktuální opravy](../../docs/slim-extreme-collagen-prehled-testy.json)

## Rozsah a globální styly
Zůstává jeden malý style blok se dvěma importy: společný `golden-life-produkt.css` a vlastní `golden-life-barvy-slim-extreme-collagen.css`. Nová sekce používá existující sdílený `story-block`; produktové téma obsahuje jen omezené korekce rozvržení, rozestupů a celého čtvercového obrázku. Společné CSS, krátký popis, tabulky složení, původní synchronizační skripty a všechny ostatní části dlouhého popisu jsou beze změny. Reverzní záměna nového bloku za staré dva obnoví přesné původní bajty dlouhého HTML.

## Ověření
Chromium 320/360/390/600/767/768/1024/1440 px a návrat na 390: správné pořadí, jeden nadpis, celý text i obrázek 2000 × 2000, bez přetečení, všechny fotografie načtené, žádné JS chyby v izolované stránce. Všech šest původních detailů látek se otevírá a zavírá na mobilu i desktopu. Na dočasně přepsané skutečné produktové stránce ověřeno rozvržení při 390 a 1440 px, hlavní fotografie hero/CTA a synchronizace veřejné ceny. Při plné shop stránce zaznamenány dvě zprávy „Failed to fetch“, původ nebyl určen; geometrické/funkční testy komponenty prošly. Vizuálně prohlédnut desktop i mobil. Nejde o uložení do CMS.

## Nasazení
Na e-shopu nebylo nic uloženo. Nahraj aktualizované barevné CSS a nahraď dlouhý popis celým aktuálním HTML. Pokud ještě není nasazená předchozí migrace, nahraj i její krátký popis. Společné CSS se kvůli této opravě nemění. Po uložení ověř veřejný produkt. Git aktualizace není nasazení do Shoptetu.

## Zdroje a výroba
Aktuální Git main 9bffda8d442d7bf81962734028f05b6d4e3826ed, oba původní odstavce stejného SKU 168, fotografie dodaná v tomto vlákně, veřejné shop styly, `brand/RULES.md` a produktový soubor `brand/product/extreme-slim-collagen/info.md`. Model GPT-6.1-sol; Python/BeautifulSoup a Chromium/Playwright. Bez nové obrazové generace a poplatků za ni; cenu běhu jazykového modelu nemám k dispozici.
