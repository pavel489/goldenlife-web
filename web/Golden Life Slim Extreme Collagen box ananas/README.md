# Slim Extreme Collagen box s příchutí ananasu – aktuální sdílené CSS

Pracovní návrh pro původní produkt **383**, 30 sáčků / 240 g. Nejde o dózu (168), mango variantu ani dárkový box s více produkty.

## Soubory
- Dlouhý popis: `Golden-Life-Slim-Extreme-Collagen-box-ananas-cz.html`.
- Krátký popis: `maly/Golden-Life-Slim-Extreme-Collagen-box-ananas-maly-cz.html`.
- Barevné CSS: `../../user/documents/upload/css/golden-life-barvy-slim-extreme-collagen-box-ananas.css`.
- Společné existující CSS: `/user/documents/upload/css/golden-life-produkt.css` – beze změny.
- Testy: `../../docs/slim-extreme-collagen-box-ananas-css-testy.json`.
- Obsahové výhrady: `../../docs/slim-extreme-collagen-box-ananas-obsahove-vyhrady.md`.

Každý popis obsahuje jediný malý STYLE blok a přesně dva importy: společné rozložení a vlastní barevné téma. Původní vložené rozvrhové CSS bylo odstraněno, nikoli překryto dalším importem. Využívá připravené rozložení Woman Hormonal Balance, ale samostatný identifikátor produktu a barevné téma. Barvy se nedeklarují na globálním :root. Zachován původní ananasový obrázek pozadí CTA s ověřenou absolutní URL. Třísloupcová tabulka používá existující opt-in marker.

## Zachování obsahu
Zdroj tvoří aktuální veřejný dlouhý a krátký popis konkrétního SKU. Veškeré vlastní textové uzly, tabulkové buňky, atributy obrázků a oba původní skripty jsou zachovány. Vynechán jen vnější nadpis Shoptet šablony „Detailní popis produktu“. Žádné převzetí složení ani textů z dózy. Obsahové nesrovnalosti nejsou vydávány za schválený copywriting.

## Skutečné testování
Chromium s reálnou kompletní stránkou e-shopu a dočasně přepsanou odpovědí pouze pro daný produkt; CSS pochází ze současného veřejného společného souboru a připraveného nového tématu. Šířky 320, 390, 768, 1024 a 1440 px, včetně návratu desktop–mobil. Bez vodorovného přetečení, bez textu oříznutého buňkami tabulky, všech 30 obrázků načteno. Zachováno všech 96 buněk; nativní a CTA cena se shodují. Samostatně dekódováno ananasové pozadí. Původní skripty se provedly při skutečném HTML načtení, ne dodatečnou simulací.

Globální skript e-shopu přesouvá úvodní `.maly-popis` na konec `.p-short-description`; celý odstavec zůstává viditelný. Náhled krátkého popisu proto zachycuje celý skutečný host, ne pouze obal s ikonami. Cookie, chat a plovoucí recenzní záložky skryty pouze v testovací záložce. Neproběhl nákup ani odeslání formuláře. Zobrazení mobilu i desktopu vizuálně zkontrolováno.

## Nasazení
Toto je Git dodávka, **ne uložení do živého Shoptetu**. Společný CSS soubor je na webu již dostupný a po normalizaci konců řádků odpovídá aktuálnímu Git souboru. Nové barevné CSS na veřejné cílové URL zatím chybí: nejdřív je nutné nahrát `golden-life-barvy-slim-extreme-collagen-box-ananas.css` do `/user/documents/upload/css/`, poté importovat oba celé popisy. Nestačí vložit pouze HTML bez nového tématu. Před živým nasazením vyřešit oddělené obsahové výhrady; po importu nezávisle zkontrolovat veřejný produkt.

## Zdroje a výroba
Veřejná stránka https://www.golden-life.cz/slim-extreme-collagen-box-s-prichuti-ananasu/, aktuální Git main, veřejný společný CSS, tokeny připraveného tématu stejné řady, `brand/RULES.md`, `brand/golden-life/visual-identity.md` a `brand/product/slim-extreme-collagen-box-s-prichuti-ananasu/info.md`. Soubor brand/NOT-ALLOWED.md nebyl dostupný; nepředstíráme jeho kontrolu. Model GPT-6.1-sol; Python/BeautifulSoup, Chromium/Playwright. Žádná placená obrazová generace; cena provozu jazykového modelu není dostupná.
