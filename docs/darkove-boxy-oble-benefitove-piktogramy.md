# Dárkové boxy — původní oblé užitkové piktogramy e-shopu

## Rozsah a výsledek
Opravené boxy **Beauty, Hormonal, Longevity, Slim a UFIRST**, krátké i dlouhé české popisy v `web/` a jejich CMS protějšky v `shoptet/`: **20 HTML souborů**.

- Generické inventární SVG krabice, lahve, míchátka, počtu produktů apod. v benefitových řadách jsou nahrazené skutečnými původními PNG piktogramy používanými na produktových stránkách e-shopu. Oblost je v kresbě originální ikony, nikoli jen v CSS zaoblení kartičky.
- Každý box má pět vlastních benefitových párování podle produktů, které skutečně obsahuje. Stejných pět ikon a popisků je v krátkém i dlouhém popisu; nejde o nahrazení benefitů počtem kusů nebo vlastností balení.
- V krátkém rozbalovacím seznamu byly odstraněné i zbývající generické dekorativní SVG před názvy produktů. Samotné názvy a seznam pěti produktů zůstaly zachované.
- Nadpis nad velkým ikonovým blokem je změněný na „Přínosy produktů v boxu“. Pět dlouhých kartiček zůstává v původním layoutu; poslední zabere zbývající dvě buňky, aby nevznikl prázdný slot po šesté inventární ikoně.
- Původní PNG barvy a poměry stran jsou zachované. Nové obrázky nedostávají starý zlatý CSS filtr; UFIRST zůstává v původní tyrkysové. Neproběhla žádná generace ani nové kreslení ikon.

## Kde jsou soubory
CMS: `shoptet/beauty.html`, `hormonal.html`, `longevity.html`, `slim.html`, `ufirst.html` a všech pět odpovídajících `*-kratky.html`.

Plné/krátké dokumenty: odpovídající adresáře `web/Golden Life Darkovy box …/` a `maly/`.

Párování ikon, popisků a konkrétního zdrojového produktu: `config/giftbox-benefit-pictograms.json`. Sdílená odnož stylů: `assets/golden-life-darkove-boxy.css`, ověřená přes veřejnou CDN HTTP 200 a připnutá v každém dodaném HTML na revizi `94653b2435aaba506bcd3bc3c195a1141f030c39`. Kvůli této odnoži není potřeba ručně nahrávat další stylesheet do Shoptetu.

Dřívější zapojení `/user/documents/upload/css/ufirst-global.css` a `/user/documents/upload/css/ufirst-global.js` v UFIRST boxu zůstalo bajtově zachované. Tyto nahrané soubory se touto úpravou nemění.

## Co zůstalo zachované
Původní skripty, všechny neikonové obrázkové atributy, pět produktových detailových tlačítek u každého boxu, produkty a jejich URL, texty mimo explicitně měněné ikonové bloky/nadpis, balicí karta, galerie, CTA a import detailů. Každou změnu lze přesně obrátit na původní zdroj; neproběhla obecná HTML reserializace.

Bílá kartička jako layoutový prvek není zaměňovaná za styl samotné ikony. UI symbol balicí karty/fotogalerie není prezentovaný jako benefit a jeho funkční fotografie/fallback se v tomto zadání nepřepisují.

## Skutečné ověření
- Pět boxů × dlouhý/krátký popis × 320, 390 a 1280 px = **30 skutečných renderů Chromium**. V každé benefitové řadě pět načtených skutečných PNG, nula inventárních SVG, žádné horizontální přetékání dokumentu ani ikonových kartiček. Krátkých pět benefitů zůstává v jednom řádku.
- **18 různých skutečných původních PNG** bylo staženo, dekódováno, zkontrolováno na kontaktních přehledech a napárováno na zdrojový produkt. Napříč dvaceti dodanými HTML jde o 100 odkazů na benefitové obrázky.
- Po odstranění dekorativních SVG v krátkých popisech bylo u všech pěti boxů při 390 px skutečným pointerem otevřeno a zavřeno rozbalení pěti produktů; názvy zůstaly viditelné a bez přetékání.
- Bajtově ověřené původní skripty, neikonové produktové fotografie a data všech původních detailových tlačítek. CSS předchozí odnože zůstává přesným prefixem; nová pravidla jsou omezená na nové `data-gl-benefits="rounded"` bloky.
- Vizuálně zkontrolované dlouhé i krátké přehledy všech pěti variant a závěrečný náhled z reálných mobilních výřezů.

Vizuální testy používaly izolované HTML fixture se skutečnými vzdálenými styly a PNG. Neměněné shop bootstrapy byly ve fixture vynechané; tyto testy nepředstírají kompletní nativní Shoptet galerii, aktuální cenu ani checkout. Neikonové fotografie s případnými původními nefunkčními URL nebyly nahrazované smyšlenými produkty. První test přímo ve shop kontextu překročil pětisekundové čekání na decode; byl nahrazen úspěšnými běžnými navigacemi fixture a kontrolami skutečně načtených obrázků.

## Popisky účinků — samostatná otevřená kontrola
**Toto je grafická implementace / pracovní návrh, ne nové právní schválení účinků.** Popisky jsou převzaté z veřejných stránek skutečných komponent. Konkrétní zdravotní tvrzení a chybějící podklady jsou po jednotlivých popiscích v `docs/darkove-boxy-claims-piktogramy.md`, včetně formulací z vlastních produktových souborů tam, kde jsou doložené. Nepřenášelo se např. tvrzení o kvalitním spánku na Care Free pouze podle motivu obrázku.

Git publikace není uložení do administrace Shoptetu. Žádný živý produktový popis nebyl touto prací uložený; pro nasazení jsou připravené aktualizované celé CMS fragmenty.

## Zdroje, model a náklady
Aktuální autorizovaný Git snapshot; veřejné stránky skutečných komponent každého boxu; jejich původní piktogramy a viditelné popisky; `brand/RULES.md`, pracovní vizuální identita Golden Life, vlastní produktové soubory a manuál UFIRST. Veřejná UFIRST rešerše byla navíc porovnána s přímým načtením vybraných souborů a skutečným renderem.

Model GPT-6.1-sol; Python/HTMLParser/Pillow, Chromium a existující Composio GitHub spojení ověřené jako bot Goldie. Bez placené generace obrázků/videí; přesná cena modelu a konektoru není poskytovaná.
