# Slim4C – konkrétní věty a rozpory z aktuálního Gitu

**Interní revize, ne právní schválení. Obsahové alternativy nebyly tiše aplikované do produktových souborů. Seznam zahrnuje i neúčinkové věty.**

## Zděděné konflikty

[
  {
    "sku": "168",
    "topic": "Jednotky biotinu",
    "evidence": "Aktuální Git: 294 mcg / 25 mcg. Starý archiv nesmí vrátit mg.",
    "decision": "Zachováno cell-for-cell aktuální Git."
  },
  {
    "sku": "168",
    "topic": "Přepočty tabulek",
    "evidence": {
      "B6_100g_mg": 823.5,
      "B6_expected_per8g_mg": 65.88,
      "B6_source_per8g_mg": 0.7,
      "fish_100g_g": 60.3,
      "fish_expected_per8g_g": 4.824,
      "fish_source_per8g_g": 5.13,
      "HCA_percent_if_source_60pct_of715mg": 429.0,
      "HCA_source_daily_mg": 500
    },
    "decision": "Číselné nesrovnalosti PŘEVZATY z aktuálního Gitu, NEOPRAVOVÁNY bez vlastníka složení."
  },
  {
    "sku": "168",
    "topic": "Odměrky a voda",
    "evidence": "Aktuální Git: 1 odměrka 8 g / 200–300 ml; starší brand info: 8 g / 2 odměrky / 300–400 ml nebo 1 l.",
    "decision": "Autoritou HTML je aktuální Git. Brand info nesmí přepsat novější šaržovou poznámku L245382/072028."
  },
  {
    "sku": "168",
    "topic": "Pevná nabídka a hodnocení",
    "evidence": "Zachované JSON-LD Offer 1350 CZK/InStock, aggregateRating 4.9/127; viditelné 1350 Kč, skladem/expedice 24 h; široký .price-final-holder bridge.",
    "decision": "Historický NEOVĚŘENÝ snapshot a bridge ponechány; nejedná se o aktuální obchodní důkaz. Žádný nový Cart POST ani cenová logika; před živým použitím vlastník ověří/rozhodne."
  },
  {
    "sku": "473",
    "topic": "Chrom",
    "evidence": "Aktuální Git používá mcg, starší info.md mg (0,55/1,11); archiv není autoritou jednotek.",
    "decision": "Přesné současné buňky a vysvětlení mcg zachovány; bez samovolné konverze."
  },
  {
    "sku": "476",
    "topic": "Chrom",
    "evidence": "Aktuální Git 25/50 mcg v tabulce i vysvětleních; starší info.md 25/50 mg.",
    "decision": "Zachovány aktuální mcg. Nikdy nevracet staré mg."
  },
  {
    "sku": "473",
    "topic": "Zdrojové claims",
    "evidence": "info.md říká žádné EFSA claims; současná plná copy a dialogy slibují blokaci kalorií, detox jater, cukr, cholesterol, imunitu atd.",
    "decision": "Neutichý přepis: vše ponecháno v interní pracovní kopii a rozpad na věty v ledgeru. Nutný samostatný obsahový/legal review."
  },
  {
    "sku": "476",
    "topic": "Zdrojové claims",
    "evidence": "Aktuální hlavní text/diallogy jsou věcné; původní long/short ikony stále slibují bleskové hubnutí, spalování, cukr a sytost.",
    "decision": "Žádné zaměnění úplných současných dialogů za starší prodejní copy. Ikonové claims zachovány pouze k výslovnému review."
  },
  {
    "sku": "476",
    "topic": "Originální artwork",
    "evidence": "GLPBLESKY.png zůstává v ID476-scoped theme; originální pixely v povoleném registru chybí.",
    "decision": "Nenačtený background není úspěšně ověřená malba; žádná vymyšlená náhrada, plné vizuální QA blokováno."
  },
  {
    "sku": "all",
    "topic": "Legal zdroje",
    "evidence": "Načteny brand/RULES.md a tři přesné product/<slug>/info.md. brand/NOT-ALLOWED.md v pracovním zdroji neexistuje.",
    "decision": "Žádné prohlášení o právním schválení; ledger je evidence/review, ne publikovatelný souhlas."
  }
]

## Povinné upozornění

ID168 v aktuálním produkčním fragmentu neobsahuje kompletní přesnou souvislou formulaci z brand/RULES.md. CSS práce ji tam tiše nedopisovala. V přiloženém označeném preview je doplněná mimo původní root. Před živým použitím vložit schválené povinné znění:
> Doplněk stravy. Není náhradou pestré a vyvážené stravy. Nepřekračujte doporučenou denní dávku. Uchovávejte mimo dosah dětí.

## Jednotlivé výskyty

### 168 · long · h1[1]:sentence1
> Slim Extreme Collagen
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim Extreme Collagen

### 168 · long · p[2]:sentence1
> Slim Extreme Collagen je výjimečný spalovač tuků , který spojuje inovativní sílu kolagenních peptidů s cíleným podporováním hubnutí a zpevňování svalů .
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[2]:sentence2
> Díky kombinaci patentovaných kolagenů Verisol® a Peptiplus® nabízí nejen pomoc při tvarování postavy, ale i zlepšení elasticity pokožky, kvality vlasů a zdraví kloubů .
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[2]:sentence3
> Je navržen tak, aby pomohl na cestě ke zdravějšímu tělu a přinášel výsledky i ve dnech bez fyzické aktivity.
Rizikový slib rychlosti/intenzity či výsledků bez aktivity; neověřeno, blokátor publikace. V rozporu s tónem bez extrémů, tvrzení není podložené produktovým claim approval.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h2[3]:sentence1
> Hlavní účinky Slim Extreme Collagen
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Hlavní účinky Slim Extreme Collagen

### 168 · long · p[4]:sentence1
> Podpora hubnutí
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[5]:sentence1
> Extrémní spalování tuků
Rizikový slib rychlosti/intenzity či výsledků bez aktivity; neověřeno, blokátor publikace. V rozporu s tónem bez extrémů, tvrzení není podložené produktovým claim approval.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[6]:sentence1
> Redukce celulitidy
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[7]:sentence1
> Redukce vrásek
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[8]:sentence1
> Pevné nehty
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[9]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 168 · long · h3[10]#gl-collagen-overview-title:sentence1
> Jak funguje Slim Extreme Collagen
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jak funguje Slim Extreme Collagen

### 168 · long · p[11]:sentence1
> Slim Extreme Collagen spojuje kolagenní peptidy Verisol® a Peptiplus® a kyselinu hyaluronovou s komplexem garcinie, zeleného čaje, synefrinu a enzymů.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim Extreme Collagen spojuje kolagenní peptidy Verisol® a Peptiplus® a kyselinu hyaluronovou s komplexem garcinie, zeleného čaje, synefrinu a enzymů.

### 168 · long · p[11]:sentence2
> Je navržený jako součást redukčního režimu a každodenní péče o krásu.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Je navržený jako součást redukčního režimu a každodenní péče o krásu.

### 168 · long · p[12]:sentence1
> Složení doplňují vitaminy a minerály.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Složení doplňují vitaminy a minerály.

### 168 · long · p[12]:sentence2
> Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.
Účinkové znění doložené v brand/product/extreme-slim-collagen/info.md, nikoli nové právní schválení. Jmenované živiny odpovídají zdrojové tabulce. Podmínky užití a aktuální EU registr nebyly v této CSS dávce ověřeny.
**Návrh, neaplikováno:** Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.

### 168 · long · h3[13]:sentence1
> Co vám přinese
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Co vám přinese

