# Beauty Star – nová grafika

## Soubory
- [Dlouhý popis](Golden-Life-Beauty-Star-cz.html)
- [Krátký popis](maly/Golden-Life-Beauty-Star-maly-cz.html)
- [Barevný model](../../user/documents/upload/css/golden-life-barvy-beauty-star.css)
- [Společný framework](../../user/documents/upload/css/golden-life-produkt.css)
- [HTML náhled](../../nahledy/beauty-star.html) – stáhni/otevři v prohlížeči, vyžaduje internet pro skutečné fotografie a shop styly. Nákup je vypnutý. GitHub zobrazuje HTML jako zdroj, ne jako živou stránku.
- [Obrázkový náhled](../../nahledy/beauty-star.png)
- [Výsledky testů](../../docs/beauty-star-testy.json)

## Nasazení
Oba CMS popisy mají přesně dva importy: společný `golden-life-produkt.css` a vlastní `golden-life-barvy-beauty-star.css`. Společné CSS se v této změně nemění; je totožné s již uloženým frameworkem. Použitý layout je nejnovější Woman Hormonal Balance, barevné téma je samostatné `beauty-star` se zelenou #07873c převzatou ze skutečné stránky Beauty Star.

Nahraj nejprve CSS do `/user/documents/upload/css/`, potom nahraď staré dlouhé a krátké popisy celými příslušnými HTML. Funkční skript mobilního rozbalování ponech. Git publikace NENÍ nasazení do Shoptetu. V době původní kontroly na webu zůstávalo staré společné CSS a nový barevný soubor vracel 404.

## Kontrola
- Aktuální veřejný zdroj: https://www.golden-life.cz/beauty-star/ ; productId 351.
- Zachováno všech 13 položek tabulky množství, ověřeno po jednotlivých buňkách.
- Offline návrh testovaný při šířkách 320, 360, 390, 520, 768, 1100, 1440 a návratu na 390 px: bez horizontálního přetečení a rozbitých obrázků, bez JS chyb a externích požadavků offline souboru.
- Skutečné CMS fragmenty se skutečnými importy a shop styly otestovány lokálním přepsáním odpovědi při 320, 390, 768 a 1440 px. Nešlo o uložení v CMS.
- Tři mobilní přepínače myší/Enterem, detail úvodu a pět detailů látek ověřené otevřením/zavřením. Vizuálně kontrolován desktop i mobil.
- Před publikací této Git verze byl navíc samostatně otevřen přiložený síťový HTML náhled.

## Obsahová omezení
- Původní krátký popis uváděl 30 g, dlouhý 65 g. Hmotnost návrh neuvádí do potvrzení etikety. Obsah 60 hvězdiček / 2 denně / 30 denních dávek vychází ze zdroje.
- Původní sliby „čistší pleť bez akné“, „rychlejší růst vlasů“ nebo „stabilizovat hormonální hladiny“ nejsou přenesené jako schválené účinky. Nové znění uvádí skutečné látky a množství.
- Specifický produktový soubor s povolenými zdravotními formulacemi není dostupný. Schválená alternativa proto nebyla domýšlená. Produktová upozornění i úplný seznam surovin je před nasazením nutné porovnat s etiketou; tabulka množství není úplný seznam surovin.
- Před případným vložením do dárkových boxů je nutné ověřit allowlist nového názvu barevného CSS v jejich loaderu. Ostatní boxy nejsou v této změně upravené.

## Výroba
Podklady: pravidla značky, veřejný Beauty Star včetně původních vlastních fotografií/dekorativního pozadí a připravené nové společné CSS s referencí Woman Hormonal Balance. Model GPT-6.1-sol, Python/BeautifulSoup, Chromium/Playwright, Pillow. Bez placené obrazové/video generace; cenu jazykového modelu nemám vyčíslenou.

Doručovací pravidlo pro tuto práci: editovatelné soubory a změny patří do tohoto Git repozitáře, nikoli do ZIP přílohy. Žádný ZIP není součástí commitu.
