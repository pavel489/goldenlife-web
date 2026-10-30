# Slim GLP-1 Activator s Berberinem – nová grafika

## Hotové soubory
- [Dlouhý popis](Golden-Life-Slim-GLP-1-Activator-cz.html)
- [Krátký popis](maly/Golden-Life-Slim-GLP-1-Activator-maly-cz.html)
- [Barevné CSS](../../user/documents/upload/css/golden-life-barvy-slim-glp-1-activator.css)
- [Společný framework](../../user/documents/upload/css/golden-life-produkt.css)
- [HTML náhled](../../nahledy/slim-glp-1-activator.html) – otevři stažený soubor v prohlížeči; fotografie, fonty a styly webu vyžadují internet. GitHub zobrazuje HTML jako zdroj, nikoli živou stránku.
- [Obrázkový náhled](../../nahledy/slim-glp-1-activator.png)
- [Výsledky testů](../../docs/slim-glp-1-activator-testy.json), [zdrojový manifest](../../docs/slim-glp-1-activator-manifest.json) a [kontrola textů](../../docs/slim-glp-1-activator-texty.md)

## Výslovná oprava jednotek u chromu
- 1 tobolka: **25 mcg** místo 25 mg.
- 2 tobolky (denní dávka): **50 mcg** místo 50 mg.

Jde o opravu chybně uvedené jednotky, nikoli o matematický převod původního množství z mg na mcg. Číselné hodnoty zůstaly stejné. Oprava je shodná v tabulce, přehledu dávky i detailu chromu. Ostatním složkám zůstávají původní mg. Zachováno i původních 125 % RHP u denní dávky chromu; ostatní značky RHP nebyly domýšlené či přepočítané. Per-tobolkové `*% RHP` a obecná poznámka o RHP jsou převzaté ze zdroje, ne nově potvrzená specifikace.

Každá buňka tabulky byla porovnaná s aktuální veřejnou stránkou. Přesně dvě obsahové změny: mg → mcg u chromu; všechna ostatní čísla a buňky zůstaly stejné. Extrakt z Berberis aristata a jeho obsah berberinu HCl jsou popsané odděleně: **485 mg HCl je součástí 500 mg extraktu**, nikoli dodatečná dávka k sečtení.

## Nová grafika
Referenční komponentový systém je nejnovější Woman Hormonal Balance / připravené produktové stránky. Produkt má vlastní téma `slim-glp-1-activator`, fialovou GLP-1 **#62388E** a ověřenou identitu **476**. Nejde o přebarvený SOS produkt: dávky, receptura, fotografie, dekorativní motiv a upozornění pocházejí ze skutečného Activatoru.

Zůstává banner, detail úvodu, hero, fotografie v informačních kartách, šest detailů látek, vlastní Nextida blok s motivem GLPBLESKY, CTA, návod, plné zdrojové složení a tabulka. Mobilní rozbalování je zachované. Obecný CSS framework se v tomto commitu **nemění**; používá už existující opt-in úpravu třísloupcové tabulky.

Každý CMS popis obsahuje přesně dva importy v jednom malém bloku:

```html
<style>
@import url("/user/documents/upload/css/golden-life-produkt.css");
@import url("/user/documents/upload/css/golden-life-barvy-slim-glp-1-activator.css");
</style>
```

## Nasazení
1. Ověř, že má e-shop aktuální společné `golden-life-produkt.css` z tohoto repozitáře. Nahraj nový barevný soubor na uvedenou cestu.
2. Nahraď dlouhý a krátký popis celými příslušnými HTML; nepřidávej je za staré vložené styly.
3. Ponech funkční skript mobilního rozbalování. Dvě CSS řeší vzhled, nikoli interaktivitu.
4. Zkontroluj skutečně uloženou stránku na telefonu/desktopu, chrom v mcg, šest detailů a produktová upozornění.

**Doručeno přes Git, bez ZIPu. Nic nebylo uložené v administraci Shoptetu.** CTA pouze odkazuje k nativnímu nákupnímu formuláři, nemá vlastní cenu/stock ani nákupní zápisy. Nákup v náhledu je vypnutý.

