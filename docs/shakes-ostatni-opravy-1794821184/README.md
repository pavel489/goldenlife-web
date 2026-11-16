# Stejné grafické opravy pro další svačinky

## Hotový rozsah
Aplikováno na zbývající samostatné české příchutě **cappuccino (547)** a **vanilka–jahoda (458)**. Kokos–bílá čokoláda slouží jako již opravený referenční vzor a není v tomto commitu znovu měněna. Sestavy/Duo a jiné jazyky nejsou součástí zadání.

U obou příchutí:
- Stejný obrysový fialový plamen jako u kokosu, v dlouhém i krátkém popisu. Reálný transparentní PNG z ověřené neměnné HTTPS revize; bez nové placené generace.
- „Co vám přinese“ obsahuje devět bodů, na desktopu 3×3. Původních osm je zachováno; devátý bod mluví o vlastní příchuti a svačinovém rituálu, nepřidává zdravotní slib.
- „Kdy naše zákaznice sahají po naší svačince?“ obsahuje devět karet, na desktopu 3×3. Původních pět je zachováno; doplněné situace cestování / mezi schůzkami / práce z domova / zpestření svačin jsou ilustrační situace, nikoli předstírané zákaznické citace.
- „Jak funguje“ má původní fotografii a celý vlastní text každé příchutě. Text je vložen do jednoho wrapperu, na desktopu vedle fotky a na telefonu pod ní, zarovnaný vlevo. Není nahrazen textem kokosové varianty.
- „Jak užívat“ je vystředěné a grid odpovídá skutečnému počtu ikon. **Vanilka–jahoda má čtyři sloupce; cappuccino má pět původních ikon včetně „Bez kofeinu“, proto zůstává pět sloupců.** Žádná původní ikona nebyla odstraněna jen kvůli počtu.
- Původní tabulky, dávkování, produktové fotografie, ingredienční karty a úplné dialogy i původní produktové skripty jsou beze změny. Žádné interní review upozornění není přidáno do zákaznického HTML.

## Co převzít do e-shopu
Připravené jsou čtyři HTML soubory a dvě vlastní CSS:

- `web/Golden Life Slim GLP-1 Shake cappuccino/Golden-Life-Slim-GLP1-Shake-cappuccino-cz.html`
- `web/Golden Life Slim GLP-1 Shake cappuccino/maly/Golden-Life-Slim-GLP1-Shake-cappuccino-maly-cz.html`
- `user/documents/upload/css/golden-life-barvy-slim-glp1-shake-cappuccino.css`
- `web/Golden Life Slim GLP-1 Shake vanilka-jahoda/Golden-Life-Slim-GLP1-Shake-vanilka-jahoda-cz.html`
- `web/Golden Life Slim GLP-1 Shake vanilka-jahoda/maly/Golden-Life-Slim-GLP1-Shake-vanilka-jahoda-maly-cz.html`
- `user/documents/upload/css/golden-life-barvy-slim-glp1-shake-vanilka-jahoda.css`

**K nasazení patří HTML i vlastní CSS**, ne jen jeden z těchto typů. Oba popisy mají aktualizovanou cache verzi importu `shakes-layout-20261116`. Společné `golden-life-produkt.css` a `golden-life-product-scheme.js` se nemění. Git předávka není uložení do živé administrace Shoptetu.

## Skutečně provedené ověření
Chromium/Playwright s aktuálním veřejným snapshotem každé přesné produktové stránky. V testovacím response override je vložen celý přesný výsledný dlouhý a krátký fragment, včetně skutečně spuštěných skriptů; načítá se celé výsledné produktové CSS. Živý CMS nebyl měněn.

