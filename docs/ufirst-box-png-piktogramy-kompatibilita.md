# UFIRST dárkový box — PNG piktogramy místo SVG data URI

Na výslovný Pavlův pokyn je použitý stejný postup jako u ověřených piktogramů Longevity: šest existujících linkových SVG je převedených do skutečných transparentních PNG 512 × 512 RGBA. Zachované jsou původní křivky, síla a zaoblení linky i tyrkysové téma; nejde o redesign nebo změnu popisků. SVG mastery zůstávají v `assets/ufirst-giftbox-line-icons/`, vedle nových souborů `.png`.

Aktualizované čtyři existující české soubory:
- `shoptet/ufirst.html`
- `shoptet/ufirst-kratky.html`
- `web/Golden Life Darkovy box UFIRST/Golden_Life_Darkovy_box_UFIRST_cz.html`
- `web/Golden Life Darkovy box UFIRST/maly/Golden-Life-Darkovy-box-UFIRST-maly-cz.html`

Mění se pouze IMG zdroje šesti ikon a stejné zdroje jejich CSS alpha masek: SVG data URI jsou nahrazené immutable HTTPS PNG odkazy z GitHub Raw, připnutými k ověřenému asset commitu `0fbf052c9ee9bfc26a4112c763e66d17ee806143`. Texty, popisky, ceny, SEO, STYLE, SCRIPT, produktové fotografie, detailové čtečky, galerie i obsluha košíku jsou bajtově stejné. Reverzní test po vrácení šesti obrazových zdrojů vrací přesné původní HTML. Ostatní boxy a původní již fungující Longevity se neměnily.

## Skutečné ověření

- Všech šest PNG má správný PNG formát, rozměry 512 × 512, RGBA, transparentní pozadí a neprázdný objekt uvnitř plátna bez ořezu.
- Každá ze šesti skutečných veřejných adres: HTTP 200, MIME `image/png`, CORS `*`, bajtová shoda s lokálním PNG.
- Všechna čtyři HTML otestována v Chromium na 1280 a 390 px. Přímé požadavky na skutečné veřejné PNG; vždy šest dekódovaných obrázků a skutečně namalované tyrkysové pixely ve všech šesti maskách. Žádné přetékání bloku a žádná zachycená JS chyba izolovaného testu.
- Mobilní náhled dlouhého ikonového bloku a krátkého popisu byl skutečně vizuálně prohlédnut. Původní šestice: 85+ složek, 30 sáčků, 3 příchutě, Rostlinné kapsle, Láhev UFIRST, USB-C míchátko.
- Výsledky: `tests/ufirst-box-png-piktogramy-kompatibilita.json`.

**Jen Git podklad.** Živý Shoptet ani nativní upload dialog se v tomto kroku neukládal a netestoval. Jde o izolované komponentové testy s reálnými veřejnými PNG, ne o nové tvrzení, že je změna už nasazená na obchodě. Uživatel v tomto vlákně potvrdil fungování předchozí stejné opravy Longevity; to samo není ověřením aktuálního živého UFIRST.

Zdroje: aktuální zadání a potvrzení Longevity v tomto vlákně, čerstvý Git snapshot `387cd2ecfe8cb79f0987f23e74b7b6b5f6763031`, šest skutečných SVG masterů, existující čtyři UFIRST HTML, `brand/RULES.md`, `brand/ufirst/creative-memory.md` a README dodaného manuálu. Barevná pravidla ani kreativní směr se nemění.

Model `gpt-6.1-sol`. Převod a testy pomocí Chromium/Pillow, bez placeného obrazového/video generování. Cenu jazykového běhu ani případné konektorové účtování rozhraní neposkytuje. Předchozí zdravotně-obsahové výhrady z dokumentace UFIRST zůstávají beze změny; technická oprava ikon nepředstavuje schválení účinkových textů.
