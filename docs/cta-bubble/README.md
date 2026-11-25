# CTA – bublina přes fotografii a dva informační boxy

Pokračování pro stejných **11 nových produktů**, pouze v Gitu. Žádné uložení do Shoptetu. Vychází z přiloženého ručně anotovaného obrázku.

## Úpravy
- Horní rohy skutečné fotografie jsou oříznuté samostatným zaobleným fotoobalem (`overflow:hidden` + clip-path). Ani přiblížený obrázek nevyčnívá.
- Původní nadpis se přesunul přes spodní hranu fotografie do samostatné zaoblené bubliny. Žádný duplicitní nadpis a žádný přepis názvu.
- Denní dávka/použití a balení jsou dvě stejně vysoké samostatné karty vedle sebe, včetně 320px telefonu.
- Komplet produktu zůstává viditelný nad bublinou; pro aktuální fotky se mírně upravilo pouze CSS přiblížení a posun, nikoli soubory nebo URL.
- Cena, fotografie, obsah dávkování/balení a nativní nákupní logika zůstávají původní. Všechny zákaznické texty, image atributy, kompletní scripts a krátké popisy jsou ověřeně stejné.

## Rozsah
- ID 383: [Slim Extreme Collagen box s příchutí ananasu](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas/Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html)
- ID 174: [Slim & Detox Super energy booster Power+](../../web/Golden%20Life%20Slim%20Detox%20Power%20Plus/Golden-Life-Slim-Detox-Power-Plus-cz.html)
- ID 464: [Slim Extreme Collagen box s příchutí ananas - mango](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas%20mango/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-cz.html)
- ID 467: [Slim Extreme Collagen sáček s příchutí ananas - mango](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas%20mango/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-cz.html)
- ID 416: [Slim Extreme Collagen sáček s příchutí ananasu](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-cz.html)
- ID 544: [Beauty Longevity NAD+](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20d%C3%B3za/Golden-Life-Beauty-Longevity-NAD-doza-cz.html)
- ID 550: [Anti-Age longevity NAD+](../../web/Golden%20Life%20Anti-Age%20Longevity%20NAD%2B/Golden-life-Anti-Age%20Longevity%20NAD%2B.html)
- ID 51: [Beauty Body & Soul®](../../web/Golden%20Life%20Beauty%20Body%20Soul/Golden-Life-Beauty-Body-Soul-cz.html)
- ID 600: [Beauty Longevity NAD+ sáček](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20s%C3%A1%C4%8Dek/Golden-Life-Beauty-Longevity-NAD-sacek-cz.html)
- ID 57: [Good Sleep & Night Burn](../../web/Golden%20Life%20Good%20Sleep%20Night%20Burn/Golden-Life-Good-Sleep-Night-Burn-cz.html)
- ID 99: [Miracle Drops](../../web/Golden%20Life%20Miracle%20Drops/Golden-Life-Miracle-Drops-cz.html)

## Nasazení a kompatibilita
Upravených 11 dlouhých HTML a `user/documents/upload/css/golden-life-cta-native-v2.css` patří k sobě. CSS import má novou verzi `?v=bubble-2`; vnějšímu CTA je přidaný opt-in `data-gl-cta-skin="bubble-2"`.
Starý CSS obsah zůstává byte-for-byte jako prefix; všechny nové definice jsou omezené tímto skin markerem. Starší HTML bez markeru tak nepřebírá nové rozložení. V izolované regresi 11 původních CTA mají shodné vypočtené styly a geometrii. Screenshoty vykázaly drobné rozdíly vykreslení hran (počty v QA), proto se netvrdí úplná pixelová identita.
Cena/košík JS se nemění ani neuploaduje znovu. Při pozdějším nasazení aktualizovat tuto CSS a připravená HTML; v tomto kroku se nic do e-shopu neukládalo.

## Ověření
77/77 finálních Chromium scénářů: 320/375/768/1280 px, tmavé okolí, chybějící native host a bez JS. Zvlášť zkontrolované zaoblení fotoobalu, překryv bubliny, geometrie dvou karet, nezakrytý ověřený obal, cena/tlačítko, změny ceny a skutečné další fotografie, špatné ID, vypnutý nákup a výměna formuláře.
11 delegací na nativní tlačítko testováno bez skutečného odeslání košíku. Offline příloha prošla přepínáním všech 11 produktů a obou šířek: 22 scénářů, nákup vypnutý, žádné externí požadavky.
Hashe přesných finálních souborů v `source-manifest.json`; úplný zkrácený protokol v `qa-summary.json`. Nejde o nasazený Shoptet, fyzický Safari ani nové právní/produktové schválení. Předchozí věcné výhrady zůstávají v [CTA v2](../cta-native-v2/README.md).

## Podklady a zpracování
Aktuální Git main, vložená obrazová korektura z tohoto vlákna, existující skutečné hlavní fotografie a brand/RULES.md. Žádný nový účinkový claim.
Model gpt-6.1-sol, Python/Chromium/Playwright a existující Composio GitHub. Bez placené obrazové generace; cena modelu/nástrojů není vyčíslená.