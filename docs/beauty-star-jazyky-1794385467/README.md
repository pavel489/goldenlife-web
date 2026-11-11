# Beauty Star — jazykové pracovní verze SK / EN / DE

Produkt **Beauty Star ID351**, nikoli Duo. Dlouhý a krátký popis podle aktuální české grafické struktury.

- **Slovenština**: [dlouhý popis](../../web/Golden%20Life%20Beauty%20Star/Golden-Life-Beauty-Star-sk.html) · [krátký popis](../../web/Golden%20Life%20Beauty%20Star/maly/Golden-Life-Beauty-Star-maly-sk.html)
- **Angličtina**: [dlouhý popis](../../web/Golden%20Life%20Beauty%20Star/Golden-Life-Beauty-Star-en.html) · [krátký popis](../../web/Golden%20Life%20Beauty%20Star/maly/Golden-Life-Beauty-Star-maly-en.html)
- **Němčina**: [dlouhý popis](../../web/Golden%20Life%20Beauty%20Star/Golden-Life-Beauty-Star-de.html) · [krátký popis](../../web/Golden%20Life%20Beauty%20Star/maly/Golden-Life-Beauty-Star-maly-de.html)

[Samostatný offline náhled](nahled-jazykove-mutace.html) — stáhnout Raw HTML a otevřít lokálně. [Obrázkový přehled](jazykove-mutace-prehled.png).

## Co je přeložené
Celý úvodní zelený banner i rozbalení, plné významové texty a všech pět ingredienčních dialogů, FAQ, složení, dávkování, upozornění, popisky obrázků/přístupnost a mobilní tlačítka. Technické identifikátory, zdrojové fotografie, CSS importy a logika zůstávají. Skripty hlavní fotografie a detekce okolního pozadí jsou byte-identické, mobilní JS obsahuje pouze lokalizované texty a odpovídající nadpisový regulární výraz.

Český zdroj: `90a7dc7acfe0ad17c6e5f2fbc31bc32d2149e5f7`. Zdrojové SHA v [manifestu](source-manifest.json). Jazyky odpovídají skutečným hreflang odkazům vlastního SKU na veřejné stránce (HTTP200 během této úlohy).

## Důležité před použitím
**Pracovní překlad, ne schválení k živé publikaci.** Věrně zachovává zděděné formulace; jejich publikace vyžaduje revizi. Přesná česká znění i cílové překlady jsou vedle sebe v [revizi tvrzení](claims-review.csv) a podrobných jazykových inventářích. Problematické jsou zejména akné, růst/vypadávání vlasů a obecné sliby hormonální rovnováhy. Automatická sekce „EFSA“ produktového souboru sama není právním potvrzením; i její formulace jsou sporné, proto je nevydáváme za schválené alternativy.

**Rozpor podkladů:** dlouhý popis uvádí **65 g**, krátký a produktový podklad **30 g**. Překlad zachovává původní hodnoty pro kontrolu, neřeší rozpor odhadem. Čísla složení, dávka 2 hvězdičky a jednotky zůstávají stejné. Žádné nové cenové/skladové sliby nejsou přidány. V anglickém krátkém popisu je navíc povinný obecný disclaimer převzatý z dlouhého popisu; slovenský a německý pár jej obsahují v dlouhém popisu. Německé dlouhé popisky obsahují typografické volitelné dělení slov, aby se na telefonu nepřekrývaly; CSS zůstává beze změny.

## Ověření skutečného výstupu
- Statické kontroly **6/6 HTML**: plné počty textových uzlů, tabulky/čísla, CSS a technické atributy, AST logika a syntaxe všech skriptů.
- **72/72 scénářů**: telefon 390 px, 767/768 px, tablety 820×1180 a 1024×768, desktop 1440 px; světlé/tmavé okolí nezávisle na preferenci systému.
- **72 otevření/zavření dialogů** a **18 mobilních přepnutí** skutečným kliknutím.
- Samostatný HTML prohlížeč **16/16 stavů**; všechny skutečné vložené obrázky dekódované, žádné JS chyby ani externí síťové požadavky v offline QA.
- Offline náhled jako jediný nastavuje příznak již připravené fotografie a skrývá neaktivní nativní cenu. V produkčních souborech zůstávají původní URL a původní synchronizace.
- Není to test fyzického iPadu/Safari/Opery ani živého CMS importu či košíku.

## Přenos
HTML stále používá stejné společné `golden-life-produkt.css`, vlastní `golden-life-barvy-beauty-star.css?v=host-bg-1` a `golden-life-product-scheme.js?v=host-bg-1`. Pro nasazení musí existovat na očekávaných adresách. V této úloze se závislosti ani české HTML nemění. **Zápis do Gitu není nasazení do Shoptetu. Živý e-shop nebyl měněn.**

Podklady: aktuální párové české HTML z Gitu, vlastní veřejné hreflang ID351, pravidla a produktový soubor; autentické archivované a stažené obrázky/fonty pro izolovaný náhled. Model GPT‑6.1‑sol, skutečné testy Node/Acorn a Chromium/Playwright. Bez placené obrazové generace; cenu modelového běhu nemáme vyčíslenou.
