# Mango CTA – desktop correction

User approved the phone layout but reported the desktop card was unbalanced, with the title below the image and an oversized blank right column. Corrected on both live Czech Mango variants (native IDs 464 and 467).

Desktop >=768px only: bounded left photo track (max320px), rounded inset photo, product name above the right-hand dose/package cards, price and unchanged purchase button. Restore the previously verified pre-bubble canonical image fit only on desktop; photo URLs and source identity reset remain unchanged. Phones retain their exact original bubble layout.

Only one scoped media-query block added to the first STYLE in the two long descriptions; removing those exact bytes restores the old source. No copy, short description, shared stylesheet, JS, quantity, native price or purchase logic was changed.

Preflight actual native-page CSS test: six 320/375/767px before/after CTA pixel comparisons are identical, ten desktop geometry cases at 768/820/1024/1280/1440px pass. Fresh anonymous published pages: 12 responsive scenarios and 28 ingredient/banner dialog interactions pass. Price matches each product’s own form, original purchase-button delegation verified without a cart request. Saved native fields independently read back exactly apart from the already-proven single trailing LF removal; shorts unchanged.

Cookie/chat/iframe/Heureka and fixed-cart overlays suppressed only inside QA to capture the actual component unobstructed; live widget behavior remains untouched. Screenshot reference: user img_d6356a3975a0.png. Sources: brand/RULES.md and Git revision23c350ade7e39f46093e0452ab505d1f3f3354c8. No paid image generation; model gpt-6.1-sol, runtime cost not quantified. Previous content-claim and weight discrepancies remain unchanged.
