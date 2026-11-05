# Collagen Slim a Collagen Beauty — nové texty a vykání

## Co bylo ověřeno a změněno

Při převzetí byl Collagen Beauty v Gitu zapracovaný podle předchozího Beauty zadání, ale některé odstavce obsahovaly tykání stejně jako dodaný originál. Collagen Slim v té chvíli ještě obsahoval starší text. Nově zaslaný text se týká **Collagen Slim**, nikoli Beauty; oba produkty nebyly sloučeny ani zaměněny.

- **Collagen Slim:** celé aktuální české zadání je zapracované do obou dlouhých i obou krátkých českých souborů. Zachovaný obsah, částky, produkty, pořadí karet a sedm FAQ; 13 strukturovaných textových polí upravených pouze do vykání. Náhodné označení „Krátký“ před slovem „Darujte“ není součástí zákaznického textu.
- **Collagen Beauty:** předchozí text zůstává přiřazený správnému boxu. V obou dlouhých českých souborech je odstraněné tykání. Krátké popisy už vykaly, proto se jejich bajtově nezměněné kopie znovu nestagují. Předchozí oprava PNG odkazů je zachovaná.
- Vlastní zákaznické odstavce, CTA, FAQ i přístupové popisky obou produktů mají vykání. Doplněný lokální skript upravuje pouze vlastní technické hlášky čtečky, ceny/dostupnosti a košíkového stavu; nemění nákupní operace ani sdílené soubory. Otestovaný úspěšný i chybový stav čtečky a výchozí stav dostupnosti. Texty samostatných dynamicky importovaných produktových stránek zůstávají samostatnými kanonickými zdroji a tento krok je globálně nepřepisuje.
- Originální SCRIPT a STYLE obsahy zůstaly zachované; přidaný lokalizační bootstrap je samostatný. Původní ID košíku a všechny zdrojové odkazy zůstaly stejné. U Slim zůstává původní root productId prázdný — nezměnil se tím režim přesměrování k nativnímu nákupu.

## Soubory

- `shoptet/slim.html`, `shoptet/slim-kratky.html`.
- Odpovídající existující české soubory v `web/Golden Life Darkovy box Slim/`.
- `shoptet/beauty.html` a odpovídající český dlouhý dokument v `web/Golden Life Darkovy box Beauty/`.
- Název, slogan a SEO pro Slim: `config/slim-darkovy-box-texty-cz.json`. Nejde o automatické uložení nativních polí administrace. Slogan je stejný jako dodaný krátký odstavec, není zbytečně zdvojený v dlouhém popisu.
- Úplný aktuální Slim text s vykáním: `docs/collagen-slim-texty-vykani.md`.
- Přehled původních a upravených polí: `config/collagen-slim-vykani-zmeny.json`.
- Beauty konfigurace zachovává dosavadní název i SEO a eviduje vykání. Původní dokumenty označené „dodané texty“ jsou historický dodaný originál, ne nová verze zákaznického znění.

## Piktogramy a identita

Šestice v dlouhém a krátkém Slim popisu má přesně dodané obsahové popisky a nyní používá skutečné, již existující HTTPS PNG zdroje z opraveného Beauty/Longevity systému. Čtyři symboly a stejná technika masky zachovávají původní kresbu; sáček s ananasovým motivem označuje příchuť ananas a mango, obecný symbol složek označuje berberin a chrom (není chemickým strukturním vzorcem). Žádné nové vložené SVG data URI, žádná nová obrazová generace, žádný nový závislý upload do Shoptetu. Beauty obrázky zůstaly beze změny.

Slim je podle uloženého veřejného snímku nativní produkt **659**, kanonická stránka `https://www.golden-life.cz/golden-life-darkovy-box-collagen-slim/`. Součásti: 464 (ananas/mango), 476 (GLP-1 Activator), 174 (Slim & Detox), 597 (láhev), 653 (míchátko). Beauty zůstává produkt **656** a vlastní ananasový nápoj 383 / Good Sleep 57.

## Skutečné testy a jejich hranice

- Ověřený výchozí vzdálený Git: `88656688faab99cb317eb9354c761371f97a5100`. Publikace musí navázat na aktuální větev, znovu zkontrolovat všechny dotčené bloby a zachovat případné souběžné cizí změny.
- V obou Slim dlouhých zdrojích ověřeno všech 59 celých očekávaných obsahových položek, v obou krátkých 7 (celý odstavec a šest popisků).
- Všech osm připravených zákaznických HTML zkontrolováno na tykací zájmena, slovesa i další české tvary končící na „š“; nulové nálezy. Kontrola nepočítá historické původní řetězce uvnitř lokalizačního mapování jako zákaznické oslovení.
- Chromium, vykonané skutečné HTML bootstrapy, šířky **1440 a 390 px**, oba produkty. Bez horizontálního přetékání dlouhých a krátkých bloků, dvanáct načtených ikon na produkt a sedm FAQ. Všech sedm FAQ i krátký obsah otevřeno/zavřeno skutečným kliknutím na každé šířce.
- Pro každý produkt na obou šířkách otevřeno/zavřeno všech pět čteček a první znovu otevřena. Správná aktivní ID, odpovídající nadpisy a podstatný obsah z uložených skutečných veřejných snímků; žádné importované SCRIPT prvky. Ověřené vykání technických hlášek po načtení i při simulovaném chybovém textu, nikoli pouze statické zdrojové odstavce. Ověřen Enter u FAQ. Žádné zachycené JS chyby.
- Fotografie a kompletní nativní šablona nejsou v tomto offline testu certifikované. Zablokované fotografie nebyly nahrazené falešnými úspěšnými odpověďmi. Skutečné veřejné PNG ikony se stahovaly z GitHubu, ostatní povolené závislosti a čtečkové podklady byly ze skutečných uložených bajtů. Do košíku se nic neodesílalo.
- Vizuálně prohlédnutý krátký Slim mobilní blok a celkový desktopový dlouhý blok. Úplné výsledky: `tests/collagen-slim-beauty-vykani-results.json`.
- Toto je **Git předání, ne živé nasazení**. Kvůli dříve potvrzenému aktivnímu HTTP403 IP bloku nebyly v tomto kroku opakované požadavky na Shoptet ani pokus obejít omezení. Nabídka, fotografie a přesný současný import na e-shopu nejsou nově živě ověřené.

