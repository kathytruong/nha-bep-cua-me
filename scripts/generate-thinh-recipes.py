#!/usr/bin/env python3
"""Generate Mẹ Thịnh recipe pages and recipe cards."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECIPES_DIR = ROOT / "recipes"

COOK = "me-thinh"
FROM = "From Mẹ Thịnh"
CSS = "../css/style.css?v=9"

RECIPES = [
    {
        "slug": "canh-ga-me-thinh",
        "title": "Cánh Gà Chiên",
        "english": "Crispy Batter Fried Chicken Wings",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "2 lb chicken wings",
            "Salt, for cleaning the chicken",
            "Soy sauce, pepper, garlic powder, sugar, and chicken base — ratio 1 : 1 : 2 (chicken base : sugar : soy sauce), mixed well",
            "For the batter: about half a bowl of water",
            "Flour and cornstarch, 5 : 1",
            "Garlic powder, chicken base, and sugar — about ½ spoon each, stirred into the batter",
            "Oil, for frying",
        ],
        "instructions": [
            "Clean the chicken wings with salt.",
            "Mix with soy sauce, pepper, garlic powder, sugar, and chicken base using the 1 : 1 : 2 ratio. Mix well and leave in the fridge to marinate.",
            "Make the batter: combine water, flour, and cornstarch (5 : 1) and mix until smooth.",
            "Stir garlic powder, chicken base, and sugar (about ½ spoon each) into the batter.",
            "Pour the batter over the chicken and coat well.",
            "Heat oil on high, then reduce to medium when frying. Fry until golden and cooked through.",
        ],
    },
    {
        "slug": "oc-nuong-me-thinh",
        "title": "Ốc Nướng",
        "english": "Broiled Mussels with Ginger & Peanuts",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "Mussels, top shell removed",
            "Fresh ginger, sliced — for stir-frying",
            "Green onions",
            "Oyster sauce",
            "Sugar",
            "Garlic",
            "Black pepper",
            "Oil, if needed",
            "Peanuts",
        ],
        "instructions": [
            "Remove the top shell from each mussel.",
            "Stir-fry ginger until fragrant.",
            "Mix green onions with oyster sauce, sugar, garlic, and pepper. Add oil if the mixture needs it.",
            "Spoon the mixture onto each mussel. Top with peanuts.",
            "Broil for about 5 minutes, until bubbling and lightly charred.",
        ],
    },
    {
        "slug": "thit-nuong-com-tam",
        "title": "Thịt Nướng Marinade",
        "english": "Pork Marinade for Bún Thịt Nướng & Cơm Tấm",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "1 lb pork shoulder, or thin-cut bone-in pork chop (will be drier)",
            "1–2 spoons condensed milk or half-and-half, to tenderize",
            "1 spoon oyster sauce",
            "1½ spoons sugar",
            "1 minced shallot",
            "Garlic",
            "Black pepper",
            "½ spoon fish sauce",
            "Coconut milk — enough to fill to the top of the meat",
            "Skewers, for bún thịt nướng",
        ],
        "instructions": [
            "Cut pork shoulder into fillets. For bún thịt nướng, pound the meat until thin.",
            "Mix the marinade ingredients and coat the meat.",
            "Pour coconut milk over the meat until it just covers the top.",
            "Marinate day-of for as long as possible — at least 4 hours.",
            "For cơm tấm: air fry at 400°F, 7 minutes on each side.",
            "For bún thịt nướng: thread pounded meat onto skewers and broil until charred at the edges.",
        ],
    },
    {
        "slug": "cha-trung",
        "title": "Chả Trứng",
        "yield": "Serves 4",
        "english": "Steamed Pork & Egg Loaf",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "¼ lb ground pork",
            "¼ onion, chopped",
            "3 whole eggs plus 1 egg white — reserve the yolk to spread on top of the loaf",
            "Nam meo (wood ear mushroom) — one pinch, soaked until expanded",
            "Bún tàu (mung bean thread noodles) — one pinch, soaked 10 minutes",
            "Salt, pepper, and chicken base, to taste",
        ],
        "instructions": [
            "Line a pan with plastic wrap for easy removal.",
            "Mix all ingredients together and pour into the pan.",
            "Spread the reserved egg yolk on top.",
            "Cover the pan tightly with foil.",
            "Steam for about 30 minutes, until the mixture is solid but not dry.",
        ],
    },
    {
        "slug": "com-tam",
        "title": "Cơm Tấm",
        "english": "Broken Rice",
        "category": "com",
        "category_label": "Cơm & Xôi",
        "ingredients": [
            "Regular long-grain rice",
            "Water — to the first crease of your pointer finger when resting on the rice",
        ],
        "instructions": [
            "To make broken rice from regular rice: soak the rice for 15 minutes.",
            "Rinse twice.",
            "Massage the rice gently to break the grains.",
            "Cook using water to the level of half the first crease of your pointer finger — the usual Vietnamese finger measure.",
        ],
    },
    {
        "slug": "bi-com-tam",
        "title": "Bì",
        "english": "Shredded Pork Skin for Cơm Tấm",
        "category": "com",
        "category_label": "Cơm & Xôi",
        "ingredients": [
            "1 lb pork shoulder",
            "Salt and garlic powder (about 1 tbsp)",
            "Que Huong Bi Tuoi (7 oz) — buy frozen; do not buy dry, which must be soaked first",
            "Kim Tu Thap Thinh Viet Nam (toasted rice powder)",
        ],
        "instructions": [
            "Season pork shoulder with salt and garlic powder.",
            "Pan-fry the pork shoulder, then slice into thin strips.",
            "Use the full bag of bì. Wash and dry thoroughly.",
            "Shred the cooked pork, bì, and rice powder together until evenly mixed.",
            "Serve with cơm tấm and thịt nướng.",
        ],
    },
    {
        "slug": "ca-nuong-me-thinh",
        "title": "Cá Nướng",
        "english": "Baked & Broiled Catfish",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "Catfish",
            "Garlic powder",
            "Black pepper",
            "Chicken base",
            "Oil",
        ],
        "instructions": [
            "Rub the stomach of the catfish with garlic powder, pepper, and chicken base. Spread with oil.",
            "Bake at 375°F for 40 minutes.",
            "Baste again with oil and broil for 12 minutes, until the skin is crispy.",
        ],
    },
    {
        "slug": "thit-kho-trung-me-thinh",
        "title": "Thịt Kho Trứng",
        "english": "Braised Pork & Eggs",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "Eggs — boil and peel",
            "Pork shoulder — trim excess fat",
            "Coconut soda or coconut water",
            "Water, to submerge",
            "Sugar — a little, if using coconut water instead of coconut soda",
            "Fish sauce",
            "2–3 cloves garlic",
            "2–3 shallots",
        ],
        "instructions": [
            "Boil and peel the eggs. Set aside.",
            "Cut off excess fat from the pork shoulder.",
            "Boil the pork shoulder ahead of time. Pour out the water and rinse clean.",
            "Add coconut soda or coconut water, then fill with water to submerge the pork.",
            "If using coconut water, add a little sugar.",
            "Season with fish sauce, garlic, and shallots.",
            "Braise until the pork is tender and the sauce is rich. Add the eggs toward the end.",
        ],
    },
    {
        "slug": "ca-ri-ga-khoai-tay",
        "title": "Cà Ri Gà Khoai Tây",
        "english": "Chicken & Potato Yellow Curry",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "Chicken",
            "Curry powder",
            "Onion powder",
            "Garlic powder",
            "Salt",
            "Coconut milk",
            "Water",
            "Potatoes",
        ],
        "instructions": [
            "Marinate the chicken in curry powder, onion powder, and garlic powder for a couple of hours.",
            "Stir-fry the chicken until lightly browned.",
            "Add salt, coconut milk, and some water.",
            "Microwave the potatoes until mostly cooked, then add to the pot.",
            "Simmer until the chicken is tender and the potatoes are soft.",
        ],
    },
    {
        "slug": "steak-marinade",
        "title": "Steak Marinade",
        "english": "Simple Steak Marinade",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "Soy sauce",
            "Oyster sauce",
            "Black pepper",
            "Garlic",
        ],
        "instructions": [
            "Combine soy sauce, oyster sauce, pepper, and garlic.",
            "Marinate steak for at least 30 minutes before cooking.",
        ],
    },
    {
        "slug": "vit-quay",
        "title": "Vịt Quay",
        "english": "Roast Duck",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "Whole duck",
            "Follow Maclam's Kitchen roast duck recipe on YouTube",
            "Mẹ Thịnh's adjustments: use 2 spoons ngũ vị hương instead of 3",
            "No tứ xuyên pepper",
        ],
        "instructions": [
            "Follow the Maclam's Kitchen roast duck video for the full method.",
            "Use 2 spoons of ngũ vị hương (five-spice) instead of 3.",
            "Leave out tứ xuyên pepper.",
        ],
        "tip": "Mẹ Thịnh built on Maclam's Kitchen method and made it her own with these small adjustments.",
    },
    {
        "slug": "do-chua-carrot-daikon",
        "title": "Đồ Chua",
        "english": "Pickled Carrot & Daikon",
        "category": "do-chua",
        "category_label": "Đồ Chua",
        "ingredients": [
            "1 medium/small daikon",
            "2 medium carrots",
            "4 tablespoons white sugar",
            "5 tablespoons white vinegar",
            "Salt — 1 tbsp for the carrots",
        ],
        "instructions": [
            "Shred the carrots and toss with 1 tbsp salt in a bowl.",
            "Shred the daikon and add to the carrots.",
            "Rinse the carrots and daikon in boiling hot water.",
            "Transfer to a bowl with the sugar and vinegar. Mix well.",
            "Let sit for a couple of hours, revisiting and stirring occasionally.",
            "Drain excess vinegar and sugar mixture before storing in a glass jar.",
        ],
    },
    {
        "slug": "cha-gio-me-thinh",
        "title": "Chả Giò",
        "english": "Fried Egg Rolls (Large Batch)",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "3 lb carrots",
            "3 large jicama (củ sắn), about 5 lb each",
            "2 lb taro (khoai môn)",
            "5 bundles vermicelli noodles (bún tàu)",
            "5 lb shrimp",
            "5 lb ground pork",
            "3 onions",
            "2 bulbs garlic",
            "½ lb shallots",
            "Salt, pepper, chicken base, sugar, and MSG — to taste",
            "4 eggs",
            "Egg roll wrappers",
            "Flour and water paste, for sealing",
            "Oil, for frying",
        ],
        "instructions": [
            "Mandolin the carrots, jicama, and taro into thin strips. Combine in a large bowl.",
            "Boil vermicelli noodles, cut into smaller pieces, and add to the vegetables.",
            "Season the ground pork separately with salt, pepper, chicken base, a little sugar, and MSG — season it a little salty; it will even out with the unseasoned vegetables.",
            "In a food processor, mince the garlic, onions, and shallots. Add to the ground pork.",
            "Blend the shrimp and add to the pork mixture.",
            "Season the pork and shrimp mixture with two spoons of chicken base and a hefty amount of garlic powder. Mix with your hands.",
            "Add some of the pork mixture to the vegetables. Add four eggs and mix. Slowly combine the rest of the pork and shrimp with the vegetables, using your hands for even coverage.",
            "Test the filling by microwaving a spoonful. Adjust seasoning to taste.",
            "Mix flour with water and microwave slowly, stirring until a paste forms — use this to seal the egg rolls.",
            "Roll and fry until golden.",
        ],
        "tip": "Mẹ Thịnh's note: enough for 100 small egg rolls and 200 large ones — a full party's worth.",
    },
    {
        "slug": "hoanh-thanh-tom",
        "title": "Hoành Thánh Tôm",
        "english": "Shrimp Wontons",
        "category": "mon-man",
        "category_label": "Món Mặn",
        "ingredients": [
            "Shrimp",
            "Chicken base",
            "Sugar",
            "Black pepper",
            "Onion powder",
            "Cornstarch or potato starch",
            "Cooking oil",
            "Wonton wrappers",
        ],
        "instructions": [
            "Blend the shrimp. Season with chicken base, sugar, pepper, onion powder, starch, and a little cooking oil.",
            "Wrap the wontons.",
            "Microwave for 1 minute before boiling — this helps them hold together.",
            "Boil until they float and the filling is cooked through.",
        ],
    },
]


def render_page(recipe):
    slug = recipe["slug"]
    ingredients = "".join(f"          <li>{item}</li>\n" for item in recipe["ingredients"])
    instructions = "".join(
        f'          <li><span>{step}</span></li>\n' for step in recipe["instructions"]
    )
    yield_block = ""
    if recipe.get("yield"):
        yield_block = f'      <p class="recipe-yield">{recipe["yield"]}</p>\n\n'

    tip_block = ""
    if recipe.get("tip"):
        tip_block = f"""
      <div class="recipe-tip">
        <p class="tip-label">Mẹ Thịnh's note</p>
        <p>{recipe["tip"]}</p>
      </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{recipe["title"]} — Nhà Bếp Của Mẹ</title>
  <link rel="stylesheet" href="{CSS}">
