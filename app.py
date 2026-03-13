import streamlit as st
import random
import re
import hashlib

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Cook de Staku - AI Recipe Generator",
    page_icon="🍳",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>
:root{
--bg-1:#ff6a00;
--bg-2:#ff8c00;
--bg-3:#ffb300;
--bg-4:#ffd54f;
--ink:#1a1a1a;
--accent:#3a0ca3;
--card:#ffffff;
--butter:#fff3cd;
--chat-user:#ffd1a1;
--chat-bot:#ffe39a;
--chat-border:rgba(0,0,0,0.12);
--input-bg:#ffe0b2;
--input-bg-strong:#ffd79a;
}

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;800;900&family=Source+Sans+3:wght@400;600;700&display=swap');

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,var(--bg-1),var(--bg-2),var(--bg-3),var(--bg-4));
background-attachment: fixed;
font-family: 'Source Sans 3', sans-serif;
color:var(--ink);
}

/* SUBTLE PATTERN OVERLAY */
[data-testid="stAppViewContainer"]::before{
content:"";
position:fixed;
inset:0;
background-image: radial-gradient(rgba(255,255,255,0.18) 1px, transparent 1px);
background-size: 18px 18px;
opacity:0.18;
pointer-events:none;
}

/* SIDEBAR */
[data-testid="stSidebar"]{
background: linear-gradient(180deg,var(--bg-2),var(--bg-3));
color:white;
font-weight:bold;
}

/* TITLES */
h1{
color:var(--accent);
font-weight:900;
font-size:3.2rem;
font-family:'Playfair Display', serif;
letter-spacing:0.5px;
text-shadow: 1px 1px 2px #ffb300;
}

h2,h3{
color:var(--accent);
font-weight:800;
text-shadow: 1px 1px 1px #ffa500;
font-family:'Playfair Display', serif;
}

