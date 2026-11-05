# Dárkové boxy – dodané úvodní texty

## Provedená implementace

Pracovní HTML pro Pavla; nejde o uložení do živého Shoptetu ani o právní schválení dodané formulace.

- `shoptet/longevity.html`: dodaný dlouhý Longevity text je hned pod hlavním nadpisem. První věta je zvýrazněná, zbytek navazuje v odstavci.
- `shoptet/slim.html`: druhý, delší Mango text je hned pod hlavním nadpisem Collagen Slim.
- `shoptet/slim-kratky.html`: první, kratší Mango text nahrazuje úvod krátkého popisu.
- Označení „Longevity dlouhý“ a „Mango“ z briefu jsou mapování, nikoli součást zákaznického textu.
- Samotná dodaná znění jsou zachována bez stylistického přepisování. Dřívější doplňkové bloky „Pro koho je box“ / „Proč vybrat právě tento“, obsah boxů, fotografie, šestice piktogramů, tabulky, styly a veškeré skripty zůstaly beze změny. Krátký Longevity popis ani ostatní boxy se neměnily.
- Základ: ověřený vzdálený commit `94d27ad83872b212bd7b5657629745415eb785db`, tedy včetně předchozí opravy rozbalených tabulek.

## Kontrola tvrzení – oddělená od implementace

Dodané texty obsahují neschválená nebo nedoložená zdravotní/faktická tvrzení. Níže nejsou tiše přepsána; před případným použitím na živém e-shopu potřebují úpravu a kontrolu. Doplněk stravy není lék a nelze jej prohlásit za náhradu infuze.

### Longevity

- „Dárek, který potěší každého v každém věku!“ – nepřiměřeně široká vhodnost, zejména děti. Neutrální alternativa: „Vánoční dárek pro milovníky každodenní péče o sebe.“ Není to zdravotní claim.
- Věta „Tento nádherný vánoční box ukrývá … podporují vitalitu, mladistvý vzhled, energii a působí proti známkám stárnutí.“ – účinky na mladistvý vzhled a stárnutí nejsou v ověřeném produktovém souboru schválené. Pro únavu a energii je v `brand/product/beauty-longevity-nad-drink/info.md` zapsáno: „Vitaminy skupiny B přispívají ke snížení míry únavy a vyčerpání, k normálnímu energetickému metabolismu a k normální funkci nervové soustavy.“ Tato formulace nepokrývá omlazení.
- Věta „Hvězdou boxu je … jediný sáček nahradí nejen 16 tablet, ale i omlazující NAD+ infuze … hollywoodskými celebritami.“ – náhrada infuzí, počet nahrazených tablet a tvrzení o celebritách nebyly doloženy. Schválený ekvivalent pro náhradu infuzí ve zdroji není. Neutrální alternativa: „Hvězdou boxu je Beauty Longevity NAD+ drink v praktických sáčcích.“
- „Nyní si tento omlazující rituál … bez jehel a za dostupnou cenu.“ – omlazení a návazné srovnání s infuzí nejsou doložené. Neutrální alternativa: „Nápoj si snadno připravíte každý den.“
- „Box navíc obsahuje produkty pro kvalitní spánek a podporu metabolismu během noci.“ – efekt na spánek a noční metabolismus vyžaduje vlastní doložené tvrzení příslušného produktu. V přečteném zdroji Beauty Longevity není; nepřebírat k jinému produktu.
- „Dokonalý vánoční dárek … zůstat mladistvý, plný energie a vitality co nejdéle.“ – dlouhodobé omlazení nedoloženo. Energetický význam lze nahradit pouze výše uvedeným konkrétním tvrzením o vitaminech B.

### Mango / Collagen Slim

