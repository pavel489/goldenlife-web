# Hair Serum — český krátký a dlouhý popis

Nově vytvořená samostatná produktová stránka v současném sdíleném systému Golden Life. Produkt **Hair Serum, ID 354**, kosmetický přípravek k zevnímu použití. Nejde o Xpress Hair Grow ani o doplněk stravy.

## Soubory pro úpravy a vložení

- [Dlouhý popis](../../web/Golden%20Life%20Hair%20Serum/Golden-Life-Hair-Serum-cz.html)
- [Krátký popis](../../web/Golden%20Life%20Hair%20Serum/maly/Golden-Life-Hair-Serum-maly-cz.html)
- [Vlastní zelené CSS](../../user/documents/upload/css/golden-life-barvy-hair-serum.css)
- [Sdílený detektor okolního pozadí](../../user/documents/upload/js/golden-life-product-scheme.js) — změna jen v seznamu podporovaných témat, přidáno `hair-serum`.
- [Společné produktové CSS](../../user/documents/upload/css/golden-life-produkt.css) — beze změny proti výchozímu commitu.
- [Samostatně otevřitelný offline náhled](nahled.html) — stáhnout a otevřít v prohlížeči; není nákupní stránka. Jen v tomto náhledu jsou autentické fotografie úsporně zakódované jako WebP; produkční HTML zachovává původní obrazové URL.
- [Dlouhý desktopový náhled](screenshots/long-1440.png), [mobilní náhled](screenshots/long-390.png), [krátký popis](screenshots/short-390.png).

## Co je hotové

- Zelená identita Hair Serum, nový banner, skutečná hlavní fotografie produktu a šest sjednocených bezrámečkových piktogramů.
- Šest karet: Capixyl™, panthenol, niacinamid, biotin, Sodium Hyaluronate a extrakt z červeného jetele. Každá má tlačítko plus a celý původní popis, nikoli náhradu obecným dávkováním.
- Zachováno 23 původních odstavců včetně složení, návodu, skladování a omezení, všech šest položek účinků. Dlouhý a krátký úvod pocházejí každý z vlastního živého zdroje.
- Zvětšení lahvičky řeší pouze ořez prázdných okrajů při zobrazení. Žádný přegenerovaný obal, retuš ani změna identity produktu. Pro jinou skutečnou fotografii stejného SKU se ořez automaticky vypne.
- Mobilní rozbalování, návrat mobil–desktop–mobil, dialogy s klávesnicí a návratem fokusu, kontrola identity při synchronizaci hlavní fotky, přizpůsobení světlému/tmavému okolí.
- Krátký popis v úzkém nákupním sloupci používá dvě řady po třech piktogramech; na širokém hostiteli jednu řadu šesti.

## Ověření

Výsledek a jednotlivé scénáře: [qa.json](qa.json).

- Chromium 156: 20 rozměrových/světlých/tmavých scénářů včetně 320, 390, 767, 768, 820, 1024 a 1440 px; navíc krátké hostitele 280/320/420 px.
- 28 průchodů všemi sedmi panely: 6 složek + návod v banneru, mobil/desktop, světlé/tmavé okolí. Ověřeno otevření/zavření ukazatelem, Escape, fokus a plné odstavce.
- 3 responzivní průchody, 4 testy skutečné fotografie včetně cizí fotky při správném ID a nesprávného ID.
- Bez vodorovného přetékání, přetékajících popisků, vadných obrázků a chyb JavaScriptu v izolovaném testu.
- Čtyři vložené skripty prošly `node --check`.
- Bez JavaScriptu zachováno světlé zobrazení a CSS otevření složky.
- Stažený offline soubor: 31 skutečných obrázků, žádné externí požadavky, otevření dialogu vyzkoušeno.
- Finální screenshoty desktopu, mobilu, krátkého popisu a tmavého dialogu byly skutečně vizuálně zkontrolované.
- Navíc [native-qa.json](native-qa.json): mobilní a desktopová kontrola v celé původní veřejné stránce s lokálně nahrazenou HTTP odpovědí a připravenými CSS/JS. Oba scénáře bez přetékání, správná hlavní fotka a zelený motiv, funkční dialog; 4 mobilní/0 desktopových přepínačů. Shopový skript přemisťuje krátký úvod mimo vlastní wrapper, ale text zůstává v nativním hostiteli. Jde o zkušební přepsání odpovědi, ne uložení CMS.

