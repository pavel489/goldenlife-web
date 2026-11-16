# Oprava piktogramů: Longevity SK a UFIRST SK

Opraveny jen chybějící obrázky a masky šesti piktogramů v krátkém a dlouhém popisu každého ze dvou boxů (24 pozic). Použity existující PNG stejného produktu z českých originálů, žádné nové generování. Texty, fotografie, CSS a skripty nebyly redesignovány ani překládány.

## Soubory pro vložení

- `web/Golden Life Darkovy box Longevity/Golden_Life_Darkovy_box_Longevity_sk.html` — dlouhý popis
- `web/Golden Life Darkovy box Longevity/maly/Golden-Life-Darkovy-box-Longevity-maly-sk.html` — krátký popis
- `web/Golden Life Darkovy box UFIRST/Golden_Life_Darkovy_box_UFIRST_sk.html` — dlouhý popis
- `web/Golden Life Darkovy box UFIRST/maly/Golden-Life-Darkovy-box-UFIRST-maly-sk.html` — krátký popis

Krátký Longevity je minimální oprava aktuálního Git souboru. Tři dosud chybějící SK soubory jsou odvozeny z aktuálních veřejných popisů a upraveny pouze v piktogramech; automatický nadpis šablony „Podrobný popis“ není součástí souborů. Nejde o surový export CMS. Před ručním vložením zálohujte původní nativní pole a zkontrolujte případné novější změny.

## Ověření

`qa.json`: přesné výsledné HTML vložené do skutečné šablony stránky dočasným přepsáním odpovědi pouze v testovacím prohlížeči. Oba boxy, oba popisy, 1440 a 390 px: osm úspěšných scénářů. Ověřeno šest načtených PNG a šest platných vykreslených masek v každém bloku; vizuálně zkontrolován `nahled.jpg`. Změny jsou reverzibilní a textový obsah zůstal beze změny. Safari/fyzický telefon neověřen.

## Stav a omezení

**Git podklady nejsou nasazení do Shoptetu. V rámci tohoto zadání nebyl uložen živý CMS.** Po vložení je nutná kontrola veřejných stránek. Existující české texty uvnitř SK mutací a dřívější produktová tvrzení zůstávají beze změny; nejde o jejich jazykové ani právní schválení.

Podklady: aktuální veřejné SK stránky, české piktogramy a Git základ 20b449a66194e538c3339d4a6696bfc6f3bb96d0; brand/RULES.md. Nástroje Python, BeautifulSoup, Playwright/Chromium a Pillow. Model asistenta gpt-6.1-sol. Žádné placené generování ani nákup služby; běžná spotřeba asistenta nevyčíslena.
