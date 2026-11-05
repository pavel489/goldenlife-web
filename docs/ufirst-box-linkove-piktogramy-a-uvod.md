# UFIRST box — oprava piktogramů a úvodního odstavce

## Přesný rozsah

- Šest piktogramů v krátkém i dlouhém popisu je nově sjednoceno do **linkových obrysů se zaoblenými konci a spoji** (`fill="none"`, `stroke-linecap="round"`, `stroke-linejoin="round"`, jednotná síla 2,6 v ploše 64 × 64). Obsahové popisky zůstávají beze změny. Složky, sáčky, příchutě, rostlinné kapsle, láhev a USB-C míchátko.
- Zachovaná tyrkysová stávajícího webového tématu; nejde o změnu globální palety. Samostatné editovatelné SVG jsou v `assets/ufirst-giftbox-line-icons/`. HTML obsahuje totožné vložené SVG jako data URI, bez nové externí závislosti.
- Nový dodaný odstavec nahrazuje předchozí úvod **přímo pod hlavním nadpisem dlouhého popisu**. Znění je doslovné, pouze `&amp;` se v prohlížeči zobrazuje jako `&`. „Ufirst dlouhy“ bylo označení části zadání, nikoli součást odstavce.
- Shodně jsou aktualizované oba existující páry v `shoptet/` a `web/Golden Life Darkovy box UFIRST/`. Ostatní části HTML zůstávají byte-for-byte původní: automatický reverzní test mění zpět pouze šest URI a úvod a musí vrátit přesné původní soubory. Obsah SCRIPT a STYLE bloků, fotografie, vazby galerie, košík, ostatní texty a SEO se neměnily.
- Pouze Git předání. Živý Shoptet se neukládal ani nepublikoval. Tento záznam nahrazuje první úvodní odstavec z předchozího editorského podkladu; ostatní části zadání platí dál.

## Nový dodaný odstavec

Dárek, který potěší každého, kdo chce mít více energie, lépe se soustředit a zvládat každý den naplno! Tento nádherný vánoční box spojuje 5 produktů pro podporu energie, výkonu, hydratace a psychické pohody. UFIRST All-in-One obsahuje více než 85 složek v jediném lahodném sáčku, včetně vitaminů, minerálů, elektrolytů, peptidů a enzymů. Brain & Focus je zaměřený na soustředění a mentální výkon, zatímco Care Free na psychickou pohodu a zvládání stresu. Součástí boxu je také stylová láhev a praktické USB míchátko. Ideální vánoční dárek pro každého, kdo chce pečovat o své tělo i mysl a dát konečně sám sebe na první místo!

## Zdravotní tvrzení — upozornění a zdrojové alternativy vedle zadání

Text byl ponechán jako **dodaný pracovní text pro kontrolu**, nikoli označen za schválené veřejné zdravotní sdělení. Doplněk stravy není lék. Níže uvedené návrhy nebyly potichu vložené místo zadání.

