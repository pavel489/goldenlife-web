# Dárkové boxy — obnovený společný zdroj produktových detailů

## Aktuální řešení
Všech pět boxů opět načítá podrobný obsah z původních produktových stránek a rozbaluje jej **přímo pod kartami na stránce boxu**. Ručně vložené náhradní odstavce a hlavní odkazy „Otevřít samostatný detail“ byly odstraněné. Zákazník kvůli podrobnému popisu nemusí odcházet z boxu.

Podrobný text, složení, dávkování, upozornění a tabulky nejsou přepsané do pěti nezávislých kopií. Zůstávají na zdrojovém produktu. Jeho změna se načte při nové návštěvě stránky boxu a prvním otevření detailu. Již otevřená stránka používá během této návštěvy paměťovou cache; nejde o okamžité přepisování otevřených panelů. Nepoužívá se localStorage ani trvalá kopie popisu.

Zachované jsou dříve odsouhlasené mobilní karty, SVG ikony boxů, cesty fotografií, stručné texty karet, FAQ a bezpečné nákupní napojení. Krátké soubory v `maly/` se touto opravou nemění. Jejich původní redakční texty nejsou automaticky generované ze zdrojového produktu — centrální načítání se týká podrobného rozbaleného obsahu.

## Ovládání a načítání
- Každá karta má „Podrobně o produktu“. Otevře jeden společný panel s názvem zvolené položky; stránka boxu zůstane otevřená.
- Detail se stahuje až na kliknutí. Opakované otevření téhož produktu v této návštěvě nevyvolá další požadavek.
- Zavření je nahoře i dole, funguje i Escape. Fokus a pozice se vracejí k původní kartě.
- Při rychlém přepnutí se zobrazí poslední vybraný produkt, nikoli opožděná odpověď předchozího. Zavření během načítání panel znovu samo neotevře.
- Chyba načtení nabízí opakování přímo na místě, bez nuceného odchodu na jinou stránku. Neúspěšné načtení se neukládá do cache.
- Kontroluje se ID zdrojového produktu: přesměrování na jiné SKU se nesmí tiše zobrazit jako správný detail.

## Opravené zdroje
Seznam ověřených adres a identifikátorů je v `config/product-detail-sources.json`. Ananasový a mangový kolagen i míchátko byly potvrzené vlastníkem zadání:
- Ananas: `/slim-extreme-collagen-box-s-prichuti-ananasu/`, ID 383.
- Mango: `/slim-extreme-collagen-box-ananas-mango/`, ID 464.
- Míchátko: `/michatko/`, ID 653.
- Beauty & Longevity NAD+: skutečný drink `/beauty-longevity-nad-drink/`, ID 544, nikoli původní přesměrování na jednotlivý sáček.
- Ostatní zdroje navazují na ověřené odpovídající produktové stránky.

**Láhev Golden Life má správný zdroj `/lahev-golden-life/`, ID 597, ale tato stránka zatím uvádí „Popis produktu není dostupný“.** Panel proto pravdivě oznámí chybějící zdrojový popis. Nevytváří vlastní náhradní text. Jakmile vlastník doplní popis přímo u láhve, další načtení jej převezme do všech boxů bez změny kódu.

## Co se přebírá a co ne
- Převzat je editorový produktový popis `.basic-description`, případně odpovídající původní blok. Výběr nevyžaduje, aby každý produkt používal stejné `#special-popis`; funguje i původní Mango bez tohoto obalu.
- Zachované jsou produktové texty a tabulky. Faktuální informace o balení z `.cta-meta` se zachovají i po odebrání nákupního boxu.
- Nepřebírají se formuláře, skripty, vlastní košík jednotlivého produktu, ceny, nákupní výzvy, navigace e-shopu nebo související nákupní widgety.
- Přirozené rozbalovací bloky a zaškrtávací přepínače složení fungují. Zdrojové JS-only zobrazení účinných látek je v čtecím náhledu přístupné bez spuštění cizího skriptu. Carousely dostávají posuvný čtecí režim. Úmyslně skryté sekce ve zdroji se plošně neodkrývají.
- Texty a cíle vnitřních kotev zůstávají dostupné. Vedlejší referenční odkazy, které už patří přímo ke zdrojovému popisu, mohou zůstat odkazy; nejsou hlavní cestou k získání informací o produktu.

