# Hormonal Duo — hlavní fotografie produktů v rozcestníku

Zdroj: pavel489/goldenlife-web, main 6b78706f220c6c4d7877f1c25cbc2844d368581e; `web/Golden Life Hormonal Duo/Golden_Life__Hormonal_duo_cz.html`.

Po vzoru úpravy Hormonal Trio jsou nahrazeny pouze dvě adresy `src` v rozcestníku „Dva produkty v balíčku“:
- Woman Hormonal Balance se Shatavari, nativní productId 644: skutečná hlavní fotografie lahvičky z veřejné galerie.
- Peptides GLP-1 Woman Balance Dark Cherry, nativní productId 635: skutečná hlavní fotografie boxu se sáčkem z veřejné galerie. Původní produktová URL přesměrovává na `/hormonal-balance-nocni-glp-1-drink/`, ID odpovídá.

Obě stránky i hlavní galerie byly znovu načteny, fotografie staženy a jejich zobrazení na desktopovém i mobilním snímku skutečně prohlédnuto. Fotografie jsou celé, správně orientované a neoříznuté. Rozdílná velikost produktů uvnitř zdrojových čtverců je zachována.

Zpětná výměna přesně dvou URL vrací bajtově shodný původní soubor. Texty, CSS, hero, CTA, skripty, importy detailů, košík i krátký popis zůstávají beze změny. Původní zdravotní tvrzení a statický sklad nejsou touto obrazovou opravou schválené; nejde o právní audit ani o test původních detailových/košíkových skriptů.

Chromium/Playwright: skutečné vzdálené fotografie úspěšně načteny při šířkách 320, 390, 768, 1024 a 1440 px; `object-fit: contain`, bez vodorovného přetoku a JS chyb testovaného rozcestníku. Přiložený offline náhled má vložené fotografie, nepoužívá síť, nahrazuje font Metropolis fontem Arial a deaktivuje import detailů pouze v náhledu.

Podklady: aktuální HTML Duo, postup již provedené úpravy Trio, veřejné galerie konkrétních produktů a brand/RULES.md. Provedení: GPT-6.1, Python, BeautifulSoup a Playwright. Bez nové placené obrazové generace; cenu agentového provozu nemáme vyčíslenou.

Publikace je pouze do GitHub main. Do administrace Shoptetu se nic neukládá.