### 168 · long · div[14]:sentence1
> ✓ Kontrola hmotnosti
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · div[15]:sentence1
> ✓ Novotvorba kolagenu a udržení normálního stavu pokožky, vlasů, nehtů a pojivových tkání
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · div[16]:sentence1
> ✓ Regenerace organismu, zlepšení jeho funkcí
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · div[17]:sentence1
> ✓ Podpora hubnutí i bez cvičení
Rizikový slib rychlosti/intenzity či výsledků bez aktivity; neověřeno, blokátor publikace. V rozporu s tónem bez extrémů, tvrzení není podložené produktovým claim approval.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · div[18]:sentence1
> ✓ Efektivní spalování tuků
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · div[19]:sentence1
> ✓ Redukce celulitidy
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · div[20]:sentence1
> ✓ Pevné nehty
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · div[21]:sentence1
> ✓ Snížení únavy
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Obecné tvrzení bez nosné živiny; k revizi konkrétní doloženou formulací B2/B3/B5.
**Návrh, neaplikováno:** Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.

### 168 · long · div[22]:sentence1
> ✓ Celková regenerace
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h3[23]:sentence1
> Aktivní látky
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Aktivní látky

### 168 · long · h4[24]:sentence1
> Garcinia cambogia
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Garcinia cambogia

### 168 · long · p[25]:sentence1
> Snižuje chuť k jídlu a podporuje spalování (HCA).
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[26]:sentence1
> Kyselina hyaluronová
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Kyselina hyaluronová

### 168 · long · p[27]:sentence1
> Hydratace, pružnost pleti a podpora kloubů.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[28]:sentence1
> Minerály a enzymy
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Minerály a enzymy

### 168 · long · p[29]:sentence1
> Enzymy bromelain, papain a zinek pro trávení.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[30]:sentence1
> B komplex
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** B komplex

### 168 · long · p[31]:sentence1
> Energie a správný metabolismus.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[32]:sentence1
> Vitamín C a E
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Vitamín C a E

### 168 · long · p[33]:sentence1
> Tvorba kolagenu a antioxidační ochrana.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[34]:sentence1
> Zelený čaj
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Zelený čaj

### 168 · long · p[35]:sentence1
> Antioxidanty a podpora spalování.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[36]:sentence1
> Garcinia cambogia
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Garcinia cambogia

### 168 · long · p[37]:sentence1
> Je tropická rostlina pocházející z Asie a po staletí se používá k navození pocitu sytosti.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[37]:sentence2
> Klíčovou účinnou látku v ní obsaženou je kyselina hydroxy-citronová (HCA), která zlepšuje trávení, snižuje chuť k jídlu a podporuje i spalování tuků.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[38]:sentence1
> Kyselina hyaluronová
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Kyselina hyaluronová

### 168 · long · p[39]:sentence1
> Látka, která se přirozeně nachází a vytváří v našem těle.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Látka, která se přirozeně nachází a vytváří v našem těle.

### 168 · long · p[39]:sentence2
> Její hlavní funkcí je zadržovat vodu, tedy hydratovat tkáně, a udržovat v nich dostatečnou vlhkost.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[39]:sentence3
> Pomáhá vyživovat pokožku, která je poté zdravější a pružnější.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[39]:sentence4
> Omezuje tak tvorbu vrásek a napomáhá regeneraci a celkovému omlazení pleti.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[39]:sentence5
> Účinně pomáhá při hojení ran a bolesti kloubů, zlepšuje jejich pohyblivost.
ROZPOR s brand/RULES: léčebné / disease-risk sdělení; blokátor publikace. Doplněk stravy není lék. Přesné historické znění zachováno jen v interní CSS pracovní kopii, nikoli schváleno.
**Návrh, neaplikováno:** Kyselina hyaluronová je jednou ze složek receptury.

### 168 · long · h4[40]:sentence1
> Minerály a enzymy
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Minerály a enzymy

### 168 · long · p[41]:sentence1
> Bromelain s papainem je unikátní kombinací dvou enzymů, které se nachází v ananasu a papáje.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Bromelain s papainem je unikátní kombinací dvou enzymů, které se nachází v ananasu a papáje.

### 168 · long · p[41]:sentence2
> Oba působí pozitivně na trávení a ovlivňují rozklad bílkovin, což ocení zejména sportovci.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[41]:sentence3
> Obsažený zinek se podílí na dělení buněk, přispívá k normálnímu metabolismu a chrání buňky před volnými radikály.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[42]:sentence1
> B komplex
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** B komplex

### 168 · long · p[43]:sentence1
> Vitamíny B jsou nezbytné pro správné fungování metabolismu a nervového systému.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[43]:sentence2
> Zároveň umožňují vstřebávání látek a napomáhají jejich lepšímu využití.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[43]:sentence3
> Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání, vitaminy B2 a B3 udržují normální stav pokožky a sliznic.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[44]:sentence1
> Vitamín C a E
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Vitamín C a E

### 168 · long · p[45]:sentence1
> Vitamin C je důležitý pro tvorbu nového kolagenu, má pozitivní vliv na imunitní systém, přispívá k ochraně a tvorbě nových buněk, lepší regeneraci a snížení únavy.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[45]:sentence2
> Vitamin E je velmi silný antioxidant, má význam pro řadu oxidoredukčních pochodů a stabilizuje některé hormony.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h4[46]:sentence1
> Zelený čaj
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Zelený čaj

### 168 · long · p[47]:sentence1
> Obsahuje antioxidanty a pomáhá bojovat proti volným radikálům.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[47]:sentence2
> Podporuje zdravý zrak a snižuje riziko srdečních onemocnění.
ROZPOR s brand/RULES: léčebné / disease-risk sdělení; blokátor publikace. Doplněk stravy není lék. Přesné historické znění zachováno jen v interní CSS pracovní kopii, nikoli schváleno.
**Návrh, neaplikováno:** Obsahuje extrakt ze zeleného čaje.

### 168 · long · p[47]:sentence3
> Účinky zeleného čaje umožňují spalování kalorií, podílí se na tvorbě dopaminu a podporují produktivitu.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h3[48]:sentence1
> Objednejte nyní
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Objednejte nyní

### 168 · long · p[49]:sentence1
> Balení: 240 g prášku · Stačí na: cca 30 dávek
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Balení: 240 g prášku · Stačí na: cca 30 dávek

### 168 · long · p[50]:sentence1
> ✓ Skladem – expedice do 24 hodin
Provozní snapshot NEOVĚŘEN; není živá dostupnost. Bez nových shop requestů po 403; původní snapshot zachován, necertifikovat.
**Návrh, neaplikováno:** Aktuální dostupnost ověř u nativního nákupního bloku.

### 168 · long · h3[51]:sentence1
> Jak užívat
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jak užívat

### 168 · long · p[52]:sentence1
> Bez lepku
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Bez lepku

### 168 · long · p[53]:sentence1
> Bez GMO
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Bez GMO

### 168 · long · p[54]:sentence1
> Bez přídatných látek
ROZPOR / nutné ověření věcného tvrzení. Ve složení jsou sladidla, aroma a regulátor kyselosti; „bez přídatných látek“ vyžaduje opravu pod vlastníkem obsahu.
**Návrh, neaplikováno:** Složení a výživové hodnoty jsou uvedeny v tabulkách.

### 168 · long · p[55]:sentence1
> Bez laktózy
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Bez laktózy

### 168 · long · p[56]:sentence1
> Bez cukru
ROZPOR / nutné ověření věcného tvrzení. Zdrojová tabulka má 2,9 g cukrů/100 g a 0,23 g/8 g; nepřenášet tvrzení jako ověřené.
**Návrh, neaplikováno:** Složení a výživové hodnoty jsou uvedeny v tabulkách.

### 168 · long · h4[57]:sentence1
> Návod k použití:
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Návod k použití:

### 168 · long · p[58]:sentence1
> 1 odměrku (8 g) rozmíchejte v 200–300 ml vody.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 1 odměrku (8 g) rozmíchejte v 200–300 ml vody.

### 168 · long · p[58]:sentence2
> Užívejte 1× denně, nejlépe ráno nebo dopoledne.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Užívejte 1× denně, nejlépe ráno nebo dopoledne.

### 168 · long · p[58]:sentence3
> Doporučená denní dávka se nesmí překročit.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doporučená denní dávka se nesmí překročit.

### 168 · long · h4[59]:sentence1
> Skladování:
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Skladování:

