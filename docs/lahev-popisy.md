# Láhev Golden Life — krátký a dlouhý popis

## Soubory
- `shoptet/lahev-kratky.html`: krátký popis, vložit do pole krátkého popisu produktu 597.
- `shoptet/lahev.html`: dlouhý popis, body-only fragment pro HTML editor dlouhého popisu produktu 597.
- `web/Golden Life Lahev/Golden_Life_Lahev_cz.html`: samostatná HTML stránka dlouhého popisu.
- `web/Golden Life Lahev/maly/Golden-Life-Lahev-maly-cz.html`: krátký popis ve stejné adresářové konvenci jako boxy.
- `nahledy/lahev.html`: samostatný offline náhled obou popisů; fotografie vložená do HTML.
- `assets/lahev-golden-life.webp`: skutečná produktová fotografie; oříznuté pouze okolní prázdné místo.
- `config/lahev-sources.json`: zdroje, ověřené vizuální vlastnosti a chybějící specifikace.
- `tests/lahev-results.json`: výsledky skutečných browser testů.

## Obsah a zdroje
Vychází z `brand/RULES.md`, aktuálního `main` repozitáře `pavel489/goldenlife-web` (základ 949ab2a6ff2a94de9ac6e24108ee2018f610fdf7), zavedené dvojice krátký/dlouhý popis a živé stránky https://www.golden-life.cz/lahev-golden-life/ (produkt 597, EAN 8594203440715). Na živé stránce při kontrole nebyl podrobný popis, fotografie již dostupná byla. Vizuálně ověřeno průhledné tělo, bílé logo Golden Life a šroubovací víčko ve stříbrném odstínu. Nejde o ověření materiálu.

Typografie na e-shopu ověřena jako Nunito. Komponenta používá Nunito/Arial a vlastní scoped CSS; offline náhled bez externího fontu používá fallback Arial. Zlatá #C6AC3F pochází ze živé konfigurace Golden Life; pro text je použit tmavý odstín kvůli čitelnosti. Jde o Golden Life core, nikoli neonové rozhraní U F1RST.

Objem, materiál, myčka, horké nápoje, deklarovaná nepropustnost a přesná prodejní cena nejsou ověřeny. Nejsou v copy ani ve strukturované nabídce. Žádné zdravotní tvrzení, domyšlená recenze, dostupnost, termín doručení nebo tvrzení o léčbě.

## Chování
Krátký popis má nativní rozbalení přípravy a péče. Dlouhý popis má tři nativní FAQ. CTA v samostatném náhledu otevírá skutečnou produktovou stránku; na Shoptetu se přepne na posun k nativnímu formuláři pouze při ověření `productID=597`. Nepřidává produkt do košíku, neodesílá objednávku ani formulář a nevkládá cenu/sklad. Chyba fotografie zobrazí textový fallback.

Existující boxy ani jejich importér nebyly měněny. Po samostatném vložení dlouhého popisu přímo do canonical stránky lahve bude mít jejich stávající importér zdrojový obsah. Toto zatím není nasazení do Shoptetu; ověření editorových transformací a živého importu do boxů musí následovat až po vložení.

## Ověření
16 reálně provedených responzivních případů v Playwright Chromium: 4 pohledy (offline náhled, krátký fragment, dlouhý fragment, oba fragmenty) × šířky 320, 390, 768 a 1440 px. Bez horizontálního přetékání, duplicit ID a JS chyb; fotografie se načítají, rozbalení funguje, CTA mají výšku alespoň 44 px. Offline náhled nevyžaduje externí síťové požadavky. CMS fragment používá pouze autentický fotografický asset. Dále samostatné explicitně syntetické testy správné/nesprávné identity hosta, žádného odeslání formuláře a chybějící fotografie. Screenshoty desktop/mobil prohlédnuty vizuálně. Nejde o živý checkout ani test fyzického zařízení či Safari.

## Výroba a náklady
Model: gpt-6.1-sol. HTML/CSS/JS vytvořeno přímo, fotografie upravena Pillow pouze ořezem okolí, testy Playwright Chromium. Bez placeného generování obrázků a bez placeného deploymentu. Cena modelového a connector běhu není v této relaci dostupná; nelze ji prohlásit za nulovou.

## Nasazení
Vložení do e-shopu nebylo součástí zadání a nebylo provedeno. Soubory mají scope vlastní komponenty. Při vložení používej HTML režim editoru, zkontroluj zachování celého skriptu, načtení obrázku, FAQ a posun CTA na nativní nabídku. Odkaz na fotografii v dlouhém CMS fragmentu míří na veřejný jsDelivr asset v repozitáři; při budoucí změně jeho URL je potřeba aktualizovat referenci nebo asset přesunout do hostovaného prostoru e-shopu.
