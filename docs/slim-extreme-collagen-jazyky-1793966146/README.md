# Slim Extreme Collagen — slovenská, anglická a německá mutace

**Pracovní jazykové verze do Gitu. Nejde o nasazení na e-shop ani právní schválení zděděných zdravotních tvrzení.**

Rozsah: Slim Extreme Collagen v dóze240g, ověřený produkt168; nikoli box nebo sáček. Tři stávající jazyky ověřené přes konkrétní hreflang produktu: SK, EN, DE. Každý má úplný dlouhý a krátký popis. Český originál, společné CSS a společný JS zůstávají beze změny.

## Soubory

### Slovenština
- Dlouhý popis: [Golden Life Slim Extreme Collagen-sk.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen/Golden%20Life%20Slim%20Extreme%20Collagen-sk.html)
- Krátký popis: [Golden Life Slim Extreme Collagen maly-sk.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen/maly/Golden%20Life%20Slim%20Extreme%20Collagen%20maly-sk.html)
- Ověřená veřejná cílová URL: https://www.golden-life.cz/sk/extreme-slim-collagen/

### Angličtina
- Dlouhý popis: [Golden Life Slim Extreme Collagen-en.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen/Golden%20Life%20Slim%20Extreme%20Collagen-en.html)
- Krátký popis: [Golden Life Slim Extreme Collagen maly-en.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen/maly/Golden%20Life%20Slim%20Extreme%20Collagen%20maly-en.html)
- Ověřená veřejná cílová URL: https://www.golden-life.cz/en/slim-extreme-collagen/

### Němčina
- Dlouhý popis: [Golden Life Slim Extreme Collagen-de.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen/Golden%20Life%20Slim%20Extreme%20Collagen-de.html)
- Krátký popis: [Golden Life Slim Extreme Collagen maly-de.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen/maly/Golden%20Life%20Slim%20Extreme%20Collagen%20maly-de.html)
- Ověřená veřejná cílová URL: https://www.golden-life.cz/de/slim-extreme-collagen/

## Zachováno a přeloženo

- Zachovaný aktuální nový vzhled a adaptace podle okolního pozadí (`host-bg-1`), oba CSS importy a stejný idempotentní loader.
- Úplné odstavce, všech6 ingredienčních dialogů a 96 tabulkových buněk v každé dlouhé verzi; dávky, jednotky, čísla a šaržové pokyny zachované.
- Přeložené viditelné texty, image alt/aria popisky, metadata a JSON-LD description/category; i mobilní Zobrazit více/méně a jejich přístupnostní labely.
- Produktové ID, modal ID/anchory, CSS markery, IMG/JS/CSS URL, galerie a logika synchronizace ceny zachované. Jediné změněné JS stringy jsou6 výskytů mobilních labelů v každé dlouhé verzi; zbytek AST je shodný.
- Zdroj nemá FAQ; žádné nebylo vymyšleno ani přidáno.

## Výslovné doplnění / výjimky proti doslovnému překladu

- Do upozornění dlouhého popisu přidáno označení doplňku stravy; na konec každého krátkého popisu doplněno lokalizované povinné minimum o pestré stravě, nepřekračování denní dávky a dosahu dětí.
- Z nových překladů odstraněny neověřené staré JSON-LD `offers` (1350CZK/InStock) a `aggregateRating` (4.9/127). Žádné zahraniční ceny, měny, sklad či recenze nebyly vymyšleny.
- Viditelná statická cenová náhrada je `—`; původní synchronizace stále přebírá hodnotu z nativního hostitele, pokud je dostupný. Místo neověřeného slibu skladem/odeslání24h je lokalizovaný odkaz na aktuální dostupnost u nákupního tlačítka. Nejde o změnu cen či dostupnosti ve Shoptetu.
- V DE krátkém popisu jsou typografické volitelné dělicí znaky u dvou dlouhých piktogramových titulků; slova a význam zůstaly stejné, ALT zůstává bez dělení.
- Český skloňovaný název jednotky `daltonů` je jazykově lokalizován, nikoli fyzikálně přepočítán.

## Otevřené obsahové kontroly před veřejnou publikací

