# UFIRST — zapojení vlastních nahraných CSS/JS do dárkového boxu

## Aktuální zdroje
Box používá přesně cesty dodané zadavatelem:
- `/user/documents/upload/css/ufirst-global.css`
- `/user/documents/upload/css/ufirst-global.js`

Obě skutečné veřejné URL byly načtené s HTTP 200; CSS má `text/css` a JS `application/javascript`. Nahrané soubory nejsou přepisované ani nahrazované vlastní kopií. Barevná paleta zůstává v jediném sdíleném CSS.

## Implementace v boxu
Do konce dlouhého CMS popisu `shoptet/ufirst.html` a odpovídajícího plného HTML `web/Golden Life Darkovy box UFIRST/Golden_Life_Darkovy_box_UFIRST_cz.html` je přidaný pouze malý bootstrap označený `data-gl-ufirst-own-assets`.

Bootstrap vloží nahrané CSS a JS do dokumentu, pokud ještě nejsou načtené globálně. Skriptu předá `data-ufirst-css` s přesnou dodanou cestou; stejný CSS soubor se tím načte i do skutečného iframe SupportBoxu. Nevkládá druhou paletu ani další CSS do každého produktu. Na boxu už proto není podmínkou samostatné zapojení globálního záhlaví.

Krátký popis, texty, fotografie, původní stylové importy a původní skripty zůstaly beze změny. Odstranění přesně přidaného bloku vrací obě původní HTML bajtově shodně.

## Volitelné použití pro ostatní UFIRST stránky
`shoptet/ufirst-globalni-vzhled.html` je zároveň přepojený na stejné vlastní nahrané URL. Lze ho jednou přidat do globálního záhlaví (Vzhled a obsah → Editor → HTML kód → Záhlaví), pokud má společná vrstva běžet i na ostatních rozpoznaných UFIRST stránkách. Produktový bootstrap podle ID nevytvoří další CSS/JS include, pokud už tento globální blok existuje.

Při přechodu ze starých CDN odkazů nahradit starý globální blok novým; neponechávat souběžně odlišné zdroje se stejnými ID.

## Skutečné ověření
- Stažené oba nahrané soubory, skutečné MIME typy, SHA-256 v test reportu a kontrola syntaxe skutečného JS pomocí `node --check`.
- Z finálního doručovaného CMS HTML byl vytažen přesný přidaný bootstrap a spuštěn na veřejné stránce dárkového boxu. Prokazatelně načetl dodané cesty, nikoli předchozí CDN soubory.
- Nadpis kontaktu černý, telefon a obálka tmavě tyrkysové, tlačítko chatu tyrkysové s černým textem. Iframe načetl `https://www.golden-life.cz/user/documents/upload/css/ufirst-global.css`.
- Opakované spuštění: jeden hlavní CSS link, jeden společný JS a jeden CSS link uvnitř iframe.
- Mobil 390 px a desktop 1280 px: skutečné otevření a minimalizace chatu, tyrkysová hlavička a černý text. Bez psaní nebo odeslání zprávy.

Test provedl pouze dočasné vložení bootstrapu do testovací karty. Newsletter/cookie překryvy byly při pointer testu skryté jen v této kartě. Git publikace ani tento test nejsou uložením produktového pole v živém Shoptetu. Pro ruční nasazení je třeba použít aktualizovaný celý dlouhý popis z Gitu; samotné nahrání CSS/JS na server nevloží odkaz do produktu.

## Zdroje a náklady
Aktuální vzdálený Git snapshot, dvě přesné URL od zadavatele, veřejná stránka boxu a skutečný SupportBox, `brand/RULES.md`, manuál UFIRST a stávající schválený rozsah vzhledu. Model GPT-6.1-sol, Python, Chromium a Composio GitHub. Bez placené generace médií; přesná cena modelu a konektoru není k dispozici. Produktové texty a zdravotní tvrzení se tímto technickým zapojením nemění ani nově neschvalují.
