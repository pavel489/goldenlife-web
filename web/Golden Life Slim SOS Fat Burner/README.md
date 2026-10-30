# Slim SOS Fat Burner – obnovený plný obsah a nové obrázky

## Aktuální oprava
Nové CSS rozložení zůstává, ale vrací se významové a prodejní texty původní verze – nikoli opakování dávek a názvů složek.

- Obnovený původní dlouhý i krátký úvod a přínosové piktogramy.
- Obnovené „Jak funguje“, „Účinky“ a souhrn „Co vám přinese“.
- Každá z pěti složek má vlastní původní odlišný teaser a plný vysvětlující odstavec v detailu.
- Pět přesně dodaných PNG je na správných kartách i uvnitř jejich detailů. Včetně skutečného obrázku chitosanu, který předchozí verzi chyběl.
- Tabulka, ceny/nákupní chování, dávkování, bezpečnostní upozornění a nové společné CSS rozložení nebyly obsahově změněné. Chrom zůstává **0,55 mcg / 1,11 mcg**.
- Mobilní rozbalování přizpůsobené obnovenému nadpisu „Účinky“ a ověřené myší/Enterem. Nezmizí žádný dlouhý odstavec.

## Soubory
- [Dlouhý popis](Golden-Life-Slim-SOS-Fat-Burner-cz.html)
- [Krátký popis](maly/Golden-Life-Slim-SOS-Fat-Burner-maly-cz.html)
- [HTML náhled](../../nahledy/slim-sos-fat-burner.html) – otevři stažený soubor v prohlížeči; obrázky a fonty vyžadují internet. Nákup je vypnutý.
- [Náhled všech pěti skutečně vyrenderovaných karet](../../nahledy/slim-sos-fat-burner-slozky.png)
- [Horní část stránky](../../nahledy/slim-sos-fat-burner.png)
- [Pět původních dodaných PNG](../../assets/slim-sos-fat-burner/ingredients/)
- [Testy](../../docs/slim-sos-fat-burner-testy.json), [manifest opravy](../../docs/slim-sos-fat-burner-manifest.json), [poznámky k tvrzením](../../docs/slim-sos-fat-burner-texty.md)

## Podklady a přesné obrázky
Původní český popis byl obnovený z uloženého původního veřejného HTML. Zkontrolované současné jazykové mutace stejného productId **473** potvrzují, že významové texty zůstaly zachované:
- https://www.golden-life.cz/sk/slim-sos-fat-burner/
- https://www.golden-life.cz/de/slim-sos-fat-burner/
- https://www.golden-life.cz/en/sos-fat--burner/

Aktuální česká veřejná stránka už na začátku opravy obsahovala předchozí zredukovanou verzi. Proto není nově vydávaná za původní referenci. Jazykové mutace se pouze četly – jejich obsah, tabulky ani staré jednotky se v této práci neměnily.

Použité dodané soubory beze změny původních bajtů a názvů:
1. `01_chitosan_sos-burner_v1.png`
2. `02_bile-fazole_sos-burner_v1.png`
3. `03_cervena-repa_sos-burner_v1.png`
4. `04_jablecny-ocet_sos-burner_v1.png`
5. `05_chrom_sos-burner_v1.png`

Obrázky jsou skutečně uložené v tomto repozitáři a HTML je odkazuje přes neměnné URL připnuté ke commitu f8aadb35e6e7fdd3a3f0c56b3c27e7f1d589808b. Není potřeba domýšlet jejich složku na Shoptetu nebo předstírat neprovedený upload.

## Stav a bezpečnost copy
**Jde o požadované pracovní obnovení původních účinkových textů, nikoli o legislativní schválení.** Tvrzení o blokaci tuků/sacharidů, detoxikaci jater, stabilizaci glukózy či účincích na chutě nejsou tímto označena za schválená. Konkrétní produktový soubor s povoleným zněním není dostupný; schválené formulace proto nejsou vymýšlené. Původní tvrzení i neutrální faktické alternativy jsou odděleně rozepsané v kontrolním souboru. Nejsou znovu tajně nahrazené pouhými dávkami v požadovaném pracovním návrhu.

Zdrojový HTML komentář a stavový atribut označují pracovní obnovení; stejný status je viditelný nahoře v náhledu. Před zveřejněním účinkového copy je nutná samostatná obsahová kontrola. Povinná upozornění k doplňku a alergenu korýši zůstávají.

## Co se neměnilo
- Obecné a barevné CSS beze změny; zachované dva importy v každém popisu.
- Celá tabulka a dříve opravené jednotky chromu beze změny.
- Aktuální CTA bez natvrdo zapsané ceny či dostupnosti; odkaz k nativnímu formuláři.
- Ostatní produkty, GLP-1 Activator, Beauty Star a jazykové mutace beze změny.
- Žádné ukládání do administrace Shoptetu, zákazníci/objednávky/platby/měření beze změny.

## Skutečné ověření
- Devět průchodů šířkami 320–1440 px včetně návratu na mobil; čtyři šířky přesných CMS fragmentů s reálnými shop styly a dvěma importy.
- Žádné rozbité použité obrázky, žádné JS chyby, bez horizontálního přetečení stránky nebo banneru.
- Všech pět detailů otevřeno/zavřeno na mobilu i desktopu: deset kombinací, včetně kontroly plného původního textu a správného nového obrázku.
- Tři mobilní přepínače ověřené myší/Enterem; po rozbalení se plný text neřeže.
- Pět skutečně odlišných teaserů, sedm původních přínosových položek, žádné dřívější obecné výplňové věty v detailech.
- Všechny dodané PNG porovnané bajt po bajtu po Git uploadu a přes skutečné veřejné URL. Náhledy karet vznikly screenshotem skutečného HTML, ne přestavěním UI v grafickém editoru.

Doručení je přes Git, bez ZIPu. Nové obsahové HTML se tímto nenasazuje do Shoptetu.

## Výroba a náklady
Podklady: původní české veřejné HTML, současné SK/DE/EN stránky stejného produktu, pět přesně jmenovaných dodaných ilustrací, aktuální Git a pravidla značky. Model GPT-6.1-sol, Python/BeautifulSoup/Pillow a Chromium/Playwright. Nevznikla nová placená obrazová/video generace; cenu běhu jazykového modelu nemám vyčíslenou. Původní náklady na dříve vytvořené dodané PNG nejsou nákladem nové generace v tomto úkolu a nejsou nově vyčíslené.
