# Krok 4D – kolagenové varianty 416 / 464 / 467

**Připravené a offline otestované pracovní kopie pro předání v Gitu. Není to nasazení do Shoptetu, schválení tvrzení ani dokončení celého bodu 4. Vlastní fotografie zatím nejsou dostupné.**

## Rozsah a zdroje
- **416:** samostatný sáček, příchuť ananas.
- **464:** box se sáčky, příchuť ananas–mango.
- **467:** samostatný sáček, příchuť ananas–mango.

Každý produkt má vlastní bajtově ověřený veřejný archiv, ověřené nativní ID a vlastní tabulky. Předchozí explicitní blokace obchodu/CDN HTTP 403 se neobcházela; v této dávce nebyl nový požadavek na obchod/CDN. Přesný současný stav přístupu není nově měřený.

Komponentový vzor je připravený ananasový box 383 z immutable Gitu `c4e862ff8504f7c9d8283e95a2d1f8f97efd33aa`. Jeho receptura, gramáž, fotografie ani účinkové věty se nepřebíraly jako údaje jiné varianty. Common i původní referenční soubory zůstaly bajtově nezměněné.

## Editovatelné soubory

### 416 · Slim Extreme Collagen sáček s příchutí ananasu
- Dlouhý: `web/Golden Life Slim Extreme Collagen sacek ananas/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-cz.html`
- Krátký: `web/Golden Life Slim Extreme Collagen sacek ananas/maly/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-maly-cz.html`
- Téma: `user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-sacek-ananas.css`

### 464 · Slim Extreme Collagen box s příchutí ananas - mango
- Dlouhý: `web/Golden Life Slim Extreme Collagen box ananas mango/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-cz.html`
- Krátký: `web/Golden Life Slim Extreme Collagen box ananas mango/maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-maly-cz.html`
- Téma: `user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-box-ananas-mango.css`

### 467 · Slim Extreme Collagen sáček s příchutí ananas - mango
- Dlouhý: `web/Golden Life Slim Extreme Collagen sacek ananas mango/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-cz.html`
- Krátký: `web/Golden Life Slim Extreme Collagen sacek ananas mango/maly/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-maly-cz.html`
- Téma: `user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-sacek-ananas-mango.css`

## Co je hotové
Vlastní produktová ID a témata, podporované rozložení `woman-hormonal-balance` / `woman-hormonal-balance-short`, v každém poli jeden STYLE a dva importy (společný soubor první). Ve všech šesti HTML je **nula statických atributů style**. Společný framework a produkty 383/168 se neupravovaly. Nepotřebná ananasová legacy CTA grafika se do nových témat nepřebírala; názvy příchutí jsou černé podle RULES.md.

Zachované jsou úplné vlastní úvody, vysvětlující karty, účinkové texty v označeném interním draftu, návod, skladování, omezení a složení. **315 buněk v 6 tabulkách** má shodné vlastní DOM innerHTML. **18 ingredientových dialogů je zachovaných v původních raw HTML bytech**; navíc jsou 3 věcné bannerové informační panely a vlastní FAQ.

Nová shrnutí 416/467 uvádějí samostatný sáček a jednu dávku, 464 box se sáčky. Rozporné staré údaje balení u 464/467 jsou dostupné jen v jasně označených historických DETAILS, včetně mobilu. Vlastní použití a složení zůstávají dohledatelné.

Výslovně nahrazené části: editorová META/HEAD/TITLE a osiřelý titulkový odstavec, generovaný nadpis „Detailní popis produktu“, staré nabídky/Offer/rating JSON-LD, cenový/skladový snapshot a nehlídané price/photo synchronizéry. Vlastní produktový úvod nebyl odstraněn. CTA je jen `#product-detail-form`, bez změn košíku, cen nebo skladu. Fotografie mají vlastní nativní ID guard a vlastní archivovanou URL jako fallback.

