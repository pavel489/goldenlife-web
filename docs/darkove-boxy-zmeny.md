# Dárkové boxy — cílené funkční a mobilní úpravy

Změny navazují na původní návrhy a odsouhlasenou ukázku Collagen Beauty, nikoli na dřívější plošný redesign. Upraveny jsou dlouhé i krátké popisy všech pěti boxů: Beauty, Hormonal, Longevity, Slim/Mango a UFIRST. Původní názvy souborů, produkty, texty produktových karet, zlaté provedení a cesty fotografií zůstávají zachované. Fotografie bude vlastník dohrávat.

## Hotové úpravy
- Kompaktnější mobilní karty, čitelnější ovládání a lepší zarovnání textů.
- Vložené SVG místo Material Symbols: tyto popisy nepotřebují stahovat externí ikonový font.
- Pět lokálních rozbalovacích detailů v každém boxu namísto importu celých dalších stránek. Otevření detailu neprovádí produktový AJAX.
- Přímé odkazy jen na ověřené odpovídající stránky. Nejasné nebo neexistující cíle nejsou nahrazené odhadnutou URL; místní popis funguje i bez ní.
- Navigace na obsah, stručné FAQ pro konkrétní box a rekapitulace po obsahu.
- Podrobný seznam v krátkém popisu je volitelně rozbalitelný.
- Cena a dostupnost navazují na hlavní produkt. Nevkládá se pevné „Skladem“, nulová/neznámá cena se v duplicitním bloku nezobrazuje.
- Odstraněno vlastní neúplné Product JSON-LD s pevným InStock; nativní strukturovaná data Shoptetu se nepřepisují.
- CSS je omezené na popis. Rozbalování podporuje klávesnici, focus je viditelný a respektuje se omezený pohyb.

## Bezpečné nákupní napojení
**Beauty:** ověřené Shoptet productId `656`. Když je hlavní nákupní tlačítko dostupné a produkt není vyprodaný, komponenta aktivuje právě je; nemění množství.

**Hormonal, Longevity, Slim/Mango, UFIRST:** jejich skutečná Shoptet ID nebyla doložena. Není v nich zkopírované ID Beauty. Tlačítko „Přejít k nákupu“ přejde k nativnímu nákupnímu tlačítku hlavního produktu; zákazník nakoupí tam. U vyprodání přejde na dostupnost. Cena a stav se čtou z hlavního formuláře. Samostatný náhled bez hostitelského produktu nákup neaktivuje.

Po ověření konkrétního produktu lze u příslušného dlouhého popisu vyplnit `data-gl-product-id` na kořenovém elementu. Teprve shoda s hlavním formulářem dovolí přímé přidání do košíku; jiné ID jej zablokuje. Žádná ID se nemají odhadovat. Integraci následně otestovat na skutečné stránce, zejména varianty, dostupnost a množství.

## Zbývající podklady
- Fotografie, finální ceny, skutečné balení/počty a produktová upozornění podle vašich připravovaných podkladů.
- Samostatné přesné cíle pro USB míchátko, ananasový/mangový kolagen a správnou prodejní jednotku Beauty & Longevity NAD+. Místní rozbalovací informace fungují, ale nejsou úplnou specifikací či složením.
- Název Slim/Mango není automaticky přejmenován.

## Co tento commit nedělá
- Nenasazuje obsah do administrace ani živého e-shopu.
- Nemění globální `main.js`, import homepage, cookie panel, newsletter ani globální sticky košík. Tyto části šablony nejsou mezi dodanými produktovými HTML. Z tohoto commitu tedy nelze odvozovat diagnostickou úsporu 57 % přenosu ani lepší naměřené LCP.
- Nepřepisuje původní zdravotní tvrzení na kartách ani je právně neschvaluje. Formulace o detoxikaci, spalování, aktivaci GLP-1, hormonální rovnováze, paměti a podobných účincích nadále vyžadují kontrolu pro konkrétní SKU. V dostupných podkladech nejsou odpovídající schválené náhrady pro všechny tyto formulace. Neutrální alternativou je popis formy, obsahu a příchuti, ne vymyšlené „schválené“ synonymum.

## Náhled a ověření
`nahledy/darkove-boxy.html` otevři lokálně v prohlížeči. Přepíná všech pět boxů, původní/novou a dlouhou/krátkou verzi. Původní stav je bezpečná statická reference; jeho staré síťové skripty se nespouštějí. Náhradní obrázky Shoptetu jsou jen v náhledu, ne změnou produkčních cest fotografií.

Výsledky jsou v `tests/darkove-boxy-results.json`: 10 HTML na 4 šířkách (320, 390, 768, 1440 px), všech 20 srovnávacích pohledů, klávesnice, detaily a lokální simulace nákupních stavů. Bez JS chyb a bez externích HTTP požadavků v offline náhledu. Ověřeno zachování původních produktových textů i cest obrázků.

Nákupní testy jsou výslovně syntetické lokální formuláře, ne živá objednávka. Pilot Beauty byl navíc ověřen ve stažené skutečné Shoptet šabloně upravené pouze v izolovaném prohlížeči. Před nasazením je potřeba integrační kontrola konkrétních stránek.

Dlouhé soubory zachovávají původní formát samostatného HTML dokumentu; při vkládání do Shoptetu použij komponentu a její style/script, ne druhý head/body dokument. Krátké popisy jsou fragmenty.

Podklady: původní HTML a veřejné produktové stránky. Zpracování: GPT-6 Astra, Python/BeautifulSoup/tinycss2, Playwright/Chromium a vizuální kontrola. Nebylo použito placené generování fotografií. Cena modelového zpracování není v nástrojích vyčíslená.
