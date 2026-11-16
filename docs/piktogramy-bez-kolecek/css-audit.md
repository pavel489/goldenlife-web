# CSS audit piktogramů — bez dekorativních koleček

Rozsah: produkční CSS a HTML v autorizovaném repozitáři. Historické `docs/`, `nahledy/` a testovací snapshoty nejsou upraveny. Obrazové URL ani artwork nebyly tímto dílčím úkolem změněny. Bez commitu, publikace a externích zápisů.

## Upravená pravidla (přesné selektory)

- `user/documents/upload/css/golden-life-barvy-double-slim-sos-burner.css`
  - `#special-popis[data-gl-theme="double-slim-sos-burner"] .gl-ingredient-cta-arrow`
  - `border-radius: 50%` → `0`, `background: rgba(var(--gl-color-primary-rgb),.10)` → `transparent`
- `user/documents/upload/css/golden-life-barvy-slim-sos-fat-burner.css`
  - `#special-popis[data-gl-theme="slim-sos-fat-burner"] .gl-ingredient-cta-arrow`
  - `border-radius: 50%` → `0`, `background: rgba(var(--gl-color-primary-rgb),.10)` → `transparent`
- `user/documents/upload/css/golden-life-produkt.css`
  - `:where([data-gl-layout="beauty-longevity"],[data-gl-layout="glp1-woman-balance"],[data-gl-layout="glp1-woman-balance-sacek"],[data-gl-layout="woman-hormonal-balance"]) .nad-ico`
  - `border-radius: 50%` → `0`, `border: 1.5px solid var(--gl-color-primary)` → `0`, `background: var(--gl-tone-nad-ico-background-1)` → `transparent`
- `user/documents/upload/css/golden-life-produkt.css`
  - `#nad-popis:where([data-gl-layout="anti-age-longevity"]) .nad-ico`
  - `border-radius: 50%` → `0`, `border: 1.5px solid var(--gl-color-primary)` → `0`, `background: var(--gl-tone-nad-ico-background-1)` → `transparent`
- `user/documents/upload/css/golden-life-produkt.css`
  - `:where(#special-popis:not([data-gl-product]),#nad-popis:not([data-gl-product])) .nad-ico`
  - `border-radius: 50%` → `0`, `border: 1.5px solid var(--gl-color-primary,#e3127e)` → `0`, `background: rgba(255,255,255,.55)` → `transparent`

Rozměry obalů 48/42 px (benefity) a 64 px (marketingová šipka), vlastní glyfy, barvy a typografie zůstaly zachovány. Šipka je samostatný dekorativní `span[aria-hidden]`, není klikacím tlačítkem; sousední nákupní odkaz zůstal netknutý. Sdílené CSS pokrývá existující jazykové kopie bez jazykově podmíněných výjimek.

## Rozšířený audit
- Zkontrolováno 186 produkčních HTML/CSS/JS souborů, 12 JS souborů, 20 CSS deklarací obsahujících URL a 110 inline SVG (9 různých kreseb).
- Inline SVG jsou dárek, list/květ, mixér, blesk, měsíc, lahev, váha, jablko a rovnováha. Nemají dekorativní vnější kruhový obrys; měsíc a oblouky skutečných symbolů se zachovávají. Žádný zásah do SVG artworku.
- CSS URL obsahují molekulu NAD, pozadí GLPBLESKY, fotografická CTA pozadí a data-SVG graf s kruhovými datovými body. Nejde o kruhové rámečky piktogramů; nic dalšího k obrazové výměně nebylo nalezeno. JS neobsahuje další samostatně definované marketingové piktogramy/rámující CSS.
- Zachovány funkční `.latky-plus`, `.latky-modal-close`, nákupní CTA, galerie/ovládání, pill štítky, zaoblení obdélníkových karet a skutečné kruhové části symbolů/grafu. Žádné globální odstranění border-radius.

## Ověření
- PASS: 56 lokálních Chromium případů; 12 skutečných produkčních stránek + 2 izolované anti-age/legacy fixture; viewporty 390 a 1440, light/dark.
- 88 kontrol cílových piktogramů: border-radius 0, průhledné pozadí, všechny border widths 0, stejné rozměry/glyf/barva/font-size.
- 656 porovnání funkčních ovládacích prvků před/po beze změny.
- Exact-scope assertion: všechny tři CSS soubory přesně odpovídají baseline + pěti schváleným náhradám; ostatní pravidla a deklarace totožné. `git diff --check` PASS.
- Spuštění: `css-audit/venv/bin/python css-audit/qa.py` (absolutní cesty ve skriptu). Výsledek `qa-results.json`; úplné nálezy `extra-audit.json`; změny `changes.json`.

## Limity
- Pouze lokální regresní test CSS; síťové zdroje kromě lokálně podaného CSS blokovány, externí obrázky a ikonový font se nenačítají. Nejde o vizuální kontrolu výsledného artworku, živého Shoptetu nebo publikace.
- První QA běh zachytil rozdílné mezistavy CSS transition při přepínání motivu; test byl stabilizován vypnutím animací/transition pouze v QA a opakován s PASS. Produkční animace se neměnily.
- Dva časové limity při přípravě inventáře byly způsobeny regexem přes obrovské HTML snapshoty; nic z nich nebylo zapsáno do repozitáře. Finální příprava používá jen skutečné style bloky a produkční soubory.
