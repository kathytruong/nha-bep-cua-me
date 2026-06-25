#!/usr/bin/env python3
"""One-time migration: extract recipe data from HTML into JSON files."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from lib.constants import CATEGORIES, COOK_LABELS  # noqa: E402

RECIPES_HTML = ROOT / "recipes.html"
RECIPES_DIR = ROOT / "recipes"
DATA_DIR = RECIPES_DIR / "data"

LABEL_TO_CATEGORY = {v: k for k, v in CATEGORIES.items()}


def parse_card_metadata():
    """Parse cook, category, card image, and grid order from recipes.html."""
    text = RECIPES_HTML.read_text(encoding="utf-8")
    pattern = re.compile(
        r'<a href="recipes/([^"]+\.html)" class="recipe-card" '
        r'data-cook="([^"]+)" data-category="([^"]+)">'
        r'(.*?)</a>',
        re.DOTALL,
    )
    cards = {}
    for order, match in enumerate(pattern.finditer(text)):
        slug = match.group(1).replace(".html", "")
        cook = match.group(2)
        category = match.group(3)
        body = match.group(4)
        img_match = re.search(
            r'<img src="([^"]+)" alt="([^"]*)">', body
        )
        placeholder = "recipe-card-image--placeholder" in body
        cards[slug] = {
            "cook": cook,
            "category": category,
            "grid_order": order,
            "card_image": img_match.group(1) if img_match and not placeholder else None,
            "card_image_alt": img_match.group(2) if img_match and not placeholder else None,
            "card_placeholder": placeholder,
        }
    return cards


def text_content(html_fragment):
    text = re.sub(r"<[^>]+>", "", html_fragment)
    return re.sub(r"\s+", " ", text).strip()


def parse_list_items(ul_html):
    items = []
    for match in re.finditer(r"<li>(.*?)</li>", ul_html, re.DOTALL):
        item = text_content(match.group(1))
        if item:
            items.append(item)
    return items


def parse_steps(ol_html):
    steps = []
    for match in re.finditer(r"<li>\s*<span>(.*?)</span>\s*</li>", ol_html, re.DOTALL):
        step = text_content(match.group(1))
        if step:
            steps.append(step)
    return steps


def parse_section(section_html):
    heading_match = re.search(r"<h2>(.*?)</h2>", section_html, re.DOTALL)
    if not heading_match:
        return None
    heading = text_content(heading_match.group(1))

    ol_match = re.search(r"<ol>(.*?)</ol>", section_html, re.DOTALL)
    if ol_match:
        return {"heading": heading, "steps": parse_steps(ol_match.group(1))}

    h3_matches = list(re.finditer(r"<h3>(.*?)</h3>", section_html, re.DOTALL))
    if h3_matches:
        groups = []
        for i, h3 in enumerate(h3_matches):
            start = h3.end()
            end = h3_matches[i + 1].start() if i + 1 < len(h3_matches) else len(section_html)
            chunk = section_html[start:end]
            ul_match = re.search(r"<ul>(.*?)</ul>", chunk, re.DOTALL)
            if ul_match:
                groups.append(
                    {
                        "heading": text_content(h3.group(1)),
                        "items": parse_list_items(ul_match.group(1)),
                    }
                )
        if groups:
            return {"heading": heading, "groups": groups}

    ul_match = re.search(r"<ul>(.*?)</ul>", section_html, re.DOTALL)
    if ul_match:
        return {"heading": heading, "items": parse_list_items(ul_match.group(1))}

    return {"heading": heading}


def cook_from_label(label):
    for cook, cook_label in COOK_LABELS.items():
        if cook_label == label:
            return cook
    return "me-oanh"


def parse_recipe_html(path, card_meta):
    slug = path.stem
    html = path.read_text(encoding="utf-8")
    meta = card_meta.get(slug, {})

    title_match = re.search(r"<h1>(.*?)</h1>", html, re.DOTALL)
    english_match = re.search(
        r'<p class="english-name">(.*?)</p>', html, re.DOTALL
    )
    from_match = re.search(r'<p class="recipe-from">(.*?)</p>', html, re.DOTALL)
    yield_match = re.search(r'<p class="recipe-yield">(.*?)</p>', html, re.DOTALL)
    category_match = re.search(
        r'<div class="meta-label">Category</div>\s*<div class="meta-value">(.*?)</div>',
        html,
        re.DOTALL,
    )

    hero_match = re.search(
        r'<div class="recipe-detail-hero">\s*<img src="([^"]+)" alt="([^"]*)">',
        html,
        re.DOTALL,
    )

    tip_match = re.search(
        r'<div class="recipe-tip">\s*<p class="tip-label">(.*?)</p>\s*<p>(.*?)</p>\s*</div>',
        html,
        re.DOTALL,
    )

    memorial_match = re.search(
        r'<div class="memorial">.*?<p>(.*?)</p>', html, re.DOTALL
    )

    scan_label_match = re.search(
        r'<p class="original-scan-label">(.*?)</p>', html, re.DOTALL
    )
    scan_images = re.findall(
        r'<div class="original-scan-images">.*?<img src="([^"]+)" alt="([^"]*)"[^>]*>',
        html,
        re.DOTALL,
    )
    if not scan_images:
        scan_images = re.findall(
            r'<div class="original-scan-images">(.*?)</div>', html, re.DOTALL
        )
        if scan_images:
            scan_images = re.findall(
                r'<img src="([^"]+)" alt="([^"]*)"[^>]*>', scan_images[0]
            )

    sections = []
    for section_match in re.finditer(
        r'<div class="recipe-section">(.*?)</div>\s*(?=<div class="(?:recipe-section|original-scan|recipe-tip|memorial)|</div>\s*</main>)',
        html,
        re.DOTALL,
    ):
        section = parse_section(section_match.group(1))
        if section:
            sections.append(section)

    cook_label = text_content(from_match.group(1)) if from_match else COOK_LABELS["me-oanh"]
    cook = meta.get("cook") or cook_from_label(cook_label)
    category_label = text_content(category_match.group(1)) if category_match else ""
    category = meta.get("category") or LABEL_TO_CATEGORY.get(category_label, "mon-man")

    data = {
        "slug": slug,
        "title": text_content(title_match.group(1)) if title_match else slug,
        "english": text_content(english_match.group(1)) if english_match else "",
        "cook": cook,
        "cook_label": cook_label,
        "category": category,
        "sections": sections,
        "grid_order": meta.get("grid_order", 999),
    }

    if yield_match:
        data["yield"] = text_content(yield_match.group(1))

    if hero_match:
        data["hero_image"] = hero_match.group(1)
        data["hero_alt"] = hero_match.group(2)

    if tip_match:
        data["tip_label"] = text_content(tip_match.group(1))
        data["tip"] = text_content(tip_match.group(2))

    if memorial_match:
        data["memorial"] = text_content(memorial_match.group(1))

    if scan_images:
        data["scan_label"] = (
            text_content(scan_label_match.group(1))
            if scan_label_match
            else "Công thức gốc · Original handwritten recipe"
        )
        data["scans"] = [{"src": src, "alt": alt} for src, alt in scan_images]

    if meta.get("card_image"):
        data["card_image"] = meta["card_image"]
        if meta.get("card_image_alt"):
            data["card_image_alt"] = meta["card_image_alt"]
    elif meta.get("card_placeholder"):
        data["card_placeholder"] = True

    return data


def main():
    card_meta = parse_card_metadata()
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    count = 0
    for path in sorted(RECIPES_DIR.glob("*.html")):
        data = parse_recipe_html(path, card_meta)
        cook_dir = DATA_DIR / data["cook"]
        cook_dir.mkdir(parents=True, exist_ok=True)
        out_path = cook_dir / f"{data['slug']}.json"
        out_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {out_path.relative_to(ROOT)}")
        count += 1

    print(f"\nExtracted {count} recipes to {DATA_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
