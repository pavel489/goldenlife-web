# Longevity dárkový box — dodané české texty a předání do Gitu

## Rozsah a stav

Pavlem dodaný text je zapracovaný do existujícího českého dlouhého i krátkého popisu. Text se stylisticky nepřepisoval; entity `&amp;` se vykreslují jako `&`. Toto je pracovní Git podklad k importu, nikoli uložení do živého Shoptetu nebo právní schválení textu.

- Dlouhý popis: `shoptet/longevity.html`.
- Krátký popis: `shoptet/longevity-kratky.html`.
- Aktualizovány také odpovídající existující české soubory v `web/Golden Life Darkovy box Longevity/` a jeho `maly/`.
- Nativní název produktu, SEO titulek a meta description jsou samostatná pole CMS: přesné hodnoty jsou v `config/longevity-darkovy-box-texty-cz.json`. Vložení HTML je v administraci samo nezmění. Samostatný webový dokument má aktualizované title, description a OG texty.
- Úplné dodané znění je v `docs/longevity-darkovy-box-dodane-texty.md`.
- Zadání je česky a ceny jsou v Kč, proto se upravovala česká dvojice, nikoli slovenské soubory. Zadaný slovenský odkaz `https://www.golden-life.cz/sk/darcekovy-box-longevity/` byl ověřen: jeho skutečný český hreflang vede na `https://www.golden-life.cz/golden-life-darkovy-box-longevity/`, nativní `productId=662`.
- Jako název v předávacím souboru je použito úvodní znění zadání „Golden Life dárkový box Longevity“. Slovenský titulek odkazu nebyl přenesen do českého názvu. Žádný název ani URL v živém obchodě se neměnily.

Zůstala původní struktura, skutečné produktové fotografie, šestá galerie vedle ikon, hlavní fotografie v CTA, druhá galerie u balení, všech pět detailových tlačítek a jejich kanonické produktové zdroje. Karty jsou nyní v dodaném pořadí: Beauty & Longevity, Anti-Age, Good Sleep, láhev, míchátko, balení. Šest nových obsahových popisků má shodné zaoblené obsahové symboly v dlouhém i krátkém popisu, ve stávající červené barvě. Symboly jsou vložené v HTML; nepřidávají další účinková tvrzení.

Text „5 produktů v dárkové krabici“ pod kartou balení je samostatný trvalý odstavec, nikoli technická `.gl-packaging-note`, kterou skript galerie přepisuje či skrývá. Dodané „Do košíku“ je ve zdroji; původní skript může text bezpečně přizpůsobit skutečné dostupnosti, samostatnému náhledu a přechodu k nativnímu nákupu. Košík se kvůli novému textu nenutí do aktivního stavu.

## Ověřená veřejná nabídka

Při tomto předání nativní blok produktu 662 uváděl cenu **3 990 Kč**, srovnávací cenu **4 690 Kč** a stav „Skladem“. Rozdíl **700 Kč** byl spočítaný v Pythonu. Na stejné stránce je hodnocení 5 a tři veřejné recenze s texty „Skvělý dárek k Vánocům.Krásné balení mých oblíbených produktů:)“, „Nádherný dárek, opravdu luxusní ❤️“ a „Vypadá fantasticky“. To odpovídá dodané parafrázi; nejde o schválení použití identit nebo fotografií zákaznic. Nabídka a hodnocení jsou aktuální veřejný snímek, nikoli garance k pozdějšímu dni zveřejnění.

## Otevřené body před publikací

1. **Doručení:** ve FAQ zůstává doslova `[DOPLŇ DATUM]`. Vánoční termín nebyl dodán a nevymýšlel se. Před publikací doplň skutečně potvrzený termín, nebo schval změnu celé věty.
2. **Good Sleep — nesoulad složení:** dodaná věta zní: „Kapsle spojují mučenku, meduňku, kozlík, chmel a hloh s garcinií kambodžskou, zlatobýlem a mořskou řasou wakame.“ Produktový soubor `brand/product/good-sleep-night-burn/info.md` i aktuální kanonická stránka mají **řimbabu obecnou**, nikoli zlatobýl. Dodané znění zůstalo v pracovním podkladu. Věcná alternativa podle těchto zdrojů: **„Kapsle spojují mučenku, meduňku, kozlík, chmel a hloh s garcinií kambodžskou, řimbabou obecnou a mořskou řasou wakame.“** Před zveřejněním potvrď oproti aktuální etiketě.
3. **NR versus jeho sůl:** zadání uvádí „300 mg nikotinamid ribosidu“, zatímco tabulky obou kanonických produktů uvádějí „300 mg nikotinamid ribosid chloridu“. Tyto názvy nejsou automaticky rovnocenným označením hmotnosti látky. U konkrétních množství je zdrojově přesnější „300 mg nikotinamid ribosid chloridu v denní dávce“; změna nebyla provedena potichu.
4. **Společné užívání:** každý ze dvou NAD+ produktů má podle veřejné tabulky vlastní denní dávku 300 mg NR chloridu. Součet při současném plném dávkování by byl 600 mg (spočítáno v Pythonu). To není doporučení ke kombinaci ani posouzení bezpečnosti či právně povolené dávky. Zachované upozornění „Společné balení neznamená společné dávkování“ je důležité; případnou konkrétní kombinaci a upozornění musí potvrdit odpovědný produktový odborník.
5. **Podklady k upozorněním:** veřejný Good Sleep potvrzuje nevhodnost pro děti, těhotné a kojící a konzultaci při lécích na tlak či sedativech; Beauty potvrzuje rybí alergen a nevhodnost v těhotenství a při kojení. Anti-Age obsahuje extrakt pšeničných klíčků. Úplnou schválenou etiketu celého boxu tento Git podklad nenahrazuje.

