# Systémový tmavý režim — 14 připravených produktů

**Stav: implementováno a otestováno v pracovních náhledech; předání přes Git, nikoli nasazení na živý e-shop.**

## Co se mění

- Automatické přepínání podle `prefers-color-scheme: dark`; žádné nové tlačítko, skript, tracking ani závislost.
- Pouze dodatky do14 existujících `golden-life-barvy-*.css`. Dlouhých/krátkých HTML se netýká žádná editace; společný framework zůstává byte-identický. Oba popisy už svoje téma importují.
- Tmavé lokální podklady, čitelný text, tabulky, karty, CTA, ingredientové dialogy, mobilní rozbalování a jeho fade, hover a klávesnicový focus. Pro464/467 jsou výslovně ošetřeny jejich zděděné legacy modalové plochy a zavírání.
- Texty, tabulkové údaje, pořadí, fotografie/IMG atributy, skripty a nákupní logika zůstávají beze změn. Zachované jsou i novější tabletové opravy635/641.
- Rozsah jsou **produktové popisy**, ne globální hlavička, menu, košík, footer ani celý Shoptet. Styly se nevztahují na U F1RST nebo jiné nevybrané produkty. Negativní kontrola cizího tématu neprokázala únik barev ani `color-scheme` na body.

## Vizuální řešení

Charcoal podklad `#19171d`, panely `#25212b` a `#302a36`, text `#f4eff4`. Pro tmavé UI jsou od původní barvy konkrétního produktu odvozené světlejší pracovní akcenty a párovaný tmavý text CTA/hlaviček tabulek. Nejde o nové oficiální swatche ani změnu světlých brandových tokenů. Původní barva je v dark dodatku uchovaná jako `--gl-dark-source-primary`; všechny původní light deklarace zůstávají přesně zachované.

Skutečné fotografie a jejich barevné pixely nejsou invertované. Světlá lokální podložka podporuje průhledné packshoty a molekulu; obrysové UI glyphy mohou mít vlastní neutrální dark variantu filtru, výjimky již zbarvených PNG zůstávají chráněné. Dekorativní data-SVG graf má pouze dark barevnou variantu, ne změnu křivky nebo dat.

## Skutečné testy finálního výstupu

- **168/168 scénářů:**14 produktů ×2 schémata ×6 viewportů390×844,767×1024,768×1024,820×1180,1024×768 a1440×1000 CSS px. Rozměry jsou ověřeny uvnitř skutečných dokumentů.
- **364** pointer otevření/zavření ingredientových dialogů, **92** cyklů rozbalit/sbalit a **32** cyklů nativních FAQ/historických details. Všechny zaznamenané cykly prošly.
- **342** dark stavů s CSS kontrastní kontrolou, včetně dialogů, rozbaleného obsahu a hover. Zahrnuté jsou i jednopísmenné glyphy „+“ a zavírací křížky. Žádná zjištěná CSS textová kontrastní chyba ve finální sadě.
- Screening používá složené RGBA podklady a vzorkované gradienty; prahy4,5:1 pro běžný text a3:1 pro velký text/UI glyphy. Není to kompletní certifikace WCAG.
- **28** skutečných pixelových srovnání bannerů/hero a krátkých popisů při820px je beze změny; **14** přepnutí dark→light obnovilo původní paletu.
- **14** produktů prošlo dark kontrolou bez JavaScriptu včetně pointer otevření/zavření prvního CSS dialogu.
- Skutečná klávesnicová navigace aktivovala14 focus-visible stavů; světlý obrys doplňuje tmavý vnitřní lem pro čitelnost na různých podkladech. Nejde o tvrzení o kompletním focus-trapu nebo screen-reader auditu.
- **84** dark scénářů ověřilo stejné SHA-256 zdrojových IMG řetězců a nepřítomnost barevné inverze/filter transformací na fotografických IMG. Chybějící obrázky se nepočítají jako zobrazené fotografie.
- Syntax všech14 dodatků prošla tinycss2. Každý dodatek obsahuje pouze systémový dark media blok; žádná nová light nebo globální CSS pravidla.
- Žádné JS chyby ani externí HTTP(S) request eventy v izolovaných offline testech. Nákupy a síťové operace jsou v náhledech záměrně vypnuté.

## Zkontrolované podklady

Zdroj je přesný Git main `72b07636ac837563428b7673ec82b628f6c3a59c`. Přes Composio byly přečteny43 vlastní soubory:14 témat,28 HTML a společné CSS; záznamy Git blob SHA a SHA-256 jsou v source-manifest.json. Všechny bajty se shodují s dříve předanými testovými podklady, kromě známých append-only tabletových oprav635/641, které byly do fixture přesně přeneseny před dark dodatkem.

Pro všechny14 produktů vznikly skutečné světlé/tmavé snímky banneru nebo hero. Vizuálně otevřené byly přehledy celé14členné sady, detail dialogu467 a finální srovnání383/550; nejde o ruční prohlédnutí každého pixelu celé dlouhé stránky.

## Otevřené limity — nic z toho není skrytě označené jako hotové

