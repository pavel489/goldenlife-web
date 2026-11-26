# Beauty & Longevity NAD+ — dóza, oprava podle dodané etikety

Český krátký a dlouhý popis. Dávkování: **1 odměrka (9 g) denně**. Dóza **270 g / 30 denních dávek**. Příprava: v 300–400 ml vody a vypít, nebo v 1 l vody a popíjet během dne. V žádném z obou HTML nezůstává dávkování v sáčcích ani sáčkový piktogram.

Tabulky aktivních látek jsou nově opsané přímo z dodaného dvoustránkového PDF `Beauty_and_Longevity_NAD_PLUS_ DOZA.pdf`: 22 řádků včetně chemických forem, denních množství a RHP. Množství souhlasí s původní denní dávkou boxu; neověřené hodnoty na 100 g a kopie seznamu pomocných látek nejsou vydávány za údaje etikety. Nutriční údaj z etikety: 26 kcal / 9 g. Etiketa v tomto PDF nedokládá úplný seznam pomocných látek.

Stejná šablona, barvy, karty a dialogy jako box. Horní produktový obrázek i fotografie v CTA automaticky přebírají načtenou hlavní fotografii z nativní galerie stejné produktové stránky. Výřez etikety ani jeho popisek se už nevkládají. Při chybějící/neplatné fotografii se nepoužije etiketa ani cizí náhradní obal. Pokud je nakonfigurované productId, kontroluje se shoda; bez nastaveného ID slouží nativní formulář pouze k nalezení hlavního obrázku téže stránky, nikoli k automatickému převzetí ceny nebo nákupu. ID boxu 544 se nové dóze nepřiřazuje; cena/nákup zůstávají bez přesného ID neaktivní.

Git main není nasazení do Shoptetu. Česká dvojice dózy je opravená; původní sáčková varianta, jiné produkty, překlady i sdílené CSS se nemění.

Původní účinkové texty zůstávají pracovní, ne nově schválené. Údaj etikety „Vhodné pro děti od 8 let“ vyžaduje odborné ověření vzhledem k NR. Podrobná revize tvrzení: docs/nad-doza-etiketa/revize-tvrzeni.md.

Podklady: dodaná etiketa, aktuální Git main, brand/RULES.md a vlastní produktový soubor. GPT-6.1-sol, HTML/CSS/Python, Chromium. Bez placené obrazové generace; cenu běhu runtime neuvádí. Testováno pět šířek 320/390/768/1024/1440, šest ingredienčních dialogů + horní dialog, Escape/návrat fokusu, mobilní rozbalování, nulové přetékání a chyby JS v offline náhledu. Nejde o test uloženého Shoptetu.