- Dodané: **„Dárek, který potěší každého, kdo chce mít více energie, lépe se soustředit a zvládat každý den naplno!“** Efektové sdělení bez pojmenované nosné živiny, v daném znění není doložené produktovým souborem. Zdrojová alternativa pro část o energii/únavě z `brand/product/ufirst-all-in-one-drink-/info.md`: **„Hořčík přispívá k elektrolytické rovnováze, k normálnímu energetickému metabolismu, k normální činnosti nervové soustavy a ke snížení míry únavy a vyčerpání.“** Tato věta nedokládá slib lepšího soustředění nebo každodenního výkonu.
- Dodané: **„Tento nádherný vánoční box spojuje 5 produktů pro podporu energie, výkonu, hydratace a psychické pohody.“** Obecné zdravotní přínosy připsané boxu, bez živin. Pro psychickou činnost produktový zdroj Care Free uvádí: **„Hořčík a vitamin B6 přispívají k normální psychické činnosti a k normální činnosti nervové soustavy.“** Pro elektrolytickou rovnováhu a energetický metabolismus je zdrojová věta All-in-One uvedená výše; není to schválení tvrzení „výkon“ nebo převod na libovolné „hydratace“.
- Dodané: **„Brain & Focus je zaměřený na soustředění a mentální výkon, zatímco Care Free na psychickou pohodu a zvládání stresu.“** Produktový soubor Brain & Focus neobsahuje schválené EFSA tvrzení pro slib lepšího soustředění či mentálního výkonu. Nevymýšlíme mu schválenou alternativu; neutrálně lze psát „Brain & Focus je doplněk stravy s rostlinnými extrakty a fosfatidylserinem.“ (návrh neutrální identifikace, ne schválené zdravotní tvrzení). Pro Care Free je doslovnou zdrojovou alternativou věta o hořčíku a B6 výše; ta nepotvrzuje slib zvládání stresu.
- Věta **„UFIRST All-in-One obsahuje více než 85 složek…“** popisuje složení, ne zdravotní účinek. Věta o láhvi a míchátku popisuje obsah boxu. Závěrečné **„Ideální vánoční dárek pro každého, kdo chce pečovat o své tělo i mysl…“** je obecné wellness sdělení, nikoli léčba; „pro každého“ se nesmí vykládat jako potvrzení vhodnosti pro děti, těhotné, kojící nebo lidi s kontraindikacemi. Produktová upozornění a etikety zůstávají rozhodující.

Před publikací je potřeba tyto tři efektové věty posoudit nebo použít odpovídající zdrojové alternativy. Samotné zveřejnění pracovního návrhu v Gitu není právní schválení. Původní chybějící vánoční datum ve FAQ zůstává samostatně otevřené; tato revize ho neměnila.

## Co bylo skutečně ověřeno a co ne

- Přesná shoda nového odstavce v obou dlouhých HTML a umístění bezprostředně za jejich hlavním nadpisem.
- Šest různých SVG, skutečné dekódování vložených obrázků v Chromium, nezměněné popisky v krátkém i dlouhém bloku, zaoblené linkové obrysy a vizuální kontrola kontaktního přehledu.
- Izolovaný náhled nadpisu, odstavce a ikon na 1280 a 390 px s původním přesně připnutým CSS boxů a aktuálním Git frameworkem. Jen náhled nastavuje přirozenou výšku vyjmuté ikonové mřížky: v náhledu chybí její sousední produktová fotografie. Tento prezentační přepínač není v dodaném HTML a neprokazuje nové plnohodnotné živé nasazení.
- Pokus o novou úplnou kontrolu v e-shopu narazil dvakrát na **HTTP 403**. Při testu nad autentickým dříve uloženým veřejným HTML byly blokované i některé závislosti, fotografie a vložené detailové popisy. Výsledek se neoznačuje za úspěšnou živou kontrolu; síťové chyby a JS chyby chybějících shopových závislostí jsou zachované v testovém JSON. Původní čtečky, fotografie a jejich skripty byly ponechané doslova, bez zásahu do provozního webu.
- Přehled ikon je čistý izolovaný náhled, ne screenshot úspěšně načtené živé produktové stránky. Nejsou v něm fingované fotografie ani úspěšné síťové odpovědi.

## Použité zdroje, model a cena

Pavlova oprava v aktuálním vlákně, čerstvý Git snapshot před změnou, `brand/RULES.md`, produktové soubory All-in-One / Care Free / Brain & Focus, kreativní poznámky značky. V původním dodaném vizuálním manuálu `gl_U_F1RST_brand_manual_a4_05_NHLD.pdf` v1.0 (2026) byly přečtené strany 13–17 pro paletu a typografii; globální styly se touto revizí nemění. Nové SVG jsou UI návrh podle zadání, ne převzaté tiskové piktogramy z obalu.

Model: `gpt-6.1-sol`. SVG a PNG náhled vytvořené kódem, bez použití placeného generátoru. Externí obrazové/video generování: 0 spuštění. Cenu jazykového běhu platforma neposkytla.