Test je **izolovaná same-origin zkušební stránka s přesnými soubory z tohoto repozitáře**, nikoli uložená změna CMS, certifikace přístupnosti, fyzický telefon nebo Safari. Písmo v izolovaném náhledu používá Arial fallback za Metropolis; živé dědění písma z šablony e-shopu nebylo tímto testem certifikováno. Žádný formulář nákupu nebyl odeslán.

## Před vložením na živý e-shop

**Nic nebylo uloženo do Shoptetu.** Zveřejnění v Gitu je předání návrhu, nikoli publikace na e-shop.

Aktuální kontrola veřejných závislostí je v [public-dependencies.json](public-dependencies.json): nové `golden-life-barvy-hair-serum.css` ještě vrací **404**; veřejné společné CSS i JS se liší od připraveného Gitu. Pro nasazení je nutné použít kompatibilní společné CSS, nové vlastní CSS a aktualizovaný sdílený JS, poté oba HTML popisy a samostatně ověřit živý výsledek. Přidat importy ke starému inline popisu není ekvivalent této hotové migrace.

## Zdroje, obsah a cena

- `brand/RULES.md` a `brand/product/hair-serum/info.md`.
- Vlastní živé krátké/dlouhé popisy a galerie na https://www.golden-life.cz/hair-serum/; skutečné ID 354.
- Aktuální sdílený framework a kosmetický vzor Miracle Drops z výchozího commitu `02e3c306915d0ba9a2a22690a4fabf9c3adc4124`; složení ani účinky Miracle Drops se nepřebírají.
- Aktuální bezrámečková monoline grafika z repozitáře včetně opraveného `hair-v5`; pouze barevná varianta, původní alfa zachována. Editovatelné PNG jsou v `assets/piktogramy/hair-serum/`, HTML obsahuje stejné PNG vložené přímo.
- Model: **gpt-6.1-sol**. Python/BeautifulSoup/Pillow, Node, Playwright/Chromium, Composio GitHub.
- **Bez placeného generování médií.** Skutečná cena modelového a nástrojového běhu není v této předávce dostupná; nulový celkový náklad netvrdíme.

Původní účinková tvrzení jsou zachována jako převzatý pracovní obsah, nikoli nově právně schválené sliby. Přesné výhrady, alternativy a odstraněné zastaralé obchodní údaje jsou odděleně v [obsah-ke-kontrole.md](obsah-ke-kontrole.md); interní poznámky nejsou ve vložitelných HTML.


## Aktualizace obrázků aktivních látek v3

Nová šestice fotografií je zapojená v dlouhém českém popisu, v kartách i dialozích. [Přehled, mapování a testy](ingredient-images-v3/README.md). Obrázky jsou v `assets/hair-serum-ingredients/`; offline `nahled.html` a hlavní screenshoty jsou aktualizované. Živý Shoptet tato Git změna nepřepisuje.


## Oprava fotografie v rozkliknutém detailu

Produktová CSS výjimka `object-fit:contain` vytvářela u širokých obrázků boční pásy. Vlastní styl Hair Serum nyní používá plnou šířku a automatickou výšku podle skutečného poměru obrázku: fotografie je od kraje ke kraji bez deformace a bez dodatečného ořezu. Krátký i dlouhý popis načítají stejné CSS s novým cache parametrem `hair-serum-2-modal`. Fotografie, texty, skripty, sdílené CSS i ostatní produkty jsou beze změny.

Opravený samostatný náhled: `nahled.html`. Podklady a testy: `modal-full-bleed/`. Pro živý Shoptet je nutné nahrát aktualizovaný `user/documents/upload/css/golden-life-barvy-hair-serum.css` a použít aktualizované importy; Git publikace sama živý obchod nepřepisuje.
