#!/usr/bin/env python3
"""Generate all CRTZ product pages from the island-puff-zip-hoodie-black.html template."""

import os

PRODUCTS_DIR = "C:/Users/vikra/Project Ai/crtz/products"
IMAGES_DIR = "C:/Users/vikra/Project Ai/crtz/images/products"

# ── Product definitions ─────────────────────────────────────────────────────
# Each entry: (slug, display_name, price, sizes, variants, desc_bullets, model_note)
# variants = list of (label, slug, grid_img_relative)
# grid_img_relative = path from products/ folder to the grid card thumbnail image
# (used in colour swatch: ../images/[img])

PRODUCTS = [
  {
    "slug": "island-puff-zip-hoodie-black",
    "name": "Island Puff Print Zip Hoodie<br>[Black]",
    "title": "Island Puff Print Zip Hoodie [Black]",
    "price": "£119.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "island-puff-zip-hoodie-black", "../images/island-puff-zip-hoodie-black.png"),
      ("Heather Grey", "island-puff-zip-hoodie-grey",  "../images/island-puff-zip-hoodie-grey.png"),
    ],
    "active_variant": "island-puff-zip-hoodie-black",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Puff Print Alcatraz Logo Left Chest &amp; Centre Back.",
      "Coverstitch Detailing Throughout.",
      "YKK Metal Two-Way Zipper.",
      "Ribbed Cuffs &amp; Bottom Hem.",
      "True to Size — Boxy Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "island-puff-zip-hoodie-grey",
    "name": "Island Puff Print Zip Hoodie<br>[Heather Grey]",
    "title": "Island Puff Print Zip Hoodie [Heather Grey]",
    "price": "£119.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "island-puff-zip-hoodie-black", "../images/island-puff-zip-hoodie-black.png"),
      ("Heather Grey", "island-puff-zip-hoodie-grey",  "../images/island-puff-zip-hoodie-grey.png"),
    ],
    "active_variant": "island-puff-zip-hoodie-grey",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Puff Print Alcatraz Logo Left Chest &amp; Centre Back.",
      "Coverstitch Detailing Throughout.",
      "YKK Metal Two-Way Zipper.",
      "Ribbed Cuffs &amp; Bottom Hem.",
      "True to Size — Boxy Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "island-puff-sweatpant-black",
    "name": "Island Puff Open Hem Sweatpant<br>[Black]",
    "title": "Island Puff Open Hem Sweatpant [Black]",
    "price": "£95.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "island-puff-sweatpant-black", "../images/island-puff-sweatpant-black.png"),
      ("Heather Grey", "island-puff-sweatpant-grey",  "../images/island-puff-sweatpant-grey.png"),
    ],
    "active_variant": "island-puff-sweatpant-black",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Puff Print Alcatraz Logo Left Hip.",
      "Open Hem Design.",
      "Elastic Waistband with Drawstring.",
      "Ribbed Cuffs.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "island-puff-sweatpant-grey",
    "name": "Island Open Hem Sweatpant<br>[Heather Grey]",
    "title": "Island Open Hem Sweatpant [Heather Grey]",
    "price": "£95.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "island-puff-sweatpant-black", "../images/island-puff-sweatpant-black.png"),
      ("Heather Grey", "island-puff-sweatpant-grey",  "../images/island-puff-sweatpant-grey.png"),
    ],
    "active_variant": "island-puff-sweatpant-grey",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Puff Print Alcatraz Logo Left Hip.",
      "Open Hem Design.",
      "Elastic Waistband with Drawstring.",
      "Ribbed Cuffs.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "island-sweatshort-black",
    "name": "Island Puff Sweatshort<br>[Black]",
    "title": "Island Puff Sweatshort [Black]",
    "price": "£65.00",
    "sizes": ["S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "island-sweatshort-black", "../images/island-sweatshort-black.png"),
      ("Heather Grey", "island-sweatshort-grey",  "../images/island-sweatshort-grey.png"),
    ],
    "active_variant": "island-sweatshort-black",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Puff Print Alcatraz Logo Left Hip.",
      "Elastic Waistband with Drawstring.",
      "Ribbed Hem.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "",
  },
  {
    "slug": "island-sweatshort-grey",
    "name": "Island Puff Sweatshort<br>[Heather Grey]",
    "title": "Island Puff Sweatshort [Heather Grey]",
    "price": "£65.00",
    "sizes": ["S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "island-sweatshort-black", "../images/island-sweatshort-black.png"),
      ("Heather Grey", "island-sweatshort-grey",  "../images/island-sweatshort-grey.png"),
    ],
    "active_variant": "island-sweatshort-grey",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Puff Print Alcatraz Logo Left Hip.",
      "Elastic Waistband with Drawstring.",
      "Ribbed Hem.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "",
  },
  {
    "slug": "mini-island-zip-black",
    "name": "Mini Island Zip Hood<br>[Black]",
    "title": "Mini Island Zip Hood [Black]",
    "price": "£119.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "mini-island-zip-black", "../images/mini-island-zip-black.png"),
      ("Heather Grey", "mini-island-zip-grey",  "../images/mini-island-zip-grey.png"),
    ],
    "active_variant": "mini-island-zip-black",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Mini Puff Print CRTZ Alcatraz Logo Left Chest.",
      "Coverstitch Detailing Throughout.",
      "YKK Metal Two-Way Zipper.",
      "Ribbed Cuffs &amp; Bottom Hem.",
      "True to Size — Boxy Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "mini-island-zip-grey",
    "name": "Mini Island Zip Hood<br>[Heather Grey]",
    "title": "Mini Island Zip Hood [Heather Grey]",
    "price": "£119.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "mini-island-zip-black", "../images/mini-island-zip-black.png"),
      ("Heather Grey", "mini-island-zip-grey",  "../images/mini-island-zip-grey.png"),
    ],
    "active_variant": "mini-island-zip-grey",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Mini Puff Print CRTZ Alcatraz Logo Left Chest.",
      "Coverstitch Detailing Throughout.",
      "YKK Metal Two-Way Zipper.",
      "Ribbed Cuffs &amp; Bottom Hem.",
      "True to Size — Boxy Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "mini-island-sweatpant-black",
    "name": "Mini Island Sweatpant<br>[Black]",
    "title": "Mini Island Sweatpant [Black]",
    "price": "£85.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "mini-island-sweatpant-black", "../images/mini-island-sweatpant-black.png"),
      ("Heather Grey", "mini-island-sweatpant-grey",  "../images/mini-island-sweatpant-grey.png"),
    ],
    "active_variant": "mini-island-sweatpant-black",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Mini Puff Print CRTZ Alcatraz Logo Left Hip.",
      "Elastic Waistband with Drawstring.",
      "Ribbed Cuffs.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "mini-island-sweatpant-grey",
    "name": "Mini Island Sweatpant<br>[Heather Grey]",
    "title": "Mini Island Sweatpant [Heather Grey]",
    "price": "£85.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "mini-island-sweatpant-black", "../images/mini-island-sweatpant-black.png"),
      ("Heather Grey", "mini-island-sweatpant-grey",  "../images/mini-island-sweatpant-grey.png"),
    ],
    "active_variant": "mini-island-sweatpant-grey",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Mini Puff Print CRTZ Alcatraz Logo Left Hip.",
      "Elastic Waistband with Drawstring.",
      "Ribbed Cuffs.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "mini-island-crewneck-black",
    "name": "Mini Island Crewneck<br>[Black]",
    "title": "Mini Island Crewneck [Black]",
    "price": "£95.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "mini-island-crewneck-black", "../images/mini-island-crewneck-black.png"),
      ("Heather Grey", "mini-island-crewneck-grey",  "../images/mini-island-crewneck-grey.png"),
    ],
    "active_variant": "mini-island-crewneck-black",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Mini Puff Print CRTZ Alcatraz Logo Left Chest &amp; Centre Back.",
      "Coverstitch Detailing Throughout.",
      "Ribbed Cuffs, Collar &amp; Bottom Hem.",
      "True to Size — Boxy Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "mini-island-crewneck-grey",
    "name": "Mini Island Crewneck<br>[Heather Grey]",
    "title": "Mini Island Crewneck [Heather Grey]",
    "price": "£95.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "mini-island-crewneck-black", "../images/mini-island-crewneck-black.png"),
      ("Heather Grey", "mini-island-crewneck-grey",  "../images/mini-island-crewneck-grey.png"),
    ],
    "active_variant": "mini-island-crewneck-grey",
    "desc": [
      "440GSM 100% Cotton Fleece.",
      "Mini Puff Print CRTZ Alcatraz Logo Left Chest &amp; Centre Back.",
      "Coverstitch Detailing Throughout.",
      "Ribbed Cuffs, Collar &amp; Bottom Hem.",
      "True to Size — Boxy Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  # ── Row 5+ ──────────────────────────────────────────────────────────────
  {
    "slug": "hmp-thermal-zip-black",
    "name": "HMP Thermal Zip Hood<br>[Black]",
    "title": "HMP Thermal Zip Hood [Black]",
    "price": "£119.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "hmp-thermal-zip-black", "../images/hmp-thermal-zip-black.png"),
      ("Heather Grey", "hmp-thermal-zip-grey",  "../images/hmp-thermal-zip-grey.png"),
    ],
    "active_variant": "hmp-thermal-zip-black",
    "desc": [
      "Thermal Waffle Knit Fabric.",
      "CRTZ Alcatraz Logo Left Chest Embroidery.",
      "Full-Length YKK Zip.",
      "Ribbed Cuffs &amp; Bottom Hem.",
      "Side Pockets.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "hmp-thermal-zip-grey",
    "name": "HMP Thermal Zip Hood<br>[Heather Grey]",
    "title": "HMP Thermal Zip Hood [Heather Grey]",
    "price": "£119.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "hmp-thermal-zip-black", "../images/hmp-thermal-zip-black.png"),
      ("Heather Grey", "hmp-thermal-zip-grey",  "../images/hmp-thermal-zip-grey.png"),
    ],
    "active_variant": "hmp-thermal-zip-grey",
    "desc": [
      "Thermal Waffle Knit Fabric.",
      "CRTZ Alcatraz Logo Left Chest Embroidery.",
      "Full-Length YKK Zip.",
      "Ribbed Cuffs &amp; Bottom Hem.",
      "Side Pockets.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "hmp-v2-sweatshirt-black",
    "name": "HMP V2 Sweatshirt<br>[Black]",
    "title": "HMP V2 Sweatshirt [Black]",
    "price": "£95.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "hmp-v2-sweatshirt-black", "../images/hmp-v2-sweatshirt-black.png"),
      ("Heather Grey", "hmp-v2-sweatshirt-grey",  "../images/hmp-v2-sweatshirt-grey.png"),
    ],
    "active_variant": "hmp-v2-sweatshirt-black",
    "desc": [
      "380GSM French Terry Cotton.",
      "CRTZ Alcatraz Logo Left Chest &amp; Centre Back.",
      "Coverstitch Detailing Throughout.",
      "Ribbed Cuffs, Collar &amp; Bottom Hem.",
      "True to Size — Boxy Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "hmp-v2-sweatshirt-grey",
    "name": "HMP V2 Sweatshirt<br>[Heather Grey]",
    "title": "HMP V2 Sweatshirt [Heather Grey]",
    "price": "£95.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "hmp-v2-sweatshirt-black", "../images/hmp-v2-sweatshirt-black.png"),
      ("Heather Grey", "hmp-v2-sweatshirt-grey",  "../images/hmp-v2-sweatshirt-grey.png"),
    ],
    "active_variant": "hmp-v2-sweatshirt-grey",
    "desc": [
      "380GSM French Terry Cotton.",
      "CRTZ Alcatraz Logo Left Chest &amp; Centre Back.",
      "Coverstitch Detailing Throughout.",
      "Ribbed Cuffs, Collar &amp; Bottom Hem.",
      "True to Size — Boxy Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "hmp-sweatpant-black",
    "name": "HMP Open Hem Sweatpant<br>[Black]",
    "title": "HMP Open Hem Sweatpant [Black]",
    "price": "£85.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "hmp-sweatpant-black", "../images/hmp-sweatpant-black.png"),
      ("Heather Grey", "hmp-sweatpant-grey",  "../images/hmp-sweatpant-grey.png"),
    ],
    "active_variant": "hmp-sweatpant-black",
    "desc": [
      "380GSM French Terry Cotton.",
      "CRTZ Alcatraz Logo Left Hip.",
      "Open Hem Design.",
      "Elastic Waistband with Drawstring.",
      "Side Pockets.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "hmp-sweatpant-grey",
    "name": "HMP Open Hem Sweatpant<br>[Heather Grey]",
    "title": "HMP Open Hem Sweatpant [Heather Grey]",
    "price": "£85.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "hmp-sweatpant-black", "../images/hmp-sweatpant-black.png"),
      ("Heather Grey", "hmp-sweatpant-grey",  "../images/hmp-sweatpant-grey.png"),
    ],
    "active_variant": "hmp-sweatpant-grey",
    "desc": [
      "380GSM French Terry Cotton.",
      "CRTZ Alcatraz Logo Left Hip.",
      "Open Hem Design.",
      "Elastic Waistband with Drawstring.",
      "Side Pockets.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "hmp-v2-sweatpant-black",
    "name": "HMP V2 Sweatpant<br>[Black]",
    "title": "HMP V2 Sweatpant [Black]",
    "price": "£85.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "hmp-v2-sweatpant-black", "../images/hmp-v2-sweatpant-black.png"),
      ("Heather Grey", "hmp-v2-sweatpant-grey",  "../images/hmp-v2-sweatpant-grey.png"),
    ],
    "active_variant": "hmp-v2-sweatpant-black",
    "desc": [
      "380GSM French Terry Cotton.",
      "CRTZ Alcatraz Logo Left Hip.",
      "Ribbed Cuffs.",
      "Elastic Waistband with Drawstring.",
      "Side Pockets.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "hmp-v2-sweatpant-grey",
    "name": "HMP V2 Sweatpant<br>[Heather Grey]",
    "title": "HMP V2 Sweatpant [Heather Grey]",
    "price": "£85.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black",        "hmp-v2-sweatpant-black", "../images/hmp-v2-sweatpant-black.png"),
      ("Heather Grey", "hmp-v2-sweatpant-grey",  "../images/hmp-v2-sweatpant-grey.png"),
    ],
    "active_variant": "hmp-v2-sweatpant-grey",
    "desc": [
      "380GSM French Terry Cotton.",
      "CRTZ Alcatraz Logo Left Hip.",
      "Ribbed Cuffs.",
      "Elastic Waistband with Drawstring.",
      "Side Pockets.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "hmp-tank-black",
    "name": "HMP Essentials Tank Top<br>[Black 3-Pack]",
    "title": "HMP Essentials Tank Top [Black 3-Pack]",
    "price": "£35.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "hmp-tank-black", "../images/hmp-tank-black.png"),
      ("White", "hmp-tank-white", "../images/hmp-tank-white.png"),
    ],
    "active_variant": "hmp-tank-black",
    "desc": [
      "100% Cotton Jersey.",
      "CRTZ Alcatraz Logo Left Chest.",
      "Pack of 3.",
      "Ribbed Collar.",
      "True to Size — Regular Fit.",
    ],
    "model": "",
  },
  {
    "slug": "hmp-tank-white",
    "name": "HMP Essentials Tank Top<br>[White 3-Pack]",
    "title": "HMP Essentials Tank Top [White 3-Pack]",
    "price": "£35.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "hmp-tank-black", "../images/hmp-tank-black.png"),
      ("White", "hmp-tank-white", "../images/hmp-tank-white.png"),
    ],
    "active_variant": "hmp-tank-white",
    "desc": [
      "100% Cotton Jersey.",
      "CRTZ Alcatraz Logo Left Chest.",
      "Pack of 3.",
      "Ribbed Collar.",
      "True to Size — Regular Fit.",
    ],
    "model": "",
  },
  {
    "slug": "alcatraz-hoodie-black",
    "name": "Alcatraz Hood<br>[Triple Black]",
    "title": "Alcatraz Hood [Triple Black]",
    "price": "£145.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Triple Black", "alcatraz-hoodie-black", "../images/alcatraz-hoodie-black.png"),
      ("Black/White",  "alcatraz-hoodie-bw",    "../images/alcatraz-hoodie-bw.png"),
    ],
    "active_variant": "alcatraz-hoodie-black",
    "desc": [
      "500GSM 100% Cotton Fleece.",
      "Embroidered Alcatraz Logo Left Chest &amp; Centre Back.",
      "Coverstitch Detailing Throughout.",
      "YKK Metal Zip.",
      "Ribbed Cuffs &amp; Bottom Hem.",
      "True to Size — Oversized Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "alcatraz-hoodie-bw",
    "name": "Alcatraz Hood<br>[Black]",
    "title": "Alcatraz Hood [Black]",
    "price": "£145.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Triple Black", "alcatraz-hoodie-black", "../images/alcatraz-hoodie-black.png"),
      ("Black/White",  "alcatraz-hoodie-bw",    "../images/alcatraz-hoodie-bw.png"),
    ],
    "active_variant": "alcatraz-hoodie-bw",
    "desc": [
      "500GSM 100% Cotton Fleece.",
      "Embroidered Alcatraz Logo Left Chest &amp; Centre Back.",
      "Coverstitch Detailing Throughout.",
      "YKK Metal Zip.",
      "Ribbed Cuffs &amp; Bottom Hem.",
      "True to Size — Oversized Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "alcatraz-sweatpant-black",
    "name": "Alcatraz Sweatpant<br>[Triple Black]",
    "title": "Alcatraz Sweatpant [Triple Black]",
    "price": "£110.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Triple Black", "alcatraz-sweatpant-black", "../images/alcatraz-sweatpant-black.png"),
    ],
    "active_variant": "alcatraz-sweatpant-black",
    "desc": [
      "500GSM 100% Cotton Fleece.",
      "Embroidered Alcatraz Logo Left Hip.",
      "Elastic Waistband with Drawstring.",
      "Ribbed Cuffs.",
      "Side Pockets.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "alcatraz-cargo-black",
    "name": "Alcatraz Cargo Pant<br>[Black]",
    "title": "Alcatraz Cargo Pant [Black]",
    "price": "£119.00",
    "sizes": ["28","30","32","34","36","38"],
    "variants": [
      ("Black", "alcatraz-cargo-black", "../images/alcatraz-cargo-black.png"),
    ],
    "active_variant": "alcatraz-cargo-black",
    "desc": [
      "100% Cotton Ripstop.",
      "Embroidered Alcatraz Logo.",
      "Multiple Cargo Pockets.",
      "Adjustable Waistband.",
      "Zip Fly with Button.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "",
  },
  {
    "slug": "bolo-down-jacket-black",
    "name": "Bolo Down Jacket<br>[Triple Black]",
    "title": "Bolo Down Jacket [Triple Black]",
    "price": "£195.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Triple Black", "bolo-down-jacket-black", "../images/bolo-down-jacket-black.png"),
    ],
    "active_variant": "bolo-down-jacket-black",
    "desc": [
      "80/20 Duck Down Fill.",
      "Nylon Shell.",
      "CRTZ Alcatraz Logo Embroidery.",
      "YKK Zip Throughout.",
      "Multiple Pockets.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "guerillaz-cargo-pant-black",
    "name": "Guerillaz Cargo Pant<br>[Black]",
    "title": "Guerillaz Cargo Pant [Black]",
    "price": "£110.00",
    "sizes": ["28","30","32","34","36","38"],
    "variants": [
      ("Black", "guerillaz-cargo-pant-black", "../images/guerillaz-cargo-pant-black.png"),
    ],
    "active_variant": "guerillaz-cargo-pant-black",
    "desc": [
      "100% Cotton Ripstop.",
      "CRTZ Alcatraz Logo Embroidery.",
      "Multiple Cargo Pockets.",
      "Adjustable Waistband.",
      "Zip Fly with Button.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "",
  },
  {
    "slug": "guerillaz-cargo-short-black",
    "name": "Guerillaz Cargo Short<br>[Black]",
    "title": "Guerillaz Cargo Short [Black]",
    "price": "£75.00",
    "sizes": ["28","30","32","34","36","38"],
    "variants": [
      ("Black", "guerillaz-cargo-short-black", "../images/guerillaz-cargo-short-black.png"),
    ],
    "active_variant": "guerillaz-cargo-short-black",
    "desc": [
      "100% Cotton Ripstop.",
      "CRTZ Alcatraz Logo Embroidery.",
      "Multiple Cargo Pockets.",
      "Adjustable Waistband.",
      "Zip Fly with Button.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "",
  },
  {
    "slug": "guerillaz-thermal-tee-black",
    "name": "Guerillaz Thermal LS Tee<br>[Black]",
    "title": "Guerillaz Thermal LS Tee [Black]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "guerillaz-thermal-tee-black", "../images/guerillaz-thermal-tee-black.png"),
      ("Cream", "guerillaz-thermal-tee-cream", "../images/guerillaz-thermal-tee-cream.png"),
    ],
    "active_variant": "guerillaz-thermal-tee-black",
    "desc": [
      "Thermal Waffle Knit Fabric.",
      "CRTZ Alcatraz Logo Left Chest.",
      "Long Sleeve.",
      "Ribbed Cuffs &amp; Collar.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "guerillaz-thermal-tee-cream",
    "name": "Guerillaz Thermal LS Tee<br>[Cream]",
    "title": "Guerillaz Thermal LS Tee [Cream]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "guerillaz-thermal-tee-black", "../images/guerillaz-thermal-tee-black.png"),
      ("Cream", "guerillaz-thermal-tee-cream", "../images/guerillaz-thermal-tee-cream.png"),
    ],
    "active_variant": "guerillaz-thermal-tee-cream",
    "desc": [
      "Thermal Waffle Knit Fabric.",
      "CRTZ Alcatraz Logo Left Chest.",
      "Long Sleeve.",
      "Ribbed Cuffs &amp; Collar.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "island-thermal-black",
    "name": "Island Waffle Thermal<br>[Black]",
    "title": "Island Waffle Thermal [Black]",
    "price": "£75.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "island-thermal-black", "../images/island-thermal-black.png"),
      ("Cream", "island-thermal-cream", "../images/island-thermal-cream.png"),
    ],
    "active_variant": "island-thermal-black",
    "desc": [
      "Thermal Waffle Knit Fabric.",
      "Puff Print Alcatraz Logo Left Chest.",
      "Long Sleeve.",
      "Ribbed Cuffs &amp; Collar.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "island-thermal-cream",
    "name": "Island Waffle Thermal<br>[Cream]",
    "title": "Island Waffle Thermal [Cream]",
    "price": "£75.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "island-thermal-black", "../images/island-thermal-black.png"),
      ("Cream", "island-thermal-cream", "../images/island-thermal-cream.png"),
    ],
    "active_variant": "island-thermal-cream",
    "desc": [
      "Thermal Waffle Knit Fabric.",
      "Puff Print Alcatraz Logo Left Chest.",
      "Long Sleeve.",
      "Ribbed Cuffs &amp; Collar.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "royale-ls-black",
    "name": "Royale Heavyweight Tee LS<br>[Black]",
    "title": "Royale Heavyweight Tee LS [Black]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "royale-ls-black", "../images/royale-ls-black.png"),
      ("Grey",  "royale-ls-grey",  "../images/royale-ls-grey.png"),
    ],
    "active_variant": "royale-ls-black",
    "desc": [
      "280GSM 100% Cotton.",
      "CRTZ Alcatraz Logo Left Chest.",
      "Long Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Boxy Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "royale-ls-grey",
    "name": "Royale Heavyweight Tee LS<br>[Grey]",
    "title": "Royale Heavyweight Tee LS [Grey]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "royale-ls-black", "../images/royale-ls-black.png"),
      ("Grey",  "royale-ls-grey",  "../images/royale-ls-grey.png"),
    ],
    "active_variant": "royale-ls-grey",
    "desc": [
      "280GSM 100% Cotton.",
      "CRTZ Alcatraz Logo Left Chest.",
      "Long Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Boxy Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "royale-heavyweight-black",
    "name": "Royale Heavyweight Tee<br>[Black]",
    "title": "Royale Heavyweight Tee [Black]",
    "price": "£55.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "royale-heavyweight-black", "../images/royale-heavyweight-black.png"),
      ("White", "royale-heavyweight-white", "../images/royale-heavyweight-white.png"),
    ],
    "active_variant": "royale-heavyweight-black",
    "desc": [
      "280GSM 100% Cotton.",
      "CRTZ Alcatraz Logo Left Chest.",
      "Dropped Shoulders.",
      "Short Sleeve.",
      "True to Size — Boxy Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "royale-heavyweight-white",
    "name": "Royale Heavyweight Tee<br>[White]",
    "title": "Royale Heavyweight Tee [White]",
    "price": "£55.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "royale-heavyweight-black", "../images/royale-heavyweight-black.png"),
      ("White", "royale-heavyweight-white", "../images/royale-heavyweight-white.png"),
    ],
    "active_variant": "royale-heavyweight-white",
    "desc": [
      "280GSM 100% Cotton.",
      "CRTZ Alcatraz Logo Left Chest.",
      "Dropped Shoulders.",
      "Short Sleeve.",
      "True to Size — Boxy Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "og-island-ls-black",
    "name": "OG Island LS Tee<br>[Black]",
    "title": "OG Island LS Tee [Black]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "og-island-ls-black", "../images/og-island-ls-black.png"),
      ("White", "og-island-ls-white", "../images/og-island-ls-white.png"),
      ("Grey",  "og-island-ls-grey",  "../images/og-island-ls-grey.png"),
    ],
    "active_variant": "og-island-ls-black",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "OG Island Print — Left Chest &amp; Centre Back.",
      "Long Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "og-island-ls-white",
    "name": "OG Island LS Tee<br>[White]",
    "title": "OG Island LS Tee [White]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "og-island-ls-black", "../images/og-island-ls-black.png"),
      ("White", "og-island-ls-white", "../images/og-island-ls-white.png"),
      ("Grey",  "og-island-ls-grey",  "../images/og-island-ls-grey.png"),
    ],
    "active_variant": "og-island-ls-white",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "OG Island Print — Left Chest &amp; Centre Back.",
      "Long Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "og-island-ls-grey",
    "name": "OG Island LS Tee<br>[Grey]",
    "title": "OG Island LS Tee [Grey]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "og-island-ls-black", "../images/og-island-ls-black.png"),
      ("White", "og-island-ls-white", "../images/og-island-ls-white.png"),
      ("Grey",  "og-island-ls-grey",  "../images/og-island-ls-grey.png"),
    ],
    "active_variant": "og-island-ls-grey",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "OG Island Print — Left Chest &amp; Centre Back.",
      "Long Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "og-island-tee-black",
    "name": "OG Island Tee<br>[Black]",
    "title": "OG Island Tee [Black]",
    "price": "£55.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "og-island-tee-black", "../images/og-island-tee-black.png"),
      ("White", "og-island-tee-white", "../images/og-island-tee-white.png"),
      ("Grey",  "og-island-tee-grey",  "../images/og-island-tee-grey.png"),
    ],
    "active_variant": "og-island-tee-black",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "OG Island Print — Left Chest &amp; Centre Back.",
      "Short Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "og-island-tee-white",
    "name": "OG Island Tee<br>[White]",
    "title": "OG Island Tee [White]",
    "price": "£55.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "og-island-tee-black", "../images/og-island-tee-black.png"),
      ("White", "og-island-tee-white", "../images/og-island-tee-white.png"),
      ("Grey",  "og-island-tee-grey",  "../images/og-island-tee-grey.png"),
    ],
    "active_variant": "og-island-tee-white",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "OG Island Print — Left Chest &amp; Centre Back.",
      "Short Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "og-island-tee-grey",
    "name": "OG Island Tee<br>[Grey]",
    "title": "OG Island Tee [Grey]",
    "price": "£55.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "og-island-tee-black", "../images/og-island-tee-black.png"),
      ("White", "og-island-tee-white", "../images/og-island-tee-white.png"),
      ("Grey",  "og-island-tee-grey",  "../images/og-island-tee-grey.png"),
    ],
    "active_variant": "og-island-tee-grey",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "OG Island Print — Left Chest &amp; Centre Back.",
      "Short Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "reminder-tee-black",
    "name": "Reminder Tee<br>[Black]",
    "title": "Reminder Tee [Black]",
    "price": "£55.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "reminder-tee-black", "../images/reminder-tee-black.png"),
      ("White", "reminder-tee-white", "../images/reminder-tee-white.png"),
    ],
    "active_variant": "reminder-tee-black",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "Graphic Print Front.",
      "Short Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "reminder-tee-white",
    "name": "Reminder Tee<br>[White]",
    "title": "Reminder Tee [White]",
    "price": "£55.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "reminder-tee-black", "../images/reminder-tee-black.png"),
      ("White", "reminder-tee-white", "../images/reminder-tee-white.png"),
    ],
    "active_variant": "reminder-tee-white",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "Graphic Print Front.",
      "Short Sleeve.",
      "Dropped Shoulders.",
      "True to Size — Relaxed Fit.",
    ],
    "model": "Javel is 5'9\" / 175cm wearing size Medium.",
  },
  {
    "slug": "wmns-alcatraz-top-bw",
    "name": "Wmns Alcatraz Baby Top<br>[Black]",
    "title": "Wmns Alcatraz Baby Top [Black]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL"],
    "variants": [
      ("Black", "wmns-alcatraz-top-bw", "../images/wmns-alcatraz-top-bw.png"),
      ("White", "wmns-alcatraz-top-wb", "../images/wmns-alcatraz-top-wb.png"),
    ],
    "active_variant": "wmns-alcatraz-top-bw",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "Alcatraz Logo Print.",
      "Cropped Fit.",
      "Short Sleeve.",
      "True to Size.",
    ],
    "model": "",
  },
  {
    "slug": "wmns-alcatraz-top-wb",
    "name": "Wmns Alcatraz Baby Top<br>[White]",
    "title": "Wmns Alcatraz Baby Top [White]",
    "price": "£65.00",
    "sizes": ["XS","S","M","L","XL"],
    "variants": [
      ("Black", "wmns-alcatraz-top-bw", "../images/wmns-alcatraz-top-bw.png"),
      ("White", "wmns-alcatraz-top-wb", "../images/wmns-alcatraz-top-wb.png"),
    ],
    "active_variant": "wmns-alcatraz-top-wb",
    "desc": [
      "230GSM 100% Cotton Jersey.",
      "Alcatraz Logo Print.",
      "Cropped Fit.",
      "Short Sleeve.",
      "True to Size.",
    ],
    "model": "",
  },
  {
    "slug": "island-trucker-hat-black",
    "name": "Island Puff Print Trucker<br>[Black]",
    "title": "Island Puff Print Trucker [Black]",
    "price": "£35.00",
    "sizes": ["One Size"],
    "variants": [
      ("Black", "island-trucker-hat-black", "../images/island-trucker-hat-black.png"),
    ],
    "active_variant": "island-trucker-hat-black",
    "desc": [
      "Mesh Back Panel.",
      "Puff Print Island Logo Front.",
      "Snapback Closure.",
      "Structured Crown.",
      "One Size Fits All.",
    ],
    "model": "",
  },
  {
    "slug": "liteworky-cap-black",
    "name": "Liteworky Cap<br>[Black]",
    "title": "Liteworky Cap [Black]",
    "price": "£35.00",
    "sizes": ["One Size"],
    "variants": [
      ("Black", "liteworky-cap-black", "../images/liteworky-cap-black.png"),
    ],
    "active_variant": "liteworky-cap-black",
    "desc": [
      "Lightweight Construction.",
      "CRTZ Embroidery Front.",
      "Adjustable Strap Back.",
      "Structured Crown.",
      "One Size Fits All.",
    ],
    "model": "",
  },
  {
    "slug": "island-duffle-black",
    "name": "Island Duffle Bag<br>[Black]",
    "title": "Island Duffle Bag [Black]",
    "price": "£85.00",
    "sizes": ["One Size"],
    "variants": [
      ("Black", "island-duffle-black", "../images/island-duffle-black.png"),
    ],
    "active_variant": "island-duffle-black",
    "desc": [
      "Heavy Duty Nylon.",
      "Puff Print Island Logo.",
      "Main Zip Compartment.",
      "Side &amp; End Pockets.",
      "Detachable Shoulder Strap.",
      "One Size.",
    ],
    "model": "",
  },
  {
    "slug": "island-card-holder-black",
    "name": "Island Leather Card Holder<br>[Black]",
    "title": "Island Leather Card Holder [Black]",
    "price": "£45.00",
    "sizes": ["One Size"],
    "variants": [
      ("Black", "island-card-holder-black", "../images/island-card-holder-black.png"),
    ],
    "active_variant": "island-card-holder-black",
    "desc": [
      "Genuine Leather.",
      "Embossed CRTZ Logo.",
      "Multiple Card Slots.",
      "Slim Profile.",
      "One Size.",
    ],
    "model": "",
  },
  {
    "slug": "boxers-alcatraz-black",
    "name": "Alcatraz Boxers<br>[Black 3-Pack]",
    "title": "Alcatraz Boxers [Black 3-Pack]",
    "price": "£35.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "boxers-alcatraz-black", "../images/boxers-alcatraz-black.png"),
      ("White", "boxers-alcatraz-white", "../images/boxers-alcatraz-white.png"),
      ("Grey",  "boxers-alcatraz-grey",  "../images/boxers-alcatraz-grey.png"),
    ],
    "active_variant": "boxers-alcatraz-black",
    "desc": [
      "95% Cotton / 5% Elastane.",
      "Alcatraz Logo Waistband.",
      "Pack of 3.",
      "Regular Fit.",
      "True to Size.",
    ],
    "model": "",
  },
  {
    "slug": "boxers-alcatraz-white",
    "name": "Alcatraz Boxers<br>[White 3-Pack]",
    "title": "Alcatraz Boxers [White 3-Pack]",
    "price": "£35.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "boxers-alcatraz-black", "../images/boxers-alcatraz-black.png"),
      ("White", "boxers-alcatraz-white", "../images/boxers-alcatraz-white.png"),
      ("Grey",  "boxers-alcatraz-grey",  "../images/boxers-alcatraz-grey.png"),
    ],
    "active_variant": "boxers-alcatraz-white",
    "desc": [
      "95% Cotton / 5% Elastane.",
      "Alcatraz Logo Waistband.",
      "Pack of 3.",
      "Regular Fit.",
      "True to Size.",
    ],
    "model": "",
  },
  {
    "slug": "boxers-alcatraz-grey",
    "name": "Alcatraz Boxers<br>[Grey 3-Pack]",
    "title": "Alcatraz Boxers [Grey 3-Pack]",
    "price": "£35.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "boxers-alcatraz-black", "../images/boxers-alcatraz-black.png"),
      ("White", "boxers-alcatraz-white", "../images/boxers-alcatraz-white.png"),
      ("Grey",  "boxers-alcatraz-grey",  "../images/boxers-alcatraz-grey.png"),
    ],
    "active_variant": "boxers-alcatraz-grey",
    "desc": [
      "95% Cotton / 5% Elastane.",
      "Alcatraz Logo Waistband.",
      "Pack of 3.",
      "Regular Fit.",
      "True to Size.",
    ],
    "model": "",
  },
  {
    "slug": "boxers-allstarz-black",
    "name": "Allstarz Boxers<br>[Black 3-Pack]",
    "title": "Allstarz Boxers [Black 3-Pack]",
    "price": "£35.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "boxers-allstarz-black", "../images/boxers-allstarz-black.png"),
      ("White", "boxers-allstarz-white", "../images/boxers-allstarz-white.png"),
      ("Grey",  "boxers-allstarz-grey",  "../images/boxers-allstarz-grey.png"),
    ],
    "active_variant": "boxers-allstarz-black",
    "desc": [
      "95% Cotton / 5% Elastane.",
      "CRTZ Allstarz Logo Waistband.",
      "Pack of 3.",
      "Regular Fit.",
      "True to Size.",
    ],
    "model": "",
  },
  {
    "slug": "boxers-allstarz-white",
    "name": "Allstarz Boxers<br>[White 3-Pack]",
    "title": "Allstarz Boxers [White 3-Pack]",
    "price": "£35.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "boxers-allstarz-black", "../images/boxers-allstarz-black.png"),
      ("White", "boxers-allstarz-white", "../images/boxers-allstarz-white.png"),
      ("Grey",  "boxers-allstarz-grey",  "../images/boxers-allstarz-grey.png"),
    ],
    "active_variant": "boxers-allstarz-white",
    "desc": [
      "95% Cotton / 5% Elastane.",
      "CRTZ Allstarz Logo Waistband.",
      "Pack of 3.",
      "Regular Fit.",
      "True to Size.",
    ],
    "model": "",
  },
  {
    "slug": "boxers-allstarz-grey",
    "name": "Allstarz Boxers<br>[Grey 3-Pack]",
    "title": "Allstarz Boxers [Grey 3-Pack]",
    "price": "£35.00",
    "sizes": ["XS","S","M","L","XL","XXL"],
    "variants": [
      ("Black", "boxers-allstarz-black", "../images/boxers-allstarz-black.png"),
      ("White", "boxers-allstarz-white", "../images/boxers-allstarz-white.png"),
      ("Grey",  "boxers-allstarz-grey",  "../images/boxers-allstarz-grey.png"),
    ],
    "active_variant": "boxers-allstarz-grey",
    "desc": [
      "95% Cotton / 5% Elastane.",
      "CRTZ Allstarz Logo Waistband.",
      "Pack of 3.",
      "Regular Fit.",
      "True to Size.",
    ],
    "model": "",
  },
  {
    "slug": "socks-black",
    "name": "Alcatraz Socks<br>[Black 2-Pack]",
    "title": "Alcatraz Socks [Black 2-Pack]",
    "price": "£18.00",
    "sizes": ["One Size"],
    "variants": [
      ("Black", "socks-black", "../images/socks-black.png"),
      ("White", "socks-white", "../images/socks-white.png"),
    ],
    "active_variant": "socks-black",
    "desc": [
      "80% Cotton / 20% Elastane.",
      "Alcatraz Logo Jacquard.",
      "Pack of 2.",
      "Ribbed Cuff.",
      "One Size Fits Most.",
    ],
    "model": "",
  },
  {
    "slug": "socks-white",
    "name": "Alcatraz Sock<br>[White 2-Pack]",
    "title": "Alcatraz Sock [White 2-Pack]",
    "price": "£18.00",
    "sizes": ["One Size"],
    "variants": [
      ("Black", "socks-black", "../images/socks-black.png"),
      ("White", "socks-white", "../images/socks-white.png"),
    ],
    "active_variant": "socks-white",
    "desc": [
      "80% Cotton / 20% Elastane.",
      "Alcatraz Logo Jacquard.",
      "Pack of 2.",
      "Ribbed Cuff.",
      "One Size Fits Most.",
    ],
    "model": "",
  },
  {
    "slug": "crib-crep-black",
    "name": "Crib Crep<br>[Black]",
    "title": "Crib Crep [Black]",
    "price": "£120.00",
    "sizes": ["UK6","UK7","UK8","UK9","UK10","UK11"],
    "variants": [
      ("Black", "crib-crep-black", "../images/crib-crep-black.png"),
      ("White", "crib-crep-white", "../images/crib-crep-white.png"),
    ],
    "active_variant": "crib-crep-black",
    "desc": [
      "CRTZ x Corteiz Signature Slipper.",
      "Faux Leather Upper.",
      "CRTZ Embossed Logo.",
      "Cushioned Footbed.",
      "Rubber Outsole.",
    ],
    "model": "",
  },
  {
    "slug": "crib-crep-white",
    "name": "Crib Crep<br>[White]",
    "title": "Crib Crep [White]",
    "price": "£120.00",
    "sizes": ["UK6","UK7","UK8","UK9","UK10","UK11"],
    "variants": [
      ("Black", "crib-crep-black", "../images/crib-crep-black.png"),
      ("White", "crib-crep-white", "../images/crib-crep-white.png"),
    ],
    "active_variant": "crib-crep-white",
    "desc": [
      "CRTZ x Corteiz Signature Slipper.",
      "Faux Leather Upper.",
      "CRTZ Embossed Logo.",
      "Cushioned Footbed.",
      "Rubber Outsole.",
    ],
    "model": "",
  },
  {
    "slug": "leather-gloves-black",
    "name": "Leather Gloves<br>[Black]",
    "title": "Leather Gloves [Black]",
    "price": "£65.00",
    "sizes": ["One Size"],
    "variants": [
      ("Black", "leather-gloves-black", "../images/leather-gloves-black.png"),
      ("White", "leather-gloves-white", "../images/leather-gloves-white.png"),
    ],
    "active_variant": "leather-gloves-black",
    "desc": [
      "Genuine Leather.",
      "Embossed CRTZ Logo.",
      "Cashmere Lining.",
      "One Size.",
    ],
    "model": "",
  },
  {
    "slug": "leather-gloves-white",
    "name": "Leather Gloves<br>[White]",
    "title": "Leather Gloves [White]",
    "price": "£65.00",
    "sizes": ["One Size"],
    "variants": [
      ("Black", "leather-gloves-black", "../images/leather-gloves-black.png"),
      ("White", "leather-gloves-white", "../images/leather-gloves-white.png"),
    ],
    "active_variant": "leather-gloves-white",
    "desc": [
      "Genuine Leather.",
      "Embossed CRTZ Logo.",
      "Cashmere Lining.",
      "One Size.",
    ],
    "model": "",
  },
]

