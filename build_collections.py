#!/usr/bin/env python3
"""Generate CRTZ collection pages at collections/[slug].html"""

import os

COLLECTIONS_DIR = "C:/Users/vikra/Project Ai/crtz/collections"
os.makedirs(COLLECTIONS_DIR, exist_ok=True)

# ── Full product catalog ─────────────────────────────────────────────────────
# (slug, img_src_from_index, display_name, price, categories)
# img_src is relative to index.html — we'll prefix ../ for collection pages
CATALOG = [
    # Island Puff — images still png (rows 1-4)
    ("island-puff-zip-hoodie-black", "images/island-puff-zip-hoodie-black.png",
     "Island Puff Print Zip Hoodie [Black]",      "£119.00", ["sweatshirts","classic"]),
    ("island-puff-zip-hoodie-grey",  "images/island-puff-zip-hoodie-grey.png",
     "Island Puff Print Zip Hoodie [Heather Grey]","£119.00", ["sweatshirts","classic"]),
    ("island-puff-sweatpant-black",  "images/island-puff-sweatpant-black.png",
     "Island Puff Open Hem Sweatpant [Black]",     "£95.00",  ["bottoms","classic"]),
    ("island-puff-sweatpant-grey",   "images/island-puff-sweatpant-grey.png",
     "Island Puff Open Hem Sweatpant [Heather Grey]","£95.00",["bottoms","classic"]),
    ("island-sweatshort-black",      "images/island-sweatshort-black.png",
     "Island Puff Sweatshort [Black]",             "£65.00",  ["shorts","classic"]),
    ("island-sweatshort-grey",       "images/island-sweatshort-grey.png",
     "Island Puff Sweatshort [Heather Grey]",      "£65.00",  ["shorts","classic"]),
    # Mini Island
    ("mini-island-zip-black",        "images/mini-island-zip-black.png",
     "Mini Island Zip Hood [Black]",               "£119.00", ["sweatshirts"]),
    ("mini-island-zip-grey",         "images/mini-island-zip-grey.png",
     "Mini Island Zip Hood [Heather Grey]",        "£119.00", ["sweatshirts"]),
    ("mini-island-sweatpant-black",  "images/mini-island-sweatpant-black.png",
     "Mini Island Sweatpant [Black]",              "£85.00",  ["bottoms"]),
    ("mini-island-sweatpant-grey",   "images/mini-island-sweatpant-grey.png",
     "Mini Island Sweatpant [Heather Grey]",       "£85.00",  ["bottoms"]),
    ("mini-island-crewneck-black",   "images/mini-island-crewneck-black.png",
     "Mini Island Crewneck [Black]",               "£95.00",  ["sweatshirts"]),
    ("mini-island-crewneck-grey",    "images/mini-island-crewneck-grey.png",
     "Mini Island Crewneck [Heather Grey]",        "£95.00",  ["sweatshirts"]),
    # HMP — webp (row 5+)
    ("hmp-thermal-zip-black",        "images/products/hmp-thermal-zip-black/01.webp",
     "HMP Thermal Zip Hood [Black]",               "£119.00", ["sweatshirts","tops"]),
    ("hmp-thermal-zip-grey",         "images/products/hmp-thermal-zip-grey/01.webp",
     "HMP Thermal Zip Hood [Heather Grey]",        "£119.00", ["sweatshirts","tops"]),
    ("hmp-v2-sweatshirt-black",      "images/products/hmp-v2-sweatshirt-black/01.webp",
     "HMP V2 Sweatshirt [Black]",                  "£95.00",  ["sweatshirts"]),
    ("hmp-v2-sweatshirt-grey",       "images/products/hmp-v2-sweatshirt-grey/01.webp",
     "HMP V2 Sweatshirt [Heather Grey]",           "£95.00",  ["sweatshirts"]),
    ("hmp-sweatpant-black",          "images/products/hmp-sweatpant-black/01.webp",
     "HMP Open Hem Sweatpant [Black]",             "£85.00",  ["bottoms"]),
    ("hmp-sweatpant-grey",           "images/products/hmp-sweatpant-grey/01.webp",
     "HMP Open Hem Sweatpant [Heather Grey]",      "£85.00",  ["bottoms"]),
    ("hmp-v2-sweatpant-black",       "images/products/hmp-v2-sweatpant-black/01.webp",
     "HMP V2 Sweatpant [Black]",                   "£85.00",  ["bottoms"]),
    ("hmp-v2-sweatpant-grey",        "images/products/hmp-v2-sweatpant-grey/01.webp",
     "HMP V2 Sweatpant [Heather Grey]",            "£85.00",  ["bottoms"]),
    ("hmp-tank-black",               "images/products/hmp-tank-black/01.webp",
     "HMP Essentials Tank Top [Black 3-Pack]",     "£35.00",  ["tops","classic"]),
    ("hmp-tank-white",               "images/products/hmp-tank-white/01.webp",
     "HMP Essentials Tank Top [White 3-Pack]",     "£35.00",  ["tops","classic"]),
    # Alcatraz
    ("alcatraz-hoodie-black",        "images/products/alcatraz-hoodie-black/01.webp",
     "Alcatraz Hood [Triple Black]",               "£145.00", ["sweatshirts"]),
    ("alcatraz-hoodie-bw",           "images/products/alcatraz-hoodie-bw/01.webp",
     "Alcatraz Hood [Black]",                      "£145.00", ["sweatshirts"]),
    ("alcatraz-sweatpant-black",     "images/products/alcatraz-sweatpant-black/01.webp",
     "Alcatraz Sweatpant [Triple Black]",          "£110.00", ["bottoms"]),
    ("alcatraz-cargo-black",         "images/products/alcatraz-cargo-black/01.webp",
     "Alcatraz Cargo Pant [Black]",                "£119.00", ["bottoms"]),
    ("bolo-down-jacket-black",       "images/products/bolo-down-jacket-black/01.webp",
     "Bolo Down Jacket [Triple Black]",            "£195.00", ["jackets","tops"]),
    # Guerillaz
    ("guerillaz-cargo-pant-black",   "images/products/guerillaz-cargo-pant-black/01.webp",
     "Guerillaz Cargo Pant [Black]",               "£110.00", ["bottoms"]),
    ("guerillaz-cargo-short-black",  "images/products/guerillaz-cargo-short-black/01.webp",
     "Guerillaz Cargo Short [Black]",              "£75.00",  ["shorts"]),
    ("guerillaz-thermal-tee-black",  "images/products/guerillaz-thermal-tee-black/01.webp",
     "Guerillaz Thermal LS Tee [Black]",           "£65.00",  ["tops"]),
    ("guerillaz-thermal-tee-cream",  "images/products/guerillaz-thermal-tee-cream/01.webp",
     "Guerillaz Thermal LS Tee [Cream]",           "£65.00",  ["tops"]),
    # Island Thermal
    ("island-thermal-black",         "images/products/island-thermal-black/01.webp",
     "Island Waffle Thermal [Black]",              "£75.00",  ["tops"]),
    ("island-thermal-cream",         "images/products/island-thermal-cream/01.webp",
     "Island Waffle Thermal [Cream]",              "£75.00",  ["tops"]),
    # Royale
    ("royale-ls-black",              "images/products/royale-ls-black/01.webp",
     "Royale Heavyweight Tee LS [Black]",          "£65.00",  ["tops","classic"]),
    ("royale-ls-grey",               "images/products/royale-ls-grey/01.webp",
     "Royale Heavyweight Tee LS [Grey]",           "£65.00",  ["tops","classic"]),
    ("royale-heavyweight-black",     "images/products/royale-heavyweight-black/01.webp",
     "Royale Heavyweight Tee [Black]",             "£55.00",  ["t-shirts","classic"]),
    ("royale-heavyweight-white",     "images/products/royale-heavyweight-white/01.webp",
     "Royale Heavyweight Tee [White]",             "£55.00",  ["t-shirts","classic"]),
    # OG Island
    ("og-island-ls-black",           "images/products/og-island-ls-black/01.webp",
     "OG Island LS Tee [Black]",                   "£65.00",  ["tops","classic"]),
    ("og-island-ls-white",           "images/products/og-island-ls-white/01.webp",
     "OG Island LS Tee [White]",                   "£65.00",  ["tops","classic"]),
    ("og-island-ls-grey",            "images/products/og-island-ls-grey/01.webp",
     "OG Island LS Tee [Grey]",                    "£65.00",  ["tops","classic"]),
    ("og-island-tee-black",          "images/products/og-island-tee-black/01.webp",
     "OG Island Tee [Black]",                      "£55.00",  ["t-shirts","classic"]),
    ("og-island-tee-white",          "images/products/og-island-tee-white/01.webp",
     "OG Island Tee [White]",                      "£55.00",  ["t-shirts","classic"]),
    ("og-island-tee-grey",           "images/products/og-island-tee-grey/01.webp",
     "OG Island Tee [Grey]",                       "£55.00",  ["t-shirts","classic"]),
    # Reminder
    ("reminder-tee-black",           "images/products/reminder-tee-black/01.webp",
     "Reminder Tee [Black]",                       "£55.00",  ["t-shirts"]),
    ("reminder-tee-white",           "images/products/reminder-tee-white/01.webp",
     "Reminder Tee [White]",                       "£55.00",  ["t-shirts"]),
    # Womens
    ("wmns-alcatraz-top-bw",         "images/products/wmns-alcatraz-top-bw/01.webp",
     "Wmns Alcatraz Baby Top [Black]",             "£65.00",  ["tops","womens","t-shirts"]),
    ("wmns-alcatraz-top-wb",         "images/products/wmns-alcatraz-top-wb/01.webp",
     "Wmns Alcatraz Baby Top [White]",             "£65.00",  ["tops","womens","t-shirts"]),
    # Hats
    ("island-trucker-hat-black",     "images/products/island-trucker-hat-black/01.webp",
     "Island Puff Print Trucker [Black]",          "£35.00",  ["hats"]),
    ("liteworky-cap-black",          "images/products/liteworky-cap-black/01.webp",
     "Liteworky Cap [Black]",                      "£35.00",  ["hats"]),
    # Bags
    ("island-duffle-black",          "images/products/island-duffle-black/01.webp",
     "Island Duffle Bag [Black]",                  "£85.00",  ["bags"]),
    ("island-card-holder-black",     "images/products/island-card-holder-black/01.webp",
     "Island Leather Card Holder [Black]",         "£45.00",  ["bags","accessories"]),
    # Boxers
    ("boxers-alcatraz-black",        "images/products/boxers-alcatraz-black/01.webp",
     "Alcatraz Boxers [Black 3-Pack]",             "£35.00",  ["accessories"]),
    ("boxers-alcatraz-white",        "images/products/boxers-alcatraz-white/01.webp",
     "Alcatraz Boxers [White 3-Pack]",             "£35.00",  ["accessories"]),
    ("boxers-alcatraz-grey",         "images/products/boxers-alcatraz-grey/01.webp",
     "Alcatraz Boxers [Grey 3-Pack]",              "£35.00",  ["accessories"]),
    ("boxers-allstarz-black",        "images/products/boxers-allstarz-black/01.webp",
     "Allstarz Boxers [Black 3-Pack]",             "£35.00",  ["accessories"]),
    ("boxers-allstarz-white",        "images/products/boxers-allstarz-white/01.webp",
     "Allstarz Boxers [White 3-Pack]",             "£35.00",  ["accessories"]),
    ("boxers-allstarz-grey",         "images/products/boxers-allstarz-grey/01.webp",
     "Allstarz Boxers [Grey 3-Pack]",              "£35.00",  ["accessories"]),
    # Socks
    ("socks-black",                  "images/products/socks-black/01.webp",
     "Alcatraz Socks [Black 2-Pack]",              "£18.00",  ["accessories"]),
    ("socks-white",                  "images/products/socks-white/01.webp",
     "Alcatraz Socks [White 2-Pack]",              "£18.00",  ["accessories"]),
    # Footwear
    ("crib-crep-black",              "images/products/crib-crep-black/01.webp",
     "Crib Crep [Black]",                          "£120.00", ["accessories"]),
    ("crib-crep-white",              "images/products/crib-crep-white/01.webp",
     "Crib Crep [White]",                          "£120.00", ["accessories"]),
    # Gloves
    ("leather-gloves-black",         "images/products/leather-gloves-black/01.webp",
     "Leather Gloves [Black]",                     "£65.00",  ["accessories"]),
    ("leather-gloves-white",         "images/products/leather-gloves-white/01.webp",
     "Leather Gloves [White]",                     "£65.00",  ["accessories"]),
]

