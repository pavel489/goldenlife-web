# Krok 4A – samostatná produktová rodina Hormonal

## Stav
Připravená první ucelená rodinná dávka po pilotu: **3 produkty, 6 HTML, 3 vlastní témata**. **Celý bod 4 tím dokončený není.** Double, Duo/Trio, dárkové boxy, příslušenství, UFIRST a další samostatné rodiny nejsou tímto převedené. Fronta všech 92 původně auditovaných nativních ID je v `migrace-po-rodinach-fronta-4a.csv` a odlišuje přípravu od nasazení.

Nejde o živé nasazení. Úplné vizuální ověření není dokončené: e-shop i skutečné aktuální hlavní fotografie vracejí HTTP403 „Access temporarily blocked“. Potvrzeno requestem, skutečným prohlížečem a jedním dalším čtením po dokončení přípravy. Blokace nebyla obcházena, nastavení ochrany se neměnilo. HTML pracuje se skutečnými byteově ověřenými veřejnými zálohami z kroku1, nikoli s předstíraným čerstvým čtením. Git výchozí revize: `136b4626cd7aa14f78a87492a246e29c5601b74a`.

## Produkty a zdroje
- **Woman Hormonal balance (ID 644)**: `web/Golden Life Woman Hormonal balance/Golden_Life_Darkovy_box_Hormonal_cz.html` a `web/Golden Life Woman Hormonal balance/maly/Golden-Life-Hormonal-maly-cz.html`; vlastní theme `user/documents/upload/css/golden-life-barvy-woman-hormonal-balance.css`. Zdrojový archiv: `644-woman-hormonal-balance.html`, SHA256 `3025d52aff5fe1026a14eb27e292ec3a1df970f62f431938fdb19a42bb56adb9`.
- **Hormonal Balance noční GLP-1 drink (ID 635)**: `web/Golden Life peptides glp-1 woman balance dark cherry/peptides-glp-1-woman-balance-dark-cherry-cz.html` a `web/Golden Life peptides glp-1 woman balance dark cherry/maly/peptides-glp-1-woman-balance-dark-cherry-maly-cz.html`; vlastní theme `user/documents/upload/css/golden-life-barvy-glp1-woman-balance.css`. Zdrojový archiv: `635-hormonal-balance-nocni-glp-1-drink.html`, SHA256 `a1b1a950217e74b63506c988ac83ba349b4fa5fda42db5a8e33486af89e1390d`.
- **Hormonal Balance noční GLP-1 drink sáček (ID 641)**: `web/Golden Life peptides glp-1 woman balance dark cherry sáček/peptides-glp-1-woman-balance-dark-cherry-sacek-cz.html` a `web/Golden Life peptides glp-1 woman balance dark cherry sáček/maly/peptides-glp-1-woman-balance-dark-cherry-sacek-maly-cz.html`; vlastní theme `user/documents/upload/css/golden-life-barvy-glp1-woman-balance-sacek.css`. Zdrojový archiv: `641-hormonal-balance-nocni-glp-1-drink-sacek.html`, SHA256 `51ea3c4e7c3d276594b67dbd8d3793dab105c3ab3a47e6d6f2013303a49989a3`.

- ID644 je samostatná Woman Hormonal Balance, přestože zděděný název souboru nesprávně obsahuje Darkovy_box. Identifikátor ani soubor nebyl zaměněn za dárkový box668.
- ID635 je box 270 g / 30 sáčků; ID641 je samostatný sáček 9 g / 1 dávka. Denní dávka se mezi nimi nenásobí. Historické názvy složek peptides...dark cherry se zachovávají; změna nativních názvů/URL/SEO není součástí práce.
- Referenční komponentová struktura GLP-1 ID476 a hotové piloty z kroku3. Žádné cizí složení, dávkování, produktové fotografie či ID se nekopírovaly.

## Rozsah změn
- Každé pole má vlastní kořen s ID, layoutem a tématem, jeden STYLE a dva CMS-safe importy (společný framework, vlastní theme).
- Původní plné intro, bohaté vysvětlující karty, příběh, FAQ, vlastní teasery a plné ingredient dialogy, návod, skladování, omezení a tabulky zůstaly. Celý příběh zůstává dostupný na mobilu i bez JavaScriptu.
- Zachováno **184 podstatných původních P/LI**, všechny krátké původní texty a obrázkové URL/ALT. Výjimky: osiřelé SEO/meta titulky mimo produktový root a původní cenové/dostupnostní placeholdery jsou odstraněné; namísto objednávkového tlačítka pouze kotva k nativnímu formuláři. ID641 má navíc výslovnou identifikaci jedné dávky. Změny jsou dokumentované, nejde o přepis účinků.
- **24 plných dialogů**, **5 tabulek / 165 vnitřních HTML buněk** shodných se zdrojem; celé dialogové markupy jsou shodné po parserové serializaci, u drinků navíc byteově zachované raw bloky.
- Sdílený `golden-life-produkt.css` je byte-identický s výchozím Gitem. Původní tři theme prefixy jsou beze změny; přidaná pravidla a chybějící tokeny míří jen na konkrétní SKU. Fonty jsou namespacované, bez globálního přepsání cizí podmnožiny.
- Dva hlavní fotografické cíle mají přesnou vlastní URL z manifestu. Bootstrap odmítá jiné nativní ID, používá bounded microtask místo rAF-only a běží i po přesunu rootu. Produkční URL nebyly přepsané na archivní packshot sáčku.

