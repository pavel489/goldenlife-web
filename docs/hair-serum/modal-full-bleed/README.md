# Hair Serum — fotografie v dialogu od kraje ke kraji

Původní stav reprodukován: široká fotografie v pevné výšce 220 px s `object-fit:contain` vytvářela postranní barevné pásy. Produktový CSS styl nyní nastavuje `width:100%;height:auto;object-fit:cover`, takže se zobrazí celý skutečný poměr fotografie bez pásů, deformace a dalšího ořezu. Změna platí jen pro Hair Serum.

Testy: 390 / 792 / 1440 px, světlý a tmavý vzhled, všech šest dialogů — 36 průchodů. Ověřeny levé/pravé hrany a výška podle přirozeného poměru každé fotografie, otevření/zavření, nulové chyby JS a aktuální samostatný offline náhled. Izolovaný Chromium test není uložením do CMS. Fotografie, texty, skripty a sdílený framework beze změny; v HTML změněn pouze cache parametr produktového CSS.

Před/po: before-desktop.png a after-792-light.png; mobil: after-390-light.png. Model gpt-6.1-sol; bez nové generace médií. Git oprava není živé Shoptet nasazení.
