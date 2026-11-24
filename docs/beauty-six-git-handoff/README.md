# Šest produktů — pokračování pouze na Gitu

Krátký a dlouhý popis všech šesti položek byl už na výchozím `main` připravený v nové produktové šabloně. Tato dávka ji nepřepisuje novým designem, ale dokončuje ověřené vady. **Bez uložení nebo publikace do Shoptetu.**

## Produkty a přesné soubory

### Beauty Longevity NAD+ — dóza (označení ze zadání) · ID 544
- [Dlouhý HTML](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20d%C3%B3za/Golden-Life-Beauty-Longevity-NAD-doza-cz.html)
- [Krátký HTML](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20d%C3%B3za/maly/Golden-Life-Beauty-Longevity-NAD-doza-maly-cz.html)

### Beauty Longevity NAD+ — sáček · ID 600
- [Dlouhý HTML](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20s%C3%A1%C4%8Dek/Golden-Life-Beauty-Longevity-NAD-sacek-cz.html)
- [Krátký HTML](../../web/Golden%20Life%20Beauty%20Longevity%20NAD%2B%20s%C3%A1%C4%8Dek/maly/Golden-Life-Beauty-Longevity-NAD-sacek-maly-cz.html)

### Anti-Age Longevity NAD+ — tablety (označení ze zadání) · ID 550
- [Dlouhý HTML](../../web/Golden%20Life%20Anti-Age%20Longevity%20NAD%2B/Golden-life-Anti-Age%20Longevity%20NAD%2B.html)
- [Krátký HTML](../../web/Golden%20Life%20Anti-Age%20Longevity%20NAD%2B/maly/Golden-life-Anti-Age%20Longevity%20NAD%2Bmaly.html)

### Beauty Body & Soul · ID 51
- [Dlouhý HTML](../../web/Golden%20Life%20Beauty%20Body%20Soul/Golden-Life-Beauty-Body-Soul-cz.html)
- [Krátký HTML](../../web/Golden%20Life%20Beauty%20Body%20Soul/maly/Golden-Life-Beauty-Body-Soul-maly-cz.html)

### Good Sleep & Night Burn · ID 57
- [Dlouhý HTML](../../web/Golden%20Life%20Good%20Sleep%20Night%20Burn/Golden-Life-Good-Sleep-Night-Burn-cz.html)
- [Krátký HTML](../../web/Golden%20Life%20Good%20Sleep%20Night%20Burn/maly/Golden-Life-Good-Sleep-Night-Burn-maly-cz.html)

### Miracle Drops · ID 99
- [Dlouhý HTML](../../web/Golden%20Life%20Miracle%20Drops/Golden-Life-Miracle-Drops-cz.html)
- [Krátký HTML](../../web/Golden%20Life%20Miracle%20Drops/maly/Golden-Life-Miracle-Drops-maly-cz.html)

## Dokončené opravy
- 544: zavírání informačních/ingredient dialogů klávesou Escape, Tab a návrat fokusu. Technický identifikátor odstraněn z ALT, ne z identity produktu.
- 550: pracovní/redakční upozornění přeneseno ze zákaznické stránky do `fixes-ledger.json`. Povinná bezpečnostní sdělení beze změny.
- 600: historická metadata měsíčního boxu a redakční doporučení kúry odstraněna ze samostatného sáčku, přesné původní bloky v ledgeru; technická archivní poznámka odstraněna z ALT.
- 57: druhý drobný mockup v CTA odstraněn; hlavní nativně hlídaná fotografie zůstává.
- 51 a 99: bez zdrojových změn, pouze nové ověření.
- Ingredientové modaly a tabulky složení zachovány; společné CSS/JS, košík, ceny, sklad a překlady beze změn.

## Aktuální identifikace obalu — nepřepisovat odhadem
**544:** zadání ho označuje jako „dóza“, ale aktuální hlavní galerie téhož nativního ID ukazuje **box a sáček**, na obalu 270 g / 30 sáčků. Vlastní aktuální galerie byla načtena a skutečná fotografie otevřena. Převzaté označení se nepovažuje za důkaz existence nové dózy. Existující autentické foto a zdrojové složení se nenahrazují vymyšleným obalem; URL a hash v `544-gallery-evidence.json`.
**550:** zadání říká „tablety“, zatímco připravený vlastní zdroj/dávkování uvádí „60 tobolek / 2 kapsle denně“. Neprovádí se svévolné sjednocení formy. Je to věc k potvrzení etikety před nasazením.

## Skutečné ověření
Výsledky finálního Chromium běhu v `qa-summary.json` jsou svázané s SHA-256 v `source-manifest.json`. Testované jsou přesné Git HTML/CSS i repository appearance JS; nejde o živý Shoptet ani fyzické Safari. Nákup nebyl odeslán. Video u 51 bylo zachováno, samotné přehrávání není certifikováno.

## Oddělená revize tvrzení
Původní účinkové texty zůstávají pracovními podklady; příprava designu není právní schválení.
- 544/600/550: NAD+, zdravé stárnutí, regenerace a případná ekvivalence tablet vyžadují vlastní podklady. Neutrální alternativa pro 550: „Anti-Age Longevity NAD+ je doplněk stravy. Složení a doporučená denní dávka jsou uvedeny v produktové tabulce.“ Pro 600: „Samostatný sáček nápoje Beauty Longevity NAD+.“
- Vlastní `beauty-longevity-nad-drink/info.md` (544) uvádí kandidátní znění: „Vitaminy skupiny B přispívají ke snížení míry únavy a vyčerpání, k normálnímu energetickému metabolismu a k normální funkci nervové soustavy.“ Nutno ověřit konkrétní živinu, dávku a podmínky; není to nový approval pro jiné NAD varianty.
- 51: zdrojový nadpis EFSA obsahuje i tvrzení o spalování a hormonech; automatický nadpis není doklad schválení. Neutrální návrh: „Beauty Body & Soul je nápoj; složení a příprava jsou uvedeny níže.“
- 57: „Spalování tuků“ a spánkové/chuťové sliby nejsou doložené schváleným ekvivalentem v jeho info.md. Neutrální návrh: „Good Sleep & Night Burn je doplněk stravy s rostlinnými extrakty.“
- 99 je kosmetické sérum k zevnímu použití, nikoli doplněk stravy. Léčebné věty o akné/ekzému/dermatitidě nejsou schválené touto přípravou. Neutrální návrh: „Pleťové sérum s kyselinou hyaluronovou a rostlinnými extrakty.“
- Podrobné dřívější věty a rozpory: [Longevity revize](../longevity-krok-4b-obsahove-vyhrady.md), [samostatné produkty](../samostatne-produkty-13/obsahove-vyhrady.md), [51/57/99 revize](../samostatne-produkty-6/content-review.cs.md).

## Podklady a zpracování
Výchozí Git main `0b0e2b29a5438d820f0ad95477eb89306d734c92`, brand/RULES.md, dostupné vlastní produktové info.md a dřívější oddělené revize. Model gpt-6.1-sol, Python/Playwright/Chromium, existující Composio GitHub. Bez placené obrazové generace; cena modelu/nástrojů není vyčíslená.