## Podklady a limity
- Veřejná https://www.golden-life.cz/slim-glp-1-activator-s-berberinem/ , productId 476.
- Produktové fotografie v bloku u třetího odstavce a v CTA čerpají z nativního hlavního obrázku produktu 476 v Shoptetu, nikoli z infografiky v popisu. Skript ověřuje productId, načtení obrázku a původ mimo vložený popis; obě místa sledují změnu hlavního obrázku. Samostatný náhled a chybové stavy mají skutečný aktuální hlavní packshot jako zálohu. Aktuální URL: https://cdn.myshoptet.com/usr/www.golden-life.cz/user/shop/big/476-3_activator-02-aktualni-mockup-v1.png?ff=1&x=1024&y=1024&q=85&ts=6adf20e6&sg=38cb01fe
- Vlastní existující lifestyle fotografie z aktuální stránky, šest ilustrací složek a vlastní dekorativní `GLPBLESKY.png`. Fotografie složek nejsou důkazem původu surovin. Současné fotografie se v tomto grafickém návrhu neredrawují ani nepřenášejí na jiný produkt.
- Původní detail L-leucinu odkazoval na `glp1-berberin_04_I-leucin.png` (404). Nově používá stejnou skutečně funkční fotografii jako vlastní karta: `glp1-berberin_04_l-leucin.png`. Jde o ověřenou existující adresu, nikoli odhad náhradního souboru.
- Plný původní seznam surovin, návod, skladování a upozornění jsou převzaté z aktuální stránky. Obecné povinné upozornění doplňku je doplněné. Botanické pojmenování „indický dřín“ ze zdroje je ponechané v doslovném složení k lidskému ověření, nikoli vydávané za novou taxonomickou kontrolu.
- Produktový soubor se schválenými zdravotními formulacemi není dostupný. Původní přísliby aktivace hormonů, „bleskového hubnutí“ či alternativy k farmaceutické GLP-1 léčbě proto nebyly přenesené jako schválené účinky. Nové znění uvádí složky, množství a užívání; podrobná revize je v samostatném souboru.
- Autentická etiketa na fotografii obsahuje vlastní účinkové nápisy (včetně rychlosti hubnutí); nebyla retušovaná. Její přítomnost na pravém obalu není novým právním schválením daného tvrzení.
- Při pozdějším vkládání detailu do boxů je potřeba ověřit allowlist nového názvu barevného CSS v jejich loaderu. Ostatní produkty ani boxy se v této změně neupravují.

## Skutečné testy
- Náhled na 320, 360, 390, 520, 767, 768, 1100, 1440 px a návrat na 390 px.
- Přesné CMS fragmenty se dvěma importy a skutečnými shop styly na 320, 390, 768 a 1440 px, pomocí dočasného lokálního přepsání odpovědi na původním originu – nikoli CMS uložení.
- Bez horizontálního přetečení stránky/banneru, bez rozbitých použitých obrázků a bez JS chyb. Rozsahy textů všech buněk měřené vůči vlastním hranám, ne pouze vůči stránce.
- Tři mobilní rozbalování myší/Enterem, detail banneru a všech šest detailů složek otevřeno/zavřeno. CTA vede k nativnímu formuláři.
- Dekódovaný skutečný obrázek pozadí Nextida; náhled nespoléhá na relativní `file:` cestu, která by nechala bílý text na bílém podkladu.
- Tabulka: přesně dvě změny jednotek, ostatní údaje beze změny. Vizuálně kontrolovaný desktop, mobil, packshot i mobilní tabulka.

## Výroba
Pravidla značky a pracovní vizuální identita Golden Life; aktuální veřejný Activator; komponenty a společný CSS z Git main 7fb242e47c6d5ade6abfddab867edda2a261906b. Model GPT-6.1-sol, Python/BeautifulSoup, Chromium/Playwright a Pillow. Bez placené obrazové/video generace; cenu jazykového modelu nemám vyčíslenou.

## Oprava hlavního obrázku a piktogramů
- Obě produktové fotografie se synchronizují s hlavním obrázkem nativní galerie pouze pro productId 476. Jiný produkt se nikdy nepřevezme. Fallback je skutečný hlavní packshot 476. Při změně hlavního obrázku galerie se obě místa aktualizují automaticky.
- Piktogramy v dlouhém i krátkém popisu už mají vlastní fialovou #62388E; odstraněno jejich druhotné CSS přebarvování (`--gl-icon-filter: none`). Zdrojové PNG a průhlednost jsou zachované. Stačí nahrát aktualizované barevné CSS a dlouhý popis; krátký popis se nemění.
- Zachované texty, všech 6 detailů, obrázky složek, tabulka včetně chromu 25/50 mcg a společné CSS. Nejde o obsahovou revizi ani schválení tvrzení na etiketě.
- [Testy této opravy](../../docs/slim-glp-1-activator-hlavni-foto-piktogramy-testy.json). Git není živé nasazení v Shoptetu.
