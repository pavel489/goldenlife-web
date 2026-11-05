# Krok4C – sjednocení připravených samostatných Slim popisů

## Rozsah a stav
**Tři produkty168/473/476, šest otestovaných HTML a tři vlastní theme dodatky. Nejde o dokončení celé řady Slim ani celého bodu4.** Double, další sáčky/boxy/shakes a další rodiny jsou mimo tuto dávku. Žádné uložení do CMS ani upload veřejných CSS.

Autorita obsahu: aktuální immutable Git `cb68ddc0a43aaddbfc328ba419eb9dd6023da27d`. Staré veřejné archivy byly pouze identifikační/srovnávací evidence, ne náhrada novějších opravených textů, tabulek a fotografií. Původní `mcg` u biotinu168 a chromu473/476 se nevracejí na starší `mg`.

## Soubory a skutečné zásahy
- **Slim Extreme Collagen (168)**: `web/Golden Life Slim Extreme Collagen/Golden Life Slim Extreme Collagen.html`, `web/Golden Life Slim Extreme Collagen/maly/Golden Life Slim Extreme Collagen maly.html`, `user/documents/upload/css/golden-life-barvy-slim-extreme-collagen.css`.
- **Slim SOS Burner (473)**: `web/Golden Life Slim SOS Fat Burner/Golden-Life-Slim-SOS-Fat-Burner-cz.html`, `web/Golden Life Slim SOS Fat Burner/maly/Golden-Life-Slim-SOS-Fat-Burner-maly-cz.html`, `user/documents/upload/css/golden-life-barvy-slim-sos-fat-burner.css`.
- **Slim GLP-1 Activator s Berberinem (476)**: `web/Golden Life Slim GLP-1 Activator/Golden-Life-Slim-GLP-1-Activator-cz.html`, `web/Golden Life Slim GLP-1 Activator/maly/Golden-Life-Slim-GLP-1-Activator-maly-cz.html`, `user/documents/upload/css/golden-life-barvy-slim-glp-1-activator.css`.

-168: nehlídaný one-shot gallery sync nahrazen vlastním ID guardem/mikroúlohou, skutečně načteným nativním zdrojem a vlastním zachovaným fallbackem. Původní celý cenový bridge je byteově stejný. Jediný nový mobilní toggle míří jen na dlouhý úvod, vlastním opt-in markerem neaktivuje cizí redesign příběhu/CTA. **Short168 zůstává byteově beze změny.**
-473: doplněno ID do shortu, původní statická barva tabulkového záhlaví přesunuta do vlastní theme, lokální short grid odstranil prokázaný10px overflow na320px. Galerie a původní mobile skript zachované.
-476: doplněno ID do shortu, tři statické inline deklarace panelu Nextida přesunuty do stejné vlastní theme se zachovanou kaskádou a přesnou původní artwork URL GLPBLESKY.png. Existující šestice ikon se nepřekresluje. Galerie a původní mobile skript zachované.
-Všechny17 hashových dialogů dostaly runtime ARIA/fokus/Tab/Escape, ale jejich celé původní HTML zůstalo nezměněné. Fungují i bez JS.
-Common `golden-life-produkt.css` je byte-identický. Původní theme jsou byte-identické prefixy; každý doplněný selector vyžaduje vlastní ID. GLP-1 dodatky proto nematchují Double461. **Double461 se zde plně nerenderoval** a jeho soubory nejsou editované.

## Obsahové a technické invarianty
Přesná shoda všech původních P/LI innerHTML multisetů, textových uzlů, IMG atributů, celých dialogových markupů a **138 buněk ve 6 tabulkách** proti aktuálnímu Gitu. Žádný návrat ke starším dávkám/jednotkám nebo zkrácení benefitů na opakované údaje. Každý field má1STYLE/2importy, správný vlastní ID/layout/theme a0statických inline stylů. Všechny CTA href zůstaly původní;168 si ponechává `/extreme-slim-collagen/#content`,473/476 nativní kotvu. Žádná nová CartPOST logika.

