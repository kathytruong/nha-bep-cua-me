#!/usr/bin/env python3
"""Build all site pages from JSON data, templates, and partials."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from lib.constants import (  # noqa: E402
    CATEGORIES,
    CATEGORY_ORDER,
    COOK_LABELS,
    CSS_VERSION,
    JS_VERSION,
)

PARTIALS = ROOT / "partials"
TEMPLATES = ROOT / "templates"
RECIPES_DIR = ROOT / "recipes"
DATA_DIR = RECIPES_DIR / "data"

STATIC_PAGES = [
    {
        "output": "index.html",
        "template": "index.html",
        "nav": "home",
        "title": "Nhà Bếp Của Mẹ — Our Family Kitchen",
        "extra_head": '  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n',
    },
    {
        "output": "about.html",
        "template": "about.html",
        "nav": "about",
        "title": "About — Nhà Bếp Của Mẹ",
    },
    {
        "output": "stories.html",
        "template": "stories.html",
        "nav": "stories",
        "title": "Stories — Nhà Bếp Của Mẹ",
    },
]


def load_partial(name):
    return (PARTIALS / name).read_text(encoding="utf-8")


def load_template(name):
    return (TEMPLATES / name).read_text(encoding="utf-8")


def fill(template, **kwargs):
    result = template
    for key, value in kwargs.items():
        result = result.replace("{{" + key + "}}", value)
    return result


def nav_active(page):
    return {
        "home_active": ' class="active"' if page == "home" else "",
        "recipes_active": ' class="active"' if page == "recipes" else "",
        "stories_active": ' class="active"' if page == "stories" else "",
        "about_active": ' class="active"' if page == "about" else "",
    }


def render_shell(base, nav_page, page_title, body, extra_head=""):
    head = fill(
        load_partial("head.html"),
        page_title=page_title,
        base=base,
        css_version=CSS_VERSION,
        extra_head=extra_head,
    )
    nav = fill(
        load_partial("nav.html"),
        base=base,
        **nav_active(nav_page),
    )
    footer = fill(
        load_partial("footer.html"),
        base=base,
        js_version=JS_VERSION,
    )
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        + head
        + "</head>\n<body>\n\n"
        + nav
        + "\n"
        + body
        + footer
        + "</body>\n</html>\n"
    )


def render_section(section):
    lines = [
        '      <div class="recipe-section">',
        f"        <h2>{section['heading']}</h2>",
    ]

    if section.get("steps"):
        lines.append("        <ol>")
        for step in section["steps"]:
            lines.append(f"          <li><span>{step}</span></li>")
        lines.append("        </ol>")
    elif section.get("groups"):
        for group in section["groups"]:
            lines.append(f"        <h3>{group['heading']}</h3>")
            lines.append("        <ul>")
            lines.extend(f"          <li>{item}</li>" for item in group["items"])
            lines.append("        </ul>")
    elif section.get("items"):
        lines.append("        <ul>")
        lines.extend(f"          <li>{item}</li>" for item in section["items"])
        lines.append("        </ul>")

    lines.append("      </div>")
    return "\n".join(lines) + "\n"


def render_recipe_body(recipe):
    parts = [
        '  <main class="container">',
        '    <div class="recipe-detail">',
        '      <a href="../recipes.html" class="back-link">← Back to recipes</a>',
        "",
    ]

    if recipe.get("hero_image"):
        parts.extend(
            [
                '      <div class="recipe-detail-hero">',
                f'        <img src="{recipe["hero_image"]}" alt="{recipe.get("hero_alt", recipe["title"])}">',
                "      </div>",
                "",
            ]
        )

    parts.extend(
        [
            f'      <h1>{recipe["title"]}</h1>',
            f'      <p class="english-name">{recipe["english"]}</p>',
            f'      <p class="recipe-from">{recipe["cook_label"]}</p>',
        ]
    )

    if recipe.get("yield"):
        parts.append(f'      <p class="recipe-yield">{recipe["yield"]}</p>')

    category_label = CATEGORIES[recipe["category"]]
    parts.extend(
        [
            "",
            '      <div class="recipe-meta">',
            '        <div class="recipe-meta-item">',
            '          <div class="meta-label">Category</div>',
            f'          <div class="meta-value">{category_label}</div>',
            "        </div>",
            "      </div>",
            "",
        ]
    )

    for section in recipe.get("sections", []):
        parts.append(render_section(section))

    if recipe.get("scans"):
        parts.extend(
            [
                '      <div class="original-scan">',
                f'        <p class="original-scan-label">{recipe.get("scan_label", "Công thức gốc · Original handwritten recipe")}</p>',
                '        <div class="original-scan-images">',
            ]
        )
        for scan in recipe["scans"]:
            alt = scan.get("alt") or recipe["title"]
            parts.append(f'          <img src="{scan["src"]}" alt="{alt}">')
        parts.extend(["        </div>", "      </div>", ""])

    if recipe.get("tip"):
        tip_label = recipe.get("tip_label", "Tip")
        parts.extend(
            [
                '      <div class="recipe-tip">',
                f'        <p class="tip-label">{tip_label}</p>',
                f'        <p>{recipe["tip"]}</p>',
                "      </div>",
                "",
            ]
        )

    if recipe.get("memorial"):
        parts.extend(
            [
                '      <div class="memorial">',
                '        <div class="flourish">❦</div>',
                f'        <p>{recipe["memorial"]}</p>',
                "      </div>",
            ]
        )

    parts.extend(["    </div>", "  </main>", ""])
    return "\n".join(parts)


def render_card(recipe):
    category_label = CATEGORIES[recipe["category"]]
    cook_label = recipe.get("cook_label") or COOK_LABELS[recipe["cook"]]

    if recipe.get("card_placeholder"):
        image_block = """          <div class="recipe-card-image recipe-card-image--placeholder">
            <span class="placeholder-icon" aria-hidden="true">❦</span>
          </div>"""
    else:
        src = recipe.get("card_image", "")
        alt = recipe.get("card_image_alt") or recipe["title"]
        image_block = f"""          <div class="recipe-card-image">
            <img src="{src}" alt="{alt}">
          </div>"""

    return f"""        <a href="recipes/{recipe['slug']}.html" class="recipe-card" data-cook="{recipe['cook']}" data-category="{recipe['category']}">
{image_block}
          <div class="recipe-card-body">
            <div class="recipe-card-category">{category_label}</div>
            <div class="recipe-card-title">{recipe['title']}</div>
            <div class="recipe-card-english">{recipe['english']}</div>
            <div class="recipe-card-from">{cook_label}</div>
          </div>
        </a>"""


def load_all_recipes():
    recipes = []
    for path in sorted(DATA_DIR.glob("*/*.json")):
        recipe = json.loads(path.read_text(encoding="utf-8"))
        recipes.append(recipe)
    return recipes


def recipe_grid_html(recipes):
    by_category = {cat: [] for cat in CATEGORY_ORDER}
    me_thinh = []

    for recipe in sorted(recipes, key=lambda r: r.get("grid_order", 999)):
        if recipe["cook"] == "me-thinh":
            me_thinh.append(recipe)
        else:
            by_category.setdefault(recipe["category"], []).append(recipe)

    lines = ['      <div class="recipe-grid" id="recipeGrid">', ""]

    for cat in CATEGORY_ORDER:
        cat_recipes = by_category.get(cat, [])
        if not cat_recipes:
            continue
        lines.append(f"        <!-- ═══ {CATEGORIES[cat]} ═══ -->")
        lines.append("")
        for recipe in cat_recipes:
            lines.append(render_card(recipe))
            lines.append("")

    if me_thinh:
        lines.append("        <!-- ═══ Mẹ Thịnh ═══ -->")
        lines.append("")
        for recipe in me_thinh:
            lines.append(render_card(recipe))
            lines.append("")

    lines.append("      </div>")
    return "\n".join(lines)


def build_recipes_page(recipes):
    grid = recipe_grid_html(recipes)
    body = f"""  <main>
    <div class="page-header">
      <p class="page-sub">Công thức gia đình</p>
      <h1>The family cookbook</h1>
      <p class="page-header-desc">Browse by dish, or by the Mẹ who made it.</p>
    </div>

    <div class="container">
      <div class="filter-group">
        <p class="filter-group-label">By dish</p>
        <div class="filter-tabs" id="dishFilters">
          <button type="button" class="filter-tab filter-tab-dish active" data-filter="all">All</button>
          <button type="button" class="filter-tab filter-tab-dish" data-filter="mon-nuoc">Phở & Canh</button>
          <button type="button" class="filter-tab filter-tab-dish" data-filter="mon-man">Món Mặn</button>
          <button type="button" class="filter-tab filter-tab-dish" data-filter="banh">Bánh</button>
          <button type="button" class="filter-tab filter-tab-dish" data-filter="desserts">Desserts</button>
          <button type="button" class="filter-tab filter-tab-dish" data-filter="com">Cơm & Xôi</button>
          <button type="button" class="filter-tab filter-tab-dish" data-filter="do-chua">Đồ Chua</button>
          <button type="button" class="filter-tab filter-tab-dish" data-filter="nuoc-cham">Nước Chấm</button>
        </div>
      </div>

      <div class="filter-group">
        <p class="filter-group-label">By cook</p>
        <div class="filter-tabs" id="cookFilters">
          <button type="button" class="filter-tab filter-tab-cook active" data-cook="all">Everyone</button>
          <button type="button" class="filter-tab filter-tab-cook" data-cook="me-oanh">Mẹ Oanh</button>
          <button type="button" class="filter-tab filter-tab-cook" data-cook="me-uyen">Mẹ Uyên</button>
          <button type="button" class="filter-tab filter-tab-cook" data-cook="me-yen">Mẹ Yên</button>
          <button type="button" class="filter-tab filter-tab-cook" data-cook="me-yen-nho">Mẹ Yên Nho</button>
          <button type="button" class="filter-tab filter-tab-cook" data-cook="me-thinh">Mẹ Thịnh</button>
        </div>
      </div>

