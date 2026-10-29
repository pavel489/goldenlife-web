# Hormonal Trio — náhledy v rozcestníku

Zdroj: pavel489/goldenlife-web, main 8aca1dade14c959a0ada6429767a771d104c983d; web/Golden Life Hormonal Trio/Golden_Life__Hormonal_triocz.html.

Změněny pouze tři src obrázků v sekci „Tři produkty v balíčku“. Každý nyní používá skutečnou hlavní fotografii příslušného samostatného produktu z veřejné galerie Shoptetu:
- productId 644: Woman Hormonal Balance se Shatavari;
- productId 635: Peptides GLP-1 Woman Balance Dark Cherry, balení box + sáček;
- productId 550: Anti-Age Longevity NAD+.

Každá stránka ověřena přes nativní productId, obrázek stažen a vizuálně prohlédnut. URL nočního drinku nyní přesměrovává na /hormonal-balance-nocni-glp-1-drink/, productId zůstává 635. Neobvyklý filename obrázku 550 není změněn: skutečný obrázek i produktové ID potvrzují NAD+.

Texty, CSS, skripty včetně importů detailů a košíku, krátký popis a ostatní fotografie zachovány. Zpětné dosazení tří starých URL vrací bajtově shodný původní HTML soubor. Tato oprava netestuje ani neschvaluje původní importní/košíkovou implementaci. Původní zdravotní tvrzení a statický údaj o skladu nejsou tímto schválené; při této obrazové opravě nebyly měněny.

Testy: Chromium/Playwright v šířkách 320, 390, 768, 1024 a 1440 px, všechny tři skutečné veřejné obrázky načtené, object-fit contain, žádný vodorovný přetok ani JS chyba testovaného rozcestníku. Offline náhled obsahuje vložené fotografie a žádné síťové požadavky; import detailů je v něm neaktivní a font je Arial místo hostovaného Metropolis. Produkční zdroj fonty ani tlačítka nemění.

Podklady: dodaná stránka, veřejné galerie tří konkrétních produktů, brand/RULES.md. Úprava GPT-6.1, Python a Playwright; bez nové obrazové generace, cenu agentového provozu nemáme vyčíslenou. GitHub main je oddělený od uložení do Shoptetu; do administrace e-shopu se neukládá.
