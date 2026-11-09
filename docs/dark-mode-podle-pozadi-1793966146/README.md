# Dark mode podle okolního pozadí — oprava 14 produktů

**Stav: otestovaná příprava pro Git. Nejde o nasazení do Shoptetu.**

## Opravené chování

- Světlé okolí produktového popisu → původní světlý vzhled, i když prohlížeč hlásí tmavou preferenci.
- Tmavé okolí → tmavý produktový vzhled, i když prohlížeč hlásí světlou preferenci.
- Samotné `prefers-color-scheme` už tmavé produktové styly neaktivuje.
- Změna okolního pozadí bez reloadu se znovu vyhodnotí. Vlastní obarvení produktu není vstup, takže nedochází k zaseknutí v černé.

## Co se změnilo

- 14 produktových barevných CSS. Původní světlá paleta a tabletové opravy zůstávají jako přesný byte-identický zdrojový prefix. Tmavé selektory vyžadují `data-gl-site-scheme="dark"` na vlastním kořeni.
- Jeden nový společný UI skript: [`golden-life-product-scheme.js`](../../user/documents/upload/js/golden-life-product-scheme.js).
- V odpovídajících 28 připravených dlouhých/krátkých HTML je pouze idempotentní načtení skriptu a verze `?v=host-bg-1` na importu barevného CSS. Text, fotografie, nákupní logika a všechny ostatní původní bajty zůstaly zachovány; změna je přesně reverzibilní.
- Společný [`golden-life-produkt.css`](../../user/documents/upload/css/golden-life-produkt.css) je **beze změny**. Fotografie se neinvertují.

## Nasazení — samotná výměna 14 CSS nestačí pro automatický dark mode

1. Nahraj 14 níže uvedených CSS pod původními názvy do `/user/documents/upload/css/`.
2. Nahraj nový JS do `/user/documents/upload/js/golden-life-product-scheme.js`.
3. Použij aktualizované připravené HTML (obsahují načtení automaticky). U vlastních/již lokalizovaných HTML zachovej text a jednorázově vlož [`vlozeni-do-hlavicky.html`](vlozeni-do-hlavicky.html) do globální hlavičky šablony před `</head>`. Opakované načtení z dlouhého i krátkého popisu je ošetřené.
4. V existujícím importu příslušného barevného CSS přidej `?v=host-bg-1`, aby se nespojil starý uložený dark CSS soubor s novým skriptem. Na slovenské stránce z příkladu jde o:

```html
<style>
@import url("/user/documents/upload/css/golden-life-produkt.css");
@import url("/user/documents/upload/css/golden-life-barvy-slim-extreme-collagen.css?v=host-bg-1");
</style>
```

**Důležitá zjištěná závislost:** při této kontrole vracela veřejná adresa `https://www.golden-life.cz/user/documents/upload/css/golden-life-produkt.css` stav **HTTP404**. Nahraj i tento již existující nezměněný společný soubor na přesnou adresu. Jinak nelze přijmout kompletní živý vzhled — chybějící rozvržení neopraví samotná barevná paleta. Příčinu nedostupnosti netvrdíme.

Nezaměňuj vlastní slovenské znění za české soubory kvůli této úpravě. Pro vlastní jazykové popisy stačí nezměněný obsah, správné importy a načtení stejného JS. Skript se rozhoduje podle podporovaného tématu a okolí, ne podle jazyka či URL.

## Ověření

- **336/336** integrovaných scénářů: 14 produktů × světlá/tmavá preference × světlé/tmavé okolí × 6 velikostí (390, 767, 768, 820, 1024 a 1440 CSS px).
- **364** cyklů otevření/zavření původních dialogů a **92** cyklů rozbalování.
- **28** pixelových porovnání: původní světlé bannery a krátké popisy beze změny, i při tmavé preferenci prohlížeče.
- **28** návratů světlé → tmavé → světlé s obnovenou paletou; **14** testů čitelného světlého fallbacku a CSS dialogů bez JS.
- **54/54** samostatných testů detektoru. Navíc 112 výslovně syntetických kombinací téma/délka/jazyk — nikoli audit skutečných překladů.
- **14** integračních testů skutečného loaderu: dlouhý+krátký popis stahují jen jednu instanci finalního JS; odpověď v tomto testu je lokálně obsloužena skutečnými finálními bajty, ne vydávaná za živý upload.
- 0 chyb JS a 0 externích požadavků ve vlastních offline produktových testech. Měření kontrastu je pro ustálené stavy po dokončení existujících CSS přechodů, nikoli certifikace celého WCAG.
- Testy běžely v Chromium. Fyzický Safari/iPad, uzavřený Shadow DOM a čistě vykreslovací inverze rozšířením nebyly ověřeny.

## Náhled

