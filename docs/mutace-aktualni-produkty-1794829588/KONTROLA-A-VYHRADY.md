# Obsahové výhrady k pracovním překladům

Všechny výhrady jsou mimo zákaznické HTML. Překlady zachovávají původní produktové texty; vytvoření jazykové mutace není právní schválení tvrzení ani potvrzení rozporů ve složení/dávkování.

## Co ověřit před vložením

- Beauty Star: v dlouhém a krátkém zdroji je 65 g versus 30 g a odlišné pojmenování formy produktu. Tvrzení o akné a hormonální rovnováze vyžadují konkrétní kontrolu; nejsou tímto schválena.
- Čaje: původní tvrzení o detoxikaci a prevenci onemocnění zůstávají neověřená; zkontrolovat počet bylin, porce a alergeny. U pH+ původní text uvádí sedm i devět bylin. U 7denního čaje se směšuje porcovaný čaj a dávkování lžičkou.
- Slim Extreme Collagen: tvrzení „Extrémní spalování tuků“ není tímto schváleno. Produktový soubor `brand/product/extreme-slim-collagen/info.md` uvádí doslova „Vitaminy B2, B3 a B5 přispívají ke snížení únavy a vyčerpání.“ Jde o jiný, živinově konkrétní úhel; není to schválení spalování tuků ani náhrada všech účinků. Formulace je evidovaná v produktovém zdroji, právní a dávkovou platnost před publikací je nutné potvrdit.
- Svačinky: zachované GLP-1 a další účinkové formulace vyžadují kontrolu. Původní podklady mají rozpory v bezcukernosti, CFU a seznamu složek; hodnoty nebyly svévolně sjednocovány.

Přesné původní a přeložené věty jsou v `qa/<ID>/...claims....json`. Souhrn všech zaznamenaných rozporů: `obsahova-kontrola.json`.

## Rozsah testů a omezení

48 finálních HTML souborů prošlo nezávislou kontrolou CSS, URL fotek, číselných buněk tabulek, kotev a syntaxe skriptů. Nezávislá integrační zkouška v Chromium: 8 produktů × 3 jazyky × 2 šířky = 48 scénářů; otevírání/zavírání informačních a prvního/posledního složkového dialogu, geometrie a JS chyby. Každý produkt má samostatné detailnější QA odkazované výše, včetně původních testů všech složkových dialogů.

Testy běžely z přesných finálních HTML v oddělené testovací stránce s autentickými uloženými prostředky. Nejde o uložení v CMS, zkoušku nativního nákupu ani kontrolu fyzického Safari/iPadu. U pH+ nebylo v samostatné offline sadě devět nových fotografií bylin; font Material Symbols není v části sad dostupný. Integrační omezená společná cache navíc neobsahuje všechny obrázky z jednotlivých samostatných sad: chybějící URL jsou přesně uvedené v `parent-browser-qa.json`, bez náhradních vymyšlených obrázků. Původní produkční URL v HTML zůstaly zachované.

U nových překladů byly odstraněny zděděné interní poznámky a u kolagenové dózy staré české cenové/skladové a ratingové náhradní hodnoty; nebyl vymyšlen kurz ani nabídka. Doplněná povinná upozornění jsou zaznamenaná v jednotlivých QA. České originály zůstávají beze změny.

Model GPT-6.1-sol, překlad a HTML; žádné placené obrazové generování. Celkové modelové vyúčtování není k dispozici.
