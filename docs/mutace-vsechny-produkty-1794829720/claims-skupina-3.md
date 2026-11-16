# ID464 / ID467 – interní jazykové návrhy

12 úplných HTML: dlouhý i krátký popis ve SK, EN a DE. Nic nepublikováno do Gitu ani e-shopu.

## Rozsah a obsah
- Zdroj: připnutý main `a5bb8abb7cc36fe702c3a1441e456417b15d0f4e`. CZ originály jsou nedotčené.
- Zachované všechny sekce, úplné dialogy, receptury, tabulky, číselné hodnoty, CSS, technická ID, URL obrázků a synchronizační logika.
- Značkové názvy (včetně historického „Slim Extreme Kolagen“ v krátkém sáčku a „Slim Extreme Collagen Box Ananas & Mango“) jsou ponechány přesně. Samostatné názvy příchutí a prodejních jednotek jsou přeložené.
- Německé složeniny v úzkých popiscích mají volitelné typografické dělení U+00AD; CSS nebylo změněno. Číselný badge sáčku používá věrné krátké „1 Beutel“. Po úpravě byly finální soubory znovu vygenerovány a otestovány.
- RHP je lokalizováno na RVH v SK a NRV v EN/DE. KJT na KTJ/CFU/KBE, miliardy/miliony významově beze změny; čárkové číselné zápisy a jednotky jsou zachované.
- Interní zdrojové varování není právní schválení. Claims ledger obsahuje přesné rizikové texty a neutrální alternativy; alternativy nebyly dosazeny namísto zadaného úplného překladu.

## Zděděné problémy
- ID464: 240 g ve zkráceném historickém bloku versus 30 × 8,2 g / 246 g v dlouhém; rozpor zachován a označen ve zdroji.
- ID467: krátký historický blok stále obsahuje 30 dní a 240 g, přestože jde o jednotlivý sáček; ponechán jako zdrojový rozpor v označeném rozbalovacím bloku, nikoli opraven odhadem.
- Oba zdrojové dlouhé popisy mají stejnou tabulku. Nesloučeno podle podobnosti, každý přeložen z vlastního souboru. Synefrin, HCA, Aquamin a procenta RHP mohou mít historické nesrovnalosti; všechny hodnoty zachovány.
- ID464: info.md uvádí zinek 1220 % a chrom 610 % na 100 g; aktuální Git HTML uvádí 1180 % a 1610 %. HTML zůstalo autoritou této jazykové mutace, hodnoty nebyly přepsány.
- Bez cukru versus tabulkové cukry 2,9 g/100 g; bez přídatných látek versus sukralóza. Přesné výroky přeloženy bez přidání nových tvrzení, nutná kontrola podmínek.
- Výrazy regenerace, spalování tukových buněk, hormonální rovnováha, celulitida, probiotika, foam-potvrzení účinných látek a limitovaná edice jsou zděděné neověřené marketingové výroky.
- Zdroj obsahuje viditelné interní upozornění a historické/kontrolní FAQ. Zachovány a přeloženy dle výslovného zadání zachovat celou aktuální strukturu; před zákaznickým nasazením musí vlastník vyřešit obsahové rozpory a odstranit interní pracovní poznámky v samostatně schválené revizi.
- Nebyly doplněny nové ceny, sklad, recenze, měny ani termíny. Nativní nákupní odkaz a logika zůstávají beze změny.

## Testy
`python3 analysis/generate.py`, `python3 analysis/test_static.py`, `node analysis/test_ast.cjs`, `node analysis/test_browser.cjs`. Skripty mají absolutní lokální základ této úlohy; běh testů nic nepublikuje.

Browser QA používá skutečné Chromium a přesné lokální CSS/JS z připnutého repozitáře. Externí fotografie/fonty se v offline fixture nenačítají; rozbité obrázky nejsou nahrazeny falešným obsahem. To není kontrola živého e-shopu, aktuální dostupnosti assetů ani nativního nákupu.
