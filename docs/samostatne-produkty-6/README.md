# Šest samostatných produktů – finální Git předání
Pouze produkty **51, 452, 57, 99, 84, 357**. Publikace je omezena na Git; žádné nasazení do e-shopu ani CMS. Původní účinková tvrzení nejsou tímto předáním nově právně schválena.
## Soubory a náhledy
- [Samostatný offline náhled se stažením všech HTML/CSS](handoff/Golden-Life-6-produktu-predani.html) – stáhněte přes **Raw** a otevřete v prohlížeči.
- [101 plných screenshotů](screenshots/) a [HTML rozcestník](screenshot-index.html).
- [Manifest finálních souborů a SHA-256](delivery-manifest.json).
- [Oddělené obsahové výhrady](content-review.cs.md), nikoli zákaznické HTML.
## Produkty
- **51 – Beauty Body & Soul®**: [dlouhý HTML](../../web/Golden%20Life%20Beauty%20Body%20Soul/Golden-Life-Beauty-Body-Soul-cz.html), [krátký HTML](../../web/Golden%20Life%20Beauty%20Body%20Soul/maly/Golden-Life-Beauty-Body-Soul-maly-cz.html), [vlastní CSS](../../user/documents/upload/css/golden-life-barvy-beauty-body-soul.css)
- **452 – Bikini Body**: [dlouhý HTML](../../web/Golden%20Life%20Bikini%20Body/Golden-Life-Bikini-Body-cz.html), [krátký HTML](../../web/Golden%20Life%20Bikini%20Body/maly/Golden-Life-Bikini-Body-maly-cz.html), [vlastní CSS](../../user/documents/upload/css/golden-life-barvy-bikini-body.css)
- **57 – Good Sleep & Night Burn**: [dlouhý HTML](../../web/Golden%20Life%20Good%20Sleep%20Night%20Burn/Golden-Life-Good-Sleep-Night-Burn-cz.html), [krátký HTML](../../web/Golden%20Life%20Good%20Sleep%20Night%20Burn/maly/Golden-Life-Good-Sleep-Night-Burn-maly-cz.html), [vlastní CSS](../../user/documents/upload/css/golden-life-barvy-good-sleep-night-burn.css)
- **99 – Miracle Drops**: [dlouhý HTML](../../web/Golden%20Life%20Miracle%20Drops/Golden-Life-Miracle-Drops-cz.html), [krátký HTML](../../web/Golden%20Life%20Miracle%20Drops/maly/Golden-Life-Miracle-Drops-maly-cz.html), [vlastní CSS](../../user/documents/upload/css/golden-life-barvy-miracle-drops.css)
- **84 – Vitamín C**: [dlouhý HTML](../../web/Golden%20Life%20Vitamin%20C/Golden-Life-Vitamin-C-cz.html), [krátký HTML](../../web/Golden%20Life%20Vitamin%20C/maly/Golden-Life-Vitamin-C-maly-cz.html), [vlastní CSS](../../user/documents/upload/css/golden-life-barvy-vitamin-c.css)
- **357 – Xpress Hair Grow s biotinem**: [dlouhý HTML](../../web/Golden%20Life%20Xpress%20Hair%20Grow/Golden-Life-Xpress-Hair-Grow-cz.html), [krátký HTML](../../web/Golden%20Life%20Xpress%20Hair%20Grow/maly/Golden-Life-Xpress-Hair-Grow-maly-cz.html), [vlastní CSS](../../user/documents/upload/css/golden-life-barvy-xpress-hair-grow.css)

## Co je změněno a co zůstává zachováno
- Odstraněny interní návrhové/právní/redakční poznámky. Povinná produktová upozornění zachována. Úplný inventář původní přípravy je v `qa/preparation-preservation.json`.
- 51: opravené skutečně nefunkční mobilní rozbalování. 452: dva dlouhé popisky při 320 px zůstávají uvnitř karet. 51/452/57: vlastní hero/CTA nepřebírá fotografii cizího SKU. Nákupní atributy a logika zůstávají stejné.
- Mezitím aktualizovaný `main` obsahoval výhradně URL změny piktogramů bez koleček v těchto souborech. **58 těchto existujících oprav je zachováno**, nikoli přepsáno staršími obrázky. Všech 31 nových HTTPS PNG bylo načteno a jejich bytes ověřeny proti pinned Git blobům; přesný důkaz reverzibility je v `merge-proof.json`.
- Žádné změny společného CSS/JS, překladů, balíčků, Double ani jiných SKU. Testy používají aktuální společné závislosti z výchozího main.

## Skutečné ověření finální sloučené verze
- Chromium **156.0.8078.4**, 6/6 produktů, **108** layoutových scénářů, **172** dialogových scénářů, **24** mobilních roundtripů, žádné `pageerror`. Šířky 320/390/768/820/1024/1440 px, světlý a tmavý host, úzké short hosty 280/320/420 px, no-JS fallback.
- 6/6 nativních foto/CTA fixture: dvě skutečně načtené vlastní fotografie, špatné productId, cizí fotografie při správném productId a nezměněný CTA cíl bez odeslání nákupu.
- Všech **99 tabulkových buněk**, **188 výskytů IMG**, **43 panelů**, celé vlastní texty a původní skripty přípravy jsou zachovány; jediná integrační změna jsou uvedené ikonové URL. 30 JS skriptů prošlo `node --check`.
- CSS-only srovnání 452 při 390 a 1440 px: **0 změněných pixelů**.
- Náhledový soubor byl samostatně testován přes `file://`: 24 responzivních scénářů, 96 otevření/zavření obrázků, všech 18 produkčních souborů skutečně staženo a ověřeno SHA-256; bez externích požadavků.

## Limity
Izolovaný same-origin Chromium test, nikoli živý celostránkový Shoptet, fyzický Safari/iPad, skutečný nákup ani právní schválení účinkových tvrzení. Video 51 a jeho autentický poster zachovány; přehrávání nebylo testováno. V QA jsou záměrně blokovány MP4 a nepoužitá Material Symbols stylesheet.