# ── HTML Template ────────────────────────────────────────────────────────────

def get_images(slug):
    """Return sorted list of image filenames for a slug."""
    img_dir = f"{IMAGES_DIR}/{slug}"
    if not os.path.isdir(img_dir):
        return ["01.webp"]
    files = sorted([f for f in os.listdir(img_dir) if f.endswith(".webp")])
    return files if files else ["01.webp"]


def build_thumbs(slug, images):
    lines = []
    for i, fname in enumerate(images):
        active = ' active' if i == 0 else ''
        src = f"../images/products/{slug}/{fname}"
        lines.append(f'''            <div class="thumb{active}" onclick="setImg('{src}', this)">
              <img src="{src}" alt="">
            </div>''')
    return "\n".join(lines)


def build_variants(variants, active_slug):
    lines = []
    for label, vslug, img in variants:
        active = ' active' if vslug == active_slug else ''
        lines.append(f'''            <a href="{vslug}.html" class="colour-swatch{active}" title="{label}">
              <img src="{img}" alt="{label}">
            </a>''')
    return "\n".join(lines)


def build_sizes(sizes):
    return "\n".join(
        f'            <button class="size-btn" onclick="selectSize(this)">{s}</button>'
        for s in sizes
    )


def build_desc(bullets):
    return "\n".join(f"              <li>{b}</li>" for b in bullets)


