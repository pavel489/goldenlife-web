# Aktivní látky SOS: pět karet + nákupní CTA

## Změna
- Slim SOS Fat Burner (473) a Double Slim SOS Burner (573): za pátou původní aktivní látku přidána jasně označená nákupní karta, nikoli šestá složka.
- Karta: „Pět složek. Jedna kombinace.“ + vlastní počet tobolek/dávek daného balení + „Přejít k nákupu“.
- Odkaz vede na stávající `#product-detail-form`; nic nevkládá do košíku a nemění nákupní logiku.
- Nad 768 px má pouze sekce `#latky` těchto dvou produktů tři sloupce, tedy dvě kompletní řady. Mobilní posouvání karet zůstává původní.
- Pět původních karet, fotografie, jejich dialogy, všechny tabulky a všechny původní skripty jsou beze změny. Zásah do HTML je jediná vratná vložka.
- Společný framework `golden-life-produkt.css`, krátké popisy a ostatní produkty beze změny.

## Soubory
- `web/Golden Life Slim SOS Fat Burner/Golden-Life-Slim-SOS-Fat-Burner-cz.html`
- `web/Golden Life Double Slim SOS Burner/Golden-Life-Double-Slim-SOS-Burner-cz.html`
- `user/documents/upload/css/golden-life-barvy-slim-sos-fat-burner.css`
- `user/documents/upload/css/golden-life-barvy-double-slim-sos-burner.css`

## Ověření
Chromium/Playwright, izolovaný výřez ze skutečných výsledných HTML/CSS: 2 produkty × 4 šířky (375, 768, 820, 1440 px) × světlý/tmavý okolní podklad = 16 scénářů. Ověřeno šest karet, pět dialogů, cíl CTA, 3 × 2 nad mobilním breakpointem a zachované mobilní posouvání; bez vodorovného přetečení dokumentu. Nová CTA nepřidává zdravotní tvrzení. Skutečných pět fotografií načteno z již použitých neměnných Git URL, nikoli generováno.

Jde o izolované lokální testy a Git předání, nikoli uložení v živém CMS či test nákupu. Náhled používá náhradní systémové písmo bez hostitelských fontů. Zachována existující barevná logika: jednotlivý SOS podporuje host-dark atribut, Double ve zdrojové šabloně zůstává světlý i na tmavém okolí; nový požadavek tuto dřívější vlastnost nepředělává.

## Podklady a náklady
Podklad: původní aktuální Git main `7d593e235ab40729e750a9f6cdb58f5994f7b3a5`, oba produktové HTML/CSS soubory, brand/RULES.md a produktový soubor Slim SOS Fat Burner. Úprava kódu a textu: GPT-6.1-sol; žádná placená obrazová generace. Inference/konektory dle tarifu nejsou v tomto běhu vyčíslené.

Původní účinkové formulace (např. „Stabilizuje hladinu cukru a snižuje chutě na sladké.“) byly při tomto úzce grafickém zásahu zachovány, nikoli právně schváleny. Produktový soubor neobsahuje schválenou EFSA formulaci; jako neutrální alternativu lze uvést „Chrom je jednou z pěti složek produktu.“. Nová CTA je bez účinkového tvrzení.

## Nasazení
Git předání samo nezmění e-shop. Při samostatně autorizovaném nasazení je potřeba převzít odpovídající produktové HTML i vlastní barevné CSS pro oba produkty. Tento běh nemění živý Shoptet.
