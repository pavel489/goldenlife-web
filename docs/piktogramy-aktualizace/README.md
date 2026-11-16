# Aktualizované piktogramy — HTML + styly

## Dokončená dávka

- **89 HTML:** 46 aktuálních souborů v `web/` a 43 navazujících pomocných podkladů `shoptet/piktogramy-dalsi/`.
- **180 výměn obrazových adres:** napojení poslední opravy šesti motivů, vlasových kořínků a přijatých piktogramů Bikini Body v3. Zachované popisky a barevnost.
- **28 CSS**: společný stylesheet a 27 lokálních dark overrides už nekreslí pozadí, rámeček, zaoblenou kartičku, stín ani hover nadzvednutí `.p-icon-card`.
- **5 samostatných HTML** má totéž odstraněné ve vlastním vloženém CSS, protože sdílený stylesheet nepřebírají. Tyto soubory jsou zahrnuté v celkových 89 HTML.
- Jednotná referenční čára 2 při konstrukci 64 × 64; zaoblené konce a spoje. Opravuje se skutečná kresba i dekorativní obal, ne jen vnější radius.

## Aktuální produktové složky se změnou HTML
- Golden Life Beauty Body Soul
- Golden Life Beauty Star
- Golden Life Bikini Body
- Golden Life Double Slim SOS Burner
- Golden Life Hormonal Duo
- Golden Life Hormonal Trio
- Golden Life Slim Extreme Collagen box ananas
- Golden Life Slim Extreme Collagen sacek ananas mango
- Golden Life Vitamin C
- Golden Life Xpress Hair Grow

Sdílené CSS má širší dosah než tento seznam; přesné změněné soubory jsou v `soubory.csv` a `zmeny-css.json`. Pomocné Shoptet podklady nejsou zárukou aktuálního exportu nativního CMS.

## Co je ověřené

- 27 veřejných HTTPS PNG: HTTP 200, image/png, přesná shoda bajtů se zdrojem, rozměry a transparentnost.
- 12 použitých SVG masterů: 2 jednotky, round caps/joins, fill none, konstrukční plocha 64 × 64.
- **196 finálních Chromium průchodů** skutečných izolovaných bloků z 49 HTML: mobil/desktop 390/1280 px, světlá/tmavá větev; všechny ikony dekódované a viditelné, `.p-icon-card` bez namalovaného pozadí/rámečku/stínu. Včetně pěti skutečně uložených inline oprav.
- Samostatná širší CSS regrese: 556 scénářů / 139 dokumentů; chráněné CTA, fotografie ingrediencí a ovladače mají stejné sledované styly. Její původní snapshot předcházel finálnímu propojení části artworku; integrační kontrola výše testuje finální soubory.
- U všech změněných HTML zachované texty, tabulky, skripty a počty IMG; přesné CSS editace ověřené proti zdrojovým bajtům. CTA a nákupní logika se tímto úkolem nemění.

## Hranice a postup nahrání

**Git není živý Shoptet.** Z tohoto úkolu nebyl uložen žádný CMS popis ani přepsaný živý soubor. K přenosu patří odpovídající krátký/dlouhý HTML a uvedené CSS (společné i produktové). Zachovejte případné novější úpravy živého obsahu; nevkládejte starší pomocný export přes novější text bez porovnání.

Tato dávka nezavádí nový master pro každou jinou rodinu ikon. Starší `piktogramy-bez` a line-icon sady některých boxů zůstávají samostatnými rodinami. Nelze proto tvrdit, že celý živý e-shop už používá právě tuto nejnovější sadu. Archivní dokumentace a historické screenshoty se hromadně nepřepisovaly.

Finální prohlížečová kontrola jsou izolované bloky bez sousední fotografie, bez nákupu a bez externě načítaných fontů; není to plný funkční test všech stránek ani nativního editoru. Přiložený HTML přepínač slouží pouze k prohlížení ikon a původních popisků.

Zdravotní tvrzení v převzatých popiscích nejsou grafickou opravou právně schválená. Konkrétní výhrady jsou odděleně v `TVRZENI.md`, ne v zákaznickém HTML.

## Původ

Aktuální Git snapshot `30fdbcd0bfa87b381bb42347e60babb7681b3d26`, původní přesná mapování a opravené SVG/PNG; schválená grafická revize Bikini Body v3; pravidla značky Golden Life. Model GPT‑6.1‑sol, Python/SVG/Pillow/Chromium. Bez placené obrazové generace. Cena modelového provozu není vyčíslena.
