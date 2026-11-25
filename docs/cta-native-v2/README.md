# Produktové CTA v2 — obě nové dávky, pouze Git

Rozsah je **všech 11 produktů ze dvou předchozích dávek** v tomto vlákně. Změněno pouze CTA v jejich českých dlouhých popisech, přidán jeho vlastní CSS soubor a editovatelný JS master. Žádné uložení do Shoptetu.

## Uspořádání
- Mobil: skutečná hlavní fotografie přes celou šířku CTA, pod ní název, denní dávka/použití a balení, živá cena včetně DPH, tlačítko **Hodit do košíku**. Nadpis je pod obrázkem, aby nezakrýval obal.
- Počítač: fotografie vlevo, stejná přehledná nákupní část vpravo.
- Beze změny produktových barev. Jeden hlavní obrázek; žádné dodatečné mockupy.

## Fotografie, cena a tlačítko
Každý fallback je skutečný aktuálně ověřený hlavní obrázek vlastního nativního SKU. Po načtení hostitelského produktu CTA sleduje první hlavní galerijní obrázek (`#main-slider-slide01`), nikoli libovolnou právě aktivní další fotografii. Platí kontrola vlastního productId a úspěšného načtení.
Přiblížení prázdných okrajů je pouze CSS a pouze pro přesné ověřené soubory (pathname). Originální soubory a produkční URL se nemění. Při jiné hlavní fotografii se její přiblížení resetuje; celý produkt není ořezán. Metadata původních pixelových mezí v `photo-fit.json`.
Cena pochází pouze z `.p-final-price-wrapper` uvnitř správného `form#product-detail-form`; nepřebírá ceny doporučených produktů. Samostatná produkční HTML nemají pevnou cenu ani skladový slib. Bez správného nativního formuláře je cena „—“, tlačítko vypnuté a zůstává odkaz k hlavnímu nákupu.
Klik deleguje na původní nákupní tlačítko stejného produktu. Nemění množství, endpoint košíku, tracking, sklad, platební údaje ani checkout. Nezobrazuje vlastní smyšlené potvrzení přidání. Ve zkouškách se skutečný požadavek do košíku neodesílá.

## Produkty
- ID 383: [Slim Extreme Collagen box s příchutí ananasu](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas/Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html)
- ID 174: [Slim & Detox Super energy booster Power+](../../web/Golden%20Life%20Slim%20Detox%20Power%20Plus/Golden-Life-Slim-Detox-Power-Plus-cz.html)
- ID 464: [Slim Extreme Collagen box s příchutí ananas - mango](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20box%20ananas%20mango/Golden-Life-Slim-Extreme-Collagen-box-ananas-mango-cz.html)
- ID 467: [Slim Extreme Collagen sáček s příchutí ananas - mango](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas%20mango/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-mango-cz.html)
- ID 416: [Slim Extreme Collagen sáček s příchutí ananasu](../../web/Golden%20Life%20Slim%20Extreme%20Collagen%20sacek%20ananas/Golden-Life-Slim-Extreme-Collagen-sacek-ananas-cz.html)
- ID 544: [Beauty Longevity NAD+](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20d%C3%B3za/Golden-Life-Beauty-Longevity-NAD-doza-cz.html)
- ID 550: [Anti-Age longevity NAD+](../../web/Golden%20Life%20Anti-Age%20Longevity%20NAD%2B/Golden-life-Anti-Age%20Longevity%20NAD%2B.html)
- ID 51: [Beauty Body & Soul®](../../web/Golden%20Life%20Beauty%20Body%20Soul/Golden-Life-Beauty-Body-Soul-cz.html)
- ID 600: [Beauty Longevity NAD+ sáček](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20s%C3%A1%C4%8Dek/Golden-Life-Beauty-Longevity-NAD-sacek-cz.html)
- ID 57: [Good Sleep & Night Burn](../../web/Golden%20Life%20Good%20Sleep%20Night%20Burn/Golden-Life-Good-Sleep-Night-Burn-cz.html)
- ID 99: [Miracle Drops](../../web/Golden%20Life%20Miracle%20Drops/Golden-Life-Miracle-Drops-cz.html)

## Integrace
- CSS: `user/documents/upload/css/golden-life-cta-native-v2.css`. Jeho import je přidaný za společné a produktové styly; při samostatném pozdějším nasazení je nutné tento **nový CSS soubor také nahrát**.
- JS master: `user/documents/upload/js/golden-life-cta-native-v2.js`. Stejné bytes jsou vložené v každém dlouhém HTML, takže pro tuto verzi není potřeba nový JS upload.
- Úplné HTML mimo původní CTA, nový CSS import a závěrečný bootstrap zůstává byte-for-byte stejné. Všech 11 krátkých popisů, tabulky složení, ingredient modaly, dávkování v úplných popisech, společné CSS/JS a jiné produkty zůstávají nezměněné.

## Otevřené věcné údaje
- 51 Beauty Body & Soul: v dostupném vlastním HTML ani na aktuální hlavní fotce není ověřená celková hmotnost. CTA uvádí pravdivé „Dóza s práškem“, denní dávku 8 g a 2 odměrky. Hmotnost balení se nedopočítává z neurčitého tvrzení „na dva měsíce“.
- 464 ananas–mango box: uvedeno 30 sáčků podle vlastního zdroje; rozpornou hmotnost 240/246 g CTA nevolí. U jednotlivých sáčků je počet 1 bez sporné gramáže.
- 544 ve starším seznamu „dóza“: aktuální skutečný hlavní obrázek téhož SKU je box se sáčky. Použit přesně podle nového požadavku, nikoli vymyšlená dóza.
- 550 ve starším seznamu „tablety“: počet a dávka zůstávají z vlastního připraveného zdroje „60 tobolek / 2 kapsle“.

## Ověření a limity
Přesné výsledky a hashe finálního běhu jsou v `qa-summary.json`. Jde o izolovaný Chromium se skutečnými zdrojovými HTML/CSS/JS, aktuálními autentickými obrázky a řízenými nativními fixture. Není to uložení do Shoptetu ani test ostrého přidání do košíku, fyzického Safari nebo právní certifikace.
Samostatný soubor `Golden-Life-nove-CTA.html` je offline příloha pro prohlížení všech 11 variant. Cena v něm je označený veřejný snímek, nákup je vypnutý a v prohlížeči se ověřuje nulová externí síť. Příloha nepředstírá živou cenu.

## Tvrzení a podklady
CTA nepřidává léčebná, hubnoucí ani anti-aging tvrzení; uvádí názvy, vlastní dávky, balení a nákupní údaje. Dřívější výhrady ke zděděným tvrzením v jiných sekcích nadále platí: [Slim dávka](../slim-five-git-handoff/README.md), [Beauty dávka](../beauty-six-git-handoff/README.md).
Použitá obrazová reference: uživatelem vložený CTA screenshot v tomto vlákně; originál uložený lokálně, nebyl použit jako zdroj produktových faktů. Dále aktuální Git main, vlastní produktové popisy, brand/RULES.md a veřejné nativní galerie.
Model gpt-6.1-sol; Python, Chromium/Playwright, existující Composio GitHub. Bez placené obrazové generace; cena modelu a nástrojů není vyčíslená.