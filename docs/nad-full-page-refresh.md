# Anti-Age Longevity NAD+ — vylepšený celý produktový popis

Základ main 47fcc622245dcba59b5873aab2e475ba74cda5b8 a veřejná aktuální stránka SKU 550. Jde o vylepšení celého dlouhého a krátkého popisu, ne jen výměnu obrázků. Zachována červená produktová paleta, skutečné fotografie, devět dodaných obrázků aktivních látek, celé původní popisy složek, tabulka složení, dávkování a upozornění. Odstraněna jedna přesně duplicitní úvodní věta.

Nový úvod s autentickým balením, fakta 60 tobolek / 2 kapsle denně / 30 denních dávek, navigace, devět nativních rozbalovacích detailů, mobilní posouvání karet, sjednocený blok CTA, přehlednější užívání a tabulka. CSS je omezené na #gl-nad a #gl-nad-short, bez globálních :root proměnných. Typografie dědí Nunito z aktuálního e-shopu; není to nová schválená fontová norma.

Fotografie hero/CTA: přesná veřejná hlavní galerie SKU 550, ořez pouze prázdných okrajů (350,280,680,790), bez generování, retuše etikety a změny proporcí. Neměnný obrázkový commit 6d5e610d7748124562ce4f7133cdc2c1bbd3e7f8. Při nové načtené hlavní fotografii téhož SKU může komponenta fotografii převzít; při chybě se vrací k dodanému základu.

Nákupní CTA pouze odkazuje/posouvá k nativnímu objednávkovému formuláři, nikdy samo neodesílá košík. Cena a dostupnost se jen zobrazují z nativního hostu pod ověřeným productId 550. Bez hostu zůstávají skryté, žádná cena 0 nebo falešné skladem. Odstraněna vložená metadata/Offer z CMS fragmentu; shopová metadata se v tomto úkolu nemění.

Zachované zdravotní účinky nejsou tímto schválené. Pro toto SKU nebyl nalezen soubor schválených tvrzení; podklady ke kontrole jsou v lokálním předávacím souboru poznamky-k-textum.md.

Ověření: reálné Chromium viewporty 320/390/768/1024/1440, devět detailů a posouvání, krátký popis v úzkém desktopovém hostu, obrázky, izolace stylů, nákupní fallback a testovací host bez odeslání objednávky. Nejde o fyzické telefony či WebKit. Nová placená obrazová generace: žádná. Git main není uložení do Shoptetu; v administraci se neukládalo.
