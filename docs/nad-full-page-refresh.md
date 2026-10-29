# Anti-Age Longevity NAD+ — stejná šablona jako Woman Hormonal Balance se Shatavari

Tato revize nahrazuje předchozí samostatný návrh přímou adaptací pojmenované předlohy. Referenční soubory: web/Golden Life Woman Hormonal balance/Golden_Life_Darkovy_box_Hormonal_cz.html a jeho maly/ fragment, z aktuálního main. Předloha zůstává beze změny.

Přeneseno: úvodní banner s hlavní látkou a denní dávkou, Metropolis font stack, produkt vlevo a šest ikon vpravo, dvě obsahové karty, seznam účinků, ingredienční fotografie s krátkou větou a tlačítkem plus vlevo nahoře, CSS :target dialogy, mobilní vodorovné posouvání, CTA s hlavní fotografií, užívání a tabulka. Obsah, červená NAD paleta, 9 dodaných fotografií, celý text podrobností, dávky, složení a upozornění zůstávají NAD; Shatavari/BioPerine ani hormonální tvrzení, graf výsledků a délka kúry z předlohy se nepřebírají. NR dávka300mg je ze stávající tabulky NAD.

Zdrojové NAD HTML před samostatným redesignem:47fcc622245dcba59b5873aab2e475ba74cda5b8. Jedna přesně duplicitní úvodní věta je odstraněna. Žádná nová účinková tvrzení nevznikají; původní texty nejsou tímto nově schválené. Schválený produktový claims soubor nebyl pro SKU nalezen.

CSS je parserem Chromium omezené na #nad-popis, krátký popis na #nad-short. Unikátní root zabraňuje kolizi hostitelských pravidel pro obecné #special-popis. Produkční karty mají vůči předloze ověřené shodné computed styly radius/imageHeight/headingSize/headingAlign/plusWidth/plusLeft/fontFamily v pěti šířkách. Offline náhled používá Arial místo hostovaného Metropolis.

Nativní bridge je omezený na productId550. Zobrazí pouze aktuální cenu/dostupnost nativního hostu a tlačítko posune/fokusuje původní formulář, neposílá nákup. Bez hostu se neukazuje smyšlená cena ani sklad. Hlavní foto a CTA mají ověřený autentický fallback; devět obrázků karet i dialogů je připnutých na dříve ověřené immutable URL.

Testy: pět šířek320/390/768/1024/1440, všech9 dialogů a horní detail, pět porovnání s předlohou, mobilní swipe, krátký host220/320/366/540px, test s aktuálními veřejnými styly e-shopu390/1440 a syntetické větve nativního bridge. Sanitizovaný hostovací fixture není uložený Shoptet; inicializační load-fade a překryvy se vypínají jen v testu. Nejde o fyzické telefony nebo WebKit.

Bez nové obrazové generace a nových obrazových assetů. Git main není uložení do Shoptetu; administrace e-shopu se neměnila.