### 168 · long · p[60]:sentence1
> Skladujte na suchém a chladném místě, mimo dosah přímého slunečního záření, při teplotě do 25 °C.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Skladujte na suchém a chladném místě, mimo dosah přímého slunečního záření, při teplotě do 25 °C.

### 168 · long · p[60]:sentence2
> Uchovávejte mimo dosah dětí.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Uchovávejte mimo dosah dětí.

### 168 · long · h4[61]:sentence1
> Upozornění:
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Upozornění:

### 168 · long · p[62]:sentence1
> Nevhodné pro těhotné a kojící ženy a osoby s alergií na některou ze složek.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nevhodné pro těhotné a kojící ženy a osoby s alergií na některou ze složek.

### 168 · long · p[62]:sentence2
> Nenahrazuje pestrou a vyváženou stravu.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · p[62]:sentence3
> Přípravek obsahuje kofein – nedoporučuje se užívat odpoledne a večer.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Přípravek obsahuje kofein – nedoporučuje se užívat odpoledne a večer.

### 168 · long · h3[63]:sentence1
> Složení
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Složení

### 168 · long · p[64]:sentence1
> hovězí kolagenní peptidy (3500 daltonů), rybí kolagenní peptidy (2000 daltonů), aroma, regulátor kyselosti: kyselina citronová, garcinia cambogia extrakt (60% kyseliny hydroxycitronové), bromelain, ananasový prášek lyofilizovaný, mango extrakt (10:1), zelený čaj extrakt (50 % polyfenolů), kyselina askorbová, papain, pantothenát vápenatý, bisglycinát zinečnatý, sladidla: sukralóza, steviosid, dl-alfa-tokoferol-acetát, citrus aurantium extrakt (95% synefrinu), hyaluronát sodný, niacinamid, pyridoxin hydrochlorid, riboflavin, thiamin, kyselina listová, kyanokobalamin, biotin, chlorid chromitý.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** hovězí kolagenní peptidy (3500 daltonů), rybí kolagenní peptidy (2000 daltonů), aroma, regulátor kyselosti: kyselina citronová, garcinia cambogia extrakt (60% kyseliny hydroxycitronové), bromelain, ananasový prášek lyofilizovaný, mango extrakt (10:1), zelený čaj extrakt (50 % polyfenolů), kyselina askorbová, papain, pantothenát vápenatý, bisglycinát zinečnatý, sladidla: sukralóza, steviosid, dl-alfa-tokoferol-acetát, citrus aurantium extrakt (95% synefrinu), hyaluronát sodný, niacinamid, pyridoxin hydrochlorid, riboflavin, thiamin, kyselina listová, kyanokobalamin, biotin, chlorid chromitý.

### 168 · long · h3[65]:sentence1
> Souhrnný obsah
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Souhrnný obsah

### 168 · long · p[66]:sentence1
> *Referenční hodnota příjmu není stanovena.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** *Referenční hodnota příjmu není stanovena.

### 168 · long · p[66]:sentence2
> Slazeno sukralózou (nízkokalorické sladidlo).
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · h3[67]:sentence1
> Nutriční hodnoty na 100 g/8 g (denní dávka)
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nutriční hodnoty na 100 g/8 g (denní dávka)

### 168 · long · p[68]:sentence1
> U šarže L245382, EXP/LOT: 072028, je doporučená denní dávka 8 g (jedna odměrka).
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** U šarže L245382, EXP/LOT: 072028, je doporučená denní dávka 8 g (jedna odměrka).

### 168 · long · img-alt[0]:sentence1
> Žena drží dózu Slim Extreme Collagen
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Žena drží dózu Slim Extreme Collagen

### 168 · long · img-alt[1]:sentence1
> Garcinia cambogia
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Garcinia cambogia

### 168 · long · img-alt[2]:sentence1
> Kyselina hyaluronová
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Kyselina hyaluronová

### 168 · long · img-alt[3]:sentence1
> Minerály a enzymy
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Minerály a enzymy

### 168 · long · img-alt[4]:sentence1
> B komplex
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** B komplex

### 168 · long · img-alt[5]:sentence1
> Vitamín C a E
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Vitamín C a E

### 168 · long · img-alt[6]:sentence1
> Zelený čaj
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Zelený čaj

### 168 · long · img-alt[7]:sentence1
> Slim Extreme Collagen
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim Extreme Collagen

### 168 · long · img-alt[8]:sentence1
> Bez lepku
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Bez lepku

### 168 · long · img-alt[9]:sentence1
> Bez GMO
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Bez GMO

### 168 · long · img-alt[10]:sentence1
> Bez přídatných látek
ROZPOR / nutné ověření věcného tvrzení. Ve složení jsou sladidla, aroma a regulátor kyselosti; „bez přídatných látek“ vyžaduje opravu pod vlastníkem obsahu.
**Návrh, neaplikováno:** Složení a výživové hodnoty jsou uvedeny v tabulkách.

### 168 · long · img-alt[11]:sentence1
> Bez laktózy
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Bez laktózy

### 168 · long · img-alt[12]:sentence1
> Bez cukru
ROZPOR / nutné ověření věcného tvrzení. Zdrojová tabulka má 2,9 g cukrů/100 g a 0,23 g/8 g; nepřenášet tvrzení jako ověřené.
**Návrh, neaplikováno:** Složení a výživové hodnoty jsou uvedeny v tabulkách.

### 168 · long · meta-description:sentence1
> Slim Extreme Collagen je výjimečný spalovač tuků s patentovanými kolageny Verisol® a Peptiplus®.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · meta-description:sentence2
> Podpora hubnutí, redukce celulitidy, zpevnění pokožky a zdraví kloubů.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · meta-description:sentence3
> Vyrobeno v ČR.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR.

### 168 · long · meta-og:description:sentence1
> Výjimečný spalovač tuků s 6000 mg kolagenních peptidů.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · meta-og:description:sentence2
> Podpora hubnutí, zpevnění pokožky, redukce vrásek a celulitidy.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · meta-og:description:sentence3
> Vyrobeno v ČR.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR.

### 168 · long · JSON-LD.description:sentence1
> Výjimečný spalovač tuků s patentovanými kolageny Verisol® a Peptiplus®.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · long · JSON-LD.description:sentence2
> 6000 mg kolagenních peptidů pro podporu hubnutí, zpevnění pokožky, redukci vrásek a celulitidy.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · p[0]:sentence1
> Slim Extreme Collagen je silný a účinný spalovač tuků v podobě osvěžujícího nápoje na hubnutí, který zároveň využívá pozitivní účinky prvotřídních kolagenových peptidů na vaše tělo.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · p[0]:sentence2
> Vyvinutý pro každého, kdo hledá podporu na cestě za zdravějším tělem.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · p[0]:sentence3
> Objevte kombinaci špičkových, patentovaných kolagenových peptidů Verisol® a Peptiplus®, které spolu se silou ananasu na hubnutí, přírodních enzymů a dalších unikátních složek podporují rychlé a efektivní spalování tuků.
Rizikový slib rychlosti/intenzity či výsledků bez aktivity; neověřeno, blokátor publikace. V rozporu s tónem bez extrémů, tvrzení není podložené produktovým claim approval.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · div[1]:sentence1
> Podpora hubnutí
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · div[2]:sentence1
> Spalování tuků
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · div[3]:sentence1
> Redukce celulitidy
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · div[4]:sentence1
> Redukce vrásek
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · div[5]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 168 · short · img-alt[0]:sentence1
> Podpora hubnutí
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · img-alt[1]:sentence1
> Spalování tuků
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · img-alt[2]:sentence1
> Redukce celulitidy
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · img-alt[3]:sentence1
> Redukce vrásek
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · img-alt[4]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 168 · short · img-alt[5]:sentence1
> hmotnost
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rybí a hovězí kolagenní peptidy; složení a množství jsou uvedeny v tabulkách.

### 168 · short · img-alt[6]:sentence1
> dávkování
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** dávkování

### 168 · short · img-alt[7]:sentence1
> čas
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** čas

### 168 · short · img-alt[8]:sentence1
> Malá odměrka
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Malá odměrka

