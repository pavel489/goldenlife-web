# Collagen Beauty — oprava načítání piktogramů

## Zjištěný rozdíl a oprava

Aktuální vzdálený Git při převzetí: `185814751d5e96b74a38df27e6fa0d1207e09ab8`.

- Beauty měla ve všech čtyřech českých souborech vložené `data:image/svg+xml;base64,…` jak v IMG, tak v CSS masce.
- Funkční referenční UFIRST a Longevity v nynějším Gitu už používají běžné HTTPS odkazy na transparentní PNG. Jejich zavedené piny zůstaly nezměněné.
- Beauty byla převedena na stejný způsob načítání: šest transparentních PNG a neměnné HTTPS URL. Přepsané jsou obě hodnoty (IMG i maska), ne jen viditelný SRC.
- Asset pin: `03e99a5fe788392a05d58056244997ce135e8770`. Všechny PNG jsou dostupné pod `https://raw.githubusercontent.com/pavel489/goldenlife-web/03e99a5fe788392a05d58056244997ce135e8770/assets/beauty-giftbox-line-icons/`.
- PNG mají 256 × 256 px, čtyřnásobek největšího 64px zobrazení. Původní SVG mistry zůstaly zachované. Při exportu se drží původní kresby, alfa obrys a styl; barevná maska stále vykresluje stávající červenou RGB 217, 8, 23. Žádné nové zdravotní popisky nebo jiné úpravy textů.

Opravené soubory:

- `shoptet/beauty.html`
- `shoptet/beauty-kratky.html`
- `web/Golden Life Darkovy box Beauty/Golden_Life_Darkovy_box_cz.html`
- `web/Golden Life Darkovy box Beauty/maly/Golden-Life-Darkovy-box-maly-cz.html`

V každém souboru se mění pouze 12 zdrojových hodnot: šest IMG URL a šest odpovídajících masek. Obrácením těchto náhrad vzniknou bajtově přesně původní soubory. Texty, fotografie, struktura, SCRIPT a STYLE obsahy i funkce košíku zůstávají beze změny. UFIRST, Longevity ani sdílené CSS se neupravovaly.

## Skutečné ověření

- Všech šest skutečných veřejných PNG URL: HTTP 200, `image/png`, CORS `*`, shodné stažené bajty s vytvořenými soubory, skutečná signatura PNG, RGBA a průhlednost.
- Chromium, izolované bloky se skutečnými produkčními CSS a novými veřejnými URL. Obrázky nebyly v prohlížeči nahrazované lokální úspěšnou odpovědí: stáhly se skutečně z veřejného GitHubu.
- Šířky 1440 a 390 px: všech 12 IMG v dlouhém a krátkém bloku načtených, žádné přetékání, žádná zachycená JS chyba.
- 24 detailních snímků barevných masek (12 na každé šířce): ověřené skutečně vykreslené červené pixely. Nejde jen o kontrolu `naturalWidth`, která by mohla přehlédnout prázdnou CSS masku.
- Piktogramový blok i mobilní krátký popis byly vizuálně zkontrolované. Izolovaný náhled bez produktové fotografie používá jen testovací `height:auto`; toto pravidlo není vložené do žádného dodávaného HTML.
- Výsledky: `tests/beauty-piktogramy-png-results.json`.

## Stav a omezení

Jde o opravu a předání v Gitu, nikoli uložení do živé administrace. Přesná veřejná stránka Beauty při normálním pokusu stále vrátila HTTP 403 „Access temporarily blocked“. Další Shoptet požadavky byly zastavené. Nemohu tak prokázat přesnou historickou příčinu jeho sanitizace ani tvrdit, že už je oprava nasazená na produktu. Rozdíl ve zdrojích byl odstraněn podle fungujících referencí; skutečné veřejné PNG i jejich vykreslení byly nezávisle otestované. Není to tvrzení o plošném zákazu SVG v Shoptetu.

Vstupy: aktuální čtyři Beauty soubory, současné referenční UFIRST/Longevity, původní Beauty SVG mistry a stejné sdílené CSS jako v předchozím předání. Model gpt-6.1-sol; převod původních kreseb v Chromium/Pillow, bez placeného generování. Cena modelového a konektorového provozu není dostupná.