## Zdravotní tvrzení — odděleno od implementace

Následující dodané věty jsou zdravotní tvrzení, nikoli jen popis balení. Zůstaly v pracovním Git znění; jejich implementace není právní souhlas s publikací:

- **„Vitamin C přispívá k normální tvorbě kolagenu pro normální funkci kůže.“** Je pod ikonami i v kartě Beauty — dvě použití téže věty.
- **„Biotin a zinek přispívají k udržení normálního stavu vlasů a kůže.“**
- **„Vitamin C, vitamin D, zinek a selen přispívají k normální funkci imunitního systému.“**
- **„Vitamin C, vitamin E, zinek a selen přispívají k ochraně buněk před oxidativním stresem.“**

Všechny jmenují nosné živiny, ale **žádná z těchto čtyř doslovných formulací není v dostupném produktovém `info.md` zapsaná jako schválená**. Jejich aktuální individuální ověření v registru EU a podmínky použití pro tuto recepturu nebyly v této implementační zakázce provedeny. Nelze je proto označit za produktově schválené jen podle běžnosti formulace.

Vedle dodaných tvrzení uvádím skutečné jediné znění z claims oddílu `brand/product/beauty-longevity-nad-drink/info.md`:

> **Vitaminy skupiny B přispívají ke snížení míry únavy a vyčerpání, k normálnímu energetickému metabolismu a k normální funkci nervové soustavy.**

To je dostupná produktově zapsaná alternativa pro sdělení o vitaminech skupiny B, **nikoli ekvivalent tvrzení o kůži, vlasech, imunitě nebo antioxidaci**. Pro tyto čtyři účinky zdroj žádnou doslovnou schválenou alternativu neposkytuje; je třeba ověření konkrétních tvrzení a jejich podmínek. Samotný nadpis automaticky generovaného souboru není nové právní posouzení.

`brand/product/good-sleep-night-burn/info.md` výslovně neuvádí žádné EFSA tvrzení. Nový text o večerní receptuře konkrétní léčebný nebo spalovací účinek neslibuje. Původní mnohem silnější tvrzení o náhradě NAD+ infuzí, omlazování a nočním spalování v přepisovaných částech nezůstala. Importované kanonické detaily jsou samostatný dynamický obsah: při otevření se načítají aktuálně z obchodu a jejich vlastní účinkový text tímto předáním nebyl redakčně ani právně schválen.

Přečteno `brand/RULES.md`. Soubor `brand/NOT-ALLOWED.md` na dostupné cestě neexistuje. Samostatný produktový `info.md` pro Anti-Age nebyl v dostupném produktovém seznamu nalezen; jeho složení bylo porovnáno s přesnou kanonickou veřejnou stránkou produktu 550, ne se stejně pojmenovaným nápojem.

## Skutečné testy

- V obou dlouhých souborech ověřeno všech **56** očekávaných plných textových položek; v obou krátkých **7** (celý úvodní odstavec a šest popisků), nikoli jen klíčová slova.
- Původní obsahy všech SCRIPT a STYLE bloků zachovány byte-for-byte. Zachované zdrojové ID/URL všech detailových tlačítek, atributy hero fotografie a prázdné původní root `data-gl-product-id` (nemění se režim košíku).
- Chromium, skutečná veřejná česká stránka s dočasným přepsáním HTML odpovědi na stejném originu; žádné uložení CMS. Původní shopové skripty i dodané bootstrapy běžely přímo z HTML.
- Šířky **1440 a 390 px**: žádné horizontální přetékání krátkého ani dlouhého bloku, šest správných ikonových popisků, šest karet v požadovaném pořadí a šest FAQ. Hero fotografie načtená (naturalWidth 1024).
- Na obou šířkách skutečně kliknutím otevřeno/zavřeno všech šest FAQ a krátký obsah; otevřeno/zavřeno všech pět produktových detailů s odpovídajícím nadpisem a podstatným obsahem v Shadow DOM. Žádné importované SCRIPT prvky. Žádná zachycená JS chyba. Nákupní požadavek se neodesílal.
- Screenshoty skutečně prohlédnuté. Newsletter/chat/sticky překryvy skryté pouze v testovacím prohlížeči, nikoli změnou obchodu. Vysoký mobilní screenshot je přehled layoutu, nikoli důkaz přečtení každého znaku v jeho zmenšeném náhledu.
- Výsledky v `tests/longevity-darkovy-box-texty-results.json`. Publikační krok musí ověřit přesnou větev, změněné soubory a vzdálené bajty; úspěch Gitu není nasazení v Shoptetu.

## Vstupy, model a náklady

Vstupy: celý text od Pavla v tomto vlákně, aktuální vzdálená verze `pavel489/goldenlife-web`, veřejný dodaný slovenský odkaz a jeho skutečný český protějšek produktu 662, přesné kanonické detaily produktů 544, 550, 57, 597 a 653, `brand/RULES.md`, produktové soubory Beauty Longevity a Good Sleep.

Model: **gpt-6.1-sol**. Úprava HTML a jednoduché zaoblené obsahové symboly vytvořeny kódem. **Bez placeného obrazového/video generování.** Cena jazykového běhu a případné konektorové účtování nejsou v tomto rozhraní dostupné; nelze tvrdit celkové nulové náklady.