# ── Collections to generate ───────────────────────────────────────────────────
COLLECTIONS = [
    ("classic",      "Classic"),
    ("t-shirts",     "T-Shirts"),
    ("tops",         "Tops / Jackets"),
    ("sweatshirts",  "Sweatshirts"),
    ("jackets",      "Jackets"),
    ("bottoms",      "Bottoms"),
    ("shorts",       "Shorts"),
    ("hats",         "Hats"),
    ("bags",         "Bags"),
    ("accessories",  "Accessories"),
    ("womens",       "Womens"),
]

# Sidebar nav items — same order as the site
NAV = [
    ("all",         "All",           "../index.html"),
    ("classic",     "Classic",       "classic.html"),
    ("cords",       "Cords",         None),         # no products, disabled
    ("t-shirts",    "T-Shirts",      "t-shirts.html"),
    ("tops",        "Tops / Jackets","tops.html"),
    ("sweatshirts", "Sweatshirts",   "sweatshirts.html"),
    ("jackets",     "Jackets",       "jackets.html"),
    ("shirts",      "Shirts",        None),          # no products, disabled
    ("bottoms",     "Bottoms",       "bottoms.html"),
    ("shorts",      "Shorts",        "shorts.html"),
    ("hats",        "Hats",          "hats.html"),
    ("bags",        "Bags",          "bags.html"),
    ("accessories", "Accessories",   "accessories.html"),
    ("womens",      "Womens",        "womens.html"),
]