def build_page(p):
    slug = p["slug"]
    images = get_images(slug)
    first_img = f"../images/products/{slug}/{images[0]}"
    title_clean = p["title"]
    name_html = p["name"]
    price = p["price"]
    model_html = f'<p class="product-model">{p["model"]}</p>' if p.get("model") else ""

    # JavaScript-safe name for addToBag
    js_name = p["title"].replace("'", "\\'").replace('"', '\\"')

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_clean} — CRTZ</title>
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

    /* ─── Cursor ─── */
    .cursor {{
      position: fixed;
      width: 7px;
      height: 7px;
      background: var(--color-white);
      border-radius: 50%;
      pointer-events: none;
      z-index: 999999;
      transform: translate(-50%, -50%);
    }}

    /* ─── Shell ─── */
    .shell {{
      display: grid;
      grid-template-columns: 162px 1fr;
      height: 100vh;
      overflow: hidden;
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
      height: 22px;
      width: 22px;
      color: rgba(255,213,0,0.35);
      transition: color 0.12s;
    }}

    .sidebar-foot-icon:hover svg {{ color: rgba(255,213,0,0.75); }}

    .sidebar-foot a {{
      display: block;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.3);
      text-decoration: none;
      padding: 3px 0;
      transition: color 0.12s;
      cursor: none;
    }}

    .sidebar-foot a:hover {{ color: rgba(255,213,0,0.75); }}

    /* ─── Main ─── */
    .main {{
      height: 100vh;
      overflow-y: auto;
      padding: 0;
      scrollbar-width: thin;
      scrollbar-color: rgba(255,255,255,0.08) transparent;
    }}

    .main::-webkit-scrollbar {{ width: 4px; }}
    .main::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,0.08); border-radius: 2px; }}

    /* ─── Top bar ─── */
    .top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 13px 18px;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      position: sticky;
      top: 0;
      background: var(--color-black);
      z-index: var(--z-sticky);
    }}

    .back-link {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.4);
      text-decoration: none;
      transition: color 0.12s;
      cursor: none;
    }}

    .back-link:hover {{ color: rgba(255,213,0,0.8); }}

    .top-bar-right {{
      display: flex;
      align-items: center;
      gap: 28px;
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
      background: transparent;
      border: none;
      outline: none;
      font-family: var(--font-body);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.5);
      width: 90px;
      cursor: none;
    }}

    .search-wrap input::placeholder {{ color: rgba(255,213,0,0.35); }}
    .search-wrap:focus-within svg   {{ color: rgba(255,213,0,0.8); }}
    .search-wrap:focus-within       {{ border-color: rgba(255,213,0,0.5); }}
    .search-wrap input:focus        {{ color: var(--color-yellow); }}

    .header-btn {{
      display: flex;
      align-items: center;
      gap: 7px;
      background: none;
      border: none;
      font-family: var(--font-body);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.5);
      cursor: none;
      padding: 0;
      transition: color 0.12s;
    }}

    .header-btn:hover {{ color: var(--color-yellow); }}
    .header-checkout  {{ color: rgba(255,213,0,0.35); }}

    /* ─── Cart drawer ─── */
    .cart-drawer {{
      position: fixed;
      top: 0; right: 0;
      width: 320px;
      height: 100vh;
      background: #0a0a0a;
      border-left: 1px solid rgba(255,255,255,0.06);
      z-index: var(--z-drawer);
      display: flex;
      flex-direction: column;
      transform: translateX(100%);
      transition: transform 0.3s ease;
    }}

    .cart-drawer.open {{ transform: translateX(0); }}

    .cart-drawer-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 18px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      flex-shrink: 0;
    }}

    .cart-drawer-head span {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--color-yellow);
    }}

    .cart-close {{
      background: none;
      border: none;
      color: rgba(255,213,0,0.4);
      font-size: 16px;
      cursor: none;
      padding: 0;
      transition: color 0.12s;
      line-height: 1;
    }}

    .cart-close:hover {{ color: var(--color-yellow); }}

    .cart-list {{
      flex: 1;
      overflow-y: auto;
      padding: 12px 0;
      scrollbar-width: none;
    }}

    .cart-list::-webkit-scrollbar {{ display: none; }}

    .cart-empty {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.25);
      padding: 24px 18px;
    }}

    .cart-item {{
      display: flex;
      gap: 12px;
      padding: 12px 18px;
      border-bottom: 1px solid rgba(255,255,255,0.04);
    }}

    .cart-item img {{
      width: 64px;
      height: 64px;
      object-fit: contain;
      background: transparent;
      flex-shrink: 0;
    }}

    .cart-item-info {{ flex: 1; min-width: 0; }}

    .cart-item-name {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.8);
      margin-bottom: 3px;
      line-height: 1.35;
    }}

    .cart-item-price {{
      font-size: 10px;
      color: rgba(255,213,0,0.4);
      margin-bottom: 8px;
    }}

    .cart-item-qty {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .cart-item-qty button {{
      background: none;
      border: 1px solid rgba(255,213,0,0.2);
      color: rgba(255,213,0,0.6);
      width: 20px;
      height: 20px;
      font-size: 13px;
      line-height: 1;
      cursor: none;
      transition: border-color 0.12s, color 0.12s;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .cart-item-qty button:hover {{ border-color: var(--color-yellow); color: var(--color-yellow); }}

    .cart-item-qty span {{
      font-size: 11px;
      font-weight: 700;
      color: var(--color-yellow);
      min-width: 16px;
      text-align: center;
    }}

    .cart-drawer-foot {{
      flex-shrink: 0;
      border-top: 1px solid rgba(255,255,255,0.06);
      padding: 16px 18px 20px;
    }}

    .cart-total {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.6);
      margin-bottom: 14px;
    }}

    .cart-total span {{ color: var(--color-yellow); }}

    .cart-checkout-btn {{
      width: 100%;
      height: 44px;
      background: var(--color-yellow);
      color: var(--color-black);
      border: none;
      font-family: var(--font-body);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      cursor: none;
      transition: opacity 0.12s;
    }}

    .cart-checkout-btn:hover {{ opacity: 0.85; }}

    .cart-overlay {{
      position: fixed;
      inset: 0;
      z-index: var(--z-overlay);
      display: none;
    }}

    .cart-overlay.open {{ display: block; }}

    /* ─── Product layout ─── */
    .product {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0;
      min-height: calc(100vh - 48px);
    }}

    /* ─── Image side ─── */
    .product-images {{
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: sticky;
      top: 0;
      height: 100vh;
    }}

    .product-main-img {{
      flex: 1;
      background: transparent;
      overflow: hidden;
      min-height: 0;
    }}

    .product-main-img img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
      transition: opacity 0.2s;
    }}

    .product-thumbs {{
      display: flex;
      gap: 8px;
      flex-shrink: 0;
      flex-wrap: wrap;
    }}

    .thumb {{
      width: 72px;
      height: 72px;
      background: transparent;
      overflow: hidden;
      cursor: none;
      border: 1px solid transparent;
      transition: border-color 0.15s;
      flex-shrink: 0;
    }}

    .thumb img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
    }}

    .thumb.active {{ border-color: rgba(255,213,0,0.5); }}
    .thumb:hover  {{ border-color: rgba(255,213,0,0.25); }}

    /* ─── Info side ─── */
    .product-info {{
      padding: 40px 36px 40px 28px;
      border-left: 1px solid rgba(255,255,255,0.05);
      overflow-y: auto;
    }}

    .product-name {{
      font-size: 22px;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--color-yellow);
      line-height: 1.15;
      margin-bottom: 14px;
    }}

    .product-price {{
      font-size: 16px;
      font-weight: 700;
      color: rgba(255,213,0,0.7);
      letter-spacing: 0.04em;
      margin-bottom: 28px;
    }}

    /* ─── Colour ─── */
    .section-label {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.35);
      margin-bottom: 10px;
    }}

    .colour-row {{
      display: flex;
      gap: 10px;
      margin-bottom: 28px;
    }}

    .colour-swatch {{
      width: 48px;
      height: 48px;
      border: 1px solid rgba(255,255,255,0.1);
      overflow: hidden;
      cursor: none;
      transition: border-color 0.15s;
      text-decoration: none;
      display: block;
    }}

    .colour-swatch img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .colour-swatch.active {{ border-color: var(--color-yellow); }}
    .colour-swatch:hover  {{ border-color: rgba(255,213,0,0.5); }}

    /* ─── Size ─── */
    .size-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 28px;
    }}

    .size-btn {{
      height: 40px;
      min-width: 52px;
      padding: 0 10px;
      background: transparent;
      border: 1px solid rgba(255,213,0,0.2);
      color: rgba(204, 40, 40, 1);
      font-family: var(--font-body);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      cursor: none;
      transition: border-color 0.12s, color 0.12s, background 0.12s;
    }}

    .size-btn:hover {{
      border-color: rgba(255,213,0,0.6);
      color: var(--color-yellow);
    }}

    .size-btn.active {{
      background: var(--color-yellow);
      color: var(--color-black);
      border-color: var(--color-yellow);
    }}

    /* ─── Add to bag ─── */
    .add-btn {{
      width: 100%;
      height: 50px;
      background: var(--color-yellow);
      color: var(--color-black);
      border: none;
      font-family: var(--font-body);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      cursor: none;
      transition: opacity 0.12s;
      margin-bottom: 32px;
    }}

    .add-btn:hover {{ opacity: 0.88; }}

    .add-btn:disabled {{
      background: rgba(255,213,0,0.15);
      color: rgba(255,213,0,0.3);
    }}

    /* ─── Description ─── */
    .product-desc {{
      border-top: 1px solid rgba(255,255,255,0.06);
      padding-top: 24px;
      margin-bottom: 24px;
    }}

    .product-desc ul {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 20px;
    }}

    .product-desc li {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.75);
      line-height: 1.4;
    }}

    .product-desc li::before {{
      content: '—';
      color: rgba(255,213,0,0.3);
      flex-shrink: 0;
    }}

    .product-model {{
      font-size: 11px;
      font-weight: 400;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: rgba(204, 40, 40, 1);
      margin-bottom: 20px;
    }}

    .product-links {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .product-links a {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: rgba(255,213,0,0.4);
      text-decoration: underline;
      text-underline-offset: 3px;
      cursor: none;
      transition: color 0.12s;
    }}

    .product-links a:hover {{ color: var(--color-yellow); }}

    /* ─── No-size warning ─── */
    .size-warning {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: rgba(255,100,100,0.7);
      margin-bottom: 10px;
      display: none;
    }}

    /* ─── Mobile ─── */
    @media (max-width: 749px) {{
      .shell {{
        grid-template-columns: 1fr;
      }}

      .sidebar {{
        height: auto;
        position: static;
        flex-direction: row;
        overflow-x: auto;
        border-right: none;
        border-bottom: 1px solid rgba(255,255,255,0.05);
      }}

      .sidebar-brand {{ border-bottom: none; border-right: 1px solid rgba(255,255,255,0.05); padding: 12px; }}
      .sidebar-nav {{ display: flex; flex-direction: row; padding: 0; }}
      .sidebar-nav ul {{ display: flex; }}
      .sidebar-nav a {{ padding: 14px 12px; }}
      .sidebar-foot {{ display: none; }}

      .product {{ grid-template-columns: 1fr; }}

      .product-images {{
        position: static;
        height: auto;
        padding: 16px;
      }}

      .product-main-img {{ height: 320px; flex: none; }}

      .product-info {{ padding: 20px 16px; border-left: none; border-top: 1px solid rgba(255,255,255,0.05); }}

      .product-name {{ font-size: 16px; }}
    }}
  </style>
