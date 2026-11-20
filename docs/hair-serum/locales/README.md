# Hair Serum — slovenská, anglická a německá mutace

Kompletní krátký a dlouhý popis ve třech jazycích, podle nejnovějšího českého zdroje. Včetně finálních fotografií aktivních látek v3, celé fotografie v dialogu a opraveného kompaktního desktopového CTA.

## Slovenština
- [Dlouhý popis](../../../web/Golden%20Life%20Hair%20Serum/Golden-Life-Hair-Serum-sk.html)
- [Krátký popis](../../../web/Golden%20Life%20Hair%20Serum/maly/Golden-Life-Hair-Serum-maly-sk.html)
- [Samostatný offline náhled](nahled-sk.html) — stáhnout a otevřít v prohlížeči.

## Angličtina
- [Dlouhý popis](../../../web/Golden%20Life%20Hair%20Serum/Golden-Life-Hair-Serum-en.html)
- [Krátký popis](../../../web/Golden%20Life%20Hair%20Serum/maly/Golden-Life-Hair-Serum-maly-en.html)
- [Samostatný offline náhled](nahled-en.html) — stáhnout a otevřít v prohlížeči.

## Němčina
- [Dlouhý popis](../../../web/Golden%20Life%20Hair%20Serum/Golden-Life-Hair-Serum-de.html)
- [Krátký popis](../../../web/Golden%20Life%20Hair%20Serum/maly/Golden-Life-Hair-Serum-maly-de.html)
- [Samostatný offline náhled](nahled-de.html) — stáhnout a otevřít v prohlížeči.

## Ověření a zachování zdrojů

`manifest.json` uvádí přesný výchozí commit, všech šest HTML a kontrolní součty. `qa.json` zaznamenává skutečné browser testy desktop/tablet/mobil, otevírání všech složkových detailů, informačního panelu, lokalizované více/méně a CTA. Screenshoty jsou v `screenshots/`.

Přeložené jsou veškeré zákaznické texty, alt/aria a čtyři textové hodnoty dynamického mobilního ovládání. Byly zachovány kompletní odstavce, INCI, číselné údaje, zdrojové obrázky a URL, ID, kotvy, CSS, technické parametry i ostatní JS. Slovensky je zachováno vykání, německy Sie. České HTML ani sdílené závislosti se nemění. Každá transformace má přesné zdrojové offsety a byla reversibilně ověřena proti původním bytům.

## Obsahové výhrady

Hair Serum je kosmetický přípravek k zevnímu použití. Překlady zachovávají původní účinková tvrzení jako pracovní jazykové mutace, nikoli jako nové právní schválení. Přesné české věty i jejich překlady jsou v `claims-ledger.json`; odborné otázky a neutrální identifikační alternativy jsou v `claims-review.md`. Produktový soubor neobsahuje schválené účinkové náhrady. EFSA tvrzení pro ústně užívané živiny nejsou důkazem pro lokálně aplikované sérum. Interní výhrady nebyly vloženy do zákaznického HTML.

Fotografie jsou AI ilustrační motivy. Avokádo, arašídy, vejce a mandle symbolizují přirozený výskyt vitaminů, nikoli ověřený výrobní původ konkrétních látek v séru nebo další INCI ingredience.

## Zdroje a nasazení

Zdroje: přesné aktuální české HTML a závislosti z `pavel489/goldenlife-web`, pravidla Golden Life, produktový soubor `brand/product/hair-serum/info.md`, dřívější oddělený přehled tvrzení. Historická cena ze souboru info.md se nepřenáší; dostupnost a cena zůstávají v nativním nákupním bloku. Model gpt-6.1-sol; bez nové placené generace médií, cena modelového provozu nebyla vyčíslena.

Git předání není uložením jazykových polí do živého Shoptetu.
