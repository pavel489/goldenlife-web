# Dárkové boxy — globální CSS a sdílená odnož

## Rozsah
Všech pět boxů: Beauty, Hormonal, Longevity, Slim, UFIRST. Dlouhé i krátké české popisy v `web/` a jejich odpovídající CMS fragmenty v `shoptet/`: celkem 20 HTML souborů. Texty, obrázkové URL, produktové identity a skripty zůstaly zachované. Není to nový design ani nové schválení dřívějších zdravotních tvrzení.

## Architektura
HTML importuje nejprve `/user/documents/upload/css/golden-life-produkt.css` stejně jako ostatní novější produktové stránky. Používá existující rozhraní `data-gl-product` a `data-gl-layout="woman-hormonal-balance"`, u krátkého popisu `woman-hormonal-balance-short`. Jde o názvy existujícího rozvržení, nikoli změnu produktu/SKU. Původní `gl-box-refined`, `gl-box-short` a ID zůstávají kvůli funkčním skriptům.

Za základním CSS se importuje jediná společná odnož `assets/golden-life-darkove-boxy.css`. Nemá kopii globálních typografických ani hero/CTA pravidel. Obsahuje barevné tokeny obou značek, specifika neřezaných packshotů, čtečky detailů, obalové karty, ovládání, SVG pásu a původního dárkového informačního boxu. Úpravy jsou omezené na dárkové komponenty. Běžné produktové stránky se nemění. V krátkých popisech byly i jednotlivé atributy `style` nahrazeny společnými třídami; zůstává nula inline stylových atributů.

Globální CSS určuje typografii, rytmus odstavců, kontejnery, základní hero a jeho ikony, obecné produktové karty, CTA a základ krátkého popisu. Test skutečně odstraňuje jeho import a potvrzuje změnu hero z gridu na block; nejde o neúčinný import vedle celé původní kopie stylů.

Velikost celé sdílené odnože: 18202 B, modelový gzip 3912 B. To je jedna mezipamětí sdílená závislost, ne samostatná kopie pro každý box. Nejde o měření celkové rychlosti stránky: stávající globální CSS je větší soubor a záleží na jeho mezipaměti.

## Publikovaná závislost
Odnož je veřejně dostupná a připnutá ke konkrétní revizi `d2e913cddda836da9ff9b3543c4ac58d1912d7d9`:

https://cdn.jsdelivr.net/gh/pavel489/goldenlife-web@d2e913cddda836da9ff9b3543c4ac58d1912d7d9/assets/golden-life-darkove-boxy.css

HTTP 200 a stažené bajty byly ověřené proti místnímu souboru. Importy již neobsahují zástupný commit. Kvůli samotnému Git předání není potřeba nejprve nahrávat CSS do Shoptetu. Jestli se CSS později přesune na firemní host, změnit jen importy; netvořit další lokální kopie pravidel. Při změně odnože nejprve publikovat a ověřit novou revizi a teprve pak aktualizovat pin.

## Ověření
- 20/20 souborů: zachované texty, skripty, obrázkové URL, odkazy a identity; změny jen ve stylování a routovacích atributech.
- 60/60 případů v Chromium: pět boxů × krátký/dlouhý popis × 320, 360, 600, 768, 1024, 1280 px. Bez horizontálního přetékání a bez JS výjimek.
- Dalších 20/20 případů při 360/1280 px používá skutečné veřejné globální CSS a skutečnou CDN odnož, nikoli lokální náhrady stylesheetů.
- Pět ikon v jednom řádku, rozbalení pěti produktů, šestá obalová karta, pět tlačítek detailů, FAQ, zachované `object-fit: contain`; čtečka byla otevřena reálným kliknutím a načetla veřejný detail u všech pěti boxů. Žádné zápisy do košíku.
- Vizuálně zkontrolované kontaktní přehledy všech pěti variant na mobilu a desktopu; fixture používá neutrální host a bez vlastní licence/hostovaných fontů může spadnout na Arial. Není to screenshot uloženého Shoptetu.

## Známé původní zdrojové problémy
Některé původní obrázkové URL se v testu nenačetly. URL byly zachované přesně, nejde o obrázky změněné CSS refaktoringem. V tomto zadání nejsou nahrazovány vymyšlenou fotografií:
- https://cdn.myshoptet.com/usr/www.golden-life.cz/user/shop/big/476-1_glp-1-tabletky-vyzualizace-pozadi.png?ff=1&x=1024&y=1024&q=85&ts=6a17fe9d&sg=38cb01fe
- https://www.golden-life.cz/user/documents/upload/mockup/darkovy-box-hormonal.png
- https://www.golden-life.cz/user/documents/upload/mockup/darkovy-box-longevity.png
- https://www.golden-life.cz/user/documents/upload/mockup/darkovy-box-mango.png
- https://www.golden-life.cz/user/documents/upload/mockup/darkovy-box-ufirst.png
- https://www.golden-life.cz/user/documents/upload/mockup/darkovy-box.png

Při následném nasazení do Shoptetu je třeba ověřit skutečnou hostitelskou stránku a její galerii. Tento commit nic neukládá do administrace Shoptetu a nemění původní globální CSS na e-shopu.

## Zdroje, nástroje a náklady
Výchozí Git revize `c890145800a33b4ff7117d84f9ba7f2193a920f4`; živé veřejné `golden-life-produkt.css` (URL a SHA-256 jsou v `tests/giftbox-global-css-results.json`); `brand/RULES.md`; existující vzor Beauty Star používající globální styl. Model GPT-6.1-sol, Python/tinycss2/lxml a Chromium/Playwright. Bez placené generace médií; přesná cena modelu a konektoru není poskytovaná. Repo publikováno jako ověřená bot identita přes existující Composio GitHub spojení.
