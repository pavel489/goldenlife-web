# Oprava dvou tabletových nálezů: ID635 a ID641

## Hotový výsledek
Opraveny oba neúspěšné tabletové scénáře: Hormonal Balance noční GLP-1 drink (ID635) a jeho samostatný sáček (ID641). V pásmu **769–1023 CSS px** jsou ikony benefitů nad textem, takže celý popisek dostane šířku svého sloupce. Původní znění, pořadí, barvy i samotné glyphy zůstaly zachované. Oprava pouze neskrývá přetečení a nerozbíjí slova na jednotlivá písmena.

Změněny jsou pouze tyto produktové závislosti:
- `user/documents/upload/css/golden-life-barvy-glp1-woman-balance.css`
- `user/documents/upload/css/golden-life-barvy-glp1-woman-balance-sacek.css`

Do každého tématu byl připojen přesně ohraničený tabletový blok. Všechny původní bajty témat jsou zachované. Čtyři dlouhé/krátké HTML, společné `golden-life-produkt.css`, fotografie, texty, tabulky, skripty a nákupní chování se nemění. Na živý Shoptet se nic nenahrávalo.

## Ověření skutečného zdroje
Před opravou byl z autorizovaného GitHubu načten aktuální `main` **3cf7fcb3544f8c46a28feb86a948ed4eaf915379** přes Composio pod identitou Goldie. Obě témata, čtyři HTML a společný framework byly přečteny podle Git blob SHA; jejich bajty jsou totožné se zdroji použitými v původním offline náhledu. Proto lze bezpečně použít stejný fixture s opravou vloženou z přesného výstupního CSS. Ostatních 12 návrhů v regresi zůstává původní předaná offline sada, nikoli tvrzení o čerstvém živém webu.

## Naměřeno po finální opravě
- Původní 6px vnitřní přetékání banneru při820px je u obou produktů **0 px**. Kontrolovány i vlastní rozměry benefitů a hranice textových uzlů.
- **56/56** scénářů původní geometrické matice prošlo: 14 návrhů × 768×1024, 820×1180, 1024×768 a767×1024 CSS px.
- **14/14** návratů telefon → tablet → desktop → tablet prošlo stejnou geometrickou kontrolou.
- **364/364** skutečných pointer otevření a zavření ingredientových dialogů prošlo.
- Navíc **22/22** podrobných před/po scénářů těchto dvou produktů: šířky390,767,768,769,780,800,820,900,1023,1024 a1440px.
- **10/10** srovnání pixelů banneru při390,767,768,1024 a1440px je před/po totožných. Oprava nemění telefon ani desktop mimo vymezené tabletové pásmo.
- V těchto offline bězích žádné JS chyby ani externí HTTP(S) request eventy.
- Finální snímky byly skutečně otevřené a vizuálně zkontrolované; první čistě typografická varianta byla před předáním zamítnuta kvůli nevhodnému lámání slov. Publikovaná finální varianta používá ikony nad popisky.

## Předání a nasazení
Opravené CSS a tento protokol jsou Git pracovní předání. HTML už tato dvě témata importuje; při budoucím autorizovaném nasazení je nutné nahrát obě celé aktualizované CSS na stejné shopové cesty, ověřit skutečné veřejné bajty a čerstvý výsledek v šabloně. Git commit nenahrává soubory do Shoptetu.

## Co touto opravou není vyřešené
Tento krok opravuje dva neúspěšné **tabletové layouty**, nikoli celou podporu tmavého režimu. Systémová tmavá paleta se nadále nepřepíná. Chybějící skutečné zdrojové fotografie a offline masky ID550 z původního auditu zůstávají samostatnými omezeními. Fyzický iPad/Safari, plný kontrastní audit a čerstvý živý e-shop nejsou ověřené. Chybějící fotografie nejsou nahrazené maketami ani vydávané za hotové nebo živě ověřené zdroje.

Historická účinková tvrzení ve snímcích nebyla v tomto CSS kroku měněna ani právně schválena; původní obsahové výhrady zůstávají platné.

## Podklady a nástroje
Zdroj: přesné remote Git blob bajty uvedené výše a původní offline viewery dávek3–4D. Důkazy: `summary.json`, `results.json`, `extended-tests.json`, `changes.json`, `source-manifest.json`, snímky před/po a samostatný offline náhled. Model GPT-6.1-Sol, Python, Chromium/Playwright. Bez placené obrazové generace; náklady modelu/connectorů tento runtime nevyčísluje.