**Zděděné účinkové sliby nejsou tímto překladem schváleny.** Rizika jsou po větách/fragmentech vedle přesného překladu v [claims-review.csv](claims-review.csv) a [claims-review.json](claims-review.json). U každého je také skutečně zaznamenaná formulace z vlastního produktového souboru o vitaminech B2/B3/B5 a její překlad. Tuto formulaci nelze bezmyšlenkovitě zaměnit za každý specifický slib o hubnutí, kolagenu či hojení.

> Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.

Původní text mimo jiné slibuje spalování tuků, redukci celulitidy/vrásek, účinky bez pohybu i účinky na bolest/hojení a riziko onemocnění. Tyto věty jsou pro kontrolu zachovány jako pracovní překlad, nikoli doporučení k publikaci.

Dávkovací podklady mají rozdílný generický pokyn v dlouhém a krátkém popisu (1 versus2 odměrky, 200–300 versus300–400ml) vedle specifické malé/velké odměrky a šaržeL245382/072028. Rozdíl jsme nezamaskovali ani recepturu neupravovali.

Podezřelá je například původní tabulka B6:823,5mg/100g proti0,7mg/8g. Doslovná čísla zůstala zachována; matematická kontrola v [verification.json](verification.json) pouze označuje nesoulad, neurčuje správnou recepturu.

## Skutečné testy finálních souborů

- Statické kontroly **6/6 HTML**: číselné tokeny, tabulky, obrázky, modal ID/odkazy, CSS a byte-identický loader; porovnání skutečně parsovaných JS AST (Acorn), ne jen regexem nad řetězci.
- **72/72** browserových scénářů:3 jazyky ×2 preference prohlížeče ×2 okolní pozadí ×6 viewportů (390,767,768,820,1024,1440CSSpx).
- **72** pointer cyklů dialogů; **6** cyklů mobilního rozbalování. Vykreslené popisy i tabulky se vešly, obrázky se dekódovaly, 0 chyb JS a0 externích požadavků v offline QA.
- Samostatný skutečný soubor `file://` náhledu: **16/16** stavů, 8 přepnutí jazyků včetně návratu, 16 dialogových cyklů uvnitř iframe; žádné přesměrování na obalový soubor ani síťové požadavky.
- Cílové veřejné jazykové URL, jazyk dokumentu a SKU168 byly ověřené samostatně. Žádný překlad nebyl uložen do CMS; nativní cenu/košík/živou galerii tento offline test necertifikuje. Safari/iPad ani rodilý lidský korektor nebyli součástí ověření.

## Náhled a vložení do e-shopu

- [Samostatný offline náhled](nahled-jazykove-mutace.html): stáhni Raw HTML a otevři v prohlížeči. Vybereš jazyk a světlé/tmavé okolí. Hlavička náhledu je interní česky, samotné produktové bloky jsou v cílovém jazyce.
- [Přehled krátkých popisů](jazykove-mutace-prehled.png) a jednotlivé náhledy jsou skutečně vykreslené snímky, ne generované fotografie.
- Základní CSS, barevné CSS a JS `golden-life-product-scheme.js` musí být dostupné ve stejných cestách jako v předchozí opravě. V této úloze se nemění; chybějící upload se neřeší překladem.
- Každý soubor patří do příslušného jazykového dlouhého nebo krátkého pole. Nejde o samostatnou změnu nativního názvu/URL/SEO polí v administraci.
- Cena a nákup nejsou v náhledu připojené. Připravenost galerie je označená pouze v QA, aby offline skript neobnovoval původní vzdálené URL; produkční script není upravený. Obrázky a fonty jsou autentické zdroje, uncropped zmenšení/WebP a odstranění nativní ceny jsou pouze pro náhled. Produkční asset URL zůstaly stejné.

## Zdroje a zpracování

- Aktuální zdrojový Git: `6e471030bd01d04aed7b5c251b07933b09fc9e6f`, původní český dlouhý+krátký popis a přesné společné závislosti; blob SHA jsou v `source-manifest.json`.
- Produktový zdroj: `brand/product/extreme-slim-collagen/info.md`; lidská pravidla `brand/RULES.md`. `brand/NOT-ALLOWED.md` v dostupném workspace nebyl nalezen; není předstíraná právní kontrola.
- Původní skutečné obrázky/fonty z ověřeného same-SKU archivu a deset nově ověřených veřejných image odpovědí; žádné generované packshoty.
- Model GPT‑6.1‑Sol; Python/Playwright/Chromium a Acorn. Bez placené obrazové/video generace; modelové/connectorové náklady nebyly v této úloze vyčísleny.
