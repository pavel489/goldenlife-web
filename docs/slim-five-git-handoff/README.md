# Pět produktů Golden Life — podklady pouze pro Git

Zdroj: aktuální `main` ověřený na `13dacd419a906a203c168eb53acd042ba6c5cfd5`.
Všech pět produktů už v tomto commitu obsahuje novou společnou šablonu v krátkém i dlouhém popisu. Nejde o nově provedený redesign. Při nové kontrole byly nalezeny a opraveny konkrétní nedostatky níže. Nový commit obsahuje pouze tyto dokončovací opravy a předávací evidenci, nikoli nový návrh již hotových šablon.
Živý Shoptet nebyl upravován. Předchozí seznam zastaralého designu popisoval živý web, ne nepřipravenost těchto souborů na Gitu.

## Soubory

### Slim & Detox Super energy booster Power+ · ID 174
- Dlouhý popis: [web/Golden Life Slim Detox Power Plus/Golden-Life-Slim-Detox-Power-Plus-cz.html](../../web/Golden%20Life%20Slim%20Detox%20Power%20Plus/Golden-Life-Slim-Detox-Power-Plus-cz.html)
- Krátký popis: [web/Golden Life Slim Detox Power Plus/maly/Golden-Life-Slim-Detox-Power-Plus-maly-cz.html](../../web/Golden%20Life%20Slim%20Detox%20Power%20Plus/maly/Golden-Life-Slim-Detox-Power-Plus-maly-cz.html)

### Slim Extreme Collagen box s příchutí ananasu · ID 383
- Dlouhý popis: [web/Golden Life Slim Extreme Collagen box ananas/Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas/Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html)
- Krátký popis: [web/Golden Life Slim Extreme Collagen box ananas/maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-maly-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas/maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-maly-cz.html)

### Slim Extreme Collagen box s příchutí ananas - mango · ID 464
- Dlouhý popis: [web/Golden Life Slim Extreme Collagen box ananas mango/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas%20mango/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-cz.html)
- Krátký popis: [web/Golden Life Slim Extreme Collagen box ananas mango/maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-maly-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas%20mango/maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-maly-cz.html)

### Slim Extreme Collagen sáček s příchutí ananasu · ID 416
- Dlouhý popis: [web/Golden Life Slim Extreme Collagen sacek ananas/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-cz.html)
- Krátký popis: [web/Golden Life Slim Extreme Collagen sacek ananas/maly/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-maly-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas/maly/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-maly-cz.html)

### Slim Extreme Collagen sáček s příchutí ananas - mango · ID 467
- Dlouhý popis: [web/Golden Life Slim Extreme Collagen sacek ananas mango/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas%20mango/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-cz.html)
- Krátký popis: [web/Golden Life Slim Extreme Collagen sacek ananas mango/maly/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-maly-cz.html](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas%20mango/maly/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-maly-cz.html)

## Dokončovací opravy
- Power+ 174: odstraněn druhý malý mockup v CTA; hlavní fotografie a její synchronizace zachovány.
- Box ananas 383: doplněno zavírání informačních a ingredient dialogů Escape a ovládání fokusu podle sourozence 416.
- Mango box/sáček 464/467: interní historické/conflict bloky a redakční formulace odstraněny ze zákaznického HTML a přesunuty do `fixes-ledger.json`. Vlastní příprava boxu, ingredientové modaly a tabulky zachovány. Sporné gramáže nejsou nahrazovány odhadem.
- Ostatní části, účinkové texty, společné CSS a nákupní logika se nepřepisovaly.

## Kontrola
- Ověřeno: 5 samostatných produktových ID, 10 HTML souborů a 6 CSS závislostí; shoda Git blob SHA proti aktuálnímu vzdálenému commitu.
- Všechny inline JavaScript bloky prošly skutečným `node --check`.
- Samotná přítomnost šablony není schválením textů ani nasazením CSS do Shoptetu. Výsledky konečné kontroly opravených zdrojů jsou v `qa-summary.json`; původní audit před opravami není vydáván za kontrolu finálních bytů.

## Obsahové výhrady — odděleně od grafiky
Původní účinkové texty zůstávají pracovními podklady k revizi. Tato příprava neschvaluje zdravotní tvrzení.
- Power+ (174): „Extrémní spalování tuků“ a „Podpora detoxikace“ nejsou doložené schváleným ekvivalentem v jeho produktovém souboru. Neutrální návrh: „Rostlinné extrakty, L-karnitin a taurin.“
- Collagen (383/416/464/467): „Podpora hubnutí i bez cvičení“, „Spalování tuků“, „Redukce celulitidy“ či „Redukce vrásek“ nejsou schválené grafickou migrací. Neutrální návrh: „Kolagenový nápoj s příchutí ananasu“ nebo „Kolagenový nápoj s příchutí ananasu a manga“ podle varianty.
- Vlastní produktové soubory 416 a 464 obsahují kandidátní znění: „Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.“ Před veřejným použitím je nutné potvrdit příslušnou recepturu, množství a podmínky tvrzení. Nepřenášet na 467 bez vlastního podkladu.
- Zdrojové rozpory 8/8,2 g, objem vody a balení manga se neřeší odhadem.

Podrobné dřívější revize v repozitáři:
- `docs/collagen-varianty-krok-4d-obsahove-vyhrady.md`
- `docs/slim-extreme-collagen-box-ananas-obsahove-vyhrady.md`
- `docs/samostatne-produkty-13/obsahove-vyhrady.md`

## Limity předání
Jen Git, bez ukládání do Shoptetu či publikace na e-shopu. Browser harness načítá přesné finální HTML/CSS i repository appearance JS. Nativní galerie, cena, dostupnost, nákup, hostitelské Shoptet CSS a CMS transformace nejsou tímto ověřené. V původním běhu se veřejný appearance JS hashově lišil od Git kopie; kvůli tomu používá finální Git-only kontrola přesné repository JS. To není automatický důkaz runtime chyby.

## Provenience
Použito brand/RULES.md, vlastní dostupné produktové info.md, přesná existující Git HTML/CSS a předchozí produktové revize. Model gpt-6.1-sol; bez placené obrazové generace. Cena modelu/nástrojů není vyčíslená.