# ── Build nav HTML for a given active slug ────────────────────────────────────
def build_nav(active_slug):
    items = []
    for slug, label, href in NAV:
        active = ' class="active"' if slug == active_slug else ''
        if href:
            items.append(f'          <li><a href="{href}"{active}>{label}</a></li>')
        else:
            items.append(f'          <li><a href="#" style="opacity:0.25;pointer-events:none">{label}</a></li>')
    return "\n".join(items)

# ── Build card HTML for a product (from collections/ folder, so prefix ../) ──
def build_card(slug, img_src, name, price):
    img = "../" + img_src        # collections/ is one level deeper
    href = f"../products/{slug}.html"
    alt = name.replace('"', "'")
    return (
        f'        <div class="card" data-href="{href}">'
        f'<div class="card-img"><img src="{img}" alt="{alt}" loading="lazy"></div>'
        f'<div class="card-info"><p class="card-name">{name}</p>'
        f'<p class="card-price">{price}</p></div></div>'
    )

# ── Page template ─────────────────────────────────────────────────────────────
def build_page(cat_slug, cat_label, cards_html, count):
    nav_html = build_nav(cat_slug)
    empty_msg = ''
    if not cards_html:
        empty_msg = '<p class="collection-empty">No products found.</p>'
        cards_html = ''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cat_label} — CRTZ</title>
  <link rel="stylesheet" href="../design-system.css">
  <link href="https://fonts.googleapis.com/css2?family=Karla:wght@400;700;800&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    html, body {{
      height: 100%;
      font-family: var(--font-body);
      background: var(--color-black);
      color: var(--color-yellow);
      cursor: none;
    }}

    .cursor {{
      position: fixed; width: 7px; height: 7px;
      background: var(--color-white); border-radius: 50%;
      pointer-events: none; z-index: 999999;
      transform: translate(-50%, -50%);
    }}

    /* ─── Shell ─── */
    .shell {{
      display: grid;
      grid-template-columns: 162px 1fr;
      min-height: 100vh;
    }}

    /* ─── Sidebar ─── */
    .sidebar {{
      background: var(--color-black);
      border-right: 1px solid rgba(255,255,255,0.05);
      height: 100vh;
      position: sticky;
      top: 0;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    .sidebar-brand {{
      padding: 18px 14px 14px;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 900px;
    }}

    .sidebar-brand img {{
      width: 100px;
      height: auto;
      display: block;
      transform: scale(1.18);
      clip-path: ellipse(42% 44% at 50% 50%);
      animation: spin3d 12s linear infinite, splashGlow 3s ease-in-out infinite alternate;
    }}

    @keyframes spin3d {{
      from {{ transform: rotateY(0deg) rotateX(6deg); }}
      to   {{ transform: rotateY(360deg) rotateX(6deg); }}
    }}

    @keyframes splashGlow {{
      from {{ filter: drop-shadow(0 0 30px rgba(255,213,0,0.25)); }}
      to   {{ filter: drop-shadow(0 0 70px rgba(255,213,0,0.6)); }}
    }}

    .sidebar-nav {{
      flex: 1;
      overflow-y: auto;
      padding: 10px 0;
      scrollbar-width: none;
    }}

    .sidebar-nav::-webkit-scrollbar {{ display: none; }}
    .sidebar-nav ul {{ list-style: none; }}

    .sidebar-nav a {{
      display: block;
      padding: 6px 14px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.45);
      text-decoration: none;
      transition: color 0.12s;
      cursor: none;
      white-space: nowrap;
    }}

    .sidebar-nav a:hover {{ color: rgba(255,213,0,0.85); }}
    .sidebar-nav a.active {{ color: var(--color-yellow); }}

    .sidebar-foot {{
      flex-shrink: 0;
      border-top: 1px solid rgba(255,255,255,0.05);
      padding: 14px 14px 20px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .sidebar-foot-icon {{
      margin-bottom: 10px;
      display: block;
      cursor: none;
    }}

    .sidebar-foot-icon svg {{
      height: 22px; width: 22px;
      color: rgba(255,213,0,0.35);
      transition: color 0.12s;
    }}

    .sidebar-foot-icon:hover svg {{ color: rgba(255,213,0,0.75); }}

    .sidebar-foot a {{
      display: block;
      font-size: 10px; font-weight: 700;
      letter-spacing: 0.08em; text-transform: uppercase;
      color: rgba(255,213,0,0.3); text-decoration: none;
      padding: 3px 0; transition: color 0.12s; cursor: none;
    }}

    .sidebar-foot a:hover {{ color: rgba(255,213,0,0.75); }}

    /* ─── Main ─── */
    .main {{
      height: 100vh;
      overflow-y: auto;
      scrollbar-width: thin;
      scrollbar-color: rgba(255,255,255,0.08) transparent;
    }}

    .main::-webkit-scrollbar {{ width: 4px; }}
    .main::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,0.08); border-radius: 2px; }}

    /* ─── Header bar ─── */
    .main-header {{
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 28px;
      padding: 13px 18px;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      position: sticky;
      top: 0;
      background: var(--color-black);
      z-index: var(--z-sticky);
    }}

    .search-wrap {{
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 1px solid rgba(255,213,0,0.25);
      padding-bottom: 2px;
    }}

    .search-wrap svg {{ color: rgba(255,213,0,0.5); flex-shrink: 0; }}

    .search-wrap input {{
      background: transparent; border: none; outline: none;
      font-family: var(--font-body); font-size: 11px; font-weight: 700;
      letter-spacing: 0.18em; text-transform: uppercase;
      color: rgba(255,213,0,0.5); width: 90px; cursor: none;
    }}

    .search-wrap input::placeholder {{ color: rgba(255,213,0,0.35); }}
    .search-wrap:focus-within svg   {{ color: rgba(255,213,0,0.8); }}
    .search-wrap:focus-within       {{ border-color: rgba(255,213,0,0.5); }}
    .search-wrap input:focus        {{ color: var(--color-yellow); }}

    .header-btn {{
      display: flex; align-items: center; gap: 7px;
      background: none; border: none;
      font-family: var(--font-body); font-size: 11px; font-weight: 700;
      letter-spacing: 0.18em; text-transform: uppercase;
      color: rgba(255,213,0,0.5); cursor: none; padding: 0;
      transition: color 0.12s;
    }}

    .header-btn:hover {{ color: var(--color-yellow); }}
    .header-checkout  {{ color: rgba(255,213,0,0.35); }}

    /* ─── Collection heading ─── */
    .collection-head {{
      padding: 28px 20px 18px;
      border-bottom: 1px solid rgba(255,255,255,0.04);
      display: flex;
      align-items: baseline;
      gap: 14px;
    }}

    .collection-title {{
      font-size: 18px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--color-yellow);
    }}

    .collection-count {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.3);
    }}

    .collection-empty {{
      padding: 60px 20px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.25);
    }}

    /* ─── Grid ─── */
    .grid-wrap {{ padding: 18px; }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2px;
    }}

    /* ─── Cards ─── */
    .card {{
      position: relative;
      cursor: none;
    }}

    .card-img {{
      aspect-ratio: 1 / 1;
      background: var(--color-black);
      overflow: hidden;
      position: relative;
    }}

    .card-img img {{
      width: 85%;
      height: 85%;
      object-fit: contain;
      display: block;
      margin: auto;
      transition: transform 0.4s ease;
    }}

    .card:hover .card-img img {{ transform: scale(1.04); }}

    .card-add-overlay {{
      position: absolute; inset: 0;
      display: flex; align-items: flex-end;
      justify-content: center;
      padding-bottom: 10px;
      opacity: 0;
      transition: opacity 0.2s;
    }}

    .card:hover .card-add-overlay {{ opacity: 1; }}

    .card-add-label {{
      font-size: 9px; font-weight: 700;
      letter-spacing: 0.18em; text-transform: uppercase;
      background: var(--color-yellow);
      color: var(--color-black);
      padding: 5px 12px;
    }}

    .card-info {{
      padding: 8px 0 18px;
    }}

    .card-name {{
      font-size: 11px; font-weight: 700;
      letter-spacing: 0.06em; text-transform: uppercase;
      color: rgba(255,213,0,0.85);
      line-height: 1.35;
      margin-bottom: 3px;
    }}

    .card-price {{
      font-size: 11px; font-weight: 400;
      color: rgba(255,213,0,0.4);
      letter-spacing: 0.02em;
    }}

    /* ─── Cart drawer ─── */
    .cart-drawer {{
      position: fixed; top: 0; right: 0;
      width: 320px; height: 100vh;
      background: #0a0a0a;
      border-left: 1px solid rgba(255,255,255,0.06);
      z-index: var(--z-drawer);
      display: flex; flex-direction: column;
      transform: translateX(100%);
      transition: transform 0.3s ease;
    }}

    .cart-drawer.open {{ transform: translateX(0); }}

    .cart-drawer-head {{
      display: flex; align-items: center;
      justify-content: space-between;
      padding: 16px 18px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      flex-shrink: 0;
    }}

    .cart-drawer-head span {{
      font-size: 11px; font-weight: 700;
      letter-spacing: 0.2em; text-transform: uppercase;
      color: var(--color-yellow);
    }}

    .cart-close {{
      background: none; border: none;
      color: rgba(255,213,0,0.4);
      font-size: 16px; cursor: none; padding: 0;
      transition: color 0.12s; line-height: 1;
    }}

    .cart-close:hover {{ color: var(--color-yellow); }}

    .cart-list {{
      flex: 1; overflow-y: auto;
      padding: 12px 0; scrollbar-width: none;
    }}

    .cart-list::-webkit-scrollbar {{ display: none; }}

    .cart-empty {{
      font-size: 11px; font-weight: 700;
      letter-spacing: 0.1em; text-transform: uppercase;
      color: rgba(255,213,0,0.25);
      padding: 24px 18px;
    }}

    .cart-item {{
      display: flex; gap: 12px;
      padding: 12px 18px;
      border-bottom: 1px solid rgba(255,255,255,0.04);
    }}

    .cart-item img {{
      width: 64px; height: 64px;
      object-fit: contain; background: transparent; flex-shrink: 0;
    }}

    .cart-item-info {{ flex: 1; min-width: 0; }}

    .cart-item-name {{
      font-size: 10px; font-weight: 700;
      letter-spacing: 0.06em; text-transform: uppercase;
      color: rgba(255,213,0,0.8);
      margin-bottom: 3px; line-height: 1.35;
    }}

    .cart-item-price {{
      font-size: 10px; color: rgba(255,213,0,0.4); margin-bottom: 8px;
    }}

    .cart-item-qty {{
      display: flex; align-items: center; gap: 10px;
    }}

    .cart-item-qty button {{
      background: none; border: 1px solid rgba(255,213,0,0.2);
      color: rgba(255,213,0,0.6); width: 20px; height: 20px;
      font-size: 13px; line-height: 1; cursor: none;
      transition: border-color 0.12s, color 0.12s;
      display: flex; align-items: center; justify-content: center;
    }}

    .cart-item-qty button:hover {{ border-color: var(--color-yellow); color: var(--color-yellow); }}

    .cart-item-qty span {{
      font-size: 11px; font-weight: 700;
      color: var(--color-yellow); min-width: 16px; text-align: center;
    }}

    .cart-drawer-foot {{
      flex-shrink: 0;
      border-top: 1px solid rgba(255,255,255,0.06);
      padding: 16px 18px 20px;
    }}

    .cart-total {{
      font-size: 11px; font-weight: 700;
      letter-spacing: 0.15em; text-transform: uppercase;
      color: rgba(255,213,0,0.6); margin-bottom: 14px;
    }}

    .cart-total span {{ color: var(--color-yellow); }}

    .cart-checkout-btn {{
      width: 100%; height: 44px;
      background: var(--color-yellow); color: var(--color-black);
      border: none; font-family: var(--font-body);
      font-size: 11px; font-weight: 700;
      letter-spacing: 0.18em; text-transform: uppercase;
      cursor: none; transition: opacity 0.12s;
    }}

    .cart-checkout-btn:hover {{ opacity: 0.85; }}

    .cart-overlay {{
      position: fixed; inset: 0;
      z-index: var(--z-overlay); display: none;
    }}

    .cart-overlay.open {{ display: block; }}

    /* ─── Mobile ─── */
    @media (max-width: 749px) {{
      .shell {{ grid-template-columns: 1fr; }}
      .sidebar {{
        height: auto; position: static;
        flex-direction: row; overflow-x: auto;
        border-right: none;
        border-bottom: 1px solid rgba(255,255,255,0.05);
      }}
      .sidebar-brand {{ border-bottom: none; border-right: 1px solid rgba(255,255,255,0.05); padding: 12px; }}
      .sidebar-nav {{ display: flex; flex-direction: row; padding: 0; }}
      .sidebar-nav ul {{ display: flex; }}
      .sidebar-nav a {{ padding: 14px 12px; }}
      .sidebar-foot {{ display: none; }}
      .grid {{ grid-template-columns: repeat(2, 1fr); gap: 2px; }}
      .collection-head {{ padding: 16px; }}
    }}
  </style>
