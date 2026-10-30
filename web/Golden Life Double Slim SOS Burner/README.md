# Double Slim SOS Burner – dvě dózy v aktuální grafice SOS

## Hotový rozsah
- Celý dlouhý a krátký popis podle aktuální připravené verze **Slim SOS Fat Burner**, nikoli nový odlišný koncept.
- Samostatný ověřený produkt **573**, canonical https://www.golden-life.cz/double-slim-sos-burner/. Referenční single má ID 473; zdroje fotografií se nesměšují.
- **2 dózy × 60 tobolek = 120 tobolek, 60 dní při 2 tobolkách denně.** Denní dávka se nezdvojnásobuje. Veškeré přehledy, FAQ, krátký popis, banner i mobilní CTA to zohledňují.
- Hmotnost je podle vlastního veřejného krátkého popisu Double **2 × 47,6 g**.
- Složení v jedné a ve dvou tobolkách je přesná kopie současného single SOS, včetně chromu **0,55 mcg / 1,11 mcg**. Nejde o množství v celé zásobě ani o zdvojení denních hodnot.
- Pět plných odlišných významových popisků a dialogů + všech pět přesně dodaných ingredientních PNG zachovaných.
- Růžové piktogramy Slim **#E40E7E**, žádný druhý barevný filtr.
- Hlavní fotografie i CTA používají vlastní skutečnou hlavní galerii Double se dvěma dózami; synchronizace je vázaná na nativní ID 573, včetně pozdějšího načtení a výměny snímku.
- Původní single SOS, ostatní produkty a společné CSS se nemění.

## Soubory k importu
- [Dlouhý popis](Golden-Life-Double-Slim-SOS-Burner-cz.html)
- [Krátký popis](maly/Golden-Life-Double-Slim-SOS-Burner-maly-cz.html)
- [Vlastní barevné CSS](../../user/documents/upload/css/golden-life-barvy-double-slim-sos-burner.css)
- [Celý HTML náhled](../../nahledy/double-slim-sos-burner.html) – stažení a otevření v prohlížeči, fonty a fotografie potřebují internet. Nákup v náhledu je vypnutý.
- [Náhled úvodu](../../nahledy/double-slim-sos-burner-uvod.png), [celá stránka](../../nahledy/double-slim-sos-burner-stranka.png).

Dlouhý i krátký HTML obsahují jeden malý style blok se dvěma importy: stávající `golden-life-produkt.css` a nové `golden-life-barvy-double-slim-sos-burner.css`. Pro import nahraj nové barevné CSS do stejné složky a nahraď oba popisy. Nepřidávej importy za původní staré vložené CSS; nahraď kompletní fragment. Git publikace není uložení do Shoptetu; administrace ani ceník nebyly změněné.

## Co se skutečně ověřilo
- Devět průchodů kombinací souborového náhledu a přesných CMS fragmentů se skutečnými shop styly při 320, 390, 768 a 1440 px, včetně návratu na mobil.
- Dvanáct explicitně lokálních fixture případů pro galerii, načtení, výměnu uzlu, srcset, chyby, obnovu a odmítnutí ID jedné dózy 473. Test neodesílá košík.
- Všech 11 ikon načtených a bez dodatečného filtru, oba produktové snímky odpovídají skutečné hlavní fotografii Double. Bez rozbitých použitých obrázků, přetečení stránky a JS chyb v izolovaných testech.
- Všech pět ingredientních dialogů otevřeno a zavřeno. Všechny tři mobilní přepínače ověřené myší/Enterem.
- Tabulka porovnaná buňku po buňce se single referencí; pěti kartám a pěti dialogům se nezměnily HTML bajty. Změny balení zahrnují také text vytvářený JavaScriptem pro mobilní CTA.
- Nový fragment byl vložen do vlastního prohlížeče skutečné veřejné stránky Double. Po inertním vložení se oba přesné bootstrap skripty jednou spustily a hlavní fotografie se správně převzala z nativní galerie 573. Šlo pouze o místní test, nikoli uložení do e-shopu.

[Strojové testy](../../docs/double-slim-sos-burner-testy.json) · [Test skutečné stránky](../../docs/double-slim-sos-burner-browser.json) · [Manifest](../../docs/double-slim-sos-burner-manifest.json) · [Výhrady k tvrzením a fotografii](../../docs/double-slim-sos-burner-texty.md).

## Podklady a stav
Aktuální verze Slim SOS Fat Burner na Gitu; vlastní veřejná Double stránka, její ID a hlavní fotografie; pět dodaných ilustrací aktivních látek; vizuální identita Golden Life. Účinkové texty jsou převzatý pracovní návrh, ne nové právní schválení. Původní fotografie nese štítek **−50 %**; platnost této nabídky nebyla ověřená a do nových textů se žádná výše slevy nepřidává.

Model GPT-6.1-sol; Python/BeautifulSoup/Pillow, Chromium/Playwright, Composio GitHub. Žádná nová placená obrazová/video generace; cenu běhu modelu nástroje neposkytují. Doručení na Git, bez ZIPu.