- [`nahled-pozadi.html`](nahled-pozadi.html): samostatný stažitelný HTML náhled s původním krátkým popisem SKU168, dvěma modelovými pozadími a tlačítkem prohození. GitHub zobrazí kód; pro spuštění stáhni Raw soubor a otevři jej v prohlížeči.
- [`svetle-a-tmave-okoli.png`](svetle-a-tmave-okoli.png): skutečně vykreslený náhled. Tři dříve chybějící piktogramy byly pro tento náhled obnoveny z přesných aktuálních veřejných PNG (ověřeno HTTP200, MIME, dekódování a SHA-256), ne nahrazeny generovanými obrázky. V produkčních URL ani obsahu se nic z toho neměnilo.
- Historická produktová účinková tvrzení jsou ponechaný zdrojový obsah, nikoli tímto technickým auditem právně schválená copy.

## Rozhodování a omezení

Detektor alfa-komponuje vypočtené barvy předků přes běžný i otevřený Shadow DOM. Tmavé pozadí určuje relativní sRGB luminance <0,179. Vlastní kořen produktu nečte. Transparentní podklad případně doplní skutečná UA barva Canvas. CSS obrázky/gradienty nebo nevyřešené kompozitní efekty konzervativně volí světlou variantu. Bez JS zůstane produkt světlý a čitelný. Tichá změna CSS může být zachycena do přibližně 1,5s na viditelné stránce.

Toto je příprava zdrojů a ověřený náhled, nikoli potvrzení opraveného živého e-shopu. Před nasazením je nutný upload a opětovná kontrola dostupnosti společného CSS, nového JS, stylů i výsledného HTML.

## Upravené produkty a přesné soubory

### 351 — Beauty Star

- CSS: [golden-life-barvy-beauty-star.css](../../user/documents/upload/css/golden-life-barvy-beauty-star.css)
- Dlouhý popis: [Golden-Life-Beauty-Star-cz.html](../../web/Golden%20Life%20Beauty%20Star/Golden-Life-Beauty-Star-cz.html)
- Krátký popis: [Golden-Life-Beauty-Star-maly-cz.html](../../web/Golden%20Life%20Beauty%20Star/maly/Golden-Life-Beauty-Star-maly-cz.html)

### 383 — Slim Extreme Collagen box s příchutí ananasu

- CSS: [golden-life-barvy-slim-extreme-collagen-box-ananas.css](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-box-ananas.css)
- Dlouhý popis: [Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas/Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html)
- Krátký popis: [Golden-Life-Slim-Extreme-Collagen-box-ananas-maly-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas/maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-maly-cz.html)

### 544 — Beauty Longevity NAD+

- CSS: [golden-life-barvy-beauty-longevity.css](../../user/documents/upload/css/golden-life-barvy-beauty-longevity.css)
- Dlouhý popis: [Golden-Life-Beauty-Longevity-NAD-doza-cz.html](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20d%C3%B3za/Golden-Life-Beauty-Longevity-NAD-doza-cz.html)
- Krátký popis: [Golden-Life-Beauty-Longevity-NAD-doza-maly-cz.html](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20d%C3%B3za/maly/Golden-Life-Beauty-Longevity-NAD-doza-maly-cz.html)

### 644 — Woman Hormonal balance

- CSS: [golden-life-barvy-woman-hormonal-balance.css](../../user/documents/upload/css/golden-life-barvy-woman-hormonal-balance.css)
- Dlouhý popis: [Golden_Life_Darkovy_box_Hormonal_cz.html](../../web/Golden%20Life%20Woman%20Hormonal%20balance/Golden_Life_Darkovy_box_Hormonal_cz.html)
- Krátký popis: [Golden-Life-Hormonal-maly-cz.html](../../web/Golden%20Life%20Woman%20Hormonal%20balance/maly/Golden-Life-Hormonal-maly-cz.html)

### 635 — Hormonal Balance noční GLP-1 drink

- CSS: [golden-life-barvy-glp1-woman-balance.css](../../user/documents/upload/css/golden-life-barvy-glp1-woman-balance.css)
- Dlouhý popis: [peptides-glp-1-woman-balance-dark-cherry-cz.html](../../web/Golden%20Life%20peptides%20glp-1%20woman%20balance%20dark%20cherry/peptides-glp-1-woman-balance-dark-cherry-cz.html)
- Krátký popis: [peptides-glp-1-woman-balance-dark-cherry-maly-cz.html](../../web/Golden%20Life%20peptides%20glp-1%20woman%20balance%20dark%20cherry/maly/peptides-glp-1-woman-balance-dark-cherry-maly-cz.html)

### 641 — Hormonal Balance noční GLP-1 drink sáček

- CSS: [golden-life-barvy-glp1-woman-balance-sacek.css](../../user/documents/upload/css/golden-life-barvy-glp1-woman-balance-sacek.css)
- Dlouhý popis: [peptides-glp-1-woman-balance-dark-cherry-sacek-cz.html](../../web/Golden%20Life%20peptides%20glp-1%20woman%20balance%20dark%20cherry%20s%C3%A1%C4%8Dek/peptides-glp-1-woman-balance-dark-cherry-sacek-cz.html)
- Krátký popis: [peptides-glp-1-woman-balance-dark-cherry-sacek-maly-cz.html](../../web/Golden%20Life%20peptides%20glp-1%20woman%20balance%20dark%20cherry%20s%C3%A1%C4%8Dek/maly/peptides-glp-1-woman-balance-dark-cherry-sacek-maly-cz.html)

