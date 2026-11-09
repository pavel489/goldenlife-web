# Kontrola tabletového zobrazení před nasazením

**Výsledek: kontrola pracovních offline návrhů proběhla; celé řešení ještě není připravené k nasazení.**

## Rozsah a zdroje

Kontrola navazuje na Pavlovo zadání tabletů a systémového tmavého režimu. Použity byly skutečné, dříve předané samostatné offline náhledy z dávek 3, 4A, 4B, 4C a 4D. Nejde o čerstvě stažený aktuální main ani o živý Shoptet. Neměnily se produktové HTML/CSS, texty, ceny, nákupní funkce ani nastavení e-shopu. Git předání tohoto protokolu není nasazením.

Produkty: 168, 351, 383, 416, 464, 467, 473, 476, 544, 550, 600, 635, 641, 644.

## Co bylo skutečně spuštěno

- Touch-enabled Chromium / Playwright. Skutečné rozměry dokumentu uvnitř iframe ověřeny, nikoli pouze rozměr vnějšího rámu.
- Světlý režim: 768 × 1024, 820 × 1180, 1024 × 768 a breakpoint 767 × 1024 CSS px u každého produktu.
- Pro každý produkt návrat 390 → 768 → 1440 → 820 px; geometrie dlouhého/krátkého popisu, tabulkové texty a vnitřní scrollWidth bannerů.
- Ingredientové dialogy: skutečné pointer otevření a zavření každého dialogu, nikoli pouze syntetický DOM click.
- Systémová tmavá preference při 820 × 1180 px: ověřeno doručení preference a porovnání sledovaných výsledných barev. Nejde o kontrastní certifikaci ani test Dark Readeru.

## Naměřené výsledky

- 54/56 světlých scénářů splnilo nastavenou geometrickou podmínku. Dva scénáře jsou označené pro interní přetékání banneru, ne pro horizontální přetékání celé stránky.
- 364/364 pointer otevření a zavření ingredientových dialogů prošlo.
- 12/14 produktových round-trip kontrol splnilo stejnou přísnou geometrickou podmínku.
- 0 JavaScriptových chyb; 0 externích HTTP(S) request eventů v izolovaných offline viewerech.
- 0/14 produktů změnilo sledovanou paletu při systémové tmavé preferenci. **Tmavý režim v této sadě není implementovaný.**

### Konkrétní nález ID635 a ID641 při 820 px

- Banner má clientWidth 790 px a scrollWidth 796 px, tedy interní rozdíl 6 px. Dlouhý a krátký kořen nepřetékají; texty tabulkových buněk jsou v mezích.
- V banneru vykazuje `.nad-feature` s textem „Podporuje metabolickou rovnováhu“ vnitřní šířku 142 px při clientWidth 130 px.
- Detailní kontrola nezjistila obdélník potomka mimo celý banner. Ve skutečně otevřeném snímku ID635 není viditelně oříznutý hlavní titul. Proto jde o **nález k doladění vnitřního layoutu, nikoli dokázaný ořez nadpisu**. Přiloženy jsou přesné naměřené hodnoty a nezměněné snímky.

## Omezení vizuální kontroly

- Offline podklady už samy označují chybějící zdrojové fotografie; ty nebyly nahrazené maketami. Jejich rozměry, ořez a vliv na finální kompozici nelze z chybějících pixelů schválit.
- Ručně byly v tomto běhu otevřené snímky ID416, ID550 a banner ID635. U ID416 je čitelný krátký popis a úvod banneru; nejde o vizuální revizi celé dlouhé stránky.
- U offline ID550 jsou dva piktogramy v krátkém popisu vykreslené jako plné červené obdélníky; tento vzhled není schválený. Není prokázáno, že se totéž děje na živém webu.
- Automatické PASS znamená pouze uvedenou geometrii a dialogy; ne potvrzení úplných fotografií, správného znění tvrzení, úplného kontrastu, každého FAQ/focus stavu nebo celé živé šablony.
- Fyzický iPad, Safari a čerstvý živý e-shop nebyly testované. V tomto běhu se na shop/CDN neodesílaly nové požadavky po předchozím dočasném IP bloku403.

## Stav před nasazením

Zbývá doladit oba označené bannery, načíst a zkontrolovat skutečné chybějící zdroje včetně piktogramů, implementovat a změřit tmavou paletu a ověřit finální stav ve skutečné šabloně a Safari/iPadu. Nejde o nové schvalování už zadané kontroly ani o souhlas s živým nasazením.

Historická účinková tvrzení zachovaná ve snímcích nejsou nově napsanou ani právně schválenou komunikací; jejich obsahové výhrady z původních předání zůstávají otevřené. Tento běh je neměnil.

## Přehled po produktech

- ID168 — Slim Extreme Collagen: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID351 — Beauty Star: geometrie 4/4, dialogy 20, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID383 — Slim Extreme Collagen box s příchutí ananasu: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID416 — Slim Extreme Collagen sáček s příchutí ananasu: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID464 — Slim Extreme Collagen box s příchutí ananas - mango: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID467 — Slim Extreme Collagen sáček s příchutí ananas - mango: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID473 — Slim SOS Burner: geometrie 4/4, dialogy 20, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID476 — Slim GLP-1 Activator s Berberinem: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID544 — Beauty Longevity NAD+: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID550 — Anti-Age longevity NAD+: geometrie 4/4, dialogy 36, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID600 — Beauty Longevity NAD+ sáček: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.
- ID635 — Hormonal Balance noční GLP-1 drink: geometrie 3/4, dialogy 36, návrat rozměrů nález; tmavá paleta se nepřepíná.
- ID641 — Hormonal Balance noční GLP-1 drink sáček: geometrie 3/4, dialogy 36, návrat rozměrů nález; tmavá paleta se nepřepíná.
- ID644 — Woman Hormonal balance: geometrie 4/4, dialogy 24, návrat rozměrů OK; tmavá paleta se nepřepíná.

## Reprodukovatelnost a původ

Podrobnosti: `results.json`, `summary.json`, `banner-detail.json`, `run_audit.py`, `banner_detail.py`. SHA-256 přesných vstupních offline souborů je v results.json. Běh nevyužil generované fotografie ani syntetické úspěšné síťové odpovědi.

Model: GPT-6.1-Sol; nástroje: Chromium/Playwright, Python. Bez placené obrazové generace. Cenu modelového běhu a connectorů tento runtime nevyčísluje.