- Krátká věta „Darujte štíhlejší postavu, krásu a sebevědomí!“ i následující „Tento nádherný vánoční box … snadněji hubnout, omezit chutě na sladké, podpořit metabolismus … pleť, vlasy a nehty.“ obsahují příslib výsledku a produktové účinky, které nejsou v tomto rozsahu doložené přečtenými schválenými tvrzeními.
- V dlouhém popisu se totéž vztahuje na věty začínající „Dárek, který potěší každého…“, „Tento nádherný vánoční box spojuje…“, „Tři produkty, které se dokonale doplňují…“ a „Ideální dárek pro každého, kdo chce zhubnout, omládnout…“. Schválená alternativa ze souboru `brand/product/slim-extreme-collagen-box-ananas-mango/info.md`: „Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.“ Nejde o schválený ekvivalent hubnutí ani omlazení.
- „Slim Extreme Collagen Mango s více než 85 složkami … pečuje o pleť, vlasy a nehty.“ – počet 85+ ani souhrnný efekt této věty nebyl z přečteného produktového souboru ověřen. Obsah kolagenu, vitaminů, enzymů a probiotické kultury ve zdroji je, to ale samo neopravňuje účinkový claim.
- „GLP-1 Activator … pocit sytosti, kontrolu chutí a metabolismus cukrů, zatímco Slim Booster … metabolismus a kontrolu hmotnosti.“ – soubor `brand/product/slim-glp-1-activator-s-berberinem/info.md` výslovně neuvádí schválené EFSA claims tohoto produktu. Berberin a Nextida® jsou uvedeny ve složení; samotná přítomnost složky není oprávnění k účinkovému tvrzení. Neutrální alternativa části o Activatoru: „GLP-1 Activator obsahuje berberin a Nextida®.“ Schválené účinkové znění ke Slim Boosteru nebylo v použitých podkladech ověřeno.
- Název „Slim Booster“ byl v dodaném úvodu zachován; existující seznam obsahu boxu používá „Slim & Detox Power“. Odkaz v seznamu vede na `/slim-detox-power-plus-booster/`, kde je při kontrole veřejné H1 „Slim & Detox Super energy booster Power+“. Seznam nebyl v rámci úpravy úvodů přejmenován.

Kopii určenou k ostrému publikování doplňte o platná produktová upozornění. Obecné pravidlo značky: „Doplněk stravy. Není náhradou pestré a vyvážené stravy. Nepřekračujte doporučenou denní dávku. Uchovávejte mimo dosah dětí.“ Soubor `brand/NOT-ALLOWED.md` v aktuálním prostoru chybí; kontrola vychází z `brand/RULES.md` a výše jmenovaných produktových souborů. Nadpis „schválené“ v automaticky převzatých zdrojích není samostatný právní posudek.

## Skutečně provedené testy

- Přesné porovnání dodaných textů s vykreslenými úvody.
- Reverzní kontrola: vrácení jen nových úvodů obnoví celé původní soubory beze změny ostatních bytů.
- Samostatná shoda všech prvků script/style/img/button/table proti původním souborům.
- Chromium: úplné veřejné stránky s dočasnou náhradou cílových popisů pouze v testu, nikoli změnou živého obchodu.
- Devět kontrol kombinací popis/šířka: Longevity dlouhý, Mango dlouhý a Mango krátký při 1440, 390 a 320 px. Vše prošlo, přesné texty, šest piktogramů v každém bloku, žádné horizontální přetečení testovaných bloků; v dlouhých popisech text před piktogramy. Krátký Mango obsah se otevřel a zavřel ve všech třech šířkách.
- Pro čisté snímky jsou jen v testovací kartě skryté překryvné cookie/chat/sticky komponenty; tyto zásahy nejsou součástí dodávaného HTML.
- Výsledky: `docs/darkove-boxy-dodane-uvodni-texty-testy.json`.

Podklady: Pavlův dodaný text, aktuální autorizovaný Git repozitář, veřejné produktové stránky, brand/RULES.md a uvedené produktové soubory. Zpracování: gpt-6.1-sol, Python/BeautifulSoup, Chromium/Playwright. Bez placené obrazové generace a bez nového placeného mediálního API volání; cenu běhu agenta nelze z použitých nástrojů vyčíslit.
