# Double Slim GLP-1 Activator s Berberinem – dlouhý a krátký popis

## Co je připravené
- `Golden-Life-Double-Slim-GLP-1-Activator-cz.html`: úplný dlouhý CMS fragment.
- `maly/Golden-Life-Double-Slim-GLP-1-Activator-maly-cz.html`: krátký CMS fragment.
- Náhled v `nahledy/double-slim-glp-1-activator.html`, skutečný browser screenshot ve stejnojmenném PNG. Samostatný offline náhled je předán jako příloha v původním vlákně; není CMS fragment.

Předloha je poslední připravený Slim GLP-1 Activator s Berberinem (produkt 476) z Git main `9351d93d9b6a9ee5c8b0fa399f03e5c793953c80` a jeho současná veřejná produktová stránka. Admin odkaz byl prohlédnut pouze do přihlašovací stránky; interní editor ani další administrační data nebyly načtené nebo měněné. Zdrojová struktura, obsah složek a dávkování se nemění.

## Double není dvojnásobná denní dávka
- Dvě dózy stejného produktu, každá 60 tobolek / 47,4 g.
- Celkem 120 tobolek, 60 denních dávek při 2 tobolkách denně.
- Bannery, úvod, krátký popis, CTA, FAQ a mobilní shrnutí odpovídají Double balení.
- Tabulka zůstává přesně na 1 tobolku a 2 tobolky (denní dávka); žádné dávky složek se nenásobí dvěma. Chrom zůstává 25/50 mcg, čísla a RHP beze změny.
- Název a fotografie nesmí zaměnit 461 (Double) a 476 (jedna dóza).

## Fotografie a styly
- V úvodu i CTA skutečná hlavní fotografie Double produktu 461, na níž jsou dvě dózy. Obě místa sledují nativní hlavní obrázek pouze při odpovídajícím productId 461. Chybějící/neplatná nebo cizí galerie použije ověřenou záložní fotografii téhož Double produktu.
- Bez generování nebo retuše produktu. Piktogramy zachovávají původní fialovou řady #62388E, bez druhého barevného filtru.
- Stejná existující dvojice importů: `/user/documents/upload/css/golden-life-produkt.css` a `/user/documents/upload/css/golden-life-barvy-slim-glp-1-activator.css`. Společný i barevný CSS jsou nezměněné; samostatný Double barevný soubor není potřebný pro identickou produktovou řadu.
- Stav živých CSS vůči Git bajtům: viz `docs/double-slim-glp-1-activator-manifest.json`. Rozdílné soubory je před nasazením třeba nahradit ověřenou připravenou verzí; úspěch lokálního testu není důkaz živého nasazení.

## Ověření
Skutečné Chromium testy na 320, 360, 390, 600, 767, 768, 1024 a 1440 px, včetně návratu z desktopu na mobil. Ve fixture byly použité aktuální veřejné styly shopu a lokální ověřené produktové CSS. Prošly všechny detaily 6 složek, banner, mobilní rozbalování včetně klávesnice, přesná produktová identita a změna galerie. Bez vodorovného přetečení, ořezu textů tabulky, rozbitých obrázků nebo chyb JavaScriptu. Nákupní CTA pouze posouvá k nativnímu nákupu; nic nepřidává do košíku. V náhledu je nákup vypnutý. Offline soubor testován s vypnutou sítí: bez externích požadavků a rozbitých obrázků. Testy jsou v `docs/double-slim-glp-1-activator-testy.json`.

## Zdravotní tvrzení – zachovaný interní návrh, ne právní schválení
Technická a obalová úprava nepředstavuje schválení zdrojových účinkových popisků. Zachované piktogramy obsahují:
- „Snižuje chuť do jídla“ – neověřené; neutrální alternativa „2 dózy stejného produktu“.
- „Stabilizuje hladinu cukru“ – neověřené; neutrální alternativa „50 mcg chromu v denní dávce“.
- „Podporuje spalování tuků“ – neověřené; neutrální alternativa „485 mg berberinu HCl v denní dávce“.
- „Zvyšuje pocit sytosti“ – neověřené; neutrální alternativa „2 tobolky denně“.
- „Bleskové hubnutí“ – neověřený příslib; neutrální alternativa „120 tobolek na 60 dní“.
- „Vyrobeno v ČR“ je údaj o původu převzatý z předlohy, nikoliv zdravotní tvrzení; samostatná výrobní dokumentace v tomto úkolu ověřena nebyla.
Konkrétní produktový soubor se schválenými zdravotními formulacemi nebyl nalezen. Alternativy výše jsou pouze věcné formulace založené na zkontrolované předloze, nikoli domyšlená autorizovaná zdravotní tvrzení. Před veřejným použitím účinkových popisků je potřeba jejich schválení nebo samostatně odsouhlasená výměna. Etiketa na autentické fotografii nebyla přepisovaná.

## Předání
Git publikace této úpravy není uložením do Shoptetu. Živý produkt nebyl změněn. Produkt 476, jeho HTML i všechna CSS zůstávají beze změny.

Model: GPT-6.1-sol. Nástroje: Composio GitHub (ověřená identita Goldie), veřejné zdroje Golden Life, Python a Chromium/Playwright. Žádná placená obrazová/video generace; samostatný generační výdaj 0. Skutečnou cenu modelu a konektorů nemám vyčíslenou.
