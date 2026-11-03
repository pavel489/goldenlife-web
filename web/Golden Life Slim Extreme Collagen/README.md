# Slim Extreme Collagen – migrace na globální styly

## Změna
Dlouhý i krátký popis mají jeden malý style blok se dvěma importy: `golden-life-produkt.css` a vlastní `golden-life-barvy-slim-extreme-collagen.css`. Rozvržení používá již existující layout `woman-hormonal-balance` / `woman-hormonal-balance-short`; jde jen o název sdílené šablony, produkt zůstává Slim Extreme Collagen, productId 168. Samostatné téma zachovává růžovou #e3127e. Původní vložené CSS krátkého popisu a barvy v inline stylech byly převedeny do sdíleného frameworku / produktového tématu. Společný framework se nemění.

V kartě **Účinky** je přesná dodaná fotografie `/user/documents/upload/ruzovy-popis/slim-collagen-ctverec-2000.jpg`, načtená v původním rozlišení 2000 × 2000. Fotografie zůstává celá čtvercová, bez ořezu obličeje a dózy. Ostatní fotografie nebyly nahrazeny. Původní texty, dávkování, upozornění, tabulky a synchronizační skripty zůstaly zachovány. Na tabulkách je již existující opt-in marker proti přetečení dlouhých slov.

## Soubory
- [Dlouhý popis](Golden%20Life%20Slim%20Extreme%20Collagen.html)
- [Krátký popis](maly/Golden%20Life%20Slim%20Extreme%20Collagen%20maly.html)
- [Vlastní téma](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen.css)
- [Obrázkový náhled](../../nahledy/slim-extreme-collagen-ucinky.png)
- [HTML náhled](../../nahledy/slim-extreme-collagen.html) – stáhnout a otevřít v prohlížeči, fotografie/fonty vyžadují internet. Nákupní formulář není součástí náhledu.
- [Testy](../../docs/slim-extreme-collagen-global-testy.json)
- [Obsahové výhrady](../../docs/slim-extreme-collagen-obsahove-vyhrady.md)

## Nasazení do Shoptetu – ještě neprovedeno
1. Nahraj nové barevné CSS do `/user/documents/upload/css/golden-life-barvy-slim-extreme-collagen.css`. Při kontrole URL vracela HTTP 404.
2. Nahraď starý dlouhý i krátký popis celými novými HTML. Nepřipojuj je za původní vlastní styly.
3. Ověř veřejný produkt po uložení. Společný `golden-life-produkt.css` už na webu odpovídá aktuální Git verzi po normalizaci CRLF/LF a není potřeba ho kvůli této změně přepisovat.

Git aktualizace není uložení do administrace Shoptetu. Tento úkol nezasahuje do objednávek, nastavení, cen ani ostatních produktů. Případní importéři v boxech mohou mít vlastní allowlist názvů CSS; jejich změna není součástí zadání a nebyla ověřována.

## Ověření
Chromium, skutečné shop styly a skutečné obrázky: 320, 360, 390, 520, 768, 1100, 1440 px a návrat na 390. Bez horizontálního přetečení a nefunkčních obrázků, celé čtvercové foto, správná růžová, bez dvojího přebarvení piktogramů. Všech šest detailů aktivních látek bylo otevřeno a zavřeno na mobilu i desktopu. Krátký popis navíc v hostech 260/300/360/420 px. V dočasně přepsané odpovědi skutečné produktové stránky ověřeny oba fragmenty, hlavní fotografie hero/CTA a synchronizace veřejné ceny při 390 a 1440 px. Tyto testy neukládaly CMS ani nic do košíku. Vizuálně prohlédnut desktop i mobil. Texty, tabulky a původní skripty jsou ověřeny programovým porovnáním.

## Zdroje a výroba
Aktuální main c0cb239d25b1caa83d277d58afd87e88587eb8dc, veřejný produkt https://www.golden-life.cz/extreme-slim-collagen/, veřejné CSS v dodané cestě, dodaná fotografie, `brand/RULES.md`, `brand/product/extreme-slim-collagen/info.md`. Model GPT-6.1-sol; Python/BeautifulSoup, Chromium/Playwright. Žádná placená obrazová generace, bez nového generování fotografie; cenu běhu jazykového modelu nemám k dispozici.