- Část skutečných fotografií/piktogramů z dřívějších podkladů chybí. Nebyly vymyšlené ani nahrazené falešnými úspěšnými odpověďmi. U550 přetrvávají nedostupné grafické zdroje krátkého popisu.
- 44 opakovaných hodnocení textu leží nad CSS obrazovým podkladem. Kontrast proti skutečným fotografickým pixelům není tímto číselným CSS screeningem certifikovaný, zvlášť když zdroj chybí.
- Některá původní zalomení dlouhých názvů, například ANANAS–MANGO u467 při tabletové šířce, zůstávají stejně jako ve světlém zdroji. Tento barevný krok je nepředělává ani neprohlašuje za finálně vizuálně schválená.
- Aktuální nativní šablona e-shopu, skutečné Safari/iPad, forced-inversion rozšíření a kompletní přístupnost nejsou ověřené. V tomto běhu nebyl znovu obcházen ani testován dřívější IP blok shopu/CDN.
- V aktuálních fragmentech nebyl doložen samostatný chybový renderer nákupu. Přidané scoped barevné fallbacky nejsou důkazem otestované skutečné chybové transakce; žádný nákup nebyl odeslán.
- Historická účinková tvrzení v podkladech a snímcích nebyla měněna ani právně schválena. Platí původní obsahové výhrady; interní varování zůstala zachovaná.

## Nasazení je samostatný krok

Pro budoucí autorizované nasazení stačí aktualizovat těchto14 úplných CSS souborů na jejich stávajících shopových cestách. Do HTML nepřidávat třetí import ani další JS. Je nutné ověřit přesné veřejné bajty, cache a nativní vykreslení po uploadu. Tento Git commit nic nenahrává do Shoptetu a nemění jeho nastavení.

## Soubory k nasazení

- **ID351 — Beauty Star:** [`golden-life-barvy-beauty-star.css`](../../user/documents/upload/css/golden-life-barvy-beauty-star.css)
- **ID383 — Slim Extreme Collagen box s příchutí ananasu:** [`golden-life-barvy-slim-extreme-collagen-box-ananas.css`](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-box-ananas.css)
- **ID544 — Beauty Longevity NAD+:** [`golden-life-barvy-beauty-longevity.css`](../../user/documents/upload/css/golden-life-barvy-beauty-longevity.css)
- **ID644 — Woman Hormonal balance:** [`golden-life-barvy-woman-hormonal-balance.css`](../../user/documents/upload/css/golden-life-barvy-woman-hormonal-balance.css)
- **ID635 — Hormonal Balance noční GLP-1 drink:** [`golden-life-barvy-glp1-woman-balance.css`](../../user/documents/upload/css/golden-life-barvy-glp1-woman-balance.css)
- **ID641 — Hormonal Balance noční GLP-1 drink sáček:** [`golden-life-barvy-glp1-woman-balance-sacek.css`](../../user/documents/upload/css/golden-life-barvy-glp1-woman-balance-sacek.css)
- **ID550 — Anti-Age longevity NAD+:** [`golden-life-barvy-anti-age-longevity.css`](../../user/documents/upload/css/golden-life-barvy-anti-age-longevity.css)
- **ID600 — Beauty Longevity NAD+ sáček:** [`golden-life-barvy-beauty-longevity-sacek.css`](../../user/documents/upload/css/golden-life-barvy-beauty-longevity-sacek.css)
- **ID168 — Slim Extreme Collagen:** [`golden-life-barvy-slim-extreme-collagen.css`](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen.css)
- **ID473 — Slim SOS Burner:** [`golden-life-barvy-slim-sos-fat-burner.css`](../../user/documents/upload/css/golden-life-barvy-slim-sos-fat-burner.css)
- **ID476 — Slim GLP-1 Activator s Berberinem:** [`golden-life-barvy-slim-glp-1-activator.css`](../../user/documents/upload/css/golden-life-barvy-slim-glp-1-activator.css)
- **ID416 — Slim Extreme Collagen sáček s příchutí ananasu:** [`golden-life-barvy-slim-extreme-collagen-sacek-ananas.css`](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-sacek-ananas.css)
- **ID464 — Slim Extreme Collagen box s příchutí ananas - mango:** [`golden-life-barvy-slim-extreme-collagen-box-ananas-mango.css`](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-box-ananas-mango.css)
- **ID467 — Slim Extreme Collagen sáček s příchutí ananas - mango:** [`golden-life-barvy-slim-extreme-collagen-sacek-ananas-mango.css`](../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-sacek-ananas-mango.css)

## Důkazy a reprodukce

`qa-summary.json`, `qa-results.json`, `verification.json`, `visual-verification.json`, `source-manifest.json`, `changes.json`, `build_dark.py`, `test_dark.py`, `contrast.js`, `verify_artifacts.py`. QA je navázaná na SHA-256 přesného build manifestu. Velké base64 obrázky jsou v protokolu nahrazené skutečnými SHA-256, nikoli duplicitně ukládané nebo vymyšlené.

Model GPT-6.1-Sol; Python, Chromium/Playwright, tinycss2 a skutečné existující referenční soubory. Neproběhla placená obrazová generace ani nákup služby. Cenu modelového běhu a connectorů tento runtime nevyčísluje.
