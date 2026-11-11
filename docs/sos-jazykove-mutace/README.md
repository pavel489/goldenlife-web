# SOS / Double SOS · EN, DE, SK

## Hotové pracovní HTML návrhy
12 souborů: 2 produkty × 3 jazyky × dlouhý/krátký popis. Zdroj: aktuální česká dvojice z Git main `95f3ff9e3ce421f4918c241a7e43fe4a8541c4d7`. Česká HTML, společné CSS a barevné CSS zůstávají beze změny. Žádné uložení v živém Shoptetu.

Přeložena plná původní produktová vysvětlení a všechny složkové dialogy, ALT/ARIA, nákupní CTA, mobilní texty v JavaScriptu i nadpisový regexp. Dlouhé verze zachovávají pět skutečných aktivních složek + šestou nákupní CTA kartu, která se nevydává za další ingredienci. Krátké verze jsou vlastní krátké popisy, nikoli přejmenovaná dlouhá stránka.

- `web/Golden Life Slim SOS Fat Burner/Golden-Life-Slim-SOS-Fat-Burner-en.html`
- `web/Golden Life Slim SOS Fat Burner/maly/Golden-Life-Slim-SOS-Fat-Burner-maly-en.html`
- `web/Golden Life Slim SOS Fat Burner/Golden-Life-Slim-SOS-Fat-Burner-de.html`
- `web/Golden Life Slim SOS Fat Burner/maly/Golden-Life-Slim-SOS-Fat-Burner-maly-de.html`
- `web/Golden Life Slim SOS Fat Burner/Golden-Life-Slim-SOS-Fat-Burner-sk.html`
- `web/Golden Life Slim SOS Fat Burner/maly/Golden-Life-Slim-SOS-Fat-Burner-maly-sk.html`
- `web/Golden Life Double Slim SOS Burner/Golden-Life-Double-Slim-SOS-Burner-en.html`
- `web/Golden Life Double Slim SOS Burner/maly/Golden-Life-Double-Slim-SOS-Burner-maly-en.html`
- `web/Golden Life Double Slim SOS Burner/Golden-Life-Double-Slim-SOS-Burner-de.html`
- `web/Golden Life Double Slim SOS Burner/maly/Golden-Life-Double-Slim-SOS-Burner-maly-de.html`
- `web/Golden Life Double Slim SOS Burner/Golden-Life-Double-Slim-SOS-Burner-sk.html`
- `web/Golden Life Double Slim SOS Burner/maly/Golden-Life-Double-Slim-SOS-Burner-maly-sk.html`

## Co se neměnilo
- Technické ID, produktové identity 473/573, zdrojové obrázky, asset URL, CSS importy a jejich pořadí, nákupní kotvy a logika.
- Čísla a jednotky tabulek/dávkování, včetně původního `0,55 mcg / 1,11 mcg` chromu; RHP je pouze lokalizováno na NRV v EN/DE, nikoli přepočítáno.
- Double má dvě dózy, 120 tobolek a 60 denních dávek, ale denní dávka zůstává dvě tobolky.
- Do krátkých překladů bylo výslovně doplněno plné povinné upozornění o doplňku stravy; původní alergenní upozornění zachováno.

## Stav účinkových tvrzení – interní návrh, nikoli právní schválení
Jde o věrné překlady současných zdrojových textů. Historická účinková tvrzení nejsou tímto překladem schválena k veřejnému použití. Nebyla potichu nahrazena opakovaným dávkováním. Konkrétní zdrojové věty, překlady a neutrální alternativy jsou samostatně zaznamenány:
- [EN kontrola tvrzení](claims-review-en.md) + [JSON](claims-review-en.json)
- [DE kontrola tvrzení](claims-review-de.md) + [JSON](claims-review-de.json)
- [SK kontrola tvrzení](claims-review-sk.md) + [JSON](claims-review-sk.json)

Produktový soubor `brand/product/slim-sos-fat-burner/info.md` výslovně neobsahuje schválené EFSA znění; schválenou náhradu proto nelze tvrdit. Příklad: původní „Stabilizuje hladinu cukru a snižuje chutě na sladké.“ → neutrální alternativa „Chrom je jednou z pěti složek produktu.“ (redakční návrh, ne schválený zdravotní claim).

Otevřené zdrojové rozpory: historické produktové info má chrom v mg, aktuální Git v mcg; také zdrojový návod před/po tučnějším jídle se liší od historického před/do jídla. Obojí je ponecháno věrně aktuálnímu Gitu, ne opraveno odhadem. Před veřejným použitím ověřit skutečnou etiketu a legislativní znění. `brand/NOT-ALLOWED.md` na známé cestě chybí; tento dokument nevymýšlí jeho obsah.

## Ověření skutečným běhovým testem
- Rodičovská kontrola všech 12 finálních souborů: přesná reverze inventarizovaných editací vrací původní UTF-8 bajty; české zdroje odpovídají pinu v Gitu.
- Acorn: syntaktická kontrola všech výsledných skriptů a porovnání AST bez nelokalizačních změn logiky; technické URL/selektory chráněny.
- Chromium/Playwright: 6 produktově-jazykových dvojic × 4 viewporty (375, 768, 820, 1440 px) = 24 scénářů. Ověřeno všech pět dialogů, šest karet a CTA, mobilní rozbalování/sbalování a ARIA; žádné JS výjimky, dokumentové přetečení ani dokončené externí požadavky v offline náhledech.
- Doručovaný offline HTML prohlížeč: všech šest voleb a opakovaný návrat na první (7 přepnutí), všech pět dialogů a CTA uvnitř iframe, úzký 320px host krátkého popisu na desktopu, mobile–desktop návrat. Nákup je vypnutý; nic se neobjednávalo.
- Použito 14 skutečně stažených zdrojových fotografií/piktogramů. Náhledové fotografie jsou pouze necropovaně zmenšeny a vloženy jako WebP. Produkční URL beze změny.
- Samostatně ověřeno 6 skutečných cizojazyčných URL: HTTP 200, správný jazyk a nativní productId. EN single má autentickou adresu `https://www.golden-life.cz/en/sos-fat--burner/` se dvěma spojovníky; nebyla normalizována.
- Souhrnný strojový důkaz: [testy-a-pokryti.json](testy-a-pokryti.json).

Izolované náhledy nejsou test uloženého CMS ani skutečného nákupu. Používají Arial místo hostitelského písma a mají pouze náhledově vypnuté vzdálené přepínání galerie a pozadí. Produkční skripty tyto náhledové výjimky nedostaly. Náhledy nebyly použity k prohlášení, že byl aktualizován živý obchod.

## Podklady / model / cena
- Aktuální české produktové HTML a stejné sdílené a produktové CSS z uvedeného pinu; `brand/RULES.md`; produktový soubor; skutečné veřejné jazykové cíle a již používané obrazové assety.
- Překlad a integrace: GPT-6.1-sol, paralelní jazykové zpracování v Hermes. Kontroly: Python, HTML parser, Acorn a Chromium/Playwright. Žádná placená obrazová generace (0 za generování obrázků). Tokenové a konektorové náklady nejsou tímto běžícím prostředím vyčíslené.
- Interní editovatelné návrhy a dokumentace jsou předány do domluveného Git repozitáře. Publikace do Shoptetu není součástí této změny.
