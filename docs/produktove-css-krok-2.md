# Produktové CSS – krok 2: připravený stabilní základ

## Stav
Dokončena příprava a lokální ověření CSS základu. Veřejné soubory ani produktová pole Shoptetu se v tomto kroku neměnily. Převod pilotních produktů patří do následujícího kroku.

Zdrojový Git snapshot: `1d15127789fb899be3ad599fe1db0ec28ee9f7ef`. Kontrola: 2026-11-05T13:57:18.837567+00:00.

## Výsledek kontroly
- Ověřeno 21 produktových CSS souborů: 17 veřejných verzí odpovídá zdrojovému Gitu po normalizaci konců řádků, jeden soubor vrací 404, tři veřejné soubory se liší.
- Společný `golden-life-produkt.css` odpovídá zdrojovému Gitu a zůstal beze změny. Není důvod měnit celý framework nebo jeho globální pravidla.
- Všechny čtyři cílové soubory jsou připravené v `user/documents/upload/css/`. Tři jsou převzaté byte-identicky ze zdrojového snapshotu; ananasové téma dostalo jediný lokální kompatibilitní doplněk popsaný níže.

## Čtyři soubory pro pozdější nahrání
1. `golden-life-barvy-slim-extreme-collagen.css` – veřejná adresa vrací 404. Soubor je připraven pro označený nový popis dózy; současný neoznačený popis se samotným nahráním nepřevede.
2. `golden-life-barvy-slim-extreme-collagen-box-ananas.css` – veřejný soubor je dostupný, ale není totožný s novou připravenou verzí. Doplněna kompatibilita se stále živým starším popisem.
3. `golden-life-barvy-slim-glp-1-activator.css` – připravená oprava dvojího barevného filtru ikon a pravidla šesti ikon pro nově označený krátký popis. Stejné téma používá samostatný i Double produkt. Samotné CSS nepřidává chybějící ikony ani nepřevádí HTML.
4. `golden-life-barvy-slim-sos-fat-burner.css` – připravená oprava dvojího filtru původních růžových ikon, bez úprav produktových fotografií.

## Ošetřená zpětná kompatibilita ananasu
Při skutečném porovnání v prohlížeči vyšlo najevo, že bezpodmínečná výměna veřejného ananasového tématu za původní připravenou Git verzi odstraní fotografické pozadí nákupní výzvy na dosud nepřevedené stránce.

Proto je původní pozadí zachováno jen pro ananasový kořen bez nového banneru: `#special-popis:where([data-gl-theme="slim-extreme-collagen-box-ananas"]):where(:not(:has(.nad-banner))) .cta-box`, pouze od 600 px. Nová připravená šablona banner má, takže tento doplněk její vzhled nemění. Použité `:has()` vyžaduje moderní prohlížeč; regresní měření zde běželo v Chromium. Nedochází k zásahu do jiných produktových témat ani společného CSS.

## Co bylo opravdu testováno
- CSS parser: 21 souborů, žádná syntaktická chyba; pravidla cílových témat jsou lokálně omezená na vlastní `data-gl-theme`.
- 19 existujících odběratelů společného CSS, vždy současné a připravené soubory, na šířkách 1440 a 390 px: celkem 76 měření.
- Použit skutečný archivovaný veřejný HTML dokument, skutečné shopové skripty a skutečné obrázky; nahrazovaly se jen CSS odpovědi v izolovaném testovacím prohlížeči.
- Zachována nativní identita a texty. U měřeného kořene, hera, CTA, tabulek a krátkého popisu se nezměnily sledované rozměry/barvy ani horizontální přesahy. Změnily se pouze očekávané filtry ikon tří dotčených produktů.
- Šest reprezentativních testů otevření a zavření dialogu látek: tři dotčené produkty, současné a připravené CSS. Nejde o test všech dialogů.
- Ananasový starší CTA blok po kompatibilitním doplnění zachovává původní pozadí. Samostatný CSS test na skutečném novém připraveném HTML ověřil, že doplněk nemění novou šablonu; v tomto dílčím CSS testu byly skripty záměrně vynechány.

## Co tento krok neznamená
Nejde o publikaci na e-shopu, převod krátkých ani dlouhých produktových popisů, kompletní test všech vložených detailů v boxech ani právní schválení textů. Tato ověření se provedou s konkrétními pilotními HTML popisy v dalším kroku.

Před pozdější výměnou veřejných souborů znovu přečíst přesné aktuální adresy, pořídit čerstvé zálohy a ověřit kanonické názvy; Shoptet může při opakovaném uploadu přidat příponu místo nahrazení. Po výměně porovnat veřejné bajty se schváleným souborem. U dlouhodobě cachovaných souborů řešit verzi zahrnutí spolu s konkrétním HTML popisem. V tomto kroku se žádné popisy kvůli verzování nepřepisovaly.

## Návrat
Dosavadní veřejné CSS odpovědi a zdrojové stránky byly pro porovnání archivovány lokálně, s SHA-256. To nenahrazuje čerstvé předpublikační zálohy z okamžiku budoucího uploadu. U dosud chybějícího souboru neexistuje původní CSS obsah k obnově.

## Zdroje a náklady
Veřejné CSS a produktové stránky, uvedený Git snapshot a `brand/RULES.md`. Zpracování GPT-6.1-Sol, CSS parser a Chromium/Playwright. Bez obrazového generování a bez placeného externího generování. Podrobné ověřené hodnoty a SHA-256 jsou v `docs/produktove-css-krok-2-testy.json`.
