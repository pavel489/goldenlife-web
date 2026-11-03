# Pořadí náhledových karet dárkových boxů

Úprava na explicitní zadání Pavla: nahoře tabletky → nápojový box → tabletky; dole láhev → USB míchátko → dárkové balení. Platí pro Beauty, Hormonal, Longevity, Slim a UFIRST.

Změněno pouze pořadí šesti celých existujících karet v `.latky-grid` pěti dlouhých popisů. Texty, zdrojové fotografie, CSS, detailové vazby, skripty, krátké popisy a ostatní soubory zůstávají beze změny. Zpětné přeskupení vrací každý původní soubor bajtově identicky.

Kontrola: Chromium/Playwright, všech pět boxů při 1440, 768, 390 a 320 px (20 kombinací). Ověřeno pořadí DOM, tři sloupce a dva řádky na desktopu/tabletu, zachovaný jednosloupcový mobilní režim, žádný vodorovný přetok. Vizuálně prohlédnutý přehled všech pěti desktopových rozcestníků. Testovací náhled obsahoval původní CSS a celý rozcestník s reálnými vzdálenými obrázky, bez importovacích a okolních shopových skriptů. Nejde o nové testování importu produktových detailů ani košíku.

Původní problém mimo tuto změnu: fotografie Slim GLP-1 Activator v boxu Slim se ze stávající URL nenačetla. Adresa byla zachována. Fotografie dárkového balení není v izolovaném náhledu naplněna, protože ji původní skript přebírá z galerie hostitelského produktu. Tento test neověřuje napojení galerie živého Shoptetu.

Podklady: aktuální vzdálená větev main repozitáře pavel489/goldenlife-web (výchozí strom d4ad3dbe49e2df9654a0ef479945897821efe808), brand/RULES.md a přímé zadání. Provedení: GPT-6.1, Python, HTMLParser, BeautifulSoup a Playwright. Bez placeného generování; cenu agentového provozu nemáme vyčíslenou. Původní textová tvrzení nebyla měněna ani právně auditována.

Publikace pouze do Gitu, ne do živého Shoptetu.
