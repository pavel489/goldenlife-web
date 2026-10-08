# Láhev Golden Life – stručné popisy

- `shoptet/lahev-kratky.html`: celý obsah vlož do krátkého popisu v HTML režimu.
- `shoptet/lahev.html`: celý obsah vlož do dlouhého popisu v HTML režimu.
- `nahledy/lahev.html`: samostatný offline náhled obou popisů se zabalenou fotografií.
- `web/Golden Life Lahev/`: dlouhý dokument a krátký fragment v `maly/`, stejně jako u boxů.

Zachována červená `#d90817` z připravených Golden Life boxů. Jen jedna produktová karta, žádné další produkty, košík, FAQ ani zdravotní tvrzení. Skutečná fotografie z galerie lahve; jen ořez prázdných okrajů, bez generování nebo úprav potisku. CMS používá původní URL fotografie z e-shopu, ne pohyblivý Git CDN odkaz.

Zdroj: `brand/RULES.md`, dokumentace barev boxů v `shoptet/README.md`, https://www.golden-life.cz/lahev-golden-life/ (produkt 597) a aktuální úvodní fotografie. Na živé stránce chyběl krátký i dlouhý popis. Objem, materiál, vhodnost do myčky, teplotní odolnost a nepropustnost nejsou doložené, proto je copy neslibuje. Font přebírá styl boxů Metropolis s Arial/Helvetica fallbackem; licence ani nový font se nepřidává.

Ověření: viz `tests/lahev-results.json`. Místní Chromium není test uložené Shoptet administrace. Nasazení na e-shop nebylo provedeno.

Model: gpt-6.1-sol. Bez placeného generování obrázků; skutečné poplatky modelu a konektoru nejsou v této relaci dostupné.