## Co skutečně prošlo
- Parent skutečně znovu spustil oba dětské testovací programy: 4/4 pro644 a 8/8 pro635/641, všechny exit0. Desktop1440, mobil390/320 a pro každý SKU390 bez JS. Doručené bootstraps se při načtení HTML reálně vykonaly. Testy používají pouze pravé dřívější asset bytes a blokují nedostupné zdroje, nevytvářejí falešné úspěšné obrázky.
- Společné ověření přesně předávaného offline HTML: **12 scénářů**, všech24 unikátních dialogů, 90 skutečných otevření/zavření včetně opakovaného přepnutí první varianty. Každý telefonní přepínač otevřen/zavřen pointerem, první také Enter/mezerník; banner info a CTA kotva fungují. Žádný horizontální overflow rootů/short hostů, žádný text přes buňky, pět krátkých ikon v jednom řádku. Žádná JS chyba ani externí request.
- Rodičovská statická kontrola všech polí, buněk, odstavců, dialogů, identit, povinného disclaimeru a SHA; syntax CSS ověřuje tinycss2. Přesné JS ověřuje Node vm.Script před Git předáním.
- Obrázky widgetů/ingrediencí se nezapočítávají jako úspěšné, pokud skutečné bytes nemáme. Pro644 máme šest pravých ingredient fotografií; hlavní produktová fotografie i další zdroje zůstávají nedostupné. Archivní čistý sáček z existujícího Git assetu byl skutečně vizuálně prohlédnut a posloužil pouze označenému fixture testu641, ne jako současná galerie.
- Screenshoty zachycují přímo neorámované dokumenty, ne vysoký obsah oříznutý pevným iframe. Ověřena viditelnost včetně předků/opacity a neuniformní malované pixely; náhled je otevřený a vizuálně prohlédnutý. První prázdná diagnostická zachycení nejsou v předání.

## Co není dokončené
- Plná vizuální QA se všemi skutečnými fotografiemi, dekorativními obrázky a ikonami: **ne**.
- Aktuální full-shop runtime, skutečná nákupní sidebar šířka a aktuální nativní galerie: **ne**. Izolovaný komponentový test není živý Shoptet.
- Přepnutí mezi dvěma aktuálně načtenými vlastními hlavními fotkami: **ne**. Bezpečné ID/fallback chování a archivní fixture641 se od toho jasně odlišují.
- Uložení do CMS, nahrání veřejných CSS, obchodní objednávky, ceny, zákazníci nebo tracking změny: **ne**.
- Schválení historického copy: **ne**. Produktové info.md pro tyto tři SKU nebylo v dostupné brand knihovně nalezeno. Výhrady a neutrální alternativy jsou v `hormonal-krok-4a-obsahove-vyhrady.md`: těhotenství/kojení, počty extraktů/složek, additives-free, ekvivalence16tablet, věk8+ proti cílení40+, časové grafy a dlouhá kúra proti obsahu jediného sáčku. Čísla ani jednotky se neopravovaly odhadem.

## Náhled a další použití
Samostatná příloha `hormonal-pracovni-nahled.html` obsahuje všechny tři varianty a funguje bez sítě. Chybějící fotografie jsou výslovně označené, nevymyšlené. Je to omezený náhled struktury; okolí nákupní části je zjednodušené, synchronizace nativní galerie a nákup jsou v preview vypnuté. Produkční HTML tyto preview úpravy neobsahuje. Obrazový přehled a mobilní/desktopové omezené capture jsou v `nahledy/`.

Před nasazením po obnovení přístupu porovnat aktuální skutečné CMS/popisy s archivem, zkontrolovat vlastní fotografie/pozadí/ikony a obě CSS odpovědi, zopakovat plný shop runtime. Pokud se zdroj mezitím změnil, nejdřív rekoncilovat konkrétní rozdíl, ne slepě vložit archivní draft. Zálohy CMS získat až před výslovně zadaným živým zápisem.

Zpracování: GPT-6.1-Sol, Python/BeautifulSoup/tinycss2, Chromium/Playwright, existující Composio GitHub cesta. Bez placeného obrazového generování. Modelové/connectorové náklady zde nejsou vyčíslené.