### 168 · short · img-alt[9]:sentence1
> Velká odměrka
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Velká odměrka

### 473 · long · h2[0]:sentence1
> CHITOSAN
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** CHITOSAN

### 473 · long · div[1]:sentence1
> Přírodní vláknina z korýšů
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Přírodní vláknina z korýšů

### 473 · long · p[2]:sentence1
> Chitosan, bílé fazole, červená řepa, jablečný ocet a chrom pro podporu trávení a kontrolu hmotnosti.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · div[3]:sentence1
> 60 tobolek v balení
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 60 tobolek v balení

### 473 · long · div[4]:sentence1
> 2 tobolky denně
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 2 tobolky denně

### 473 · long · div[5]:sentence1
> 30 denních dávek
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 30 denních dávek

### 473 · long · h4[6]:sentence1
> Chitosan
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chitosan

### 473 · long · p[7]:sentence1
> Chitosan je přírodní vláknina získaná z korýšů, která působí jako účinný „lapač tuků".
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chitosan je přírodní vláknina získaná z korýšů, která působí jako účinný „lapač tuků".

### 473 · long · p[7]:sentence2
> Váže na sebe tuky a cholesterolové látky v trávicím traktu a brání jejich vstřebávání.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[7]:sentence3
> Pomáhá tak snížít příjem kalorií, podpořit redukci váhy a udržet zdravou hladinu cholesterolu.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[7]:sentence4
> Díky své jedinečné schopnosti tvořit gel v žaludku navíc prodlužuje pocit sytosti a zlepšuje kontrolu nad jídelníčkem.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[8]:sentence1
> Obsahuje chitosan z korýšů.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů.

### 473 · long · p[8]:sentence2
> Osoby alergické na korýše by neměly produkt užívat.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Osoby alergické na korýše by neměly produkt užívat.

### 473 · long · h1[9]:sentence1
> Slim SOS Fat Burner
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim SOS Fat Burner

### 473 · long · p[10]:sentence1
> Slim SOS Fat Burner je ideálním pomocníkem při redukci váhy i v běžném životním stylu, kdy chcete podpořit trávení a metabolismus.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[10]:sentence2
> Kombinace chitosanu, extraktu z bílých fazolí, červené řepy, jablečného octa a chromu přináší komplexní podporu – od blokace tuků a sacharidů až po zvýšení vitality a udržení stabilní hladiny cukru v krvi.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[11]:sentence1
> Balení obsahuje 60 tobolek .
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Balení obsahuje 60 tobolek .

### 473 · long · p[11]:sentence2
> Při doporučené dávce 2 tobolky denně vystačí na 30 dní.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Při doporučené dávce 2 tobolky denně vystačí na 30 dní.

### 473 · long · p[11]:sentence3
> Doplněk stravy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doplněk stravy.

### 473 · long · h2[12]:sentence1
> Hlavní účinky Slim SOS Fat Burner
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Hlavní účinky Slim SOS Fat Burner

### 473 · long · p[13]:sentence1
> Blokuje tuky a sacharidy
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[14]:sentence1
> Podporuje trávení
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[15]:sentence1
> Dodává vitalitu a energii
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[16]:sentence1
> Podpora imunity
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[17]:sentence1
> Rovnováha metabolismu
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[18]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 473 · long · h4[19]:sentence1
> Jak funguje
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jak funguje

### 473 · long · p[20]:sentence1
> Slim SOS Fat Burner využívá synergii pěti účinných složek pro efektivní podporu hubnutí.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[20]:sentence2
> Základem je chitosan – přírodní vláknina, která váže tuky v trávicím traktu a brání jejich vstřebávání, čímž pomáhá snížit kalorický příjem.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[20]:sentence3
> Extrakt z bílých fazolí zpomaluje štěpení sacharidů a udržuje stabilní hladinu cukru v krvi, což omezuje prudké výkyvy energie a chuť na sladké.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[20]:sentence4
> Červená řepa bohatá na antioxidanty podporuje vitalitu, okysličení tkání a detoxikaci organismu.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[20]:sentence5
> Jablečný ocet přirozeně podporuje trávení, tvorbu trávicích šťáv a metabolismus tuků, zatímco chrom jako klíčový stopový prvek stabilizuje hladinu glukózy v krvi a snižuje chutě na sladké.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[20]:sentence6
> Díky této komplexní kombinaci přípravek působí na více úrovních – blokuje vstřebávání přebytečných kalorií, podporuje zdravé trávení, dodává energii a pomáhá udržet kontrolu nad tělesnou hmotností bez drastických diet.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[21]:sentence1
> Účinky
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Účinky

### 473 · long · p[22]:sentence1
> Blokace části tuků a sacharidů ze stravy.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[22]:sentence2
> Přirozená kontrola tělesné hmotnosti.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[22]:sentence3
> Lehčí trávení po tučnějším jídle.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[22]:sentence4
> Podpora vitality, energie a imunity.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[22]:sentence5
> Vyrovnaný metabolismus cukrů a tuků.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[22]:sentence6
> Stabilní hladina glukózy v krvi a snížené chutě na sladké.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[22]:sentence7
> Podpora detoxikace jater a okysličení tkání.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h3[23]:sentence1
> Co vám přinese
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Co vám přinese

### 473 · long · div[24]:sentence1
> ✓ Blokace části tuků a sacharidů ze stravy.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · div[25]:sentence1
> ✓ Přirozená kontrola tělesné hmotnosti.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · div[26]:sentence1
> ✓ Lehčí trávení po tučnějším jídle.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · div[27]:sentence1
> ✓ Podpora vitality, energie a imunity.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · div[28]:sentence1
> ✓ Vyrovnaný metabolismus cukrů a tuků.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · div[29]:sentence1
> ✓ Stabilní hladina glukózy v krvi a snížené chutě na sladké.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · div[30]:sentence1
> ✓ Podpora detoxikace jater a okysličení tkání.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h3[31]:sentence1
> Aktivní látky
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Aktivní látky

### 473 · long · h4[32]:sentence1
> Chitosan
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chitosan

### 473 · long · p[33]:sentence1
> Přírodní „lapač tuků" pro nižší kalorický příjem.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[34]:sentence1
> Extrakt z bílých fazolí
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Extrakt z bílých fazolí

### 473 · long · p[35]:sentence1
> Zpomaluje štěpení sacharidů a snižuje chuť na sladké.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[36]:sentence1
> Červená řepa
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Červená řepa

### 473 · long · p[37]:sentence1
> Antioxidanty pro vitalitu, okysličení a detoxikaci.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[38]:sentence1
> Jablečný ocet
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jablečný ocet

### 473 · long · p[39]:sentence1
> Podpora trávení, metabolismu tuků a lehkosti po jídle.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[40]:sentence1
> Chrom
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chrom

### 473 · long · p[41]:sentence1
> Stabilizuje hladinu cukru a snižuje chutě na sladké.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[42]:sentence1
> Chitosan
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chitosan

### 473 · long · p[43]:sentence1
> Chitosan je přírodní vláknina získaná z korýšů, která působí jako účinný „lapač tuků".
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chitosan je přírodní vláknina získaná z korýšů, která působí jako účinný „lapač tuků".

### 473 · long · p[43]:sentence2
> Váže na sebe tuky a cholesterolové látky v trávicím traktu a brání jejich vstřebávání.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[43]:sentence3
> Pomáhá tak snížít příjem kalorií, podpořit redukci váhy a udržet zdravou hladinu cholesterolu.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[43]:sentence4
> Díky své jedinečné schopnosti tvořit gel v žaludku navíc prodlužuje pocit sytosti a zlepšuje kontrolu nad jídelníčkem.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[44]:sentence1
> Extrakt z bílých fazolí
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Extrakt z bílých fazolí

### 473 · long · p[45]:sentence1
> Zpomaluje štěpení a vstřebávání sacharidů, čímž omezuje prudké výkyvy hladiny cukru v krvi.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[45]:sentence2
> Udržuje delší pocit sytosti, snižuje chuť na sladké a podporuje kontrolu hmotnosti.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[45]:sentence3
> Obsahuje přírodní blokátory alfa-amylázy, enzymu odpovědného za rozklad škrobů.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[46]:sentence1
> Červená řepa
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Červená řepa

