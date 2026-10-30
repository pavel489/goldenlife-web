# Double Slim SOS Burner – styly krátkého popisu

Uživatelův screenshot zachycuje neostylovaný krátký popis produktu 573: ikony svisle a slepená metadata. Při novém skutečném načtení veřejné stránky už společný i barevný CSS vracejí HTTP 200 a styly se aplikují. Historickou příčinu stavu na screenshotu nelze z této kontroly prokázat; cache ani chybný import nebyly doloženy.

Živý současný krátký popis přesto přebíral obecný zalamovací flex a v úzkém hostu přetékal první popisek ikony. Oprava přidává pouze pravidla pro přesný krátký layout a téma double-slim-sos-burner:
- Pevná pětisloupcová mřížka minmax(0,1fr), všechny popisky uvnitř buněk a rozumné mobilní rozměry ikon.
- Samostatné řádky balení, počtu denních dávek a dávkování místo slepených řetězců.
- Zachovaná růžová #E40E7E, stejné originální ikony, všechna slova a čísla.

Nezměněné zůstaly oba HTML popisy, složení, dávky, hlavní fotografie a sdílený golden-life-produkt.css. Pravidla nemíří do dlouhého popisu ani na jiné produkty.

## Nasazení
Vyměň pouze `/user/documents/upload/css/golden-life-barvy-double-slim-sos-burner.css` za stejnojmenný úplný soubor z tohoto commitu. HTML nemusíš znovu vkládat. Git publikace není upload tohoto souboru do Shoptetu. Po jeho výměně je potřeba ověřit skutečný web; předaný screenshot zachycuje lokální test navrženého CSS na skutečné stránce.

## Testy
Chromium načetlo skutečnou veřejnou stránku se všemi jejími skripty; pouze přesná odpověď barevného CSS byla v testu lokálně nahrazená návrhem. Prošlo 320, 360, 390, 600, 767, 768, 1024, 1280 a 1440 px i návrat na mobil: pět ikon v jedné řadě, žádné přetečení či ořez textu v komponentě, metadata po řádcích, žádné rozbité ikony nebo chyby JS. Cookie, chat a plovoucí widgety jsou skryté pouze pro kontrolní snímek; jejich nastavení na webu se neměnilo.

Podklady: uživatelův screenshot, současný veřejný Double Slim SOS Burner, poslední main a jeho barevný soubor. Model GPT-6.1-sol, Python/Playwright, Composio GitHub. Bez placené obrazové generace; cenu modelového běhu nemám vyčíslenou. Převzaté účinkové texty nebyly tímto CSS zásahem schvalované ani obsahově přepisované; předchozí claims ledger zůstává v platnosti.
