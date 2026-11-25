# CTA – denní dávka pouze jako množství

Oprava pro všech stejných 11 produktů, jen Git. V levém CTA boxíku jsou dva řádky: štítek a krátké množství, nikoli celý návod.

## Denní množství
- ID 383: 1 sáček
- ID 174: 2 tobolky
- ID 464: 1 sáček
- ID 467: 1 sáček
- ID 416: 1 sáček
- ID 544: 1 sáček
- ID 550: 2 kapsle
- ID 51: 8 g
- ID 600: 1 sáček
- ID 57: 2 tobolky
- ID 99: 3–5 kapek

U Detoxu je v CTA **Denní dávka / 2 tobolky** podle explicitní opravy a vlastního `brand/product/slim-detox-power-plus-booster/info.md` (běžná denní dávka 2 tobolky). Detailní návod prvního týdne, další bezpečnostní pokyny a dávkování v úplném popisu zůstávají byte-for-byte beze změny. U Miracle Drops zůstává kosmetický štítek „Použití“, nikoli dávkování doplňku stravy.

Změněná je pouze hodnota prvního DD ve vlastním CTA každého produktu. Fotografie, bublina, balení, CSS, cena/košík JS i všechny krátké popisy se nemění. Přesný původní a nový text je v changes-ledger.json.

## Ověření
55/55 izolovaných CTA scénářů: 320px viewport s 280px hostem i plnou šířkou, 375/768/1280 px; každý první DT i DD má přesně jeden vykreslený textový řádek a nepřetéká. Nákupní klik deleguje na nativní fixture bez reálného odeslání košíku. Offline náhled 22/22 scénářů, nákup vypnutý a bez externí sítě.
Není to nasazení do Shoptetu ani změna etikety nebo odborné schválení. Předchozí věcné výhrady zůstávají platné.

Podklady: vlastní aktuální Git a produktový soubor Detoxu, brand/RULES.md a uživatelova oprava. Model gpt-6.1-sol, bez placené obrazové generace; cena modelu/nástrojů není vyčíslená.