### 473 · long · p[47]:sentence1
> Bohatá na antioxidanty, vitaminy a minerály.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[47]:sentence2
> Podporuje vitalitu, okysličení tkání i sportovní výkon.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[47]:sentence3
> Díky betainu chrání buňky před oxidačním stresem a podporuje detoxikaci jater.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[47]:sentence4
> Obsahuje také dusičnany, které přirozeně zlepšují prokrvení a výkonnost.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[48]:sentence1
> Jablečný ocet
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jablečný ocet

### 473 · long · p[49]:sentence1
> Podporuje trávení, tvorbu trávicích šťáv a metabolismus tuků.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[49]:sentence2
> Pomáhá udržet pocit lehkosti po jídle a přirozenou kontrolu chuti k jídlu.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[49]:sentence3
> Kyselina octová v něm obsažená zlepšuje vstřebávání živin a podporuje zdravou střevní mikroflóru.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · h4[50]:sentence1
> Chrom
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chrom

### 473 · long · p[51]:sentence1
> Stopový prvek důležitý pro metabolismus cukrů, tuků a bílkovin.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[51]:sentence2
> Stabilizuje hladinu cukru v krvi, snižuje chutě na sladké a podporuje energii během dne.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[51]:sentence3
> Chrom je nezbytný pro správnou funkci inzulínu a pomáhá udržet stabilní tělesnou hmotnost.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[52]:sentence1
> Ilustrační obrázky aktivních látek.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační obrázky aktivních látek.

### 473 · long · h3[53]:sentence1
> Časté otázky
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Časté otázky

### 473 · long · h4[54]:sentence1
> Na jak dlouho balení vystačí?
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Na jak dlouho balení vystačí?

### 473 · long · p[55]:sentence1
> Balení obsahuje 60 tobolek.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Balení obsahuje 60 tobolek.

### 473 · long · p[55]:sentence2
> Při doporučeném užívání 2 tobolek denně vystačí na 30 dní.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Při doporučeném užívání 2 tobolek denně vystačí na 30 dní.

### 473 · long · h4[56]:sentence1
> Obsahuje produkt alergen?
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Obsahuje produkt alergen?

### 473 · long · p[57]:sentence1
> Ano, chitosan pochází z korýšů.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ano, chitosan pochází z korýšů.

### 473 · long · p[57]:sentence2
> Osoby alergické na korýše by neměly produkt užívat.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Osoby alergické na korýše by neměly produkt užívat.

### 473 · long · h4[58]:sentence1
> V jaké jednotce je uveden chrom?
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** V jaké jednotce je uveden chrom?

### 473 · long · p[59]:sentence1
> Množství chromu je uvedené v mcg (mikrogramech), nikoli v mg.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Množství chromu je uvedené v mcg (mikrogramech), nikoli v mg.

### 473 · long · p[59]:sentence2
> Přesné hodnoty najdeš v tabulce složení.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Přesné hodnoty najdeš v tabulce složení.

### 473 · long · h3[60]:sentence1
> Slim SOS Fat Burner
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim SOS Fat Burner

### 473 · long · p[61]:sentence1
> 47,6 g · 60 tobolek · 30 denních dávek
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 47,6 g · 60 tobolek · 30 denních dávek

### 473 · long · p[62]:sentence1
> Denní dávka: 2 tobolky
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Denní dávka: 2 tobolky

### 473 · long · p[63]:sentence1
> Aktuální cenu a dostupnost najdeš u nákupu nahoře.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Aktuální cenu a dostupnost najdeš u nákupu nahoře.

### 473 · long · h3[64]:sentence1
> Jak užívat
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jak užívat

### 473 · long · h4[65]:sentence1
> Návod k použití:
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Návod k použití:

### 473 · long · p[66]:sentence1
> 2 tobolky denně, zapít dostatečným množstvím vody, ideálně před nebo po tučnějším jídle.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 2 tobolky denně, zapít dostatečným množstvím vody, ideálně před nebo po tučnějším jídle.

### 473 · long · h4[67]:sentence1
> Skladování:
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Skladování:

### 473 · long · p[68]:sentence1
> Skladujte v suchu, při teplotě do 25 °C, mimo dosah dětí a slunečního záření.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Skladujte v suchu, při teplotě do 25 °C, mimo dosah dětí a slunečního záření.

### 473 · long · p[68]:sentence2
> Po každém použití obal dobře uzavřete.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Po každém použití obal dobře uzavřete.

### 473 · long · h4[69]:sentence1
> Upozornění:
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Upozornění:

### 473 · long · p[70]:sentence1
> Doplněk stravy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doplněk stravy.

### 473 · long · p[70]:sentence2
> Nenahrazuje pestrou stravu.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nenahrazuje pestrou stravu.

### 473 · long · p[70]:sentence3
> Nevhodné pro děti, těhotné a kojící ženy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nevhodné pro děti, těhotné a kojící ženy.

### 473 · long · p[70]:sentence4
> Uchovávejte mimo dosah dětí.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Uchovávejte mimo dosah dětí.

### 473 · long · p[70]:sentence5
> Nepřekračujte doporučenou denní dávku.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nepřekračujte doporučenou denní dávku.

### 473 · long · p[70]:sentence6
> Osoby alergické na korýše by neměly produkt užívat (obsahuje chitosan).
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Osoby alergické na korýše by neměly produkt užívat (obsahuje chitosan).

### 473 · long · p[71]:sentence1
> Doplněk stravy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doplněk stravy.

### 473 · long · p[71]:sentence2
> Není náhradou pestré a vyvážené stravy.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · long · p[71]:sentence3
> Nepřekračujte doporučenou denní dávku.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nepřekračujte doporučenou denní dávku.

### 473 · long · p[71]:sentence4
> Uchovávejte mimo dosah dětí.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Uchovávejte mimo dosah dětí.

### 473 · long · h3[72]:sentence1
> Složení
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Složení

### 473 · long · p[73]:sentence1
> Obsahuje: Chitosan, extrakt z bílých fazolí, červená řepa, jablečný ocet a chrom.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Obsahuje: Chitosan, extrakt z bílých fazolí, červená řepa, jablečný ocet a chrom.

### 473 · long · p[74]:sentence1
> Alergen: korýši (chitosan).
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Alergen: korýši (chitosan).

### 473 · long · h3[75]:sentence1
> Množství látek v denní dávce
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Množství látek v denní dávce

### 473 · long · p[76]:sentence1
> *Referenční hodnota příjmu není stanovena.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** *Referenční hodnota příjmu není stanovena.

### 473 · long · img-alt[0]:sentence1
> Slim SOS Fat Burner – aktuální fotografie dózy
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim SOS Fat Burner – aktuální fotografie dózy

### 473 · long · img-alt[1]:sentence1
> Chitosan
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chitosan

### 473 · long · img-alt[2]:sentence1
> Extrakt z bílých fazolí
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Extrakt z bílých fazolí

### 473 · long · img-alt[3]:sentence1
> Červená řepa
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Červená řepa

### 473 · long · img-alt[4]:sentence1
> Jablečný ocet
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jablečný ocet

### 473 · long · img-alt[5]:sentence1
> Chrom
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chrom

### 473 · long · img-alt[6]:sentence1
> Chitosan
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chitosan

### 473 · long · img-alt[7]:sentence1
> Extrakt z bílých fazolí
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Extrakt z bílých fazolí

### 473 · long · img-alt[8]:sentence1
> Červená řepa
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Červená řepa

### 473 · long · img-alt[9]:sentence1
> Jablečný ocet
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jablečný ocet

### 473 · long · img-alt[10]:sentence1
> Chrom
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chrom

### 473 · long · img-alt[11]:sentence1
> Slim SOS Fat Burner
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim SOS Fat Burner

