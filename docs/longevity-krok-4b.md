# Krok4B – další samostatná dávka Longevity

## Stav
**2 produkty / 4 HTML / 2 vlastní témata připravené jako interní pracovní kopie. Nejde o dokončení celého bodu4 ani živé nasazení.**

- ID550 Anti-Age longevity NAD+: původní existující long/short cesty zachovány, 9 plných dialogů.
- ID600 Beauty Longevity NAD+ sáček: nový oddělený pár a samostatné `golden-life-barvy-beauty-longevity-sacek.css`, 6 plných dialogů. Nové souhrny říkají jednu dávku, ne měsíc a ne box. Spornou gramáž nevybírají odhadem.
- Hotový pilot544 i jeho původní theme zůstávají beze změny. Společný `golden-life-produkt.css` byteově beze změny.

Výchozí immutable Git `185814751d5e96b74a38df27e6fa0d1207e09ab8`. Vlastní bohaté copy pochází z byteově ověřených veřejných archivů téhož auditu; není vydávané za nově načtený shop. V tomto běhu nevznikl žádný nový shop/CDN požadavek ani pokus obejít předchozí explicitní IP blokaci403.

## Soubory
- **550**: `web/Golden Life Anti-Age Longevity NAD+/Golden-life-Anti-Age Longevity NAD+.html`, `web/Golden Life Anti-Age Longevity NAD+/maly/Golden-life-Anti-Age Longevity NAD+maly.html`, `user/documents/upload/css/golden-life-barvy-anti-age-longevity.css`.
- **600**: `web/Golden Life Beauty Longevity NAD+ sáček/Golden-Life-Beauty-Longevity-NAD-sacek-cz.html`, `web/Golden Life Beauty Longevity NAD+ sáček/maly/Golden-Life-Beauty-Longevity-NAD-sacek-maly-cz.html`, `user/documents/upload/css/golden-life-barvy-beauty-longevity-sacek.css`.

## Zachovaný obsah a funkce
- Vlastní banner/hero, bohaté vysvětlující karty, všechny vlastní teasery a úplné dialogy, návod, upozornění, složení a původní tabulky. Každé pole jeden STYLE se dvěma CMS-safe importy a vlastními marker ID/layout/theme, žádné statické inline CSS.
- **86 původních podstatných p/li**, **15 celých dialogových markupů** a **100 vnitřních HTML buněk ve 4 tabulkách** ověřených proti archivním polím. Krátké původní textové uzly i všechny původní short IMG URL/ALT jsou zachované. Výjimky: osiřelá metadata mimo vlastní root a staré cenové/dostupnostní placeholdery. Čísla/jednotky se nepřepočítávaly.
- **ID550 nemá ve skutečném původním zdroji story-block, FAQ ani vykreslený časový graf.** Nic takového nebylo domyšleno nebo přeneseno z reference. Čtvrté mobilní rozbalování zpřístupňuje vlastní původní bohatý text k užívání. Nepoužívaná původní CSS definice grafu zůstává jen ve starém prefixu; žádný nový graf se nezobrazuje.
- ID600 zachovává celý vlastní příběh, FAQ a tabulky. Historická boxová CTA metadata270g/30sáčků/30dní a doporučení dlouhé kúry jsou pouze v označeném rozporovém disclosure, ne nová specifikace jediného sáčku. Původní lifestyle fotografie mohou ukazovat dřívější balení a nejsou vydávané za aktuální samostatný packshot.
- Mobile/no-JS obsah je dosažitelný. CTA jen kotva k vlastnímu nativnímu formuláři; žádná cena/skladová simulace ani Cart POST.
- Foto-bootstrap bounded microtask, vlastní ID guard, vlastní fallback, přežije přesun rootu mimo `.basic-description`. ID550 zachovává skutečně stažený a prohlédnutý původní vlastní immutable Git packshot. Není to čerstvě ověřená fotografie dnešní nativní galerie; matoucí jméno archivní nativní URL samo nedokazuje její obsah. ID600 používá přesnou vlastní archivní nativní URL; chybějící bajty nejsou nahrazené boxem544.