- Dva produkty, osm viewport průchodů na každý: 1440×1050, 1024×768, 820×1180, 768×1024, 767×1024, 390×844, 320×740, návrat na 1440×1050. Celkem **16 průchodů**.
- V každém průchodu přesně devět přínosů a devět situačních karet; plná šířka a levé zarovnání všech odstavců „Jak funguje“, žádný horizontální přesah dokumentu.
- Počet sloupců užívání roven skutečnému počtu ikon, jediný řádek a geometricky ověřené vystředění celého bloku. Oba plameny v párově vloženém dlouhém/krátkém popisu skutečně načtené.
- Skutečný pointer test všech devíti ingredienčních dialogů u každého produktu: **18 otevření a zavření**, plus oba horní informační panely. Žádné JS výjimky.
- Porovnáním zdrojů ověřeno zachování všech tabulkových buněk (90 u každé příchuti), úplných dialogů, skriptů a původních vysvětlujících odstavců.
- Ověřený PNG: HTTP 200, image/png, CORS a shoda skutečných bajtů s již dodanou kresbou. Načten také v běžícím nativním shopovém prostředí.
- Finální desktopové přehledy a mobilní sekce vizuálně kontrolované. Plovoucí košík/consent/externí widgety skryté pouze pro čisté screenshoty; produkční soubory jejich chování nemění.
- Výstupní skripty z HTML prošly `node --check`. Nebylo přidáno interní upozornění do produktového obsahu.

## Oddělená kontrola původních tvrzení
Tato předávka řeší grafiku a požadované počty karet, **není schválením původních účinkových tvrzení**. Oba vlastní produktové soubory v `brand/product/` uvádějí, že nemají doložené schválené zdravotní znění. Nelze tedy dodat vymyšlenou „schválenou“ náhradu. Níže jsou konkrétní obavy a neutrální faktické návrhy k redakčnímu rozhodnutí, nikoli právní schválení:

- „Potlačení chuti k jídlu a lepší kontrola hladu.“, „Efektivní spalování tuků a podpora redukce hmotnosti.“ a „Dlouhodobý pocit sytosti díky micelárnímu kaseinu.“ jsou účinková tvrzení. Neutrální návrh podle tabulky: „20,3 g bílkovin v jedné 30g dávce.“
- „Zdravá střevní mikroflóra díky probiotikům LactoSpore®.“ a „Podpora trávení a metabolismu díky směsi 7 enzymů OPTI7DIGEST®.“: neověřené účinkové znění. Neutrálně: „Obsahuje LactoSpore®.“ / „Obsahuje směs enzymů OPTI7DIGEST®.“
- „Energie, imunita a vitalita díky 12 bioaktivním vitamínům.“ neuvádí ověřené konkrétní znění u živiny. Neutrálně: „S vitamíny uvedenými v tabulce složení.“
- „Omlazení pokožky, vlasů a nehtů díky bioaktivním kolagenním peptidům.“: účinek kolagenu není doložen schváleným produktovým zněním. Neutrálně: „4 g kolagenních peptidů v jedné dávce.“
- „Rychlá rehydratace a doplnění minerálů díky Aquamin® s více než 72 prvky.“: neověřený účinek/počet. Neutrálně: „100 mg Aquamin® Soluble v jedné dávce.“
- Sekce „Jak funguje“ a původní situační karty obsahují další neověřené sliby (např. 27% snížení vstřebávání tuků, ochrana kloubů/šlach, sedmihodinová sytost, zastavení hladu, spalování tuků). Zachovány v původním znění, nikoli schváleny. Neutrální směr: vlastní složky a ověřené tabulkové dávky.
- „Bez cukru“ ve stávající užívací ikoně odporuje údajům 8 g cukrů / 100 g a 2,4 g / 30 g. Faktická alternativa: „2,4 g cukrů v dávce“. V tomto grafickém zásahu nebyla potichu měněna ikona ani její popisek.
- Probiotické množství: původní texty uvádějí 8,9 mld. CFU, zdrojové tabulky 0,75 mld. KJT v dávce. Rozpor zůstává k potvrzení, nikoli náhodnému přepsání.

## Podklady a výroba
Aktuální Git `95e88725a8b59df8303107e3d5ca153f6c2fb128`, předchozí kokosová oprava, skutečné veřejné stránky obou příchutí, `brand/RULES.md`, vlastní produktové soubory pro cappuccino a vanilka–jahoda. Model GPT‑6.1‑sol, HTML/CSS a Chromium/Playwright. Použita již hotová linková kresba plamene; žádná placená obrazová generace. Cena modelového běhu není vyčíslená.