{grid}
    </div>
  </main>
"""
    return render_shell("", "recipes", "Recipes — Nhà Bếp Của Mẹ", body)


def build_static_pages():
    for page in STATIC_PAGES:
        body = load_template(page["template"])
        html = render_shell(
            "",
            page["nav"],
            page["title"],
            body,
            extra_head=page.get("extra_head", ""),
        )
        out = ROOT / page["output"]
        out.write_text(html, encoding="utf-8")
        print(f"  {page['output']}")


def main():
    if not DATA_DIR.exists() or not any(DATA_DIR.glob("*/*.json")):
        print("No recipe JSON found. Run: python3 scripts/extract-recipes.py")
        sys.exit(1)

    recipes = load_all_recipes()
    print(f"Building {len(recipes)} recipes...")

    for recipe in recipes:
        body = render_recipe_body(recipe)
        page_title = f"{recipe['title']} — Nhà Bếp Của Mẹ"
        html = render_shell("../", "recipes", page_title, body)
        out = RECIPES_DIR / f"{recipe['slug']}.html"
        out.write_text(html, encoding="utf-8")
        print(f"  recipes/{out.name}")

    (ROOT / "recipes.html").write_text(build_recipes_page(recipes), encoding="utf-8")
    print("  recipes.html")

    print("Building site pages...")
    build_static_pages()
    print("Done.")


if __name__ == "__main__":
    main()