## Skutečné ověření a jeho hranice
- Parent znovu spustil oba dodané testovací programy: každý4/4 PASS (1440/390/320 s JS,390 bezJS), skutečné exit0. Ověřeny přesné bootstraps, pointer dialogy, klávesnice/ARIA/fokus/Escape, mobilní přepínače, změna šířek, no-JS fallback, identity guard a přesun rootu. ID550 reálně načetl svůj archivní packshot a všech18 ingredient instancí; fixture mutace není test současné nativní galerie.
- Parent navíc ověřil přesně přiložený file:// viewer: **9 scénářů**, všech15 unikátních dialogů, **72 pointer otevření/zavření** včetně opakovaného přepnutí. Viditelný text každého dialogu obsahuje všechny vlastní úplné původní odstavce — nepoužívá se arbitrární minimální délka, která by odmítla pravdivě kratší zdroj. Mobile toggles a první ovladač klávesnicí prošly; rooty/shorty/tabulkové texty nepřetékají. Žádná JS chyba ani externí request.
- Statická kontrola identity, odstavců, celých dialogů, tabulek, short obrazových metadat, importů, povinného disclaimeru a SHA; tinycss2 bez chyb. Před Git předáním navíc Node vm.Script ověří přesné doručené JS.
- Screenshoty přímo z neorámovaných dokumentů, kontrola skutečné painted visibility a neuniformních pixelů, doplněná vizuálním otevřením přehledu. Nejsou to aktuální shop screenshoty.
- **Úplná vizuální a full-shop QA není dokončená.** ID550 chybí pět původních obrazových URL (některé opakovaně také vshortu), ID600 vlastní packshot, navíc externí fontová stylesheet závislost. Přesné chybějící závislosti jsou v testovém JSON. Pravý existující NAD packshot/ingredient fotografie se skutečně načetly; neúspěchy nejsou přeznačené na úspěšné makety.
- Po předchozí dočasné403 v tomto běhu nebyl shop/CDN znovu sondován. Přesný současný stav vzdálené blokace tedy netvrdíme. Produkční závislosti nezmizely jen proto, aby prošel offline test.

## Copy a podklady
Vlastní schválené produktové info.md pro550/600 nebylo nalezeno. Existující boxový podklad544 není automatické schválení pro600. Historické vlastní copy zůstává viditelně označeným interním návrhem, ne právním souhlasem. Konkrétní citace, konflikty a neutrální neaplikované návrhy v `longevity-krok-4b-obsahove-vyhrady.md`: mj.tablety versus kapsle, wheat/gluten/vegan/free-from specifikace,16tablet, děti8+, stará boxová metadata a kúra proti jedné dávce.

V aktuálně předaném archivu600 se samostatný potvrzený údaj8g nenašel; upozornění na možný8g/9g rozpor není faktické tvrzení o této etiketě. Nové shrnutí gramáž nevybírá. Před živým použitím nutná vlastní etiketa a čerstvá kontrola skutečných editorových polí.

## Předání
Editovatelné zdroje, testy, omezené mobilní/desktopové snímky a úplná původní fronta92ID jsou v Gitu. Samostatný `longevity-pracovni-nahled.html` je přiložený ve Slacku; má přepínání dvou variant a viewportu, vložené pouze skutečné dostupné assety, jasně označené chybějící obrázky, vypnutou síť a nákup. Zjednodušené okolí/galerie preview není produkční změna.

Bez uložení do CMS, veřejného nahrání CSS nebo změn cen, zákazníků, objednávek, plateb či trackingu. Před případným výslovně zadaným nasazením znovu zkontrolovat aktuální zdroje proti archivům a získat čerstvé raw zálohy.

Zpracování GPT-6.1-Sol, Python/BeautifulSoup/tinycss2, skutečný Chromium/Playwright a existující Composio GitHub cesta. Bez placeného obrazového generování; modelové/connectorové náklady zde nevyčíslené.