/* BUTTON STYLE */
.stButton>button{
background: linear-gradient(90deg,#f77f00,#ffb300);
color:white;
border-radius:15px;
border:none;
height:3.2em;
font-weight:bold;
font-size:1.1rem;
transition:0.3s;
box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
}

.stButton>button:hover{
background: linear-gradient(90deg,#ff6a00,#ffb300);
transform:scale(1.05);
}

/* INPUT BOX */
.stTextInput>div>div>input{
border-radius:12px;
border:2px solid #ff8c00;
padding:8px;
font-size:1rem;
background:var(--input-bg);
}

/* CHAT INPUT */
div[data-testid="stChatInput"]{
background:#000000;
border-radius:16px;
padding:6px;
border:1px solid #000000;
}

div[data-testid="stChatInput"]>div{
background:transparent;
}

div[data-testid="stChatInput"] textarea{
border-radius:14px;
border:2px solid #000000;
padding:10px;
font-size:1rem;
background:#000000;
color:#ffffff;
}

/* RECIPE CARD */
.recipe-card{
background: rgba(255,255,255,0.96);
padding:25px;
border-radius:20px;
box-shadow: 0px 10px 25px rgba(0,0,0,0.25);
margin-top:20px;
transition: 0.3s;
border:1px solid rgba(255,255,255,0.5);
backdrop-filter: blur(2px);
}

.recipe-card:hover{
transform: scale(1.02);
}

/* USER CHAT BOX */
.chatbox{
background:var(--chat-user);
padding:18px;
border-radius:15px;
margin-top:10px;
box-shadow:0px 4px 12px rgba(0,0,0,0.15);
font-size:1rem;
border:1px solid var(--chat-border);
}

/* AI CHAT BOX */
.botbox{
background:var(--chat-bot);
padding:18px;
border-radius:15px;
margin-top:10px;
box-shadow:0px 4px 12px rgba(0,0,0,0.15);
font-size:1rem;
border:1px solid var(--chat-border);
}

/* CHAT MESSAGE */
.stChatMessage>div{
border-radius:15px;
}

div[data-testid="stChatMessage"]>div{
background:var(--chat-bot);
color:var(--ink);
border:1px solid var(--chat-border);
box-shadow: 0px 6px 14px rgba(0,0,0,0.12);
}

.stChatMessage.stChatMessageUser>div{
background:var(--chat-user);
}

.stChatMessage.stChatMessageAssistant>div{
background:var(--chat-bot);
}

/* INPUT BOX HIGHLIGHT */
.stTextInput>div>div>input:focus{
border:2px solid #ff6a00;
box-shadow:0 0 8px #ffa500;
}

div[data-testid="stChatInput"] textarea:focus{
border:2px solid #ff6a00;
box-shadow:0 0 8px #ffa500;
}

/* HORIZONTAL RULE */
hr{
border-top: 2px solid #ff8c00;
}

/* SECTION BADGE */
.section-badge{
display:inline-block;
padding:6px 12px;
border-radius:999px;
background:rgba(255,255,255,0.7);
border:1px solid rgba(255,255,255,0.9);
font-weight:700;
letter-spacing:0.3px;
}

/* SUBTLE ANIMATION */
@keyframes floatIn {
from { opacity:0; transform:translateY(6px); }
to { opacity:1; transform:translateY(0); }
}
.recipe-card, .botbox, .chatbox{
animation: floatIn 0.35s ease-out;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# TITLE
# -------------------------
st.title("🍳 Cook de Staku")
st.subheader("Smart Recipe Coach for Modern Home Cooks")

# -------------------------
# NAVIGATION
# -------------------------
st.write("### 🍽 Select Cook de Staku Mode")
col1, col2, col3 = st.columns(3)

if "mode" not in st.session_state:
    st.session_state.mode = "Generate Recipe"

with col1:
    if st.button("🍳 Recipe Generator"):
        st.session_state.mode = "Generate Recipe"

with col2:
    if st.button("🔄 Ingredient Substitute"):
        st.session_state.mode = "Ingredient Substitute"

with col3:
    if st.button("📅 Meal Planner"):
        st.session_state.mode = "Meal Planner"

mode = st.session_state.mode

# -------------------------
# SIDEBAR SETTINGS
# -------------------------
st.sidebar.title("⚙ Cooking Settings")

skill_level = st.sidebar.select_slider(
    "Cooking Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

servings = st.sidebar.number_input("Serving Size", 1, 10, 2)

diet = st.sidebar.multiselect(
    "Dietary Preference",
    ["Vegan", "Vegetarian", "Keto", "Gluten Free"]
)

st.sidebar.write("---")
st.sidebar.write("👨‍🍳 Team Summer Daze Members")
st.sidebar.write("👤 Nikolai Javier Jr.")
st.sidebar.write("👤 Claudine Margaret Ricablanca")
st.sidebar.write("👤 Gwyn Sapio")

st.sidebar.write("---")
st.sidebar.write("👨‍🍳 ChefDaze AI Response Team by (BINI x All Time Low)")
st.sidebar.write("👤💙 Jhoanna")
st.sidebar.write("👤💚 Colet")
st.sidebar.write("👤💛 Maloi")
st.sidebar.write("👤❤️ Mikha")
st.sidebar.write("👤🩷 Stacey")
st.sidebar.write("👤🩵 Aiah")
st.sidebar.write("👤🧡 Gwen")
st.sidebar.write("👤💜 Sheena")
st.sidebar.write("👤🤍 Alex Gaskarth")
st.sidebar.write("👤🩶 Jack Barakat")
st.sidebar.write("👤🖤 Zack Merrick")
st.sidebar.write("👤🤎 Rian Dawson")

# -------------------------
# SMART AI RECIPE FUNCTION
# -------------------------
def parse_ingredients(raw):
    if not raw:
        return []
    cleaned = re.sub(r"\s+(and|with|plus)\s+", ",", raw, flags=re.I)
    parts = re.split(r"[,\n;]+", cleaned)
    items = [p.strip() for p in parts if p.strip()]
    stop_words = {
        "a", "an", "the", "and", "or", "with", "plus", "for", "from", "to",
        "i", "me", "my", "we", "you", "your", "our", "can", "could", "would",
        "what", "how", "please", "give", "show", "need", "want", "have",
        "make", "cook", "recipe", "using", "use"
    }
    seen = set()
    result = []
    for item in items:
        words = re.findall(r"[a-zA-Z]+", item.lower())
        if not words:
            continue
        filtered = [w for w in words if w not in stop_words]
        if not filtered:
            continue
        cleaned_item = " ".join(filtered)
        key = cleaned_item.lower()
        if key not in seen:
            seen.add(key)
            result.append(cleaned_item)
    return result


def suggest_add_ons(ingredients_lower, existing_items):
    candidates = [
        "Onion",
        "Garlic",
        "Ginger",
        "Lemon or Lime",
        "Chili Flakes",
        "Fresh Herbs",
        "Cheese",
        "Nuts or Seeds",
        "Crunchy Breadcrumbs",
        "Yogurt",
        "Coconut Milk",
        "Tomato Sauce"
    ]
    existing_lower = {item.lower() for item in existing_items}
    picks = []
    for item in candidates:
        item_lower = item.lower()
        if item_lower not in ingredients_lower and item_lower not in existing_lower:
            picks.append(item)
    return picks[:6]


def stable_seed(text):
    digest = hashlib.md5(text.encode("utf-8")).hexdigest()
    return int(digest[:8], 16)


def seeded_choice(options, seed_value):
    if not options:
        return None
    rng = random.Random(seed_value)
    return rng.choice(options)


def generate_recipe(ingredients):
    ingredients_input = ingredients.strip()
    if not ingredients_input:
        return "Please enter a few ingredients so I can build a recipe."

    ingredients_lower = ingredients_input.lower()
    parsed_items = parse_ingredients(ingredients_input)
    display_items = [item.title() for item in parsed_items]
    display_name = ", ".join(display_items) if display_items else ingredients_input
    seed = stable_seed(ingredients_lower)

    base = f"### 🥗 Smart Recipe for: {display_name}\n\nServing Size: {servings}\n"

    # Default Prep & Cook Time
    prep = "Prep Time: 10 mins"
    cook = "Cook Time: 20 mins"

    profiles = []

    def add_profile(tag, name_options, core_ingredients, steps, method_label, method_pool=None):
        profiles.append({
            "tag": tag,
            "name_options": name_options,
            "ingredients": core_ingredients,
            "steps": steps,
            "method": method_label,
            "method_pool": method_pool
        })

    # Chicken-based
    if "chicken" in ingredients_lower:
        add_profile(
            "chicken",
            ["Soy Garlic Chicken", "Lemon Pepper Chicken", "Honey Chili Chicken"],
            ["Chicken", "Garlic", "Soy Sauce", "Cooking Oil", "Black Pepper"],
            [
                "Pat chicken dry and season with salt and pepper.",
                "Heat oil in a pan over medium-high heat.",
                "Cook chicken until browned and nearly cooked through.",
                "Add garlic and a splash of soy sauce, then toss.",
                "Simmer briefly and serve with a carb or vegetables."
            ],
            "Skillet",
            ["Skillet", "Sheet-Pan Roast", "Stir-Fry Bowl"]
        )
    # Pasta-based
    if "pasta" in ingredients_lower or "spaghetti" in ingredients_lower or "noodle" in ingredients_lower:
        add_profile(
            "pasta",
            ["Garlic Butter Pasta", "Tomato Basil Pasta", "Creamy Pepper Pasta"],
            ["Pasta", "Garlic", "Olive Oil", "Butter", "Parmesan Cheese"],
            [
                "Boil pasta until al dente and reserve a splash of water.",
                "Warm olive oil and butter in a pan.",
                "Add garlic and cook until fragrant.",
                "Toss pasta with the sauce and a little pasta water.",
                "Season and finish with cheese."
            ],
            "Skillet Pasta",
            ["Skillet Pasta", "Noodle Bowl"]
        )
    # Vegetable-based
    if any(x in ingredients_lower for x in ["vegetable", "broccoli", "carrot", "spinach", "zucchini", "mushroom"]):
        add_profile(
            "vegetable",
            ["Quick Veggie Stir-Fry", "Garlic Veggie Skillet", "Bright Lemon Veg Medley"],
            ["Mixed Vegetables", "Garlic", "Soy Sauce", "Olive Oil"],
            [
                "Heat oil in a pan over medium-high heat.",
                "Add vegetables and cook until crisp-tender.",
                "Stir in garlic and cook for 30 seconds.",
                "Add soy sauce or a splash of citrus and toss.",
                "Serve hot as a side or a light main."
            ],
            "Stir-Fry",
            ["Stir-Fry Bowl", "Skillet", "Soup", "Salad"]
        )
    # Beef-based
    if "beef" in ingredients_lower or "steak" in ingredients_lower:
        add_profile(
            "beef",
            ["Pepper Garlic Beef", "Soy Glaze Beef", "Chili Beef Skillet"],
            ["Beef", "Garlic", "Black Pepper", "Soy Sauce", "Cooking Oil"],
            [
                "Pat beef dry and season with salt and pepper.",
                "Heat oil in a pan until hot.",
                "Sear beef for 2-3 minutes per side.",
                "Add garlic and a splash of soy sauce.",
                "Rest briefly, then slice and serve."
            ],
            "Skillet",
            ["Skillet", "Stir-Fry Bowl", "Sheet-Pan Roast"]
        )
    # Pork-based
    if "pork" in ingredients_lower or "bacon" in ingredients_lower:
        add_profile(
            "pork",
            ["Garlic Pepper Pork", "Sweet Soy Pork", "Smoky Paprika Pork"],
            ["Pork", "Garlic", "Black Pepper", "Cooking Oil", "Salt"],
            [
                "Season pork with salt and pepper.",
                "Heat oil in a pan over medium-high heat.",
                "Cook pork until browned and cooked through.",
                "Add garlic and a spoon of sauce or spices.",
                "Serve with rice, potatoes, or vegetables."
            ],
            "Skillet",
            ["Skillet", "Sheet-Pan Roast", "Stir-Fry Bowl"]
        )
    # Tofu-based
    if "tofu" in ingredients_lower:
        add_profile(
            "tofu",
            ["Crispy Garlic Tofu", "Ginger Soy Tofu", "Chili Lime Tofu"],
            ["Tofu", "Soy Sauce", "Garlic", "Cornstarch", "Cooking Oil"],
            [
                "Pat tofu dry and cut into cubes.",
                "Toss with cornstarch, salt, and pepper.",
                "Pan-fry until golden on all sides.",
                "Add garlic and soy sauce, then toss.",
                "Serve with rice or vegetables."
            ],
            "Skillet",
            ["Skillet", "Stir-Fry Bowl", "Salad"]
        )
    # Shrimp-based
    if "shrimp" in ingredients_lower:
        add_profile(
            "shrimp",
            ["Lemon Butter Shrimp", "Garlic Chili Shrimp", "Herb Shrimp Skillet"],
            ["Shrimp", "Garlic", "Lemon", "Butter", "Olive Oil"],
            [
                "Pat shrimp dry and season with salt and pepper.",
                "Heat butter and oil in a pan.",
                "Cook shrimp 1-2 minutes per side.",
                "Add garlic and a squeeze of lemon.",
                "Serve immediately."
            ],
            "Skillet",
            ["Skillet", "Stir-Fry Bowl", "Grain Bowl"]
        )
    # Fish-based
    if any(x in ingredients_lower for x in ["fish", "salmon", "tuna"]):
        add_profile(
            "fish",
            ["Pan-Seared Lemon Fish", "Garlic Herb Fish", "Spiced Fish Skillet"],
            ["Fish", "Lemon", "Olive Oil", "Garlic", "Salt"],
            [
                "Season fish with salt and pepper.",
                "Heat oil in a pan over medium-high heat.",
                "Cook fish until flaky and opaque.",
                "Finish with lemon and garlic.",
                "Serve with a side of vegetables or rice."
            ],
            "Skillet",
            ["Skillet", "Sheet-Pan Roast", "Salad"]
        )
    # Egg-based
    if "egg" in ingredients_lower:
        egg_names = ["Veggie Egg Skillet", "Cheesy Egg Scramble"]
        if "rice" in ingredients_lower:
            egg_names.append("Quick Egg Fried Rice")
        add_profile(
            "egg",
            egg_names,
            ["Eggs", "Garlic", "Cooking Oil", "Salt", "Black Pepper"],
            [
                "Heat oil in a pan over medium heat.",
                "Add aromatics like garlic or onion, if using.",
                "Pour in beaten eggs and stir gently.",
                "Fold in vegetables or cooked rice if available.",
                "Season to taste and serve."
            ],
            "Skillet",
            ["Skillet", "Stir-Fry Bowl", "Grain Bowl"]
        )

    def gather(map_list):
        found = []
        for key, label in map_list:
            if key in ingredients_lower:
                found.append(label)
        return found

    def build_steps(method, protein, veg, carb):
        main = protein or "your main ingredients"
        veg_text = veg or "vegetables"
        carb_text = carb or "a carb of choice"
        if method == "Skillet Pasta":
            return [
                "Cook pasta until al dente and reserve a splash of water.",
                f"Warm oil in a pan and cook {main} until done.",
                f"Add {veg_text} and cook until tender.",
                "Toss pasta with the skillet and a splash of pasta water.",
                "Season and finish with cheese or herbs."
            ]
        if method == "Noodle Bowl":
            return [
                "Cook noodles until just tender and drain.",
                f"Cook {main} in a hot pan until browned.",
                f"Add {veg_text} and cook briefly.",
                "Toss everything with sauce and serve warm."
            ]
        if method == "Stir-Fry Bowl":
            return [
                f"Cook {main} in a hot pan until browned.",
                f"Add {veg_text} and stir-fry until crisp-tender.",
                "Add sauce and toss well.",
                f"Serve over {carb_text}."
            ]
        if method == "Grain Bowl":
            return [
                f"Cook {carb_text} until tender.",
                f"Cook {main} in a skillet with oil and seasoning.",
                f"Add {veg_text} and cook until just tender.",
                "Assemble in a bowl and finish with a drizzle of sauce."
            ]
        if method == "Sheet-Pan Roast":
            return [
                "Preheat oven to 400 F.",
                f"Toss {main} and {veg_text} with oil, salt, and pepper.",
                "Spread on a sheet pan and roast until browned.",
                "Finish with lemon or herbs and serve."
            ]
        if method == "Soup":
            return [
                "Heat oil in a pot and cook aromatics until soft.",
                f"Add {main} and cook briefly.",
                f"Add {veg_text} and enough liquid to cover.",
                "Simmer until everything is tender.",
                "Season to taste and serve hot."
            ]
        if method == "Salad":
            return [
                f"Cook {main} and let it cool slightly.",
                f"Chop {veg_text} and combine in a bowl.",
                "Add a simple dressing of oil, acid, and seasoning.",
                "Top with the protein and toss gently."
            ]
        if method == "Wrap":
            return [
                f"Cook {main} until done and season well.",
                f"Warm the wrap and add {veg_text}.",
                "Add sauce or dressing, then roll tightly.",
                "Slice and serve."
            ]
        if method == "Sandwich":
            return [
                f"Cook {main} until done and season well.",
                f"Toast bread and layer with {veg_text}.",
                "Add sauce or spread, then assemble.",
                "Slice and serve."
            ]
        if method == "Skillet Hash":
            return [
                "Cook potatoes in oil until golden and tender.",
                f"Add {main} and cook until done.",
                f"Stir in {veg_text} and cook briefly.",
                "Season and serve hot."
            ]
        return [
            "Prep ingredients: wash, chop, and pat dry as needed.",
            "Heat a pan with oil over medium heat.",
            f"Cook {main} until browned and nearly done.",
            f"Add {veg_text} and cook until tender.",
            "Season to taste and serve."
        ]

    selected = seeded_choice(profiles, seed)
    if selected:
        method_pool = selected.get("method_pool") or [selected["method"]]
        method_label = seeded_choice(method_pool, seed + 9) or selected["method"]
        recipe_name = seeded_choice(selected["name_options"], seed + 11)
        ingredient_list = list(selected["ingredients"])
        protein_hint = None
        veg_hint = None
        carb_hint = None
        if selected["tag"] in ["chicken", "beef", "pork", "tofu", "shrimp", "fish"]:
            protein_hint = selected["tag"].title()
        if selected["tag"] == "egg":
            protein_hint = "Eggs"
        if selected["tag"] == "vegetable":
            veg_hint = "vegetables"
        if selected["tag"] == "pasta":
            carb_hint = "pasta"
        instructions = build_steps(method_label, protein_hint, veg_hint, carb_hint)
    else:
        protein_map = [
            ("chicken", "Chicken"),
            ("beef", "Beef"),
            ("steak", "Beef"),
            ("pork", "Pork"),
            ("fish", "Fish"),
            ("salmon", "Salmon"),
            ("tuna", "Tuna"),
            ("shrimp", "Shrimp"),
            ("tofu", "Tofu"),
            ("egg", "Eggs"),
            ("beans", "Beans"),
            ("lentil", "Lentils"),
            ("chickpea", "Chickpeas"),
            ("turkey", "Turkey")
        ]
        carb_map = [
            ("rice", "Rice"),
            ("pasta", "Pasta"),
            ("noodle", "Noodles"),
            ("bread", "Bread"),
            ("tortilla", "Tortillas"),
            ("potato", "Potatoes"),
            ("quinoa", "Quinoa"),
            ("oat", "Oats")
        ]
        veg_map = [
            ("broccoli", "Broccoli"),
            ("carrot", "Carrot"),
            ("spinach", "Spinach"),
            ("tomato", "Tomato"),
            ("pepper", "Bell Pepper"),
            ("onion", "Onion"),
            ("garlic", "Garlic"),
            ("mushroom", "Mushroom"),
            ("zucchini", "Zucchini"),
            ("cabbage", "Cabbage"),
            ("corn", "Corn")
        ]
        proteins = gather(protein_map)
        carbs = gather(carb_map)
        veggies = gather(veg_map)

        protein_pick = seeded_choice(proteins, seed + 1)
        carb_pick = seeded_choice(carbs, seed + 2)
        veg_pick = seeded_choice(veggies, seed + 3)

        method_pool = []
        if any(x in ingredients_lower for x in ["pasta", "spaghetti", "noodle"]):
            method_pool += ["Skillet Pasta", "Noodle Bowl"]
        if any(x in ingredients_lower for x in ["rice", "quinoa"]):
            method_pool += ["Stir-Fry Bowl", "Grain Bowl"]
        if any(x in ingredients_lower for x in ["tortilla", "bread", "wrap"]):
            method_pool += ["Wrap", "Sandwich"]
        if "potato" in ingredients_lower:
            method_pool += ["Skillet Hash", "Sheet-Pan Roast"]
        if not method_pool:
            method_pool = ["Skillet", "Sheet-Pan Roast", "Soup", "Salad"]
        else:
            method_pool += ["Skillet", "Soup"]

        method_label = seeded_choice(method_pool, seed + 4) or "Skillet"

        main_name = protein_pick or veg_pick or "Pantry"
        if method_label in ["Wrap", "Sandwich"]:
            recipe_name = f"{main_name} {method_label}"
        else:
            recipe_name = f"{method_label} {main_name}"

        ingredient_list = [item for item in [
            protein_pick, veg_pick, carb_pick, "Garlic", "Olive Oil", "Salt", "Black Pepper"
        ] if item]
        instructions = build_steps(method_label, protein_pick, veg_pick, carb_pick)

    time_map = {
        "Skillet Pasta": ("Prep Time: 10 mins", "Cook Time: 15 mins"),
        "Noodle Bowl": ("Prep Time: 10 mins", "Cook Time: 12 mins"),
        "Stir-Fry Bowl": ("Prep Time: 12 mins", "Cook Time: 12 mins"),
        "Grain Bowl": ("Prep Time: 12 mins", "Cook Time: 18 mins"),
        "Sheet-Pan Roast": ("Prep Time: 15 mins", "Cook Time: 25 mins"),
        "Soup": ("Prep Time: 15 mins", "Cook Time: 30 mins"),
        "Salad": ("Prep Time: 12 mins", "Cook Time: 8 mins"),
        "Skillet Hash": ("Prep Time: 12 mins", "Cook Time: 20 mins"),
        "Skillet": ("Prep Time: 10 mins", "Cook Time: 15 mins"),
        "Wrap": ("Prep Time: 10 mins", "Cook Time: 10 mins"),
        "Sandwich": ("Prep Time: 8 mins", "Cook Time: 8 mins")
    }
    if method_label in time_map:
        prep, cook = time_map[method_label]

    # Other common ingredients
    if "rice" in ingredients_lower:
        ingredient_list.append("Rice")
    if "egg" in ingredients_lower:
        ingredient_list.append("Eggs")
    if "potato" in ingredients_lower:
        ingredient_list.append("Potatoes")

    # Ensure user ingredients are included
    ingredient_list += [item.title() for item in parsed_items]

    # Fallback instructions
    if not instructions:
        instructions = [
            "Prep all ingredients: wash, chop, and pat dry as needed.",
            "Heat a pan with a little oil over medium heat.",
            "Cook aromatics like onion or garlic until fragrant, if using.",
            "Add your main ingredients and cook until tender and cooked through.",
            "Season to taste with salt, pepper, and a sauce or acid.",
            "Finish with fresh herbs, citrus, or a drizzle of oil."
        ]

    # Remove duplicates
    ingredient_list = list(dict.fromkeys(ingredient_list))
    if not ingredient_list:
        ingredient_list = [
            "Any protein",
            "Any vegetable",
            "A carb (rice or pasta)",
            "Garlic or onion",
            "Oil or butter"
        ]

    sys_rng = random.SystemRandom()

    signature_options = [
        "Finish with a squeeze of lemon and a drizzle of olive oil.",
        "Top with chopped herbs and a sprinkle of cheese.",
        "Add a spoon of yogurt for a creamy finish.",
        "Sprinkle chili flakes for heat and color.",
        "Add toasted nuts or seeds for crunch."
    ]
    signature_finish = sys_rng.choice(signature_options)

    variation_options = [
        "Swap the protein for tofu and add sesame oil.",
        "Make it spicy with chili flakes or hot sauce.",
        "Turn it creamy with coconut milk or cream.",
        "Add a crunchy topping like breadcrumbs or nuts.",
        "Brighten it with lemon or lime zest."
    ]
    variation_count = 2 if len(variation_options) < 3 else sys_rng.randint(2, 3)
    variation_picks = sys_rng.sample(variation_options, min(variation_count, len(variation_options)))
    variations_text = "\n".join(f"- {v}" for v in variation_picks)

    # Format output
    ingredients_text = "\n".join(f"- {i}" for i in ingredient_list)
    instructions_text = "\n".join(f"{idx+1}. {step}" for idx, step in enumerate(instructions))
    add_ons = suggest_add_ons(ingredients_lower, ingredient_list)
    if len(add_ons) > 2:
        pick_count = sys_rng.randint(2, min(6, len(add_ons)))
        add_ons = sys_rng.sample(add_ons, pick_count)
    add_ons_text = "\n".join(f"- {i}" for i in add_ons)
    flavor_options = [
        "Savory: soy sauce + garlic + black pepper",
        "Bright: lemon + olive oil + fresh herbs",
        "Spicy: chili flakes + paprika + hot sauce",
        "Creamy: butter or yogurt + cheese",
        "Smoky: paprika + cumin + lime",
        "Sweet Heat: honey + chili + lime",
        "Herby: basil + parsley + olive oil"
    ]
    flavor_pick_count = 3 if len(flavor_options) >= 3 else len(flavor_options)
    flavor_picks = sys_rng.sample(flavor_options, flavor_pick_count)
    flavor_text = "\n".join(f"- {f}" for f in flavor_picks)

    recipe_text = f"""
{base}
**Recipe Name**  
{recipe_name}

**Method**  
{method_label}

{prep}  
{cook}  

**Ingredients**  
{ingredients_text}

**Instructions**  
{instructions_text}
"""
    if add_ons:
        recipe_text += f"""

**Optional Add-Ons**  
{add_ons_text}
"""
    recipe_text += f"""

**Flavor Options**  
{flavor_text}

**Signature Finish**  
{signature_finish}

**Variations**  
{variations_text}

**Chef Tip**  
Taste at the end and adjust salt, acid, or heat to match your preference.
"""
    return recipe_text

# -------------------------
# Ingredient Substitute
# -------------------------
def substitute_ingredient(question):
    question = question.lower()
    subs = {
        "egg": ["1/4 cup applesauce", "1 mashed banana", "1 tbsp flaxseed + 3 tbsp water", "Yogurt"],
        "milk": ["Almond milk", "Soy milk", "Oat milk", "Coconut milk"],
        "butter": ["Margarine", "Olive oil", "Coconut oil", "Avocado"],
        "sugar": ["Honey", "Maple syrup", "Agave nectar"],
        "flour": ["Oat flour", "Almond flour", "Coconut flour"]
    }
    for key, value in subs.items():
        if key in question:
            return f"🥚 {key.title()} Substitutes\n\n- " + "\n- ".join(value)
    return "Try specifying which ingredient you want to substitute."

# -------------------------
# Weekly Meal Plan
# -------------------------
def meal_plan():
    return """
📅 Simple Weekly Meal Plan

Monday – Chicken Stir Fry  
Tuesday – Garlic Butter Pasta  
Wednesday – Fried Rice  
Thursday – Grilled Chicken Salad  
Friday – Vegetable Stir Fry  
Saturday – Homemade Pizza  
Sunday – Soup and Sandwich
"""

# -------------------------
# Recipe Image
# -------------------------
def get_recipe_image(recipe_name):
    images = {
        "chicken": "https://images.unsplash.com/photo-1604908177522-040cbe7c5a67",
        "pasta": "https://images.unsplash.com/photo-1551183053-bf91a1d81141",
        "stir fry": "https://images.unsplash.com/photo-1604908177261-8f3ec5d5b3c2",
        "salad": "https://images.unsplash.com/photo-1546069901-ba9599a7e63"
    }
    for key in images:
        if key in recipe_name.lower():
            return images[key]
    return "https://images.unsplash.com/photo-1495195134817-aeb325a55b65"

# -------------------------
# Nutrition Calculator
# -------------------------
def nutrition_estimate(ingredients):
    ingredients = ingredients.lower()
    calories = 0
    protein = 0
    if "chicken" in ingredients: calories += 250; protein += 30
    if "beef" in ingredients or "steak" in ingredients: calories += 300; protein += 26
    if "pork" in ingredients or "bacon" in ingredients: calories += 280; protein += 25
    if "turkey" in ingredients: calories += 200; protein += 28
    if "tofu" in ingredients: calories += 150; protein += 15
    if "shrimp" in ingredients: calories += 120; protein += 20
    if "fish" in ingredients or "salmon" in ingredients or "tuna" in ingredients: calories += 220; protein += 24
    if "beans" in ingredients or "lentil" in ingredients or "chickpea" in ingredients: calories += 160; protein += 9
    if "pasta" in ingredients: calories += 200; protein += 7
    if "rice" in ingredients: calories += 180
    if "quinoa" in ingredients: calories += 120; protein += 4
    if "bread" in ingredients or "tortilla" in ingredients: calories += 140; protein += 4
    if "potato" in ingredients: calories += 160
    if "butter" in ingredients: calories += 100
    if "cheese" in ingredients: calories += 110; protein += 7
    if "egg" in ingredients: calories += 70; protein += 6
    if "milk" in ingredients or "yogurt" in ingredients: calories += 60; protein += 3
    if "garlic" in ingredients: calories += 5
    return f"""
🥗 Estimated Nutrition (per serving)

Calories: {calories} kcal  
Protein: {protein} g  
Carbohydrates: ~30 g  
Fat: ~10 g
"""

# -------------------------
# Grocery List
# -------------------------
def grocery_list(ingredients):
    items = ingredients.split(",")
    grocery = "\n".join([f"- {item.strip().title()}" for item in items if item])
    return f"""
🛒 Grocery List

{grocery}

Tip: Check your pantry before shopping!
"""

# -------------------------
# MAIN CONTENT
# -------------------------
if mode == "Generate Recipe":
    st.write("## 🧾 Enter Ingredients")
    ingredients = st.text_input("Example: chicken, garlic, rice, broccoli")
    if st.button("Generate Recipe"):
        recipe = generate_recipe(ingredients)
        image = get_recipe_image(ingredients)
        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
        st.image(image, use_container_width=True, caption="🍽 Your Dish Preview")
        st.markdown(recipe)
        st.markdown(nutrition_estimate(ingredients))
        st.markdown(grocery_list(ingredients))
        st.markdown('</div>', unsafe_allow_html=True)
        st.success("Recipe generated by Cook de Staku!")

elif mode == "Ingredient Substitute":
    st.write("## 🔄 Ingredient Substitute")
    question = st.text_input("Example: What can I use instead of eggs?")
    if st.button("Find Substitute"):
        response = substitute_ingredient(question)
        st.markdown('<div class="botbox">', unsafe_allow_html=True)
        st.write("👨‍🍳 Cook de Staku AI:")
        st.write(response)
        st.markdown('</div>', unsafe_allow_html=True)

elif mode == "Meal Planner":
    st.write("## 📅 Weekly Meal Planner")
    if st.button("Generate Meal Plan"):
        plan = meal_plan()
        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
        st.write(plan)
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# ChatGPT-Style Chat Interface with 12 Personas
# -------------------------
st.write("---")
st.write("## 💬 Chat with ChefDaze AI")

personas = {
    "Jhoanna": "💙",
    "Colet": "💚",
    "Maloi": "💛",
    "Mikha": "❤️",
    "Stacey": "🩷",
    "Aiah": "🩵",
    "Gwen": "🧡",
    "Sheena": "💜",
    "Alex": "🤍",
    "Jack": "🩶",
    "Zack": "🖤",
    "Rian": "🤎"
}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_chat = st.chat_input("Ask anything about cooking or recipes...")

if user_chat:
    st.session_state.chat_history.append(("user", user_chat))
    
    persona_name, persona_icon = random.choice(list(personas.items()))
    
    if "substitute" in user_chat.lower():
        response = substitute_ingredient(user_chat)
    elif "meal plan" in user_chat.lower():
        response = meal_plan()
    else:
        response = generate_recipe(user_chat)
    
    st.session_state.chat_history.append(("assistant", persona_name, persona_icon, response))

for message in st.session_state.chat_history:
    if message[0] == "user":
        with st.chat_message("user"):
            st.write(message[1])
    else:
        _, persona_name, persona_icon, text = message
        with st.chat_message("assistant"):
            st.markdown(f"**{persona_icon} {persona_name}:** {text}")
