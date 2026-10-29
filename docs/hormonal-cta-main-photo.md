# Woman Hormonal Balance — hlavní fotografie v CTA

CTA používá ověřenou hlavní fotografii produktu 644 z živé galerie Woman Hormonal Balance. Namísto starého cta.png má rovnou funkční veřejnou URL aktuálního packshotu jako výchozí obrázek. Stejná hlavní fotografie se po úspěšném načtení první galerie zrcadlí v hero i CTA; sleduje se také src/srcset, pozdní galerie a výměna elementu. Zrcadlení je omezené na productId 644; při chybě galerie zůstává výchozí fotografie. Není třeba nový upload obrázku.

Základní revize: def7acade0545f43c07bd8e3a467ae46a6c1373c. Původní texty, šest nových obrázků aktivních látek, ostatní sekce, cena a košík nebyly změněny.

Test: Chromium/Playwright, osm syntetických scénářů zrcadlení a chybových stavů, skutečná fotografie ve vizuálním náhledu na 390 a 1440 px, kontrola JS syntaxe. Testy jsou lokální, nikoli uložení do Shoptetu. Offline náhled používá Arial místo Metropolis a má neaktivní nákup.

Podklady: zdrojový HTML, veřejná hlavní galerie https://www.golden-life.cz/woman-hormonal-balance/, brand/RULES.md. Nástroje: GPT-6.1, Python, Chromium/Playwright; bez nové obrazové generace. Původní zdravotní tvrzení se tímto neschvalují. GitHub main a uložení do Shoptetu jsou samostatné kroky.