### 473 · short · p[0]:sentence1
> Slim SOS Fat Burner je první pomoc pro trávení i štíhlou linii.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · p[0]:sentence2
> Spojuje účinky přírodního chitosanu , extraktu z bílých fazolí, červené řepy a jablečného octa s chromem pro vyrovnanou hladinu cukru v krvi.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · p[0]:sentence3
> Praktické tobolky, které pomohou, když jídelníček zrovna není úplně vyvážený.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · div[1]:sentence1
> Blokuje tuky a sacharidy
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · div[2]:sentence1
> Podporuje trávení
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · div[3]:sentence1
> Kontrola chuti k jídlu
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · div[4]:sentence1
> Vitalita a energie
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · div[5]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 473 · short · p[6]:sentence1
> Obsahuje chitosan z korýšů.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů.

### 473 · short · p[6]:sentence2
> Nevhodné pro osoby alergické na korýše, děti, těhotné a kojící ženy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nevhodné pro osoby alergické na korýše, děti, těhotné a kojící ženy.

### 473 · short · img-alt[0]:sentence1
> Blokuje tuky a sacharidy
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · img-alt[1]:sentence1
> Podporuje trávení
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · img-alt[2]:sentence1
> Kontrola chuti k jídlu
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · img-alt[3]:sentence1
> Dodává vitalitu a energii
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje chitosan z korýšů, extrakt z bílých fazolí, červenou řepu, jablečný ocet a chrom.

### 473 · short · img-alt[4]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 476 · long · h2[0]:sentence1
> BERBERIN
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** BERBERIN

### 476 · long · div[1]:sentence1
> Berberin HCl v rostlinném extraktu
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Berberin HCl v rostlinném extraktu

### 476 · long · p[2]:sentence1
> Rostlinné extrakty, L-leucin, chrom a Nextida® GLP-1.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Rostlinné extrakty, L-leucin, chrom a Nextida® GLP-1.

### 476 · long · p[2]:sentence2
> Složení v konkrétních množstvích.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Složení v konkrétních množstvích.

### 476 · long · div[3]:sentence1
> 60 tobolek v balení
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 60 tobolek v balení

### 476 · long · div[4]:sentence1
> 2 tobolky denně
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 2 tobolky denně

### 476 · long · div[5]:sentence1
> 30 denních dávek
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 30 denních dávek

### 476 · long · h4[6]:sentence1
> Berberin HCl a další složky
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Berberin HCl a další složky

### 476 · long · p[7]:sentence1
> Denní dávka obsahuje 500 mg extraktu z Berberis aristata, z toho 485 mg berberinu HCl.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Denní dávka obsahuje 500 mg extraktu z Berberis aristata, z toho 485 mg berberinu HCl.

### 476 · long · p[7]:sentence2
> Dále obsahuje extrakt z morušovníku, skořici, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Dále obsahuje extrakt z morušovníku, skořici, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · p[8]:sentence1
> Chrom je v tabulce uveden v mikrogramech: 25 mcg v jedné tobolce a 50 mcg ve dvou tobolkách.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chrom je v tabulce uveden v mikrogramech: 25 mcg v jedné tobolce a 50 mcg ve dvou tobolkách.

### 476 · long · p[8]:sentence2
> Doplněk stravy, nikoli lék.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doplněk stravy, nikoli lék.

### 476 · long · h1[9]:sentence1
> Slim GLP-1 Activator s Berberinem
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim GLP-1 Activator s Berberinem

### 476 · long · p[10]:sentence1
> Každodenní rutina s přehledně uvedeným složením.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Každodenní rutina s přehledně uvedeným složením.

### 476 · long · p[10]:sentence2
> Slim GLP-1 Activator kombinuje extrakt z Berberis aristata standardizovaný na berberin HCl, bílý morušovník, cejlonskou skořici, L-leucin, chrom a Nextida® GLP-1.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim GLP-1 Activator kombinuje extrakt z Berberis aristata standardizovaný na berberin HCl, bílý morušovník, cejlonskou skořici, L-leucin, chrom a Nextida® GLP-1.

### 476 · long · p[11]:sentence1
> 60 tobolek · 2 tobolky denně · 30 denních dávek.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 60 tobolek · 2 tobolky denně · 30 denních dávek.

### 476 · long · p[11]:sentence2
> Doporučené užívání je s jídlem a dostatkem vody, ideálně s obědem.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doporučené užívání je s jídlem a dostatkem vody, ideálně s obědem.

### 476 · long · p[11]:sentence3
> Doplněk stravy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doplněk stravy.

### 476 · long · h2[12]:sentence1
> Slim GLP-1 Activator zblízka
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim GLP-1 Activator zblízka

### 476 · long · p[13]:sentence1
> Snižuje chuť do jídla
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · p[14]:sentence1
> Stabilizuje hladinu cukru
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · p[15]:sentence1
> Podporuje spalování tuků
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · p[16]:sentence1
> Zvyšuje pocit sytosti
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · p[17]:sentence1
> Bleskové hubnutí
Rizikový slib rychlosti/intenzity či výsledků bez aktivity; neověřeno, blokátor publikace. V rozporu s tónem bez extrémů, tvrzení není podložené produktovým claim approval.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · p[18]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 476 · long · h4[19]:sentence1
> Jak funguje
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jak funguje

### 476 · long · p[20]:sentence1
> Denní dávku tvoří dvě tobolky.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Denní dávku tvoří dvě tobolky.

### 476 · long · p[20]:sentence2
> Množství jednotlivých složek je přehledně rozepsané v tabulce pro jednu i dvě tobolky.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Množství jednotlivých složek je přehledně rozepsané v tabulce pro jednu i dvě tobolky.

### 476 · long · p[20]:sentence3
> Označení produktu není tvrzením, že nahrazuje léčbu nebo léky.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Označení produktu není tvrzením, že nahrazuje léčbu nebo léky.

### 476 · long · h4[21]:sentence1
> Fakta, ne fráze
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Fakta, ne fráze

### 476 · long · p[22]:sentence1
> 500 mg rostlinného extraktu zahrnuje 485 mg berberinu HCl.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 500 mg rostlinného extraktu zahrnuje 485 mg berberinu HCl.

### 476 · long · p[22]:sentence2
> Nejde o dvě dávky, které se sčítají.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nejde o dvě dávky, které se sčítají.

### 476 · long · p[22]:sentence3
> Recepturu doplňuje 500 mg extraktu z morušovníku a 200 mg Nextida® GLP-1 v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Recepturu doplňuje 500 mg extraktu z morušovníku a 200 mg Nextida® GLP-1 v denní dávce.

### 476 · long · h3[23]:sentence1
> Přehledně v denní dávce
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Přehledně v denní dávce

### 476 · long · div[24]:sentence1
> ✓ 485 mg berberinu HCl v 500 mg extraktu
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** ✓ 485 mg berberinu HCl v 500 mg extraktu

### 476 · long · div[25]:sentence1
> ✓ 500 mg extraktu z morušovníku
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** ✓ 500 mg extraktu z morušovníku

### 476 · long · div[26]:sentence1
> ✓ 50 mg skořice
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** ✓ 50 mg skořice

### 476 · long · div[27]:sentence1
> ✓ 40 mg L-leucinu
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** ✓ 40 mg L-leucinu

### 476 · long · div[28]:sentence1
> ✓ 50 mcg chromu
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** ✓ 50 mcg chromu

### 476 · long · div[29]:sentence1
> ✓ 200 mg Nextida® GLP-1
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** ✓ 200 mg Nextida® GLP-1

### 476 · long · h4[30]:sentence1
> Nextida®
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nextida®

### 476 · long · p[31]:sentence1
> Nextida® GLP-1 je složka na bázi kolagenních peptidů.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nextida® GLP-1 je složka na bázi kolagenních peptidů.

### 476 · long · p[31]:sentence2
> Jedna tobolka obsahuje 100 mg, doporučená denní dávka dvou tobolek 200 mg.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jedna tobolka obsahuje 100 mg, doporučená denní dávka dvou tobolek 200 mg.