### 550 — Anti-Age longevity NAD+

- CSS: [golden-life-barvy-anti-age-longevity.css](../../user/documents/upload/css/golden-life-barvy-anti-age-longevity.css)
- Dlouhý popis: [Golden-life-Anti-Age Longevity NAD+.html](../../web/Golden%20Life%20Anti-Age%20Longevity%20NAD%2B/Golden-life-Anti-Age%20Longevity%20NAD%2B.html)
- Krátký popis: [Golden-life-Anti-Age Longevity NAD+maly.html](../../web/Golden%20Life%20Anti-Age%20Longevity%20NAD%2B/maly/Golden-life-Anti-Age%20Longevity%20NAD%2Bmaly.html)

### 600 — Beauty Longevity NAD+ sáček

- CSS: [golden-life-barvy-beauty-longevity-sacek.css](../../user/documents/upload/css/golden-life-barvy-beauty-longevity-sacek.css)
- Dlouhý popis: [Golden-Life-Beauty-Longevity-NAD-sacek-cz.html](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20s%C3%A1%C4%8Dek/Golden-Life-Beauty-Longevity-NAD-sacek-cz.html)
- Krátký popis: [Golden-Life-Beauty-Longevity-NAD-sacek-maly-cz.html](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20s%C3%A1%C4%8Dek/maly/Golden-Life-Beauty-Longevity-NAD-sacek-maly-cz.html)

### 168 — Slim Extreme Collagen

- CSS: [golden-life-barvy-slim-extreme-collagen.css](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen.css)
- Dlouhý popis: [Golden Life Slim Extreme Collagen.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen/Golden%20Life%20Slim%20Extreme%20Collagen.html)
- Krátký popis: [Golden Life Slim Extreme Collagen maly.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen/maly/Golden%20Life%20Slim%20Extreme%20Collagen%20maly.html)

### 473 — Slim SOS Burner

- CSS: [golden-life-barvy-slim-sos-fat-burner.css](../../user/documents/upload/css/golden-life-barvy-slim-sos-fat-burner.css)
- Dlouhý popis: [Golden-Life-Slim-SOS-Fat-Burner-cz.html](../../web/Golden%20Life%20Slim%20SOS%20Fat%20Burner/Golden-Life-Slim-SOS-Fat-Burner-cz.html)
- Krátký popis: [Golden-Life-Slim-SOS-Fat-Burner-maly-cz.html](../../web/Golden%20Life%20Slim%20SOS%20Fat%20Burner/maly/Golden-Life-Slim-SOS-Fat-Burner-maly-cz.html)

### 476 — Slim GLP-1 Activator s Berberinem

- CSS: [golden-life-barvy-slim-glp-1-activator.css](../../user/documents/upload/css/golden-life-barvy-slim-glp-1-activator.css)
- Dlouhý popis: [Golden-Life-Slim-GLP-1-Activator-cz.html](../../web/Golden%20Life%20Slim%20GLP-1%20Activator/Golden-Life-Slim-GLP-1-Activator-cz.html)
- Krátký popis: [Golden-Life-Slim-GLP-1-Activator-maly-cz.html](../../web/Golden%20Life%20Slim%20GLP-1%20Activator/maly/Golden-Life-Slim-GLP-1-Activator-maly-cz.html)

### 416 — Slim Extreme Collagen sáček s příchutí ananasu

- CSS: [golden-life-barvy-slim-extreme-collagen-sacek-ananas.css](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-sacek-ananas.css)
- Dlouhý popis: [Golden-Life-Slim-Extreme-Collagen-sacek-ananas-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-cz.html)
- Krátký popis: [Golden-Life-Slim-Extreme-Collagen-sacek-ananas-maly-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas/maly/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-maly-cz.html)

### 464 — Slim Extreme Collagen box s příchutí ananas - mango

- CSS: [golden-life-barvy-slim-extreme-collagen-box-ananas-mango.css](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-box-ananas-mango.css)
- Dlouhý popis: [Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas%20mango/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-cz.html)
- Krátký popis: [Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-maly-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas%20mango/maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-maly-cz.html)

### 467 — Slim Extreme Collagen sáček s příchutí ananas - mango

- CSS: [golden-life-barvy-slim-extreme-collagen-sacek-ananas-mango.css](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-sacek-ananas-mango.css)
- Dlouhý popis: [Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas%20mango/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-cz.html)
- Krátký popis: [Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-maly-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas%20mango/maly/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-maly-cz.html)

## Zdroje a zpracování

- Aktuální vzdálený zdroj: `978e8c038401aa5a33217465170d7ad4be645a66`; finální JS SHA-256 `6e6905ff3144c01e8e30312d723f24d6a9368936b2f602232a393190f58e7d07`.
- Podklady: aktuální Git, skutečné dříve uložené produktové fragmenty a autentické assety, aktuální veřejný SK fragment a tři ověřené PNG. Žádná zákaznická/finanční data.
- Model: GPT‑6.1‑Sol; kontroly Python/Playwright/Chromium. Bez placené tvorby obrázků či videa; náklad modelového běhu nebyl v této úloze vyčíslen.