</head>
<body>

  <nav>
    <div class="container">
      <a href="../index.html" class="nav-brand"><span class="nav-brand-script">Nhà Bếp Của Mẹ</span><span class="nav-brand-serif">Our Family Kitchen</span></a>
      <button class="mobile-menu-btn" onclick="toggleMenu()" aria-label="Menu">☰</button>
      <ul class="nav-links" id="navLinks">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../recipes.html" class="active">Recipes</a></li>
        <li><a href="../stories.html">Stories</a></li>
        <li><a href="../about.html">About</a></li>
        <li><a href="../recipes.html" class="nav-browse">Bếp Nhà · Browse</a></li>
      </ul>
    </div>
  </nav>

  <main class="container">
    <div class="recipe-detail">
      <a href="../recipes.html" class="back-link">← Back to recipes</a>

      <h1>{recipe["title"]}</h1>
      <p class="english-name">{recipe["english"]}</p>
      <p class="recipe-from">{FROM}</p>

{yield_block}      <div class="recipe-meta">
        <div class="recipe-meta-item">
          <div class="meta-label">Category</div>
          <div class="meta-value">{recipe["category_label"]}</div>
        </div>
      </div>

      <div class="recipe-section">
        <h2>Nguyên liệu · Ingredients</h2>
        <ul>
{ingredients}        </ul>
      </div>

      <div class="recipe-section">
        <h2>Cách làm · Instructions</h2>
        <ol>
{instructions}        </ol>
      </div>{tip_block}
    </div>
  </main>

  <footer>
    <div class="container">
      <div class="footer-content">
        <div>
          <div class="footer-brand-script">Nhà Bếp Của Mẹ</div><div class="footer-brand-serif">Our Family Kitchen</div>
          <p class="footer-tagline">A keeping place for our family's Vietnamese recipes — so our cousins, and our children, never lose them.</p>
        </div>
        <ul class="footer-links">
          <li><a href="../recipes.html">Recipes</a></li>
          <li><a href="../stories.html">Stories</a></li>
          <li><a href="../about.html">About</a></li>
        </ul>
      </div>
      <div class="footer-bottom">
        <p>Made with love · Làm với tình thương · by Kathy Trương</p>
      </div>
    </div>
  </footer>

  <script src="../js/main.js?v=3"></script>
</body>
</html>
"""


def render_card(recipe):
    return f"""        <a href="recipes/{recipe["slug"]}.html" class="recipe-card" data-cook="{COOK}" data-category="{recipe["category"]}">
          <div class="recipe-card-image recipe-card-image--placeholder">
            <span class="placeholder-icon" aria-hidden="true">❦</span>
          </div>
          <div class="recipe-card-body">
            <div class="recipe-card-category">{recipe["category_label"]}</div>
            <div class="recipe-card-title">{recipe["title"]}</div>
            <div class="recipe-card-english">{recipe["english"]}</div>
            <div class="recipe-card-from">{FROM}</div>
          </div>
        </a>
"""


def main():
    cards = []
    for recipe in RECIPES:
        path = RECIPES_DIR / f"{recipe['slug']}.html"
        path.write_text(render_page(recipe))
        cards.append(render_card(recipe))
        print(f"Wrote {path.name}")

    cards_path = ROOT / "scripts" / "thinh-recipe-cards.html"
    cards_path.write_text("\n".join(cards))
    print(f"Wrote card snippet to {cards_path.name}")


if __name__ == "__main__":
    main()
