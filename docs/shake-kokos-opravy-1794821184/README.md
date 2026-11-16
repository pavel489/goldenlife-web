# Slim GLP‑1 Shake kokos – bílá čokoláda: cílené grafické opravy

Stav: připravené a v prohlížeči ověřené pracovní HTML/CSS. **Nejde o uložení do živého Shoptetu ani o schválení účinkových tvrzení.**

## Rozsah
- V dlouhém i krátkém popisu je původní plný piktogram spalování nahrazen nově nakresleným obrysovým plamenem. Fialová #62388E, oblé konce/spoje, transparentní PNG 256×256 a editovatelný SVG master. Bez nového obvodového kruhu; okolí nadále řídí CSS.
- „Co vám přinese“: zachováno původních osm položek, přidána devátá „Kokosovo-čokoládová chuť pro příjemnější svačinový rituál.“
- „Kdy naše zákaznice sahají po naší svačince?“: zachováno původních pět karet, přidány čtyři ilustrační situace — cestování, pauza mezi schůzkami, práce z domova, zpestření svačin. Nejde o skutečné zákaznické citace nebo výzkum. Nové karty používají vykání; původní dodaná redakce zůstala beze změny.
- „Jak funguje“: původní obrázek a všech pět plných odstavců zachováno. Nadpis a text jsou ve vlastním textovém bloku, na počítači vedle fotografie, na mobilu pod ní. Zarovnání vlevo místo roztaženého textu v samostatných úzkých sloupcích.
- „Jak užívat“: přesně čtyři stávající piktogramy, čtyři sloupce a vystředěný celý blok i jednotlivé symboly/popisky.

## Příčina reprodukované chyby
Na skutečné veřejné stránce měl `.shake-compare-block` `display:flex`; obrázek, nadpis a jednotlivé odstavce byly přímí sourozenci. Každý se stlačil do samostatného úzkého sloupce (odstavce přibližně 80–128 px v desktopovém měření). Oprava přidává jediný wrapper a produktově omezený dvousloupcový grid.

## Nasazované soubory
- `web/Golden Life Slim GLP-1 Shake kokos-bila-cokolada/Golden-Life-Slim-GLP1-Shake-kokos-bila-cokolada-cz.html`
- `web/Golden Life Slim GLP-1 Shake kokos-bila-cokolada/maly/Golden-Life-Slim-GLP1-Shake-kokos-bila-cokolada-maly-cz.html`
- `user/documents/upload/css/golden-life-barvy-slim-glp1-shake-kokos-bila-cokolada.css`

Je potřeba převzít oba popisy **i vlastní barevné CSS**. Oba importy mají novou cache verzi `kokos-layout-20261116`. Společné CSS a společný JS jsou beze změny. PNG se načítá z ověřené neměnné HTTPS revize GitHubu; SVG není vkládáno jako nutný CMS upload.

## Ověření
- Chromium/Playwright: skutečný veřejný HTML snapshot stránky a její běžné skripty, pouze testovací nahrazení cílového popisu a kompletního produktového CSS. Není to live CMS save.
- Sedm viewport průchodů: 1440×1050, 1024×768, 820×1180, 768×1024, 390×844, 320×740 a návrat na 1440×1050.
- V každém průchodu přesně 9 přínosů, 9 situací, 4 užívací piktogramy; žádný horizontální přesah dokumentu. Na desktopu oba obsahové gridy 3×3; užívání vždy čtyři sloupce.
- Ověřena plná šířka všech odstavců v textovém sloupci a jejich zarovnání vlevo, rovnováha čtyř ikon kolem středu.
- Devět otevření/zavření původních ingredienčních dialogů, otevření/zavření horního informačního panelu. Bez JavaScriptových výjimek.
- Beze změny všechny tabulkové buňky, úplné ingredienční dialogy, původní odstavce „Jak funguje“ a původní produktové skripty. Původní fotografie zachované.
- Veřejné HTTPS PNG ověřeno status/MIME/CORS a porovnáním skutečných bajtů, následně načteno v obou popisech v běžícím prohlížeči.
- Finální desktopové a mobilní snímky vizuálně prohlédnuté. Plovoucí košík, recenze, consent a chat byly skryty jen v testovacím screenshotu, nikoli v produkčních souborech.

## Samostatná obsahová výhrada před nasazením
Původní účinkový text je zachován podle grafického zadání, nikoli prohlášen za schválený. Produktový soubor `brand/product/svacinka-slim-glp-1-shake-s-prichuti-kokos-bila-cokolada/info.md` **neobsahuje ověřená schválená zdravotní tvrzení**. Nelze tedy vedle problémů poctivě uvést schválené produktové znění; následující alternativy jsou neutrální faktické návrhy, ne právní schválení.

- „Efektivní spalování tuků a podpora redukce hmotnosti.“, „Potlačení chuti k jídlu a lepší kontrola hladu.“, „Dlouhodobý pocit sytosti díky micelárnímu kaseinu.“: účinková tvrzení, nutná samostatná kontrola. Neutrální návrh: „20,3 g bílkovin v jedné 30g dávce.“
- „Zdravá střevní mikroflóra díky probiotikům LactoSpore®.“ a „Podpora trávení a metabolismu díky směsi 7 enzymů OPTI7DIGEST®.“: účinková tvrzení. Neutrální návrhy: „Obsahuje LactoSpore®.“ a „Obsahuje směs enzymů OPTI7DIGEST®.“
- „Energie, imunita a vitalita díky 12 bioaktivním vitamínům.“: chybí ověřené přesné znění u konkrétního vitaminu. Neutrální návrh: „S vitamíny uvedenými v tabulce složení.“
- „Omlazení pokožky, vlasů a nehtů díky bioaktivním kolagenním peptidům.“: neověřený účinek kolagenu. Neutrální návrh: „4 g kolagenních peptidů v jedné dávce.“
- „Rychlá rehydratace a doplnění minerálů díky Aquamin® s více než 72 prvky.“: neověřené účinkové a počtové tvrzení. Neutrální návrh: „100 mg Aquamin® Soluble v jedné dávce.“
- Sekce „Jak funguje“ a původní situační karty dále obsahují např. ochranu kloubů/šlach, vstřebávání kaseinu 7 hodin, 27% snížení vstřebávání tuků, spalování tuků, dlouhodobé zastavení hladu a další účinky. Jsou zachované ve stávajícím pracovním návrhu; schválené produktové znění v uvedeném souboru není doloženo. Neutrální alternativou je popis skutečných složek a tabulkových dávek, nikoli doplnění nového slibu.
- „Bez cukru“ ve stávajícím užívacím piktogramu odporuje zdrojovým hodnotám 8 g cukrů / 100 g a 2,4 g / 30 g. Neutrální alternativa: „2,4 g cukrů v dávce“. V tomto grafickém zásahu nebyla původní ikona ani popisek potichu měněna.
- Probiotika: text uvádí 8,9 mld. CFU, tabulka 0,75 mld. KJT v dávce. Nevybírat jednu hodnotu bez potvrzení odpovědné osoby.

## Podklady a výroba
Aktuální Git `7756477f8fe1194155a7a7f89ca9e16c8b69888a`, skutečná veřejná stránka SKU 470, Pavlův snímek chyby, `brand/RULES.md`, vizuální identita Golden Life a vlastní produktový soubor. Model GPT‑6.1‑sol; SVG kresba a Chromium rasterizace/QA. Bez placeného generování obrázků. Cena modelového provozu není vyčíslená.
