# Oprava tabulek v rozbalených detailech dárkových boxů

## Stav
Připravená a otestovaná oprava pro Git. **Nejde o uložení do živého Shoptetu.**

## Příčina a změna
Načítací skript přidával přímo na `<table>` třídu `.gl-reader-table`, jejíž `display:block` změnilo tabulku na blok. Barevný rám měl plnou šířku, ale vnitřní mřížka řádků mohla být výrazně užší. Příčina byla reprodukována na veřejné stránce Collagen Slim a odpovídá zaslanému screenshotu.

Oprava zachovává nativní `display:table`. Třídu s vodorovným posuvem, ovládáním z klávesnice a popiskem dostává samostatný obal `<div role="region" tabindex="0">`. Samotné buňky, text, čísla, dávkování ani barvy zdrojových produktů se neupravují. Shadow DOM, sanitizace a odstranění nákupních prvků z importu zůstávají zachované.

Při testování aktuálního Slim GLP-1 bylo nutné povolit ještě jeho přesný živý CSS soubor `/user/documents/upload/css/golden-life-barvy-slim-glp-1-activator.css` (HTTP 200, text/css). Obecné stahování libovolných stylů není povoleno.

## Soubory k importu
Vlož do **dlouhého popisu** odpovídajícího produktu kompletní obsah z:
- `shoptet/beauty.html` — dárkový box Collagen Beauty
- `shoptet/slim.html` — dárkový box Collagen Slim
- `shoptet/hormonal.html` — dárkový box Hormonal Balance
- `shoptet/longevity.html` — dárkový box Longevity
- `shoptet/ufirst.html` — dárkový box UFIRST

Zrcadla dlouhých popisů v `web/` mají stejnou aktualizaci pinu. Krátké popisy se nemění. U dlouhých popisů a bootstrapů se mění pouze neměnný odkaz na verzi skriptu a jeho SHA-384, nikoli ostatní obsah. Není třeba přepisovat globální CSS e-shopu ani nahrávat upravené složení.

Loader: `assets/giftbox-detail-loader.js`, pin `45c603ef2f6582495668bbb0c02d81a761bf2344`.
SRI: `sha384-rYz8YJu1CWSuV4Cfmxu1YxvJpdkRTXrVyaCQ/nmD4S4x5rX3lKA2xKXWlmb05R1p`.

## Reálné ověření
Chromium / Playwright, veřejné rodičovské stránky s dočasnou náhradou dlouhého popisu přesnými dodávanými HTML a přesným skriptem se správným SRI. Dětské stránky a produktové styly byly skutečně načtené z e-shopu. Cookies, chat a analytické/widgetové vrstvy byly potlačené pouze v testu, nikoli změněné na webu.

- 5 boxů × 5 produktových tlačítek × 3 šířky (1440, 390, 320 px) = **75 rozbalení**.
- **78 vykreslení tabulek**: nativní tabulkový layout, rozdíl rám/mřížka pod 6 px včetně okrajů, obal nepřesahuje hostitele.
- Všechny buňky porovnány s aktuálním zdrojovým produktem: beze změny.
- Otevření, přepnutí produktu, zavření, opětovné otevření z cache a Escape: prošlo na všech boxech a šířkách.
- Importované skripty, formuláře a nákupní tlačítka: 0.
- Porovnání s předchozím režimem na stejném obsahu: žádné nové vodorovné přetékání hostitele.
- Vizuálně zkontrolovaný screenshot Collagen Slim na desktopu i mobilu. Mobilní tabulka může být vysoká, ale zachovává všechny sloupce. U širokých tabulek UFIRST funguje samostatný posuvný obal místo roztažení tabulkového rámu.

Podrobnosti: `tests/giftbox-table-layout-results.json`.
Před/po: `docs/images/tabulky-pred-opravou-1440.png`, `docs/images/tabulky-po-oprave-1440.png`.

### Další sady a limity
Živé Hormonal Duo a Hormonal Trio používají jiný importér. Z 15 kontrol jejich detailů ve třech šířkách se 12 načetlo (18 vykreslení tabulek) bez této chyby `display:block`; tři kontroly třetího detailu Hormonal Trio skončily `Popis nenalezen.`. Živý importér Trio nezahrnuje `#nad-popis`, zatímco soubor v Git už tento kořen má. Tato starší nenahraná oprava se v tomto zásahu znovu neupravovala.

Předexistující přetékání jiných částí importovaného obsahu zůstává u Collagen Beauty (ID 383) na 390/320 px a UFIRST all-in-one (576) a Brain & Focus (582) na 320 px. Je zaznamenané samostatně; není to nová chyba této opravy ani důvod tvrdit, že byl přepracovaný celý mobilní popis. Oprava míří na odskočené tabulky, nikoli na redesign zdrojových stránek.

Nasazení na e-shop bude hotové až po uložení dlouhých popisů a novém anonymním otevření živých boxů. Git publikace sama nemění již vložené, pevně připnuté skripty na e-shopu.

## Opakování testu
Z kořene repozitáře s izolovaným Pythonem a balíčky `playwright`, `beautifulsoup4`, `requests`:

```
python -m playwright install chromium
python tests/giftbox-table-layout.py
```

Test vypíše adresář s důkazy; nic neukládá do administrace e-shopu. Dílčí read-only kontrola Duo/Trio je zachycená v JSON reportu.

## Podklady a výroba
Zaslaný screenshot, aktuální veřejné popisy pěti boxů a jejich 15 unikátních komponent, aktuální Git `pavel489/goldenlife-web` z výchozího commitu `2c283004d1b057d28424124b2287a6d2ed74d6a1`, `brand/RULES.md` a pracovní vizuální identita Golden Life. Model gpt-6.1-sol; implementace a ověření Python / Chromium / Playwright. Bez placené obrazové či video generace (0 za generovací služby); cena běhu agenta/modelu není vyčíslená. Nové produktové či zdravotní tvrzení nevzniklo.
