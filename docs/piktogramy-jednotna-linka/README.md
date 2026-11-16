# Jednotná tloušťka linky piktogramů

Oprava obou dosud dodaných sad bez vnějších koleček. Nestačilo ztenčit hotové PNG: původní sady kombinovaly siluety, výplně a několik vah obrysů. Proto jsou vlastní symboly nově nakreslené jedním linkovým systémem, nejsou to původní pixely po filtru.

## Jednotný systém
- Konstrukční plocha 64 × 64.
- Šířka každé čáry **2 jednotky**; tedy referenčně 2 px při zobrazení 64 × 64 px.
- Zaoblené konce i spoje: `stroke-linecap="round"`, `stroke-linejoin="round"`.
- `fill="none"`; bez plných siluet a bez dekorativních vnějších kruhů.
- Žádné individuální šířky čar nebo dodatečné škálování cest v jednotlivých symbolech.
- Smysluplné vnitřní kruhové tvary, například talíř, hlava či oko, nejsou vnějším rámem a zůstávají součástí motivu.
- Barvy jednotlivých variant jsou převzaté z viditelného inkoustu dosavadních PNG. Jde o sjednocení kresby, ne návrh nové palety; původní barevné rastry s přechodem jsou pro tento pracovní systém převedeny na jednu jejich skutečnou inkoustovou barvu, ne vydávány za nové oficiální vzorníky.

Při zobrazení PNG v jiné velikosti se celá kresba včetně tloušťky poměrně škáluje. Neslibujeme fyzicky stejné 2 CSS px pro současně rozdílně velké obrázky. Všechny varianty však mají shodnou váhu při stejné zobrazovací velikosti. Kontrola zahrnuje 40, 64 a 85 px.

## Dodáno
- 46 editovatelných SVG motivů v `assets/piktogramy/monoline-v3/masters/`.
- 104 barevných transparentních PNG, 256 × 256 px, v `assets/piktogramy/monoline-v3/`.
- Mapování všech 109 původních obrazových variant z obou dosavadních sad.
- 203 HTML souborů s 1 090 výměnami obrazových adres. Texty, popisky, tabulky, skripty, nákupní logika a ostatní bajty jsou zachované; rozdíl je inventarizovaný po URL.
- Neměnné nové adresy obrázků používají asset revizi `286002abbca46d80f336fac0579177c82e7c8c37`.

Rozsah není tvrzením, že byly nově překreslené všechny jiné, nedotčené rodiny ikon v celém e-shopu nebo že se změna uložila do živého Shoptetu. Staré kontaktní listy, archivní testy a původní obrazové podklady zůstávají jako historie.

## Přehled a důkazy
- `nahled-pred-po.jpg`: stručný přehled změny váhy skutečných předloh.
- `vsechny-motivy-64px.png` a `vsechny-motivy-40px.png`: všechny motivy v referenční a malé velikosti.
- `kontrolni-nahled.html`: samostatný offline náhled všech barevných PNG v 64 a 40 px.
- `mapovani.json`: přesné vazby starý asset → motiv/barva → nový asset a kontrolní hashe.
- `kresba-qa.json`: všechny SVG mají jednu stejnou šířku, konce, spoje a prázdnou výplň; PNG nejsou prázdná ani oříznutá. Referenční čára byla skutečně vykreslena a změřena alfa pokrytím při 40/64/85/256 px.
- `https-qa.json`: 104 skutečných HTTPS PNG, HTTP 200 / image/png, shodné bajty se zdrojem.
- `browser-qa.json`: dvě Chromium scény na 390/1280 px; pokaždé načteno všech 208 ukázek (104 variant × dvě velikosti), bez vodorovného přetečení samostatného náhledu.
- `html-qa.json`: zdrojová revize a přesné výměny pro každý z 203 změněných souborů.
- `regeneruj.py`: funkční reprodukce PNG z dodaných SVG a mapování. Vyžaduje Pillow a CairoSVG; spuštěno z kořene repozitáře příkazem `python3 docs/piktogramy-jednotna-linka/regeneruj.py`, ověřuje i shodu výsledných hashů.

Vizuálně zkontrolovány všechny motivy v 64 i 40 px a finální srovnávací náhled. Záměrné spoje anatomických částí, překřížení DNA či samotné přeškrtnutí nejsou různou nastavenou vahou čáry. Nejde o kompletní test dialogů, obchodní logiky nebo každého nativního mobilního hostitele.

## Nasazení a původ
Soubory jsou připravené na Gitu. Do živého CMS nebylo zapisováno. Při nasazení zachovejte všechny novější úpravy CMS a aplikujte jen aktuální obrazové adresy; starší veřejné podklady v `shoptet/piktogramy-dalsi/` nejsou automaticky surovým exportem nativního editoru. Samotný nový obrázek neopravuje dříve zjištěné mobilní rozložení krému ani skrytý mobilní řádek U F1RST.

Podklady: `brand/RULES.md`, pracovní vizuální identita, dosavadní skutečné PNG a jejich obrazové motivy, původní mapování a aktuální Git. Původní přílohy se smíšenými vahami byly skutečně otevřené; nová kresba je autorská vektorová adaptace týchž typů symbolů, ne tvrzení o pixelově totožném masteru. Původní produktové účinkové popisky zůstaly beze změny a nejsou touto grafickou opravou právně schválené.

Model GPT-6.1-sol, SVG/Python/CairoSVG/Pillow/Chromium. Bez placeného generování obrázků — 0 za generovací služby. Cena agentového/modelového provozu zde není vyčíslena. Původní lidský manuál a `brand/RULES.md` zůstaly beze změny.
