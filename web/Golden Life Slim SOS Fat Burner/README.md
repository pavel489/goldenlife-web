# Slim SOS Fat Burner – nová produktová grafika

## Hotové soubory
- [Dlouhý popis](Golden-Life-Slim-SOS-Fat-Burner-cz.html)
- [Krátký popis](maly/Golden-Life-Slim-SOS-Fat-Burner-maly-cz.html)
- [Obecné produktové CSS](../../user/documents/upload/css/golden-life-produkt.css)
- [Barevný model Slim SOS](../../user/documents/upload/css/golden-life-barvy-slim-sos-fat-burner.css)
- [HTML náhled](../../nahledy/slim-sos-fat-burner.html) – otevři stažený soubor v prohlížeči; skutečné obrázky, fonty a shop styly vyžadují internet. GitHub HTML nezobrazuje jako živou stránku.
- [Obrázkový náhled](../../nahledy/slim-sos-fat-burner.png)
- [Testy](../../docs/slim-sos-fat-burner-testy.json) a [regrese sdíleného CSS](../../docs/slim-sos-css-regrese.json)
- [Kontrola původních tvrzení](../../docs/slim-sos-fat-burner-texty.md)

## Výslovná oprava Chromu / Chromium
Ve složení byla opravena pouze jednotka, přesně podle zadání:
- 1 tobolka: **0,55 mcg** místo 0,55 mg.
- 2 tobolky – denní dávka: **1,11 mcg** místo 1,11 mg.

Číselné hodnoty zůstaly stejné. Nejde o matematický převod původních mg na mikrogramy; jde o opravu chybně uvedené jednotky. Stejné mcg jsou v tabulce, přehledech i detailu chromu. Všechny ostatní tabulkové buňky zůstaly obsahově stejné. Původní značení `*% RHP` a poznámka o RHP nebyly při této opravě přepočítávané; jejich správnost je samostatný otevřený produktový podklad, ne ověřené tvrzení této migrace.

## Nový vzhled
Stejný komponentový systém jako nejnovější Woman Hormonal Balance a připravená Beauty Star: banner s rozbalením, hero, fakta, karty s pěti detaily látek, CTA, užívání a tabulka. Vlastní téma `slim-sos-fat-burner`, hlavní barva Slim Pink Strong **#E40E7E** z pracovního brandového manuálu. Produktová identita 473; referenční layout marker neznamená jiný produkt.

Každý CMS popis obsahuje jeden malý style blok a právě dva importy:

```html
<style>
@import url("/user/documents/upload/css/golden-life-produkt.css");
@import url("/user/documents/upload/css/golden-life-barvy-slim-sos-fat-burner.css");
</style>
```

Obecné CSS dostalo pouze malý přídavný opt-in komponent pro třísloupcovou tabulku `data-gl-table="three-columns"`: rozumné šířky sloupců a čitelné mobilní zalamování. Původní obsah CSS zůstal beze změny jako přesný prefix souboru. Pravidlo nematchuje ostatní současné HTML; Beauty Star má pixelově shodný výsledek před/po na mobilu i desktopu.

## Nasazení
1. Nahraj aktuální společné CSS a nové barevné CSS na stejné cesty do e-shopu.
2. Nahraď staré dlouhé a krátké popisy celými HTML, nepřidávej je za staré inline styly.
3. Ponech funkční skript mobilního rozbalování; CSS samo chování neimplementuje.
4. Ověř skutečně uloženou stránku na telefonu i desktopu, jednotky chromu, pět detailů a upozornění.

**Git publikace není nasazení do Shoptetu. V této práci se nic neukládalo v administraci e-shopu.** CTA odkazuje k nativnímu formuláři, neprovádí vlastní nákup ani nevymýšlí cenu/dostupnost. Nákup v náhledu je vypnutý. Soubory jsou doručené přes Git, bez ZIPu.

## Podklady a omezení
- Aktuální veřejný https://www.golden-life.cz/slim-sos-fat-burner/ , native productId 473.
- Skutečná aktuální hlavní fotografie; pro hero je oříznutý pouze prázdný okraj. Produkt nebyl generovaný ani přebarvený. Originál: https://cdn.myshoptet.com/usr/www.golden-life.cz/user/shop/big/473-1_sos-web.png?ff=1&x=1024&y=1024&q=85&ts=6adf0f19&sg=38cb01fe. Ořez je uložený v repozitáři, nikoli závislý na novém uploadu do Shoptetu.
- Existující skutečné fotografie bílých fazolí, řepy, octa a chromu. Jsou ilustrační, nikoli důkaz původu surovin.
- Původní odkazy `[jak-funguje.jpg]`, `[ucinky.jpg]` a `[SOS-chitosan.png]` vracejí 404. Do nového HTML se nepřenášejí rozbité zástupné cesty. Chitosan má plnohodnotný textový detail bez domyšlené fotografie.
- Zůstává produktové upozornění na korýše, děti, těhotné a kojící ženy i pokyny ke skladování. Doplněno obecné povinné upozornění k doplňku stravy.
- Produktový soubor se schválenými formulacemi nebyl dostupný. Původní sliby blokace tuků/cukrů, detoxikace jater či potlačení chutí se proto nepřenášejí jako schválená účinková tvrzení; nové znění uvádí složky a množství. Revize je rozepsaná zvlášť. Autentická etiketa na fotografii nebyla retušovaná; její vlastní účinkové nápisy jsou původní obal, ne dodatečně ověřený claim.
- Kompletní seznam pomocných surovin zdroj neposkytuje; stručný původní seznam pěti složek není vymyšleně rozšířený o další suroviny. Před nasazením ho porovnej s etiketou.
- Původní krátký a dlouhý popis se liší v časování vůči jídlu. Nový krátký uvádí pouze 2 tobolky denně s vodou, dlouhý zachovává původní produktový návod. Časování je potřeba sjednotit podle etikety.
- Při pozdějším vkládání do dárkových boxů je třeba ověřit allowlist názvu nového barevného CSS v jejich loaderu. Boxy nebyly v tomto zadání měněné.

## Skutečné ověření
- Náhled: 320, 360, 390, 520, 767, 768, 1100, 1440 px a návrat na 390 px.
- Skutečné dodané CMS fragmenty se dvěma importy a veřejným shop CSS: 320, 390, 768 a 1440 px, pomocí dočasných lokálních odpovědí na původním originu.
- Bez horizontálního přetečení stránky/banneru, bez rozbitých obrázků, bez JavaScript chyb. Text všech tabulkových buněk měřený pomocí DOM Range – žádný vpravo oříznutý nadpis.
- Tři mobilní rozbalování myší/Enterem, detail banneru a všech pět detailů složek otevřeno/zavřeno. Ověřený návrat mobil–desktop–mobil.
- Přesně dvě změny obsahu tabulky: mg → mcg u chromu; zbytek shodný se zdrojem.
- Nová fotka před Git uploadem testovaná skutečnými připravenými bajty pomocí lokálního response override; po publikaci se samostatně ověřuje skutečná veřejná URL.
- Vizuálně kontrolovaný horní desktop, celá mobilní stránka, aktuální packshot a detail mobilní tabulky.

## Výroba a náklady
Podklady: pravidla značky, pracovní vizuální identita Golden Life, aktuální veřejná stránka Slim SOS Fat Burner, sdílený framework a komponentová reference z Git `main` 68a7bff4553f3b4e35d2832d4eb6eef21c0354da. Model GPT-6.1-sol; Python/BeautifulSoup, Chromium/Playwright, Pillow. Bez placené obrazové nebo video generace. Cenu jazykového modelu nemám vyčíslenou.