## Izolace a bezpečnost
Obsah se parsuje v inertním template, aby se při výběru fragmentu nestahovaly nesouvisející obrázky celé stránky. Sanitizace používá přiložený DOMPurify 3.4.16, zachovává licenční podmínky a odstraňuje aktivní cizí kód. Fragment a jeho vlastní lokální styly jsou v Shadow DOM, takže se nerozbíjí vzhled boxu ani šablony. Nenačítají se všechny globální stylesheety zdrojové stránky. Zdroje musí být na povolené doméně a odpovídat ověřenému productId.

Je-li v konkrétním zdrojovém popisu Material Symbols, font se vyžádá až při otevření takového detailu. Tento font není potřebný pro původní SVG ikony boxu. Fotografie detailu se přebírají ze zdroje; vzdálené obrázky níže jsou načítané líně.

`assets/giftbox-detail-loader.js` je kompletní funkční loader včetně sanitizéru. Stejný kód je vložený do jednotlivých dlouhých HTML pro samostatné použití v editoru Shoptetu; žádný nový externí hosting skriptu není potřeba. Při úpravě loaderu je nutné jeho verzi sjednotit také ve všech dlouhých HTML.

## Ověření
Výsledky jsou v `tests/darkove-boxy-results.json`:
- Test všech 25 tlačítek napříč pěti boxy a 14 zdrojů.
- 20 otevření načetlo úplný dostupný popis; pět výskytů téže láhve správně zachytilo prázdný zdroj.
- Zachování tabulek, žádný produktový požadavek před kliknutím, opakované otevření z paměti, zavírání, fokus, Escape, úzký mobil bez přetékání.
- Explicitní syntetické testy změny zdroje mezi návštěvami, dočasné HTTP chyby a opakování, nesprávného SKU, rychlého přepínání a zavření při načítání.
- Syntetický bezpečnostní test vloženého skriptu, event handleru, javascript odkazu a nesouvisejících obrázků; aktivní kód ani cizí obrazové požadavky neprošly.
- Navíc skutečné HTTPS načítání míchátka, Good Sleep, U F1RST drinku a mangového kolagenu v izolovaném prohlížeči. U U F1RST ověřeno viditelné rozbalení a přepínač složení. Žádná živá objednávka ani zápis do e-shopu.

`nahledy/darkove-boxy.html` je přenosná ukázka **s uloženými snímky ověřených popisů**, aby fungovala i mimo stejnou doménu bez CORS. Není to produkční zdroj informací. Produkční HTML načítá stránky živě. Obrázky/fonty v rozbaleném detailu ukázky mohou vyžadovat internet.

## Hranice této opravy
Git commit není nasazení do Shoptetu. Globální import homepage, newsletter, cookies ani globální sticky košík se nemění. Dřívější bezpečné přímé přidání do košíku u Beauty a přechod k hlavnímu nákupu u boxů bez ověřeného ID zůstávají zachované.

Zdravotní a produktová tvrzení se tímto technicky nepřepisují ani právně neschvalují. Jejich správné místo pro obsahovou opravu je nyní přímo zdrojový produkt, ne nezávislé kopie v boxech. Zdrojové nesrovnalosti (například metadata ananasového produktu obsahující označení Mango) je potřeba opravit centrálně; potvrzené ID/URL se kvůli nim automaticky nezaměňuje.

Podklady: původní HTML, skutečné veřejné produktové popisy a vlastníkem potvrzené URL. Zpracování: GPT-6 Astra, Python, Playwright/Chromium, DOMPurify a kontrola screenshotů. Bez placeného generování obrázků; cena modelového/konektorového zpracování není vyčíslená.
