# Slim Extreme Collagen box ananas – aktuální šablona Activator

Pracovní návrh pro přesné SKU **383**, box s 30 sáčky / 240 g, ne dóza 168 ani dárkový set. Referencí této opravy je uživatelem výslovně dodaná aktuální veřejná stránka https://www.golden-life.cz/slim-glp-1-activator-s-berberinem/ a její skutečné HTML, ne pouze sdílený CSS soubor.

## Co je nově podle reference
- Úvodní produktový banner s fakty o ananasovém boxu, denní dávkou a otevíracím blokem „Co je uvnitř“.
- Dvě původní vysvětlující karty; na mobilu úvod i každá z karet mají funkční „Zobrazit více / méně“ se stavem ARIA, na desktopu plný text.
- Šest karet aktivních látek se stručným úvodem a samostatnými otevíracími detaily. Plné původní texty všech šesti látek byly zachovány v detailech, ne nahrazeny dávkováním.
- Blok častých otázek s údaji o tomto konkrétním balení.
- CTA se stejnou strukturou jako reference a odkazem na skutečný nákupní formulář nahoře. Starý mockup nahrazen skutečnou hlavní fotografií z galerie produktu; hero i CTA se synchronizují s nativní galerií pouze při productId 383. Ověřená fotka téhož SKU slouží jako fallback, žádná fotografie Activatoru se nepřenáší.
- Stejně jako aktuální reference neobsahuje CTA pevně zapsanou cenu a „Skladem“, ale odkazuje na aktuální nákupní blok. Změna se netýká cenových dat e-shopu ani nákupní logiky.
- Odstraněna cizí/stará metadata Mango/LactoSpore/Aquamin a nedoložené vložené JSON-LD hodnocení ze starého popisu. Systémová SEO pole ani veřejný e-shop se neměnily.

## Co zůstalo
Původní věcné odstavce, význam sdělení, dvě vysvětlující karty, vlastní piktogramy a všechny tabulky složení ananasového boxu. Každý původní obsahový odstavec mimo nahrazenou CTA byl programově dohledán v novém HTML; tabulky jsou bajtově totožné. Krátký popis se v této opravě neměnil. Tvrzení o účincích tím nejsou právně schválena; předchozí oddělené obsahové výhrady zůstávají relevantní kromě již odstraněných metadat.

Společný golden-life-produkt.css zůstává beze změny. Vlastní barevný model zůstává růžový; odstraněna pouze stará výjimka s ananasovým pozadím CTA, aby CTA odpovídalo aktuální referenci. Jediný malý STYLE blok a přesně dva importy. Žádné berberinové složení, fialová paleta nebo údaje o tobolkách v ananasové stránce.

## Soubory a nasazení
- Dlouhý popis: `Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html`.
- Krátký popis: `maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-maly-cz.html`, v této opravě nezměněný.
- Aktualizované téma: `../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-box-ananas.css`.
- Kontroly: `../../docs/slim-extreme-collagen-box-ananas-css-testy.json`.
- Náhled: `../../nahledy/slim-extreme-collagen-box-ananas-desktop.jpg`, mobilní CTA: `../../nahledy/slim-extreme-collagen-box-ananas-cta-mobil.png`.

**Toto je Git dodávka, ne živé uložení do Shoptetu.** Pro nasazení této verze aktualizuj vlastní barevné CSS a nahraď celý dlouhý popis. Společné CSS ani krátký popis kvůli této opravě není třeba měnit. Po importu ověř veřejnou stránku; dočasný testovací přepis odpovědi není nasazení.

## Provedené testy
Chromium s kompletní skutečnou stránkou e-shopu a dočasným same-origin přepisem dlouhého popisu/tématu; původní shop skripty i nové bootstrapy se provedly při HTML načtení. Šířky 320/390/768/1024/1440 px a návraty desktop–mobil. Bez přetékání a oříznutých tabulkových textů, všechny obrázky načteny. Otevření/zavření všech šesti ingrediencí a bannerového detailu skutečným klikem na desktopu a mobilu. Tři mobilní více/méně přepínače ověřeny v obou stavech. Galerie synchronizována se dvěma skutečnými načtenými snímky téhož produktu; záměna nativního ID za jiný produkt vede na vlastní fallback; odebrání a opožděné vrácení nativních obrázků ověřeno. Nákupní odkaz otestován bez odeslání košíku. Žádné JavaScriptové chyby při finálním průchodu. Prezentanční widgety skryty pouze v testovací záložce.

## Výroba
Zdroje: výslovně dodaná veřejná referenční stránka Activator, současná veřejná stránka cílového SKU, aktuální Git main, vlastní tabulky a produktový soubor ananasového boxu a brand/RULES.md. Model GPT-6.1-sol; Python/BeautifulSoup a Chromium/Playwright. Bez placené obrazové generace; cenu provozu jazykového modelu nemám k dispozici. Náhledy jsou skutečné snímky renderu, nikoli generované produktové fotografie.
