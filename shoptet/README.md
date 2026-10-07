# Dárkové boxy – verze s vycentrovanými pilulkovými tlačítky

Pro vložení do HTML režimu **dlouhého popisu** použij celý obsah příslušného souboru:

- `beauty.html` – Collagen Beauty
- `hormonal.html` – Hormonal
- `longevity.html` – Longevity
- `slim.html` – Slim
- `ufirst.html` – U F1RST

Nahraď celý předchozí dlouhý popis. Nevkládej kód do krátkého popisu ani jako obyčejný text ve vizuálním editoru. Fotografie, obsah boxů a krátké popisy zůstávají beze změny.

## Co se změnilo

- Vycentrované decentní pilulky, jemný obrys v barvě příslušné značky; mobilní tlačítko uprostřed přes šířku karty.
- Místo velkého vloženého skriptu je malý spouštěč. Kompletní čtečka se stáhne až při prvním kliknutí z veřejného repozitáře přes jsDelivr, připnutá ke commitu `912c837872b8ed6b882746590b0b7aaf94f8f44c` a ověřená pomocí SRI SHA-384. Nejde o pohyblivou poslední verzi.
- Při selhání CDN se zobrazí zpráva a možnost opakování. Obsah produktu se dál načítá z jeho kanonické stránky, zůstává uvnitř boxu a během návštěvy se ukládá do paměti.
- Každý fragment má méně než 32 kB. Na testovací živé stránce byl předchozí velký inline skript prokazatelně uříznutý uprostřed; přesný limit ani důvod zkrácení v administraci nebyl ověřen.

## Ověření a meze

Všech 25 produktových tlačítek otestováno proti uloženým skutečným produktovým HTML: 20 detailů, 5 hlášek prázdného popisu láhve. Čtyři šířky pro každý box, kontrola vystředění, zavření, opakování, cache, selhání CDN, chybného SKU a nebezpečného obsahu. Beauty navíc ověřena v lokální kopii živé Shoptet šablony se skutečnými požadavky na CDN a produktové stránky. Žádný test neprovedl nákup.

Zdrojová láhev nemá podrobný popis. U ananasového kolagenu zůstává v převzatém obsahu v úzkém mobilním panelu vnitřní přesah některých benefitů; oprava pilulek nemění jeho zdrojové rozvržení. Samostatné překryvné bannery/chat a sticky košík e-shopu nejsou součástí této změny.

Publikace do Gitu není nasazení do Shoptetu. Po uložení v administraci je třeba zkontrolovat skutečně publikované HTML a kliknutí; místní test neumí garantovat, že editor kód nezmění.

`web/` obsahuje stejné upravené plné dokumenty. Starší `nahledy/darkove-boxy.html` je historický náhled před pilulkami, nikoli zdroj pro nasazení.

## Produktové náhledové fotografie

Karty nyní používají přímo ověřené URL úvodních obrázků z hlavní galerie jednotlivých produktů. Celková fotografie dárkového boxu se nemění. U láhve má zdrojová stránka pouze chybějící obrázek, proto zůstává původní připravená cesta. Jde o převzetí aktuálních URL, ne o dodatečné stahování celých produktových stránek při prvním renderu. Pokud u produktu nahraješ jinou fotografii s novou URL, odkazy v boxech bude potřeba znovu obnovit; popisy dál zůstávají dynamické.

## Barevné sladění boxů

U F1RST: PANTONE 3105 C, dodané RGB (91, 207, 222), web `#5bcfde`. Ostatní čtyři boxy: PANTONE 3517 C, dodané RGB (217, 8, 23), web `#d90817`. Barvy zadal Pavel v pracovním vlákně a potvrdil sladění s grafikou boxů. Jde o barevnost těchto stránek, ne o změnu celého brand manuálu. Světlá tyrkysová je v plochách a akcentech; text je tmavý kvůli čitelnosti. Produktové fotografie ani styly načteného kanonického detailu se nepřebarvují. Stejná paleta je i v krátkých popisech v `web/*/maly/`.
