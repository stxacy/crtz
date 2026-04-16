#!/usr/bin/env python3
"""Patch index.html: add data-href to all cards, update images for row 5+."""

INDEX = "C:/Users/vikra/Project Ai/crtz/index.html"

with open(INDEX, "r", encoding="utf-8") as f:
    html = f.read()

# ── Ordered list of all cards: (slug, update_image)
# update_image=True for row 5+ products (webp from products folder)
CARDS = [
    # Row 1
    ("island-puff-zip-hoodie-black",  False),  # already has data-href
    ("island-puff-zip-hoodie-grey",   False),
    ("island-puff-sweatpant-black",   False),
    ("island-puff-sweatpant-grey",    False),
    ("island-sweatshort-black",       False),
    ("island-sweatshort-grey",        False),
    # Row 2
    ("mini-island-zip-black",         False),
    ("mini-island-zip-grey",          False),
    ("mini-island-sweatpant-black",   False),
    ("mini-island-sweatpant-grey",    False),
    ("mini-island-crewneck-black",    False),
    ("mini-island-crewneck-grey",     False),
    # Row 5+ (update images)
    ("hmp-thermal-zip-black",         True),
    ("hmp-thermal-zip-grey",          True),
    ("hmp-v2-sweatshirt-black",       True),
    ("hmp-v2-sweatshirt-grey",        True),
    ("hmp-sweatpant-black",           True),
    ("hmp-sweatpant-grey",            True),
    ("hmp-v2-sweatpant-black",        True),
    ("hmp-v2-sweatpant-grey",         True),
    ("hmp-tank-black",                True),
    ("hmp-tank-white",                True),
    ("alcatraz-hoodie-black",         True),
    ("alcatraz-hoodie-bw",            True),
    ("alcatraz-sweatpant-black",      True),
    ("alcatraz-cargo-black",          True),
    ("bolo-down-jacket-black",        True),
    ("guerillaz-cargo-pant-black",    True),
    ("guerillaz-cargo-short-black",   True),
    ("guerillaz-thermal-tee-black",   True),
    ("guerillaz-thermal-tee-cream",   True),
    ("island-thermal-black",          True),
    ("island-thermal-cream",          True),
    ("royale-ls-black",               True),
    ("royale-ls-grey",                True),
    ("royale-heavyweight-black",      True),
    ("royale-heavyweight-white",      True),
    ("og-island-ls-black",            True),
    ("og-island-ls-white",            True),
    ("og-island-ls-grey",             True),
    ("og-island-tee-black",           True),
    ("og-island-tee-white",           True),
    ("og-island-tee-grey",            True),
    ("reminder-tee-black",            True),
    ("reminder-tee-white",            True),
    ("wmns-alcatraz-top-bw",          True),
    ("wmns-alcatraz-top-wb",          True),
    ("island-trucker-hat-black",      True),
    ("liteworky-cap-black",           True),
    ("island-duffle-black",           True),
    ("island-card-holder-black",      True),
    ("boxers-alcatraz-black",         True),
    ("boxers-alcatraz-white",         True),
    ("boxers-alcatraz-grey",          True),
    ("boxers-allstarz-black",         True),
    ("boxers-allstarz-white",         True),
    ("boxers-allstarz-grey",          True),
    ("socks-black",                   True),
    ("socks-white",                   True),
    ("crib-crep-black",               True),
    ("crib-crep-white",               True),
    ("leather-gloves-black",          True),
    ("leather-gloves-white",          True),
]

# Possible old image extensions the grid cards might use
IMG_EXTS = [".png", ".jpg", ".jpeg", ".webp"]

def find_old_img_src(html, slug):
    """Find the old image src attribute for this slug's card."""
    for ext in IMG_EXTS:
        pattern = f'images/{slug}{ext}'
        if pattern in html:
            return pattern
    # For royale-heavyweight-white, the img was royale-heavyweight-grey.png (mislabeled)
    # We need to find it by context — check for known mislabels
    return None


changed = 0
for slug, update_image in CARDS:
    href = f"products/{slug}.html"

    # 1. Add data-href (skip if already present)
    if f'data-href="{href}"' in html:
        # Already has correct data-href. Only update image if needed.
        if update_image:
            old_src = find_old_img_src(html, slug)
            if old_src:
                new_src = f"images/products/{slug}/01.webp"
                if old_src != new_src and old_src in html:
                    html = html.replace(old_src, new_src, 1)
                    print(f"  img updated: {old_src} -> {new_src}")
                    changed += 1
        continue

    # 2. Find the card opening without data-href
    # Cards look like: <div class="card"><div class="card-img">
    # We want the one containing this slug's image
    old_src = find_old_img_src(html, slug)
    if old_src is None:
        print(f"  WARN: no image found for {slug}")
        continue

    # Build old card opening (no data-href)
    old_card_open = f'<div class="card"><div class="card-img"><img src="{old_src}"'

    if old_card_open not in html:
        print(f"  WARN: card pattern not found for {slug} (old_src={old_src})")
        continue

    if update_image:
        new_src = f"images/products/{slug}/01.webp"
        new_card_open = f'<div class="card" data-href="{href}"><div class="card-img"><img src="{new_src}"'
    else:
        new_card_open = f'<div class="card" data-href="{href}"><div class="card-img"><img src="{old_src}"'

    html = html.replace(old_card_open, new_card_open, 1)
    print(f"  patched: {slug}")
    changed += 1

with open(INDEX, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nDone — {changed} cards patched in index.html")
