# Globální vzhled UFIRST: kontakt a SupportBox

## Co je jiné oproti předchozí opravě
Kontakt a chat se již neřeší uvnitř jednotlivých produktových popisů. Existuje jediný sdílený `assets/ufirst-global.css` a jediný malý `assets/ufirst-global.js` pro rozpoznání UFIRST stránky a načtení stejného CSS do skutečného iframe SupportBoxu.

Barevné hodnoty jsou pouze v CSS: tyrkysová #5BCFDE, tmavá tyrkysová #1F9CAD, žlutá #EDFF00 a černý text. JavaScript neobsahuje druhou kopii palety. Kontakt a chat zůstávají funkčně stejné; obrázky, tel/mail cíle, zprávy, ceny, košík, sledování i nastavení poskytovatele se nemění. Globální v tomto zadání znamená společnou vrstvu pro dříve určené kontaktní/chatovací komponenty, nikoli nový design celé šablony či přebarvení kampaní.

## Jednorázové zapojení
Vložit celý soubor `shoptet/ufirst-globalni-vzhled.html` do globálního **Vzhled a obsah → Editor → HTML kód → Záhlaví (před koncovým tagem HEAD)**. Přidat k existujícímu obsahu, ne jej přepsat. Oficiální umístění ověřeno: https://podpora.shoptet.cz/html-kody/.

Soubor načítá dvě veřejně dostupné, neměnně připnuté závislosti. Obě odpověděly HTTP 200 a jejich bajty byly porovnány s Git soubory. Není nutné kopírovat styl do každého produktu ani nejdřív nahrávat CSS do Shoptetu.

Samostatný `shoptet/ufirst.html` teď již globální nastavení neinstaluje. Původní lokální patch byl odstraněn z obou dlouhých UFIRST dokumentů; ostatní produktový obsah a skripty zůstaly zachovány. Předchozí `ufirst-prvky-stranky.html` a jeho produktově specifické assety jsou nahrazené touto globální vrstvou.

## Na kterých stránkách se aktivuje
Inicializátor používá přesný seznam veřejně ověřených UFIRST produktových cest z brandového výpisu `/znacka/u-first/`, včetně dárkového boxu, dále vlastní láhev, brandový výpis a UFIRST landing `/ufirstlab/`. Nehledá pouze slovo UFIRST v textu doporučených produktů a nepřebarví tím běžnou Golden Life stránku.

Novou UFIRST stránku lze přidat centrálně do seznamu v JS, nebo ji výslovně označit prvkem `data-gl-page-brand="ufirst"` před spuštěním globálního defer skriptu. Barvy pak zůstávají stále v jednom společném CSS.

Pro budoucí změnu barev se mění jen sdílený CSS zdroj a jeho verzovaný odkaz v jednom globálním bloku. `data-ufirst-css` na skriptu odkazuje na tentýž soubor jako hlavní link a přenáší správnou verzi i do chatu. Alternativně lze oba soubory hostovat na vlastních stabilních URL v Shoptetu a změnit pouze tyto globální odkazy. Nevyměňovat společnou barvu za samostatné kopie CSS v produktech.

## Proč dosud změna na webu nebyla vidět
Čerstvá veřejná navigace na UFIRST dárkový box prokázala: žádný předchozí page-elements bootstrap, žádný jeho marker a stále růžový kontakt. Nešlo tedy o prokázanou chybu mezipaměti; původní oprava nebyla na stránce načtená. Nahrání do Gitu samo nepřidá kód do globálního záhlaví e-shopu.

Živé globální nastavení v této práci nebylo uloženo. Byl otevřen skutečný administrační login; existující bezpečně uložené vlastní přihlášení se nepodařilo vyplnit dedikovaným vault nástrojem (`No fillable login field matched the saved item on this page`). Heslo nebylo čteno ani ručně zadáváno. Shoptet MCP v dostupné sadě nevystavuje editor šablony/HTML kódů, takže tuto operaci nenahrazuje.

## Skutečné testy
- Skutečné vzdálené CSS/JS na veřejném boxu, Brain & Focus a brandovém výpisu: kontakt černý/tmavě tyrkysový, chat tyrkysový s černým textem, iframe používá stejný CSS soubor.
- Veřejná titulní stránka: bez UFIRST markeru, původní růžové komponenty, bez vloženého iframe CSS.
- Inicializace v DOMContentLoaded ještě před vznikem reálného SupportBox iframe; po jeho pozdějším přidání správně načtený jediný CSS link.
- Mobil 390 px a desktop 1280 px: skutečné otevření a minimalizace chatu pointerem; při ověření vyčkáno na dokončení animace. Žádná zpráva nebyla napsána ani odeslána.
- Syntaxe JS ověřena `node --check`; původní produktové HTML je proti předchozí verzi stejné mimo odstranění přesného starého lokálního bloku.

Testy byly provedené vložením globálních referencí pouze do testovací karty a jednorázovou inicializací při navigaci, nikoli zápisem do živé šablony. Newsletter/cookie překryvy byly dočasně skryté pouze v testovací kartě pro pointer test. Při případném budoucím přechodu SupportBoxu na cizí origin se přístup bezpečně přeskočí; ochrana prohlížeče se neobchází.

## Zdroje a náklady
Aktuální vzdálený Git snapshot, skutečné veřejné stránky a brandový výpis UFIRST, předchozí dva snímky zadavatele, brand/RULES.md a manuál UFIRST, oficiální Shoptet dokumentace HTML kódů. Model GPT-6.1-sol; Python, Chromium, Composio GitHub. Bez placené generace médií; přesná cena modelu/konektoru není k dispozici.
