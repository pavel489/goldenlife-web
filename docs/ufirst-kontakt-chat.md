# UFIRST dárkový box: kontakt a chat na hlavní stránce

## Správný rozsah podle dvou snímků
Jde o nativní kontaktní blok „Potřebujete poradit? Kontaktujte nás“ a plovoucí tlačítko „Pomůžeme s výběrem“, nikoli o podstránky produktů nebo produktový popis.

- Původní růžová kontaktního nadpisu `rgb(238,0,131)` je nahrazena černou; růžové maskované ikony telefonu a obálky jsou tmavě tyrkysové `#1F9CAD`.
- Skutečný widget je SupportBox (`#supportBox-iframe`), nikoli pouze na stránce rovněž uvedený Smartsupp. Tlačítko i hlavička otevřeného chatu mají tyrkysovou `#5BCFDE`, text a bublina jsou černé pro čitelnost.
- Zelená dostupnost a červené upozornění zůstávají stavovými indikátory. Fotografie operátorky, tel/mail odkazy, texty, funkce chatu, nastavení poskytovatele a sledování se nemění. Žádná zpráva nebyla odeslána.
- Zásah se aktivuje pouze na přesné adrese `/ufirst-darkovy-box/` (i bez posledního lomítka). Není to globální přebarvení e-shopu.

## Předání a nasazení
`shoptet/ufirst-prvky-stranky.html` je samostatný malý blok pro vložení do HTML na této stránce. Obsahuje scoped CSS a bootstrap do již dostupného same-origin iframe. Pro přehlednost jsou jejich zdroje i v `assets/ufirst-giftbox-page-elements.css` a `.js`; samostatný blok nemá externí závislost na těchto souborech.

Stejný blok je již zahrnutý v `shoptet/ufirst.html` a plném dokumentu `web/Golden Life Darkovy box UFIRST/Golden_Life_Darkovy_box_UFIRST_cz.html`. Krátký popis není nutné pro tuto opravu měnit.

Předchozí mylně zacílené změny palety popisů a vloženého USB doporučení jsou v tomto commitu vráceny; původní sdílené CSS i původní piny jsou obnoveny. Produktové texty a původní funkční skripty jsou zachovány. Nepoužívat již předchozí barevný commit jako zdroj k importu.

Publikace v Gitu není uložení do Shoptetu. Náhled vznikl lokálním vykonáním testovaných stylů a kódu na skutečné veřejné stránce; žádná CMS ani administrátorská změna na živém webu neproběhla.

## Ověření
- Skutečný veřejný DOM: `.detail-contact-box .top-navigation-contacts`, jeho telefonní/mailové pseudoelementy a skutečný dokument SupportBox iframe.
- Desktop 1280 px a mobil 390 px: všechny nalezené instance kontaktu včetně responzivních kopií mají požadované barvy a stejné href; chat má tyrkysovou plochu, černý text a jediný vložený styl.
- Reálným kliknutím otevřeno a minimalizováno chatovací okno; tyrkysová hlavička a černý titulek. Bez psaní či odeslání zprávy.
- Inicializace po DOMContentLoaded prokazatelně proběhla ještě před vznikem skutečného iframe. Po jeho pozdějším vložení se styl aplikoval. Opakované zavolání bootstrapu i událost load nevytvořily duplikát.
- Na skutečné titulní stránce zůstal původní růžový kontakt, nebyl přidán marker ani iframe styl.
- Syntaxe JavaScriptu ověřena `node --check`. Při ověření vzhledu byly newsletter/cookie překryvy skryté pouze v testovací kartě; nastavení souhlasu není součástí opravy.
- Přiložený náhled obsahuje výřezy skutečného vykreslení opraveného kontaktu a chatovacího tlačítka, zvětšené pro čitelnost.

Same-origin přístup je ověřen pro současný SupportBox. Pokud poskytovatel v budoucnu přesune obsah do cizího původu, bootstrap to bezpečně přeskočí; neobchází ochranu prohlížeče.

## Zdroje a náklady
Dva snímky zadavatele, skutečná veřejná stránka UFIRST dárkového boxu, aktuální Git snapshot, `brand/RULES.md`, manuál UFIRST a navazující pracovní pravidla. Model GPT-6.1-sol, Python a Chromium. Bez placené generace médií; přesná cena modelu a konektoru není dostupná.
