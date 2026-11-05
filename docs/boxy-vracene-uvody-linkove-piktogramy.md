# Longevity a Hormonal Balance — vrácení úvodů a sjednocení piktogramů

## Rozsah této revize

Na Pavlův výslovný pokyn se do pracovních Git podkladů vrací přesně dodané znění:

- **Longevity, dlouhý popis:** celý odstavec začínající „Dárek, který potěší každého v každém věku!“ přímo pod dosavadním hlavním nadpisem.
- **Hormonal Balance, krátký popis:** celý odstavec začínající „Darujte hormonální rovnováhu, krásu a dlouhověkost!“ v `.maly-popis`.
- Krátký text se podle obsahu i předchozího rozlišení v tomto vlákně týká Hormonal Balance, ne Longevity. Nezaměňují se produkty ani jejich formulace. Označení „ongevity dlouhý..“ je identifikátor části zadání, nikoli součást výsledného odstavce.
- Pro oba boxy jsou sjednocené skutečné piktogramy v krátkém i dlouhém popisu: obrysové SVG, `fill="none"`, jednotná síla tahu **2.6 / 64 × 64**, kulaté konce i spoje. Jde o překreslení samotných glyphů, nikoli pouze zakulacení karet.
- Referencí je nejnovější skutečně načtená úprava UFIRST v commitu `136b4626cd7aa14f78a87492a246e29c5601b74a`, zejména `assets/ufirst-giftbox-line-icons/` a `docs/ufirst-box-linkove-piktogramy-a-uvod.md`. Pět obsahově použitelných glyphů Longevity přímo přebírá tyto stejné křivky; vlastní kolagenový symbol a šest benefitových symbolů Hormonal mají totožné parametry linky. Referenční i nové symboly byly společně skutečně vykresleny a prohlédnuty.
- **Barva zůstává vlastní Golden Life červená**, ne tyrkysová UFIRST. Vložené SVG mají červenou `#d90817` pro fallback, původní CSS alpha maska dál používá barvu příslušného tématu. Žádná změna globální palety nebo filtrů fotografií.
- Popisky všech šesti ikon každého boxu se neměnily. Long/short sada daného boxu je shodná. Dvanáct editovatelných SVG masterů je v `assets/longevity-giftbox-line-icons/` a `assets/hormonal-giftbox-line-icons/`; stejné bajty jsou vložené jako data URI do HTML, bez nové síťové závislosti.

Aktualizované existující páry jsou v `shoptet/longevity.html`, `shoptet/longevity-kratky.html`, `shoptet/hormonal.html`, `shoptet/hormonal-kratky.html` a v odpovídajících českých souborech pod `web/Golden Life Darkovy box Longevity/` a `web/Golden Life Darkovy box Hormonal/`. Nejsou změněny jiné jazykové verze, UFIRST, ostatní boxy, SEO, ceny nebo nativní nastavení obchodu.

**Pouze pracovní předání do Gitu. Živý Shoptet se touto revizí neukládá ani nepublikuje.** Tato revize nahrazuje výhradně uvedené dvě intro části starších obsahových podkladů; zbytek posledních textů zůstává v platnosti.

## Zdravotní tvrzení — dodané znění není schválením

Doplněk stravy není lék. Oba odstavce byly vráceny doslova na výslovný požadavek, jako pracovní text k odborné kontrole. Následující alternativy **nebyly** potichu dosazené místo zadání.

### Longevity

- Dodané: **„Tento nádherný vánoční box ukrývá doslova nadupané a účinné složení prémiových ingrediencí, které podporují vitalitu, mladistvý vzhled, energii a působí proti známkám stárnutí.“**
  - Jde o obecná a konkrétní účinková tvrzení bez uvedení nosné živiny. Znění není doložené claims oddílem produktového souboru.
  - Dostupné doslovné produktově zapsané znění pro část o energii/únavě z `brand/product/beauty-longevity-nad-drink/info.md`: **„Vitaminy skupiny B přispívají ke snížení míry únavy a vyčerpání, k normálnímu energetickému metabolismu a k normální funkci nervové soustavy.“** V komunikaci musí být jasná vazba těchto vitaminů na nápoj. Tato věta nedokládá omlazení ani působení proti stárnutí.
- Dodané: **„Hvězdou boxu je lahodný Beauty Longevity NAD+ drink, jehož jediný sáček nahradí nejen 16 tablet, ale i omlazující NAD+ infuze, které jsou v Americe mimořádně populární mezi hollywoodskými celebritami.“**
  - **Nedoložená ekvivalence s infuzním postupem**, včetně neurčitého srovnání se 16 tabletami. Produktový soubor žádný takový ekvivalent ani údaj o hollywoodských celebritách nedokládá. Není k dispozici schválená zdravotní formulace stejného významu.
  - Návrh neutrálního věcného znění: **„Součástí boxu je Beauty & Longevity NAD+ — malinový nápoj s 6 000 mg mořského kolagenu Peptan® a 300 mg nikotinamid ribosid chloridu v denní dávce.“** To je popis složení podle zdroje, ne schválené tvrzení o náhradě zákroku.
- Dodané: **„Nyní si tento omlazující rituál můžete dopřát každý den, jednoduše, chutně, bez jehel a za dostupnou cenu.“**
  - Slib omlazení a návazné srovnání s jehlami nejsou podložené produktovým claimem. Neutrální návrh: **„Nápoj si připravíš rozmícháním jednoho sáčku ve 300–400 ml vody.“** Popis přípravy, nikoli schválený zdravotní účinek.