## Skutečně provedené ověření
- **416: 4/4 kontextů Chromium PASS** – 1440/390/320 px s JS a 390 px bez JS. Všech šest dialogů, bannerový panel, FAQ, klávesnice/Tab/Escape, návrat fokusu, tři mobilní přepínače a změny šířek. Pět ikonových pozic v jedné řadě také v desktopovém hostu 240 px.
- **464/467: 372/372 jednotlivých kontrol PASS** – nikoli 372 produktových scénářů. Rodič znovu spustil celou sadu proti přesným finálním souborům v rodičovském `out/`, po dokončení CSS. Šířky 1440/390/320 px s JS i bez JS, short host 240 px, všechny ingredientové dialogy, ovládání a historická DETAILS, mobilní přepínače a responzivní přechody.
- **Společná stažitelná příloha: 12/12 scénářů PASS** – 1440/390/320 px, přepínání všech variant a opakované přepnutí první. Otevřená vysvětlení obsahují všechny své původní odstavce. Nulové přetékání kořene, shortu a textu za hranice buněk. Žádné JS chyby, žádné vadné vložené cache obrázky ani externí request eventy v tomto upraveném vieweru.
- CSS ověřeno parserem tinycss2, devět doručených skriptů přes Node vm.Script. Šest finálních přímých screenshotů ověřeno proti průhledným předkům a prázdným pixelům; označený přehled skutečně otevřen a prohlédnut. Iframe testy nepřepisují přímé snímky.
- Při rodičovské kontrole se externalizovalo 20 zbývajících statických atributů style v mango výstupech: 10 řádkových záhlaví tabulek a 10 short/historických prvků. Dostaly vlastní scoped třídy. Doplněny přímé čitelné 10px popisky ikon a černé názvy příchutí. Buňky a modal HTML se nepozměnily. Sada 372 kontrol byla potom znovu provedena na těchto finálních souborech.

### Co nejsou testy skutečné galerie
416 prošel pouze označenou syntetickou native-ID/source-change fixture s reálnými cache piktogramy a vypnutým rAF. Piktogramy se nevydávají za produktové fotografie a nikdy nejsou v doručených fotkách. U manga se testovalo odmítnutí nesprávného ID a neproduktové fotografie. **Pozitivní přepnutí mezi dvěma aktuálními vlastními gallery fotografiemi není ověřené.**

CSP a další blokace se vykazují pravdivě: mango sada emitovala 346 CSP blokovaných request eventů, nula dokončených externích fetchů. Není to tvrzení „nula request eventů“. Příloha používá vložené skutečné cache obrázky; chybějící originály jsou výslovně označené a jejich síťové načítání vypnuté jen v preview.

## Otevřené věci před živým použitím
**asset_complete=false:** registr má 17 dostupných a 27 nedostupných URL. Chybějí vlastní hlavní fotografie a část ingredientových/ikonových zdrojů. Pět ikonových pozic není potvrzení pěti načtených originálů. Žádné falešné HTTP 200, generované obaly ani záměny za box 383.

Plná foto kontrola, aktuální veřejné CSS/HTTP 200 a shoda bajtů, skutečné hostitelské styly a skripty Shoptetu, CMS sanitizace a uložení do administrace nejsou ověřené.

Obsahové rozpory a **189 konkrétních vět/výskytů** (včetně neúčinkových) jsou v `collagen-varianty-krok-4d-obsahove-vyhrady.md` a strojově v JSON. Neaplikované alternativy jsou vedle původních vět:
- **416:** vlastní archiv uvádí 8,2 g a jiné složení než starší info.md s 8 g; short 200–300 ml proti long 300–400 ml, obě verze také umožňují 1 litr.
- **464:** rozpor 240 g proti 30 × 8,2 g. Nové shrnutí nevybírá gramáž.
- **467:** dříve opsané údaje 240 g / 30 dní / 30 sáčků nejsou aktivním balením samostatného sáčku; zůstávají jen v historickém rozbalení.
- Účinkové/free-from/patentované věty nejsou schválené vizuálním převodem. Automatický nadpis EFSA v produktovém zdroji není právní schválení. Pro 467 nebyl nalezen vlastní info.md; ananasové info není zdrojem mango formule.
- Přesný povinný disclaimer je ve všech long. RULES.md použitý; NOT-ALLOWED.md nebyl na očekávané cestě nalezen. Žádný chybějící podklad se nevymýšlel.

## Předání, nikoli nasazení
Šest HTML, tři vlastní témata, protokol, testy, revize, fronta původních 92 ID a omezené snímky se předávají přes existující Git. **Žádná změna živého CMS, upload veřejných CSS ani zásah do zákazníků, objednávek, plateb nebo trackingu.** Celý bod 4 zůstává otevřený pro další rodiny.

Samostatný `collagen-varianty-pracovni-nahled.html` je příloha se třemi přepínatelnými variantami. Síť, nákup a nativní foto synchronizace jsou vypnuté pouze v preview; produkční URL zůstávají ve zdrojových HTML. Není to záloha editačních polí ani důkaz CMS nasazení.

Před živým nasazením: potvrdit etiketu/balení a claimy, doplnit pravé fotografie, porovnat čerstvá editorová data s aktuálním Gitem, uložit raw CMS zálohy a pak pod samostatným zadáním nasazovat malé dávky s nezávislým readbackem.

Zpracování: GPT-6.1-Sol, Python/BeautifulSoup/Pillow/tinycss2, skutečný Chromium/Playwright a existující Composio GitHub. Bez placené obrazové generace. Náklady modelu/connectorů zde nevyčíslené; nevydávají se za nulu.