## Obsahové body před živým zveřejněním

- Ve FAQ zůstává `[DOPLŇ DATUM]`; termín nebyl dodán a nevymýšlel se.
- Částky 3 890 Kč a 4 500 Kč jsou podle nového zadání, rozdíl 610 Kč je spočítaný v Pythonu; nebyly měněné skutečné cenové údaje v administraci. Stejně tak hodnocení/recenze zůstávají pracovní dodané znění, ne nové živé ověření.
- GLP-1 karta uvádí „485 mg berberinu z extraktu z dřišťálu“. Vlastní produktový soubor eviduje **485 mg Berberin HCl**, což není bez dalšího stejné označení hmotnosti jako čistý berberin. Tentýž historický soubor zároveň používá označení „indický dřín“ a má podezřelou jednotku mg u chromu; nelze jej považovat za bezchybnou současnou etiketu. Dodaný text se nepřepisoval potichu. Přesnou formu, botanický zdroj a účinné množství musí potvrdit aktuální etiketa. Návrh přesnější číselné formulace, pokud odpovídá etiketě: „485 mg berberin hydrochloridu v denní dávce“.
- U Beauty stále platí předchozí rozpor zlatobýl/řimbaba u Good Sleep; změna oslovení nebyla schválením či skrytou opravou složení.

## Zdravotní tvrzení — zachována jako pracovní znění, ne schválena implementací

Konkrétní účinkové věty nového Slim zadání:

- „Chrom … přispívá k udržení normální hladiny glukózy v krvi“ v úvodu a kartě GLP-1.
- „Vitamin C přispívá k normální tvorbě kolagenu pro normální funkci kůže.“ pod ikonami a v kartě nápoje.
- „Biotin a zinek přispívají k udržení normálního stavu vlasů a kůže.“
- „Zinek přispívá k udržení normálního stavu nehtů.“
- „Chrom přispívá k udržení normální hladiny glukózy v krvi a k normálnímu metabolismu makroživin.“
- „Kyselina pantothenová, niacin, vitamin B12 a vitamin C přispívají ke snížení míry únavy a vyčerpání.“

Jmenují nosné živiny; doslovná schválení celých těchto konkrétních vět ale ve zpřístupněných vlastních souborech pro všechny uvedené živiny zapsaná nejsou. GLP-1 soubor uvádí, že žádné EFSA claims nezaznamenává. Aktuální individuální ověření EU registru a podmínek receptur nebylo v této implementaci provedeno; nelze tvrdit právní schválení podle názvu automaticky generovaného oddílu.

Vlastní ananas–mango soubor nabízí vedle dodané věty o únavě tuto skutečně zapsanou alternativu:

> Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.

U vitaminu C je ve stejném souboru historicky zapsaná širší věta:

> Vitamin C je důležitý pro tvorbu nového kolagenu, zároveň má pozitivní vliv na imunitní systém, přispívá k ochraně a tvorbě nových buněk, lepší regeneraci organismu a snížení míry únavy.

Je to doslovný zdrojový záznam k produktové kontrole, nikoli nové právní doporučení publikovat jeho celý široký význam. Pro dodaná tvrzení o chromu, vlasech/nehtech/biotinu dostupné přesné produktové soubory schválenou doslovnou alternativu neposkytují. Také obecné sliby krásné pleti, vlasů a nehtů je nutné posuzovat v kontextu celé stránky. Formulace nebyly během převodu do vykání posílené ani nahrazené tvrzením o léčbě.

## Vstupy a výroba

Použit celý nově dodaný Slim text, předchozí Beauty zadání a ověřené současné Git soubory obou produktů, současné HTTPS PNG reference, uložené veřejné snímky správných SKU, `brand/RULES.md` a vlastní produktové soubory ananas–mango, GLP-1 Activator a dříve kontrolované Slim & Detox / Good Sleep. Lidská brandová pravidla se neměnila. Korekce vykání platí pro tento produktový handoff, nikoli pro tykání Goldie při běžné komunikaci s týmem.

Model gpt-6.1-sol. Kódová implementace a testy; **bez placeného obrazového/video generování**. Cena modelového a konektorového provozu není dostupná.