- Dodané: **„Box navíc obsahuje produkty pro kvalitní spánek a podporu metabolismu během noci.“**
  - Účinek na spánek a noční metabolismus. `brand/product/good-sleep-night-burn/info.md` neuvádí schválený EFSA claim; nelze nabídnout schválený slib téhož významu.
  - Neutrální návrh: **„Box obsahuje také doplňky stravy Anti-Age Longevity NAD+ a Good Sleep & Night Burn.“**
- Dodané: **„Dokonalý vánoční dárek pro každého, kdo chce zůstat mladistvý, plný energie a vitality co nejdéle.“**
  - Celkový dojem navazuje na tvrzení o dlouhodobém omlazení/energii. Pro část energie je k dispozici pouze výše uvedené znění o vitaminech B; schválenou alternativu pro „zůstat mladistvý co nejdéle“ zdroj neposkytuje. Neutrální návrh: **„Vánoční dárek pro dospělou ženu, kterou baví moderní péče o sebe.“**
- Úvodní **„Dárek, který potěší každého v každém věku!“** sám není léčebný slib, ale nesmí se vykládat jako potvrzení vhodnosti doplňků pro děti, těhotné, kojící nebo osoby s kontraindikacemi. Zachovaná produktová upozornění a etikety jsou rozhodující.

### Hormonal Balance

- Dodané: **„Darujte hormonální rovnováhu, krásu a dlouhověkost!“**
- Dodané: **„Tento nádherný vánoční box je ideálním dárkem pro ženy 40+, které chtějí zvládat menopauzu bez návalů a hormonálních výkyvů, kvalitně spát, vypadat mladší a cítit se skvěle v každém věku.“**

Tvrzení o hormonální rovnováze, vymizení návalů/výkyvů, kvalitě spánku a mladším vzhledu nejsou doložená dostupným schváleným produktovým zněním. Absolutní slib „bez návalů a hormonálních výkyvů“ vyžaduje zvláštní pozornost. Soubor `brand/product/woman-hormonal-balance/info.md` není na dostupné cestě přítomný; nevymýšlí se mu schválená alternativa ani se za ni nepovažují starší veřejné bannery.

Neutrální návrh podle skutečného obsahu pracovního HTML (nikoli schválený zdravotní claim): **„Dárkový box pro ženu 40+, kterou baví péče o sebe. Woman Hormonal Balance, nápoj Dark Cherry, Anti-Age Longevity NAD+, láhev a USB míchátko v jedné dárkové krabici.“**

Stávající účinkové popisky ikon Hormonal se na pokyn k opravě **stylu** neměnily; jejich ponechání a nové glyphy nepředstavují zdravotní schválení. Dřívější otevřené otázky z `docs/longevity-darkovy-box-predani.md` (vánoční termín, zlatobýl versus řimbaba, přesné označení NR chloridu a společné dávkování) zůstávají otevřené a tato omezená revize je neřeší.

## Skutečné ověření

- Všech osm změněných HTML: reverzní bajtový test vrací **přesný původní soubor**, pokud se vrátí jen šest obrazových URI a příslušný úvod. Tím jsou ověřené všechny ostatní bajty — včetně nadpisů, fotografií, SCRIPT, STYLE, detailových URL/ID, košíku a ostatních odstavců — nikoli jen vybrané atributy.
- Ve čtyřech souborech s obnoveným intro textem je ověřen celý přesný odstavec a jeho správné umístění. U zbylých čtyř se intro neměnilo.
- Osm HTML na 1280 a 390 px v Chromium; vždy šest skutečně dekódovaných SVG, žádné horizontální přetékání ikon/popisků a žádná JS chyba izolovaného náhledu. U krátkých variant kliknutím ověřeno otevření i zavření obsahu boxu.
- Každá vložená SVG se bajtově shoduje s odpovídajícím editovatelným masterem; XML ověření parametrů linky. Popisky jsou stejné jako před změnou.
- Skutečně prohlédnuté PNG srovnání UFIRST/Longevity/Hormonal a mobilní výřezy změněných úvodů. Náhled používá systémové písmo a vlastní prezentační rám; není to screenshot živého obchodu. U izolovaného dlouhého bloku je pouze v náhledu přirozená výška mřížky, protože vedle ní není nativní produktová fotografie.
- Kvůli dříve zjištěnému HTTP 403 nebyly posílány nové požadavky na Shoptet ani měněn transport/IP k obcházení blokace. Testy jsou lokální a offline, bez podvržených úspěšných shopových odpovědí. Neproběhla nová živá kontrola čteček nebo košíku; jejich kód se nezměnil.
- JSON s výsledky je v `tests/boxy-vracene-uvody-linkove-piktogramy.json`.

## Zdroje, model a náklady

Aktuální zadání a předchozí rozlišení produktů v tomto vlákně; čerstvý `main` repozitáře `pavel489/goldenlife-web`; současné editovatelné SVG a dokumentace poslední opravy UFIRST; `brand/RULES.md`; dostupné `info.md` Beauty Longevity a Good Sleep. Žádné čtení cizích soukromých konverzací. `brand/NOT-ALLOWED.md` nebyl při předchozí kontrole dostupný; nenahrazuje se domnělým schválením.

Model **gpt-6.1-sol**. Úpravy HTML/SVG a náhledy vznikly kódem a Chromium. Bez placeného obrazového či video generování. Skutečná cena jazykového běhu a případné účtování konektoru nejsou v tomto rozhraní dostupné.
