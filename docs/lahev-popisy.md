# Láhev Golden Life – popisy, odkazy a hlavní fotografie

- `shoptet/lahev.html`: celý fragment vlož do **dlouhého popisu v HTML režimu**. Není to celý HTML dokument; neobsahuje `<html>`, `<head>` ani `<body>`.
- `shoptet/lahev-kratky.html`: krátký popis s doplněným objemem 0,5 l.
- `nahledy/lahev.html`: samostatný offline náhled s vloženými skutečnými fotografiemi.
- `web/Golden Life Lahev/Golden_Life_Lahev_cz.html`: samostatný pracovní dokument. I ten nyní používá funkční veřejnou fotografii a synchronizaci hlavní galerie, ne relativní `/assets/` cestu.

## Rozsah úpravy
Zachována jedna hlavní karta láhve a stručný text doplněný o objem 0,5 l, červená `#d90817` a font Metropolis/Arial/Helvetica. Do karty doplněno pět skutečných odkazů s malými obrázky, obdobně jako vizuální seznam na https://www.golden-life.cz/michatko/: Slim Extreme Collagen ananas, Slim Extreme Collagen ananas/mango, Peptides GLP-1 Woman Balance, Slim GLP-1 Shake cappuccino a Beauty & Longevity NAD+. Každý cíl a packshot je ověřen z aktuálního e-shopu včetně přesného ID produktu. Nápoj cappuccino vede na ID 547, nikoliv na příslušenství pojmenované Shaker.

## Oprava fotografie
Při živé kontrole popis láhve obsahoval `/assets/lahev-golden-life.webp`, který na e-shopu nefungoval, a žádné převzetí hlavní galerie. Galerie přitom obsahovala skutečnou načtenou fotografii produktu 597. Nový skript přebírá úspěšně načtený `currentSrc` z `#main-slider-slide01 img`, reaguje na načtení, změnu `src/srcset` a výměnu elementu. Synchronizuje jen na hostiteli s nativním ID 597. Na jiném produktu, bez galerie či při její chybě zůstává ověřený veřejný obrázek láhve; když selže i ten, zobrazí se textový fallback. Žádné obrázky jiného produktu se nepřebírají. Opakované selhání stejného zrcadleného zdroje nevyvolává nekonečné požadavky.

Skript je v CMS vložen přímo; nenačítá externí JS. `assets/bottle-main-photo.js` je jeho čitelná zdrojová kopie. Offline fotografie jsou převedeny do WebP bez změn produktu či loga; nová hlavní fotografie je zachována celá.

## Zdroje a ověření
`brand/RULES.md`, dosavadní popis z ověřeného `main`, živé stránky láhve a míchátka, pět propojených produktových stránek. Přesné URL, ID, rozměry a hashe jsou v `config/lahev-sources.json`. Testy jsou v `tests/lahev-results.json`: prohlížeč Chromium, mobil/desktop, skutečné stažené fotografie, zachycené navigace, synchronizace galerie a explicitně syntetické chybové/identitní scénáře. Vzhled ověřen na offline náhledu. Lokální vložení do zachyceného živého DOM neznamená uložení do Shoptetu.

Objem **0,5 l** je doplněn do krátkého i dlouhého popisu podle aktuálního zadání Pavla. Materiál, myčka, teplotní odolnost ani nepropustnost nejsou doložené a copy je neslibuje. Přidané odkazy obsahují identifikační názvy, nikoliv nová zdravotní tvrzení. Boxy, ceny a košík se nemění. Krátký popis se rozšiřuje pouze o potvrzený objem. Nasazení do Shoptetu nebylo provedeno.

Model: gpt-6.1-sol. Bez placené obrazové generace; celkové poplatky modelu a konektoru nejsou v nástrojích vyčíslené.