</head>
<body>

  <div class="cursor" id="cursor"></div>

  <div class="shell">

    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-brand">
        <a href="../index.html"><img src="../crtzlogo.png" alt="CRTZ"></a>
      </div>
      <nav class="sidebar-nav">
        <ul>
          <li><a href="../index.html">All</a></li>
          <li><a href="../index.html">Classic</a></li>
          <li><a href="../index.html">T-Shirts</a></li>
          <li><a href="../index.html">Tops / Jackets</a></li>
          <li><a href="../index.html">Sweatshirts</a></li>
          <li><a href="../index.html">Jackets</a></li>
          <li><a href="../index.html">Bottoms</a></li>
          <li><a href="../index.html">Shorts</a></li>
          <li><a href="../index.html">Hats</a></li>
          <li><a href="../index.html">Bags</a></li>
          <li><a href="../index.html">Accessories</a></li>
          <li><a href="../index.html">Womens</a></li>
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

    <!-- Main -->
    <main class="main">

      <!-- Top bar -->
      <div class="top-bar">
        <a href="../index.html" class="back-link">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
          Back
        </a>
        <div class="top-bar-right">
          <div class="search-wrap">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <input type="text" placeholder="Search" onkeydown="if(event.key==='Enter') window.location='../index.html?q='+encodeURIComponent(this.value)">
          </div>
          <button class="header-btn" onclick="toggleCart()">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
            Cart (<span id="cart-count">0</span>)
          </button>
        </div>
      </div>

      <div class="product">

        <!-- Images -->
        <div class="product-images">
          <div class="product-main-img">
            <img id="main-img" src="{first_img}" alt="{title_clean}">
          </div>
          <div class="product-thumbs">
{build_thumbs(slug, images)}
          </div>
        </div>

        <!-- Info -->
        <div class="product-info">
          <h1 class="product-name">{name_html}</h1>
          <p class="product-price">{price}</p>

          <!-- Colour -->
          <p class="section-label">Colour</p>
          <div class="colour-row">
{build_variants(p["variants"], p["active_variant"])}
          </div>

          <!-- Size -->
          <p class="section-label">Size</p>
          <div class="size-row">
{build_sizes(p["sizes"])}
          </div>

          <p class="size-warning" id="size-warning">Please select a size</p>

          <button class="add-btn" onclick="addToBag()">Add to Bag</button>

          <!-- Description -->
          <div class="product-desc">
            <ul>
{build_desc(p["desc"])}
            </ul>
            {model_html}
            <div class="product-links">
              <a href="#">Size Guide</a>
              <a href="#">Shipping Policy</a>
            </div>
          </div>

        </div>
      </div>
    </main>

  </div>

  <!-- Cart overlay -->
  <div class="cart-overlay" id="cart-overlay" onclick="toggleCart()"></div>

  <!-- Cart drawer -->
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

    /* Image switcher */
    function setImg(src, thumb) {{
      document.getElementById('main-img').src = src;
      document.querySelectorAll('.thumb').forEach(t => t.classList.remove('active'));
      thumb.classList.add('active');
    }}

    /* ─── Cart ─── */
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

    /* ─── Size selector ─── */
    let selectedSize = null;

    function selectSize(btn) {{
      document.querySelectorAll('.size-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedSize = btn.textContent;
      document.getElementById('size-warning').style.display = 'none';
    }}

    /* ─── Add to bag ─── */
    function addToBag() {{
      if (!selectedSize) {{
        document.getElementById('size-warning').style.display = 'block';
        return;
      }}
      const name   = `{js_name} — ${{selectedSize}}`;
      const price  = '{price}';
      const imgSrc = document.getElementById('main-img').src;
      const existing = cart.find(i => i.name === name);
      if (existing) {{ existing.qty++; }} else {{ cart.push({{ name, price, imgSrc, qty: 1 }}); }}
      renderCart();
      toggleCart();
    }}
  </script>

</body>
</html>'''


# ── Generate all pages ────────────────────────────────────────────────────────
os.makedirs(PRODUCTS_DIR, exist_ok=True)
for p in PRODUCTS:
    out_path = f"{PRODUCTS_DIR}/{p['slug']}.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(build_page(p))
    print(f"OK {p['slug']}.html")

print(f"\nGenerated {len(PRODUCTS)} product pages.")