### 476 · long · p[31]:sentence3
> Přesná množství všech složek jsou uvedená v tabulce níže.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Přesná množství všech složek jsou uvedená v tabulce níže.

### 476 · long · h3[32]:sentence1
> Aktivní látky
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Aktivní látky

### 476 · long · h4[33]:sentence1
> Berberin HCl
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Berberin HCl

### 476 · long · p[34]:sentence1
> 485 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 485 mg v denní dávce.

### 476 · long · h4[35]:sentence1
> Extrakt z bílého morušovníku
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Extrakt z bílého morušovníku

### 476 · long · p[36]:sentence1
> 500 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 500 mg v denní dávce.

### 476 · long · h4[37]:sentence1
> Cejlonská skořice
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Cejlonská skořice

### 476 · long · p[38]:sentence1
> 50 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 50 mg v denní dávce.

### 476 · long · h4[39]:sentence1
> L-Leucin
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** L-Leucin

### 476 · long · p[40]:sentence1
> 40 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 40 mg v denní dávce.

### 476 · long · h4[41]:sentence1
> Chrom
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chrom

### 476 · long · p[42]:sentence1
> 50 mcg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 50 mcg v denní dávce.

### 476 · long · h4[43]:sentence1
> Nextida® GLP-1
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nextida® GLP-1

### 476 · long · p[44]:sentence1
> 200 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 200 mg v denní dávce.

### 476 · long · h4[45]:sentence1
> Berberin HCl
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Berberin HCl

### 476 · long · p[46]:sentence1
> 485 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 485 mg v denní dávce.

### 476 · long · p[47]:sentence1
> Toto množství je součástí 500 mg extraktu z Berberis aristata standardizovaného na 97 % berberinu HCl.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Toto množství je součástí 500 mg extraktu z Berberis aristata standardizovaného na 97 % berberinu HCl.

### 476 · long · p[47]:sentence2
> Jedna tobolka obsahuje 250 mg extraktu, z toho 242,5 mg berberinu HCl.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jedna tobolka obsahuje 250 mg extraktu, z toho 242,5 mg berberinu HCl.

### 476 · long · p[48]:sentence1
> Fotografie je ilustrační; není dokladem původu suroviny.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Fotografie je ilustrační; není dokladem původu suroviny.

### 476 · long · h4[49]:sentence1
> Extrakt z bílého morušovníku
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Extrakt z bílého morušovníku

### 476 · long · p[50]:sentence1
> 500 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 500 mg v denní dávce.

### 476 · long · p[51]:sentence1
> Extrakt z bílého morušovníku (Morus alba) doplňuje rostlinné složky receptury.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Extrakt z bílého morušovníku (Morus alba) doplňuje rostlinné složky receptury.

### 476 · long · p[51]:sentence2
> Jedna tobolka obsahuje 250 mg.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jedna tobolka obsahuje 250 mg.

### 476 · long · p[52]:sentence1
> Fotografie je ilustrační; není dokladem původu suroviny.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Fotografie je ilustrační; není dokladem původu suroviny.

### 476 · long · h4[53]:sentence1
> Cejlonská skořice
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Cejlonská skořice

### 476 · long · p[54]:sentence1
> 50 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 50 mg v denní dávce.

### 476 · long · p[55]:sentence1
> Cejlonská skořice (Cinnamomum verum) je uvedená ve složení.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Cejlonská skořice (Cinnamomum verum) je uvedená ve složení.

### 476 · long · p[55]:sentence2
> Jedna tobolka obsahuje 25 mg.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jedna tobolka obsahuje 25 mg.

### 476 · long · p[56]:sentence1
> Fotografie je ilustrační; není dokladem původu suroviny.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Fotografie je ilustrační; není dokladem původu suroviny.

### 476 · long · h4[57]:sentence1
> L-Leucin
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** L-Leucin

### 476 · long · p[58]:sentence1
> 40 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 40 mg v denní dávce.

### 476 · long · p[59]:sentence1
> L-leucin je aminokyselina uvedená v receptuře.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** L-leucin je aminokyselina uvedená v receptuře.

### 476 · long · p[59]:sentence2
> Jedna tobolka obsahuje 20 mg.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jedna tobolka obsahuje 20 mg.

### 476 · long · p[60]:sentence1
> Fotografie je ilustrační; není dokladem původu suroviny.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Fotografie je ilustrační; není dokladem původu suroviny.

### 476 · long · h4[61]:sentence1
> Chrom
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Chrom

### 476 · long · p[62]:sentence1
> 50 mcg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 50 mcg v denní dávce.

### 476 · long · p[63]:sentence1
> Množství chromu je uvedené v mikrogramech (mcg), nikoli v miligramech: 25 mcg v jedné tobolce a 50 mcg ve dvou tobolkách.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Množství chromu je uvedené v mikrogramech (mcg), nikoli v miligramech: 25 mcg v jedné tobolce a 50 mcg ve dvou tobolkách.

### 476 · long · p[64]:sentence1
> Fotografie je ilustrační; není dokladem původu suroviny.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Fotografie je ilustrační; není dokladem původu suroviny.

### 476 · long · h4[65]:sentence1
> Nextida® GLP-1
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nextida® GLP-1

### 476 · long · p[66]:sentence1
> 200 mg v denní dávce.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 200 mg v denní dávce.

### 476 · long · p[67]:sentence1
> Nextida® GLP-1 je ve zdrojovém složení uvedená jako kolagenní peptidy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nextida® GLP-1 je ve zdrojovém složení uvedená jako kolagenní peptidy.

### 476 · long · p[67]:sentence2
> Jedna tobolka obsahuje 100 mg.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jedna tobolka obsahuje 100 mg.

### 476 · long · p[68]:sentence1
> Fotografie je ilustrační; není dokladem původu suroviny.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Fotografie je ilustrační; není dokladem původu suroviny.

### 476 · long · h3[69]:sentence1
> Časté otázky
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Časté otázky

### 476 · long · h4[70]:sentence1
> Jak produkt užívat?
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jak produkt užívat?

### 476 · long · p[71]:sentence1
> Dvě tobolky denně, nejlépe s jídlem a dostatkem vody, ideálně s obědem.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Dvě tobolky denně, nejlépe s jídlem a dostatkem vody, ideálně s obědem.

### 476 · long · p[71]:sentence2
> Doporučenou denní dávku nepřekračuj.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doporučenou denní dávku nepřekračuj.

### 476 · long · h4[72]:sentence1
> Na jak dlouho balení vystačí?
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Na jak dlouho balení vystačí?

### 476 · long · p[73]:sentence1
> Balení obsahuje 60 tobolek.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Balení obsahuje 60 tobolek.

### 476 · long · p[73]:sentence2
> Při doporučeném dávkování 2 tobolek denně vystačí na 30 dní.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Při doporučeném dávkování 2 tobolek denně vystačí na 30 dní.

### 476 · long · h4[74]:sentence1
> Jaké jednotky má chrom?
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jaké jednotky má chrom?

### 476 · long · p[75]:sentence1
> 25 mcg v jedné tobolce a 50 mcg ve dvou tobolkách.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 25 mcg v jedné tobolce a 50 mcg ve dvou tobolkách.

### 476 · long · p[75]:sentence2
> Jednotka mcg znamená mikrogram.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jednotka mcg znamená mikrogram.

### 476 · long · h3[76]:sentence1
> Slim GLP-1 Activator s Berberinem
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim GLP-1 Activator s Berberinem

### 476 · long · p[77]:sentence1
> 47,4 g · 60 tobolek · 30 denních dávek
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** 47,4 g · 60 tobolek · 30 denních dávek

### 476 · long · p[78]:sentence1
> Denní dávka: 2 tobolky s jídlem a vodou
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Denní dávka: 2 tobolky s jídlem a vodou

### 476 · long · p[79]:sentence1
> Aktuální cenu a dostupnost najdeš u nákupu nahoře.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Aktuální cenu a dostupnost najdeš u nákupu nahoře.

### 476 · long · h3[80]:sentence1
> Jak užívat
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jak užívat