## Skutečně provedené ověření
-Parent znovu spustil skutečný test_slim.py: **12/12 Chromium PASS** – každý produkt1440/390/320 sJS a390bezJS. Přesné doručené skripty se reálně vykonaly, testy neposlaly žádný write ani síťový fetch. Není to plný živý Shoptet.
-All17 dialogů pointerem otevřeno/zavřeno/reopen/backdrop, JS klávesnice/fokus/Escape; mobile toggles168=1,473=3,476=3, ARIA a změny šířek. Úplné vysvětlení/příběh dostupné i bezJS. Short řady mají5/5/6 ikon v jedné řadě.
-Dlouhé desktopové komponenty jsou ve třech izolovaných párech **pixelově shodné s aktuálním Gitem při stejných dostupných cache médiích a vyrovnaném původu capture**. Nejde o plné foto/brand schválení. Short se posuzuje odděleně,473 má záměrnou lokální změnu.
-Parent samostatně ověřil přesný přiložený file://viewer: **12 scénářů**, všech17 unikátních dialogů, **69 skutečných pointer otevření/zavření** včetně opakovaného přepnutí první varianty. Viditelný každý modal obsahuje všechny své aktuální původní odstavce. Žádný horizontální overflow rootů/shortů, žádný text za buněčnou hranicí, žádná JS chyba ani externí request.
-CSS parser tinycss2, source/field hashe a nezávislá Node syntax přesných doručených skriptů před Git předáním. Screenshoty přímo neorámované, ověřená painted visibility včetně předků a neuniformní pixely; označený přehled byl otevřen a prohlédnut.
-Negativní identity/fallback fixture s pravými jinými ingredient pixely prošel; **pozitivní změna aktuální vlastní nativní galerie není ověřená**. Vlastní current packshoty i část ikon/artwork/media chybí: dostupných24 reálnýchURL,33 bez dostupných bajtů v registru. Žádné fake200/nepravé náhrady.

## Otevřené věci před živým použitím
**Obsahové/claims schválení ani plná vizuální QA nejsou hotové.** Ledger `slim-krok-4c-obsahove-vyhrady.md` uvádí430 jednotlivých vět/caption/meta/alt včetně neúčinkových. Nic z navržených alternativ není tiše aplikované.

-168 má nesoulady B6 a přepočtů100g→8g, hlavní odměrku versus šaržovou poznámku vshortu a starším brand info, neověřené free-from a rizikové léčebné věty. Čísla se neopravovala bez vlastníka etikety.
-168 také zachovává původní historické JSON-LD Offer/aggregateRating, viditelnou snapshot cenu/dostupnost a široký price-final-holder bridge. **Nejsou tím ověřené aktuální cena, sklad, expedice ani hodnocení.** Nákupní/cenová logika se mimo zadání nepředělávala. V přiloženém preview byly jen tyto nabídky/JSON-LD odstraněné a nákup deaktivovaný.
-U168 chybí kompletní přesné souvislé povinné brand znění v produkčním HTML. Propozice správné formulace je vledgeru a vpreview doplněná mimo původní root. Tento nedostatek se neprohlašuje za vyřešený vCMS.
-473/476 mají neověřená účinková a ikonová tvrzení, včetně kalorických blokací/detox a „Bleskové hubnutí“. Starší info.md používá v některých místechmg, novějšíGitmcg zůstalo zachováno. Existence nadpisuEFSA není nové právní ověření.
-Plný shop runtime, aktuální vlastní fotografie/pozadí/GLPBLESKY artwork, dopad současných shop skriptů a CMS sanitizace/import nejsou dokončeně ověřené. V tomto běhu nebyl žádný shop/CDNreprobe po předchozím explicitním IPblocku403, jeho současný stav se nevydává za nově zjištěný.

## Předání
Editovatelné existující cesty, tři vlastní theme a relevantní testy/omezené snímky jsou předávané vGitu. Původní short168 a společný framework nejsou nově přepsané. Fronta92původníchID odlišuje pilot/4A/4B/4C od skutečného živého nasazení a nezařazuje tuto omezenou dávku jako hotový celý bod4.

Samostatný `slim-pracovni-nahled.html` je příloha se třemi přepínatelnými variantami a viewporty. Má pouze pravé dostupné cache/Git obrázky; nedostupné originály výslovně přiznává. Galerijní/cenový sync a historické nabídky/schema jsou vypnuté pouze v preview, CTA přesměrovaná jen na lokální vysvětlení, síť/nákup zakázané, povinný disclaimer doplněný vpreview mimo původní root. Tyto preview změny nejsou v produkčním HTML.

Po návratu přístupu je potřeba porovnat skutečně uložené editorové hodnoty se současným Gitem, získat raw CMS zálohy, dořešit etiketu/claimy a potom pod výslovným zadáním nasadit/readbackovat. Žádné ceny, objednávky, zákazníci, platby nebo tracking nebyly v této práci změněné.

Zpracování GPT-6.1-Sol, Python/BeautifulSoup/tinycss2, skutečný Chromium/Playwright a existující ComposioGitHub. Bez placené obrazové generace; modelové/connectorové náklady zde nevyčíslené.
