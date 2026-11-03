# UFIRST: společný modrý/tyrkysový vzhled kontaktu a plovoucích prvků

## Skutečná příčina a oprava
Na veřejném dárkovém boxu se obě nahrané závislosti už načítaly. Nešlo o chybějící upload. Shoptet ale přepsal URL JavaScriptu na `cdn.myshoptet.com/usr/www.golden-life.cz/...`. Původní inicializátor vyhodnotil kořenovou cestu CSS vůči původu skriptu a vložil do SupportBox iframe neplatnou URL `https://cdn.myshoptet.com/user/documents/upload/css/ufirst-global.css`. Hlavní dokument tak byl označený UFIRST, ale chat zůstal růžový.

`assets/ufirst-global.js` nyní vyhodnocuje dodanou cestu vůči veřejné stránce obchodu, aktualizuje i již existující chybný CSS link a stále obsluhuje pozdější vložení/načtení skutečného same-origin iframe. Revize `ufirst-2` umožňuje opravit starší inicializaci bez násobení linků. CSS odkaz nese verzi kvůli roční veřejné cache.

`assets/ufirst-global.css` zachovává původní paletu #5BCFDE / #1F9CAD / černá. Doplňuje vzhled newsletterového teaseru Leadhub podle selektoru ověřeného v jeho skutečném veřejném skriptu. Ovládací prvky označené `PRIVACY_TEASER` zůstávají výslovně mimo tento selektor. Opravené je i přečnívání textu u mobilního ikonového tlačítka SupportBoxu; desktopový text zůstává viditelný.

## Skutečně provedeno v Shoptetu
- Opravené CSS a JS jsou nahrané na stejné dodané veřejné cesty `/user/documents/upload/css/ufirst-global.css` a `/user/documents/upload/css/ufirst-global.js`.
- Správce souborů nepřepisuje existující jména: první upload vytvořil `_1` kopie. Jejich bajty byly ověřené. Původní dva soubory byly přes nativní přejmenování zachované jako `ufirst-global-backup-42be.css` a `.js`, nové kopie následně dostaly původní jména. Konečné veřejné CSS i JS byly nezávisle stažené a porovnané bajt po bajtu s testovaným výstupem.
- V `Vzhled a obsah → Editor → HTML kód`, skutečná cesta `/admin/html-kody/`, je jednou přidaný verzovaný společný include ze `shoptet/ufirst-globalni-vzhled.html` do pole **Záhlaví**. Inicializátor uplatňuje paletu jen na ověřených UFIRST cestách či výslovně označené UFIRST stránce.
- Před zápisem byla uchovaná lokální záloha. Po nové navigaci bylo ověřeno celé přesné uložené záhlaví a bajtová shoda nezměněných polí footer, orderFinale, robotsFile a llmsFile. Žádné měření, formulář, text kampaně, odesílání ani nastavení objednávek se neupravovalo.
- Živé produktové popisy se nepřepisovaly. Připravený CMS a plný HTML soubor boxu na Gitu mají pouze aktualizované společné URL s verzí; odstranění těchto přesných záměn vrací ostatní bajty beze změny.

## Ověření
`tests/ufirst-palette-live-results.json` popisuje nezávislý anonymní Chromium běh bez síťových podvrhů či ručního vložení inicializátoru pro ověření stránek:
- Dárkový box, all-in-one drink a Trio: skutečný chat má `rgb(91, 207, 222)`; iframe načítá správnou veřejnou CSS URL; jeden link v hlavním dokumentu a jeden ve frame.
- Box 1280 px / 390 px: skutečné kliknutí, otevření offline panelu a minimalizace bez napsání či odeslání zprávy.
- Domovská stránka jako negativní kontrola: žádné UFIRST označení ani CSS ve frame, původní růžový chat zůstává.
- Samostatný opakovací test inicializátoru: žádné zdvojení CSS.
- Newsletterový teaser: ověřený provider selektor a označený DOM kontraktní test barvy; privacy varianta beze změny. **Historický teaser „Sleva 10 %“ se v této návštěvě nespustil; jeho živé zobrazení proto není potvrzené.** Tento test není vydáván za živou kampaň ani její snímek.
- Dočasné skrytí cookie/newsletter překryvů pro čistý snímek platilo pouze v testovací kartě. Nastavení návštěvnického souhlasu se na serveru neměnilo.

## Soubory a zdroje
Aktuální Git snapshot, přesné dva veřejné uploady zadavatele, skutečný veřejný box/drink/Trio a SupportBox, veřejný `agent-plugin-popup.js`, `brand/RULES.md`, existující UFIRST barevná paleta. Model GPT-6.1-sol, Chromium/Playwright, Python a Composio GitHub; vlastní účet Goldie pro nativní správce souborů a HTML editor. Bez placené generace médií; cena modelu a konektorů není z použitých nástrojů dostupná. Produktové texty ani zdravotní tvrzení se neměnila.
