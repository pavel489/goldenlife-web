# Piktogramy Longevity / Hormonal — PNG pro kompatibilní nahrávání

## Pozorovaná chyba a oprava

Pavel dodal snímek s doslovnou chybou **„Failed to upload image: Nesprávný typ souboru“**. Snímek ukazuje odmítnutí při nahrávání, nikoli síťové nenalezení obrázku. Neobsahuje název odmítnutého souboru ani konkrétní upload endpoint, takže sám neprokazuje zákaz SVG v celém Shoptetu. Poslední předaná sada ale skutečně obsahovala SVG mastery a SVG data URI v HTML. Proto je připravená kompatibilnější PNG varianta místo tvrzení, že je problém jen v cache.

Oficiální dokumentace Shoptetu k fotogalerii uvádí JPG, PNG, GIF a WebP: https://podpora.shoptet.cz/fotogalerie/ . Je to doklad podporovaného PNG ve fotogalerii, nikoli přímý test konkrétního Pavlova dialogu.

- Všech **12** současných ikon Longevity a Hormonal je převedeno ze skutečných posledních SVG do **512 × 512 PNG s průhledným pozadím (RGBA)**. Nejde o přejmenování přípony. Tvar, červená barva i poslední oprava nože jsou zachované; původní SVG zůstávají jako editovatelné mastery.
- PNG jsou ve stejných Git složkách jako SVG, se stejným názvem a příponou `.png`: `assets/longevity-giftbox-line-icons/` a `assets/hormonal-giftbox-line-icons/`.
- V osmi existujících českých HTML (long/short v `shoptet/` a jejich protějšky v `web/`) jsou pouze odpovídající zdroje šesti ikon nahrazené skutečnými HTTPS PNG odkazy. Aktualizovaný zdroj nevyžaduje upload SVG ani zpracování SVG data URI editorem.
- PNG URL jsou připnuté k ověřenému commitu `4a61d15f2e6ecd18da28ebbd87e3170888f4ac04`, nikoli k proměnlivé větvi. Jde o veřejné zdroje GitHub Raw, ne o tvrzení, že byly nahrané do Shoptetu.
- Původně zkoušená jsDelivr cesta u jednoho PNG vrátila HTTP 403; v dodaném HTML se proto nepoužívá. Všech dvanáct skutečných GitHub Raw URL bylo samostatně načteno a ověřeno.

## Skutečná kontrola

- Dvanáct dekódovaných PNG: správná signatura/formát, rozměry 512 × 512, RGBA, alfa od 0 do 255, neprázdný objekt s rezervou uvnitř plátna. Kontaktní přehled všech dvanácti PNG byl vizuálně prohlédnut.
- Všech dvanáct veřejných HTTPS odpovědí: HTTP 200, MIME `image/png`, `Access-Control-Allow-Origin: *` a bajtová shoda s lokálním PNG. Žádná syntetická úspěšná odpověď se za síťový výsledek nevydává.
- Osm HTML na 1280 a 390 px v Chromium s přímými skutečnými požadavky na veřejné PNG. V každém bloku šest úspěšně dekódovaných PNG a skutečně namalované červené pixely ve všech šesti CSS maskách; žádné horizontální přetékání a žádná zachycená JS chyba.
- Reverzní porovnání všech osmi HTML: změnilo se pouze šest obrazových zdrojů (IMG a odpovídající maska), ostatní bajty včetně popisků, textů, SCRIPT, STYLE, produktových fotografií a odkazů zůstaly stejné.
- Detailní výsledky: `tests/boxy-png-piktogramy-kompatibilita.json`.

**Hranice ověření:** test je izolovaný náhled komponent s reálnými veřejnými obrázky, ne úspěšný upload přes konkrétní administrativní dialog. Neproběhla změna CMS ani živého Shoptetu; dřívější omezení přístupu k obchodu se neobcházelo. Nelze tvrdit, že byla nová verze v obchodě uložena, dokud se přesný cílový popis neuloží a nezávisle nenačte zpět.

## Zdroje, model a náklady

Aktuální Pavlův snímek, poslední ověřený Git `53edb2727ba9f676a9603c3e3c29eecacc7bbd30`, dvanáct SVG masterů, `brand/RULES.md`, aktuální oficiální výsledek vyhledání podpory Shoptet. Souběžná nová úprava Beauty byla při konfliktu větve identifikovaná a zůstala nedotčená.

Model `gpt-6.1-sol`. Převod skutečných SVG pomocí Chromium a kontrola PNG pomocí Pillow; bez placeného obrazového/video generování. Cenu jazykového běhu ani případného konektorového účtování rozhraní neposkytuje.