</head>
<body>

  <div class="cursor" id="cursor"></div>

  <div class="shell">

    <aside class="sidebar">
      <div class="sidebar-brand">
        <a href="../index.html"><img src="../crtzlogo.png" alt="CRTZ"></a>
      </div>
      <nav class="sidebar-nav">
        <ul>
{nav_html}
        </ul>
      </nav>
      <div class="sidebar-foot">
        <a href="https://www.instagram.com/corteiz" class="sidebar-foot-icon" target="_blank" rel="noopener">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-label="Instagram">
            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
            <circle cx="12" cy="12" r="4.5"/>
            <circle cx="17.5" cy="6.5" r="0.5" fill="currentColor" stroke="none"/>
          </svg>
        </a>
        <a href="#">Archive</a>
        <a href="#">Newsletter</a>
        <a href="#">Shipping Policy</a>
        <a href="#">Terms of Service</a>
      </div>
    </aside>

    <main class="main">

      <header class="main-header">
        <div class="search-wrap">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="text" id="search-input" placeholder="Search">
        </div>
        <button class="header-btn" onclick="toggleCart()">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          Cart (<span id="cart-count">0</span>)
        </button>
        <button class="header-btn header-checkout">Checkout</button>
      </header>

      <div class="collection-head">
        <h1 class="collection-title">{cat_label}</h1>
        <span class="collection-count">{count} Product{"s" if count != 1 else ""}</span>
      </div>

      <div class="grid-wrap">
        <div class="grid" id="grid">
{cards_html}
        </div>
        {empty_msg}
      </div>

    </main>
  </div>

  <div class="cart-overlay" id="cart-overlay" onclick="toggleCart()"></div>

  <div class="cart-drawer" id="cart-drawer">
    <div class="cart-drawer-head">
      <span>Your Bag</span>
      <button class="cart-close" onclick="toggleCart()">✕</button>
    </div>
    <div class="cart-list" id="cart-list">
      <p class="cart-empty">Your bag is empty.</p>
    </div>
    <div class="cart-drawer-foot">
      <div class="cart-total">Total&nbsp; <span id="cart-total">£0.00</span></div>
      <button class="cart-checkout-btn">Checkout</button>
    </div>
  </div>

  <script>
    /* Cursor */
    const cur = document.getElementById('cursor');
    document.addEventListener('mousemove', e => {{
      cur.style.left = e.clientX + 'px';
      cur.style.top  = e.clientY + 'px';
    }});

    /* Cart */
    const cart = [];

    function toggleCart() {{
      document.getElementById('cart-drawer').classList.toggle('open');
      document.getElementById('cart-overlay').classList.toggle('open');
    }}

    function adjustQty(name, delta) {{
      const idx = cart.findIndex(i => i.name === name);
      if (idx === -1) return;
      cart[idx].qty += delta;
      if (cart[idx].qty <= 0) cart.splice(idx, 1);
      renderCart();
    }}

    function renderCart() {{
      const count = cart.reduce((s, i) => s + i.qty, 0);
      document.getElementById('cart-count').textContent = count;
      const total = cart.reduce((s, i) => s + parseFloat(i.price.replace(/[^0-9.]/g, '')) * i.qty, 0);
      document.getElementById('cart-total').textContent = '£' + total.toFixed(2);
      const list = document.getElementById('cart-list');
      if (!cart.length) {{ list.innerHTML = '<p class="cart-empty">Your bag is empty.</p>'; return; }}
      list.innerHTML = cart.map(item => `
        <div class="cart-item">
          <img src="${{item.imgSrc}}" alt="${{item.name}}">
          <div class="cart-item-info">
            <p class="cart-item-name">${{item.name}}</p>
            <p class="cart-item-price">${{item.price}}</p>
            <div class="cart-item-qty">
              <button onclick="adjustQty('${{item.name.replace(/'/g, "\\\\'")}}',-1)">−</button>
              <span>${{item.qty}}</span>
              <button onclick="adjustQty('${{item.name.replace(/'/g, "\\\\'")}}'",1)">+</button>
            </div>
          </div>
        </div>
      `).join('');
    }}

    /* Wire up cards */
    document.querySelectorAll('.card').forEach(card => {{
      const overlay = document.createElement('div');
      overlay.className = 'card-add-overlay';
      overlay.innerHTML = '<span class="card-add-label">View Product</span>';
      card.querySelector('.card-img').appendChild(overlay);

      card.addEventListener('click', () => {{
        window.location.href = card.dataset.href;
      }});
    }});

    /* Search */
    document.getElementById('search-input').addEventListener('input', function() {{
      const q = this.value.toLowerCase();
      document.querySelectorAll('.card').forEach(c => {{
        const name = c.querySelector('.card-name').textContent.toLowerCase();
        c.style.display = name.includes(q) ? '' : 'none';
      }});
    }});
  </script>

</body>
</html>'''


# ── Generate each collection page ─────────────────────────────────────────────
for cat_slug, cat_label in COLLECTIONS:
    matching = [(s, img, n, p) for s, img, n, p, cats in CATALOG if cat_slug in cats]
    cards_html = "\n".join(build_card(s, img, n, p) for s, img, n, p in matching)
    count = len(matching)
    html = build_page(cat_slug, cat_label, cards_html, count)
    out = f"{COLLECTIONS_DIR}/{cat_slug}.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK {cat_slug}.html — {count} products")

print(f"\nGenerated {len(COLLECTIONS)} collection pages.")