### 476 · long · h4[81]:sentence1
> Návod k použití
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Návod k použití

### 476 · long · p[82]:sentence1
> Doporučená denní dávka: 2 tobolky denně, nejlépe s jídlem a dostatkem vody (ideálně s obědem).
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doporučená denní dávka: 2 tobolky denně, nejlépe s jídlem a dostatkem vody (ideálně s obědem).

### 476 · long · p[82]:sentence2
> Doporučená denní dávka nesmí být překročena.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doporučená denní dávka nesmí být překročena.

### 476 · long · h4[83]:sentence1
> Skladování
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Skladování

### 476 · long · p[84]:sentence1
> Skladujte na suchém místě do 25 °C.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Skladujte na suchém místě do 25 °C.

### 476 · long · p[84]:sentence2
> Uchovávejte mimo dosah dětí a přímého slunečního záření.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Uchovávejte mimo dosah dětí a přímého slunečního záření.

### 476 · long · h4[85]:sentence1
> Upozornění
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Upozornění

### 476 · long · p[86]:sentence1
> Nevhodné pro těhotné a kojící ženy a při alergii na některou z použitých surovin.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nevhodné pro těhotné a kojící ženy a při alergii na některou z použitých surovin.

### 476 · long · p[86]:sentence2
> Nenahradí vyváženou stravu.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · p[87]:sentence1
> Doplněk stravy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doplněk stravy.

### 476 · long · p[87]:sentence2
> Není náhradou pestré a vyvážené stravy.
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · p[87]:sentence3
> Nepřekračujte doporučenou denní dávku.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nepřekračujte doporučenou denní dávku.

### 476 · long · p[87]:sentence4
> Uchovávejte mimo dosah dětí.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Uchovávejte mimo dosah dětí.

### 476 · long · h3[88]:sentence1
> Složení
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Složení

### 476 · long · p[89]:sentence1
> Extrakt z indického dřínu ( Berberis aristata ) standardizovaný na berberin HCl 97 %, extrakt z bílého morušovníku ( Morus alba ), cejlonská skořice ( Cinnamomum verum ), L-leucin, chrom, Nextida® GLP-1 (kolagenní peptidy), protispékavá látka: stearan hořečnatý, tobolka: hydroxypropylmethylcelulóza.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Extrakt z indického dřínu ( Berberis aristata ) standardizovaný na berberin HCl 97 %, extrakt z bílého morušovníku ( Morus alba ), cejlonská skořice ( Cinnamomum verum ), L-leucin, chrom, Nextida® GLP-1 (kolagenní peptidy), protispékavá látka: stearan hořečnatý, tobolka: hydroxypropylmethylcelulóza.

### 476 · long · h3[90]:sentence1
> Složení a výživové hodnoty
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Složení a výživové hodnoty

### 476 · long · p[91]:sentence1
> *RHP – Referenční hodnota příjmu není stanovena.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** *RHP – Referenční hodnota příjmu není stanovena.

### 476 · long · img-alt[0]:sentence1
> Slim GLP-1 Activator s Berberinem – skutečný produkt
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim GLP-1 Activator s Berberinem – skutečný produkt

### 476 · long · img-alt[1]:sentence1
> Snižuje chuť do jídla
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · img-alt[2]:sentence1
> Stabilizuje hladinu cukru
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · img-alt[3]:sentence1
> Podporuje spalování tuků
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · img-alt[4]:sentence1
> Zvyšuje pocit sytosti
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · img-alt[5]:sentence1
> Bleskové hubnutí
Rizikový slib rychlosti/intenzity či výsledků bez aktivity; neověřeno, blokátor publikace. V rozporu s tónem bez extrémů, tvrzení není podložené produktovým claim approval.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · long · img-alt[6]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 476 · long · img-alt[7]:sentence1
> Jak funguje
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Jak funguje

### 476 · long · img-alt[8]:sentence1
> Fakta, ne fráze
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Fakta, ne fráze

### 476 · long · img-alt[9]:sentence1
> Ilustrační fotografie: Berberin HCl
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Berberin HCl

### 476 · long · img-alt[10]:sentence1
> Ilustrační fotografie: Extrakt z bílého morušovníku
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Extrakt z bílého morušovníku

### 476 · long · img-alt[11]:sentence1
> Ilustrační fotografie: Cejlonská skořice
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Cejlonská skořice

### 476 · long · img-alt[12]:sentence1
> Ilustrační fotografie: L-Leucin
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: L-Leucin

### 476 · long · img-alt[13]:sentence1
> Ilustrační fotografie: Chrom
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Chrom

### 476 · long · img-alt[14]:sentence1
> Ilustrační fotografie: Nextida® GLP-1
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Nextida® GLP-1

### 476 · long · img-alt[15]:sentence1
> Ilustrační fotografie: Berberin HCl
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Berberin HCl

### 476 · long · img-alt[16]:sentence1
> Ilustrační fotografie: Extrakt z bílého morušovníku
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Extrakt z bílého morušovníku

### 476 · long · img-alt[17]:sentence1
> Ilustrační fotografie: Cejlonská skořice
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Cejlonská skořice

### 476 · long · img-alt[18]:sentence1
> Ilustrační fotografie: L-Leucin
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: L-Leucin

### 476 · long · img-alt[19]:sentence1
> Ilustrační fotografie: Chrom
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Chrom

### 476 · long · img-alt[20]:sentence1
> Ilustrační fotografie: Nextida® GLP-1
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Ilustrační fotografie: Nextida® GLP-1

### 476 · long · img-alt[21]:sentence1
> Slim GLP-1 Activator s Berberinem
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim GLP-1 Activator s Berberinem

### 476 · short · p[0]:sentence1
> Slim GLP-1 Activator s Berberinem – rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1 v tobolkách.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Slim GLP-1 Activator s Berberinem – rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1 v tobolkách.

### 476 · short · p[0]:sentence2
> Doplněk stravy.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Doplněk stravy.

### 476 · short · div[1]:sentence1
> Snižuje chuť do jídla
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · div[2]:sentence1
> Stabilizuje hladinu cukru
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · div[3]:sentence1
> Podporuje spalování tuků
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · div[4]:sentence1
> Zvyšuje pocit sytosti
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · div[5]:sentence1
> Bleskové hubnutí
Rizikový slib rychlosti/intenzity či výsledků bez aktivity; neověřeno, blokátor publikace. V rozporu s tónem bez extrémů, tvrzení není podložené produktovým claim approval.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · div[6]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR

### 476 · short · p[7]:sentence1
> Nevhodné pro těhotné a kojící ženy a při alergii na některou z použitých surovin.
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Přeneseno beze změny z aktuálního Gitu; původ není právním schválením.
**Návrh, neaplikováno:** Nevhodné pro těhotné a kojící ženy a při alergii na některou z použitých surovin.

### 476 · short · img-alt[0]:sentence1
> Snižuje chuť do jídla
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · img-alt[1]:sentence1
> Stabilizuje hladinu cukru
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · img-alt[2]:sentence1
> Podporuje spalování tuků
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · img-alt[3]:sentence1
> Zvyšuje pocit sytosti
Účinkové tvrzení NEOVĚŘENO; nepublikovat bez claim review. Pro konkrétní složku, dávku a přesné znění zde chybí ověřené právní schválení. Historický web/Git ani nadpis EFSA v info.md nejsou souhlas.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · img-alt[4]:sentence1
> Bleskové hubnutí
Rizikový slib rychlosti/intenzity či výsledků bez aktivity; neověřeno, blokátor publikace. V rozporu s tónem bez extrémů, tvrzení není podložené produktovým claim approval.
**Návrh, neaplikováno:** Obsahuje rostlinné extrakty, L-leucin, chrom a kolagenní peptidy Nextida® GLP-1.

### 476 · short · img-alt[5]:sentence1
> Vyrobeno v ČR
Není účinkovým tvrzením; identifikace, složení, množství nebo obsluha. Původ tvrzený zdrojem; výrobní doklad nebyl v designové dávce ověřen.
**Návrh, neaplikováno:** Vyrobeno v ČR