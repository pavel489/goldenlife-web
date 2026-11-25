# Živé nasazení – Slim Extreme Collagen ananas–mango

Nasazeny pouze české popisy boxu (nativní ID 464) a samostatného sáčku (ID 467), oba krátké i dlouhé, na explicitní pokyn vlastníka úkolu „dej teda na web“ / „obě“.

- https://www.golden-life.cz/slim-extreme-collagen-box-ananas-mango/
- https://www.golden-life.cz/slim-extreme-collagen-sacek-s-prichuti-ananas-mango/

Zdrojová revize: 42e50c5414c6b83d657195205d4b9ea0b2a468ae. Dávka v CTA je jen „Denní dávka“ / „1 sáček“. Aktuální hlavní fotografie, bublina a nativní přebírání ceny zachovány. Ceny, sklad, SEO, další jazyky, kategorie a globální šablona nebyly cílem změny. V nativním formuláři byla měněna jen dvě pole popisů.

## Závislosti a izolace
Nahrány tři nové CSS soubory. Dvě produktové kopie schválených témat mají vlastní názvy, aby nebyly přepisovány styly dalších existujících jazykových popisů. Jejich přídavek frameless stylů je ekvivalent schválené společné varianty omezený na vlastní produkt. Původní společný CSS a veřejný scheme JS zůstávají beze změny; živý scheme JS už obě témata podporuje. CTA JS je původní přesná inline kopie z Gitu, bez nové změny logiky.

Živý nativní host na 320px je užší než izolovaný náhled. Do prvního STYLE ve dvou dlouhých popisech byla přidána produktově omezená korekce paddingu, velikosti a mezer štítků do 400px, aby dávka zůstala skutečně na dvou řádcích.

## Skutečné ověření
- Tři veřejné CSS byly po uploadu přečteny zpět a souhlasí SHA-256.
- Všechny čtyři CMS popisy byly po novém otevření editoru porovnány; CMS odstranil právě jeden koncový LF a jinak je obsah přesný.
- Čerstvý anonymní prohlížeč načetl obě živé stránky bez náhrad odpovědí nebo produktových stylů.
- 12 responzivních scénářů: 320/375/768/820/1024/1280 px pro obě varianty, dva textové řádky dávky, správná hlavní fotografie, shoda ceny s vlastním nativním nákupním formulářem.
- 28 otevření/zavření: šest ingredienčních dialogů a bannerové info u obou produktů na telefonu a desktopu.
- Delegace CTA byla ověřena zachycením nativního kliknutí bez odeslání nákupu. Žádný reálný košíkový požadavek nebyl odeslán. Žádná pageerror.
- Cookies, chat/iframe a promo překryvy byly skryty jen v QA pro čisté snímky; na produkci se jejich chování neměnilo.

## Obsahové výhrady
Nasazení designu není právním schválením převzatých účinkových tvrzení ani rozporů gramáží (240/246 g, 8/8,2 g). Předchozí obsahové výhrady zůstávají platné; tvrzení nebyla potichu přepisována. Detailní návody a bezpečnostní upozornění zůstaly zachované.

Podklady: brand/RULES.md, vlastní připravené soubory Gitu a explicitní pokyn k nasazení obou variant. Model gpt-6.1-sol. Bez placené generace nebo nákupu; cena běhu nástrojů/modelu není vyčíslená.
