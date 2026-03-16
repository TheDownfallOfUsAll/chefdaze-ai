import streamlit as st
import random
import re


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
--bg-1:#fff7ed;
--bg-2:#ffedd5;
--bg-3:#fde68a;
--bg-4:#fecaca;
--ink:#1f1b16;
--muted:#5c4a3a;
--accent:#b45309;
--accent-2:#0f766e;
--card:rgba(255,255,255,0.9);
--card-strong:#ffffff;
--butter:#fff3cd;
--chat-user:#ffe6c7;
--chat-bot:#fff2d6;
--chat-border:rgba(31,27,22,0.12);
--input-bg:#fff7d6;
--input-bg-strong:#ffe4a3;
--focus:#f59e0b;
--shadow-sm:0 4px 12px rgba(31,27,22,0.12);
--shadow-md:0 12px 28px rgba(31,27,22,0.18);
}

@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@700;900&family=Manrope:wght@400;600;700&display=swap');

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"]{
background:
radial-gradient(circle at 8% 8%, rgba(255,255,255,0.85) 0%, rgba(255,255,255,0.4) 25%, transparent 45%),
linear-gradient(135deg,var(--bg-1),var(--bg-2),var(--bg-3),var(--bg-4));
background-attachment: fixed;
font-family: 'Manrope', sans-serif;
color:var(--ink);
}

/* SUBTLE PATTERN OVERLAY */
[data-testid="stAppViewContainer"]::before{
content:"";
position:fixed;
inset:0;
background-image:
linear-gradient(120deg, rgba(255,255,255,0.28) 0, rgba(255,255,255,0.28) 1px, transparent 1px, transparent 16px),
radial-gradient(rgba(31,27,22,0.08) 1px, transparent 1px);
background-size: 24px 24px, 18px 18px;
opacity:0.35;
pointer-events:none;
}

/* SIDEBAR */
[data-testid="stSidebar"]{
background: linear-gradient(180deg,#fde68a,#f7b267);
color:var(--ink);
font-weight:700;
}

[data-testid="stSidebar"] *{
color:var(--ink);
}

/* TITLES */
h1{
color:var(--accent);
font-weight:900;
font-size:3.1rem;
font-family:'Fraunces', serif;
letter-spacing:0.4px;
text-shadow: 0 2px 10px rgba(180,83,9,0.2);
}

h2,h3{
color:var(--accent-2);
font-weight:800;
text-shadow: 0 1px 6px rgba(15,118,110,0.15);
font-family:'Fraunces', serif;
}

/* BUTTON STYLE */
.stButton>button{
background: linear-gradient(90deg,#fde68a,#f59e0b);
color:var(--ink);
border-radius:14px;
border:1px solid rgba(31,27,22,0.15);
height:3em;
font-weight:700;
font-size:1rem;
transition:0.25s ease;
box-shadow: var(--shadow-sm);
}

.stButton>button:hover{
background: linear-gradient(90deg,#ffe39a,#f59e0b);
transform:translateY(-2px);
box-shadow: var(--shadow-md);
}

/* INPUT BOX */
.stTextInput>div>div>input,
.stTextArea>div>div>textarea,
.stNumberInput input,
div[data-baseweb="select"] input{
border-radius:12px;
border:2px solid var(--input-bg-strong);
padding:10px;
font-size:1rem;
background:var(--input-bg);
color:var(--ink);
}

.stTextInput>div>div>input::placeholder,
.stTextArea>div>div>textarea::placeholder{
color:rgba(31,27,22,0.55);
}

/* CHAT INPUT */
div[data-testid="stChatInput"]{
background:var(--input-bg);
border-radius:16px;
padding:6px;
border:1px solid var(--input-bg-strong);
}

div[data-testid="stChatInput"]>div{
background:transparent;
}

div[data-testid="stChatInput"] textarea{
border-radius:14px;
border:2px solid var(--input-bg-strong);
padding:10px;
font-size:1rem;
background:var(--input-bg);
color:var(--ink);
}

div[data-testid="stChatInput"] textarea::placeholder{
color:rgba(31,27,22,0.55);
}

/* RECIPE CARD */
.recipe-card{
background: var(--card);
padding:24px;
border-radius:20px;
box-shadow: var(--shadow-md);
margin-top:20px;
transition: 0.25s ease;
border:1px solid rgba(255,255,255,0.7);
backdrop-filter: blur(6px);
}

.recipe-card:hover{
transform: translateY(-2px);
}

/* USER CHAT BOX */
.chatbox{
background:var(--chat-user);
padding:18px;
border-radius:15px;
margin-top:10px;
box-shadow:var(--shadow-sm);
font-size:1rem;
border:1px solid var(--chat-border);
}

/* AI CHAT BOX */
.botbox{
background:var(--chat-bot);
padding:18px;
border-radius:15px;
margin-top:10px;
box-shadow:var(--shadow-sm);
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
box-shadow: var(--shadow-sm);
}

.stChatMessage.stChatMessageUser>div{
background:var(--chat-user);
}

.stChatMessage.stChatMessageAssistant>div{
background:var(--chat-bot);
}

/* INPUT BOX HIGHLIGHT */
.stTextInput>div>div>input:focus,
.stTextArea>div>div>textarea:focus,
.stNumberInput input:focus,
div[data-testid="stChatInput"] textarea:focus{
border:2px solid var(--focus);
box-shadow:0 0 8px rgba(245,158,11,0.4);
}

/* HORIZONTAL RULE */
hr{
border-top: 2px solid rgba(245,158,11,0.6);
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


def build_rng(seed_value=None):
    if seed_value is None:
        return random.SystemRandom()
    return random.Random(seed_value)


def generate_recipe(ingredients, seed_value=None):
    ingredients_input = ingredients.strip()
    if not ingredients_input:
        return "Please enter a few ingredients so I can build a recipe.", None, None

    rng = build_rng(seed_value)

    ingredients_lower = ingredients_input.lower()
    parsed_items = parse_ingredients(ingredients_input)
    display_items = [item.title() for item in parsed_items]
    display_name = ", ".join(display_items) if display_items else ingredients_input.strip()

    base = f"### 🥗 Smart Recipe for: {display_name}\n\nServing Size: {servings}\nSkill Level: {skill_level}\n"
    if diet:
        base += f"Diet Preferences: {', '.join(diet)}\n"

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
            [
                "Soy Garlic Chicken",
                "Lemon Pepper Chicken",
                "Honey Chili Chicken",
                "Ginger Lime Chicken",
                "Smoky Paprika Chicken",
                "Herb Butter Chicken"
            ],
            ["Chicken", "Garlic", "Soy Sauce", "Cooking Oil", "Black Pepper"],
            [
                "Pat chicken dry and season with salt and pepper.",
                "Heat oil in a pan over medium-high heat.",
                "Cook chicken until browned and nearly cooked through.",
                "Add garlic and a splash of soy sauce, then toss.",
                "Simmer briefly and serve with a carb or vegetables."
            ],
            "Skillet",
            ["Skillet", "Sheet-Pan Roast", "Stir-Fry Bowl", "Grain Bowl"]
        )
    # Pasta-based
    if "pasta" in ingredients_lower or "spaghetti" in ingredients_lower or "noodle" in ingredients_lower:
        add_profile(
            "pasta",
            [
                "Garlic Butter Pasta",
                "Tomato Basil Pasta",
                "Creamy Pepper Pasta",
                "Lemon Herb Pasta",
                "Chili Olive Oil Pasta",
                "Roasted Veg Pasta"
            ],
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
            [
                "Quick Veggie Stir-Fry",
                "Garlic Veggie Skillet",
                "Bright Lemon Veg Medley",
                "Sesame Veggie Bowl",
                "Roasted Market Veg",
                "Spicy Veggie Saute"
            ],
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
            [
                "Pepper Garlic Beef",
                "Soy Glaze Beef",
                "Chili Beef Skillet",
                "Ginger Beef Stir-Fry",
                "Smoky Beef Skillet"
            ],
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
            [
                "Garlic Pepper Pork",
                "Sweet Soy Pork",
                "Smoky Paprika Pork",
                "Honey Garlic Pork",
                "Citrus Herb Pork"
            ],
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
            [
                "Crispy Garlic Tofu",
                "Ginger Soy Tofu",
                "Chili Lime Tofu",
                "Sesame Tofu Bowl",
                "Maple Pepper Tofu"
            ],
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
            [
                "Lemon Butter Shrimp",
                "Garlic Chili Shrimp",
                "Herb Shrimp Skillet",
                "Paprika Lime Shrimp",
                "Ginger Shrimp Bowl"
            ],
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
            [
                "Pan-Seared Lemon Fish",
                "Garlic Herb Fish",
                "Spiced Fish Skillet",
                "Citrus Pepper Fish",
                "Miso Glaze Fish"
            ],
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
        egg_names = ["Veggie Egg Skillet", "Cheesy Egg Scramble", "Herb Egg Hash"]
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

    def pick(options):
        return rng.choice(options) if options else None

    selected = pick(profiles)
    if selected:
        method_pool = selected.get("method_pool") or [selected["method"]]
        method_label = pick(method_pool) or selected["method"]
        recipe_name = pick(selected["name_options"])
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

        protein_pick = pick(proteins)
        carb_pick = pick(carbs)
        veg_pick = pick(veggies)

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

        method_label = pick(method_pool) or "Skillet"

        main_name = protein_pick or veg_pick or "Pantry"
        if method_label in ["Wrap", "Sandwich"]:
            recipe_name = f"{main_name} {method_label}"
        else:
            recipe_name = f"{method_label} {main_name}"

        adjectives = ["Quick", "Cozy", "Bright", "Smoky", "Herb", "Zesty", "Savory"]
        if rng.random() < 0.7:
            recipe_name = f"{rng.choice(adjectives)} {recipe_name}"

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

    signature_options = [
        "Finish with a squeeze of lemon and a drizzle of olive oil.",
        "Top with chopped herbs and a sprinkle of cheese.",
        "Add a spoon of yogurt for a creamy finish.",
        "Sprinkle chili flakes for heat and color.",
        "Add toasted nuts or seeds for crunch."
    ]
    signature_finish = rng.choice(signature_options)

    variation_options = [
        "Swap the protein for tofu and add sesame oil.",
        "Make it spicy with chili flakes or hot sauce.",
        "Turn it creamy with coconut milk or cream.",
        "Add a crunchy topping like breadcrumbs or nuts.",
        "Brighten it with lemon or lime zest."
    ]
    variation_count = 2 if len(variation_options) < 3 else rng.randint(2, 3)
    variation_picks = rng.sample(variation_options, min(variation_count, len(variation_options)))
    variations_text = "\n".join(f"- {v}" for v in variation_picks)

    # Format output
    ingredients_text = "\n".join(f"- {i}" for i in ingredient_list)
    instructions_text = "\n".join(f"{idx+1}. {step}" for idx, step in enumerate(instructions))
    add_ons = suggest_add_ons(ingredients_lower, ingredient_list)
    if len(add_ons) > 2:
        pick_count = rng.randint(2, min(6, len(add_ons)))
        add_ons = rng.sample(add_ons, pick_count)
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
    flavor_picks = rng.sample(flavor_options, flavor_pick_count)
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
    signature = f"{recipe_name}|{method_label}|{display_name}"
    return recipe_text, signature, recipe_name

# -------------------------
# Ingredient Substitute
# -------------------------
def clean_ingredient_name(text):
    if not text:
        return ""
    text = re.sub(r"[^a-zA-Z\s]", " ", text.lower())
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    stop_words = {
        "a", "an", "the", "and", "or", "with", "for", "to", "instead", "of",
        "use", "using", "substitute", "replace", "swap", "can", "i", "you",
        "your", "my", "please", "what", "which", "is", "are", "in", "on"
    }
    words = [w for w in text.split() if w not in stop_words]
    if not words:
        return ""
    if len(words) >= 2:
        candidate = " ".join(words[-2:])
    else:
        candidate = words[0]
    if candidate.endswith("ies"):
        candidate = candidate[:-3] + "y"
    elif candidate.endswith("s") and not candidate.endswith("ss"):
        candidate = candidate[:-1]
    return candidate.strip()


def extract_ingredient_name(question):
    if not question:
        return ""
    text = question.lower()
    if "," in text:
        text = text.split(",")[0]
    patterns = [
        r"instead of ([a-zA-Z\s]+)",
        r"substitute for ([a-zA-Z\s]+)",
        r"replace ([a-zA-Z\s]+)",
        r"swap ([a-zA-Z\s]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return clean_ingredient_name(match.group(1))
    return clean_ingredient_name(text)


def detect_category(ingredient):
    ingredient_lower = ingredient.lower()
    protein_keys = {
        "chicken", "beef", "pork", "fish", "salmon", "tuna", "shrimp",
        "tofu", "tempeh", "egg", "bean", "lentil", "chickpea", "turkey"
    }
    dairy_keys = {"milk", "cream", "butter", "cheese", "yogurt"}
    grain_keys = {"rice", "pasta", "noodle", "bread", "flour", "oat", "quinoa", "tortilla"}
    veg_keys = {
        "spinach", "broccoli", "carrot", "zucchini", "mushroom", "pepper",
        "onion", "tomato", "cabbage", "cauliflower", "potato", "eggplant"
    }
    sweetener_keys = {"sugar", "honey", "maple", "agave", "syrup"}
    fat_keys = {"oil", "butter", "ghee", "lard"}
    acid_keys = {"vinegar", "lemon", "lime"}
    herb_keys = {"basil", "parsley", "cilantro", "mint", "rosemary", "thyme", "dill"}
    spice_keys = {"cumin", "paprika", "chili", "pepper", "curry", "turmeric", "cinnamon", "ginger"}
    thickener_keys = {"cornstarch", "arrowroot", "starch"}

    if any(k in ingredient_lower for k in protein_keys):
        return "protein"
    if any(k in ingredient_lower for k in dairy_keys):
        return "dairy"
    if any(k in ingredient_lower for k in grain_keys):
        return "grain"
    if any(k in ingredient_lower for k in veg_keys):
        return "vegetable"
    if any(k in ingredient_lower for k in sweetener_keys):
        return "sweetener"
    if any(k in ingredient_lower for k in fat_keys):
        return "fat"
    if any(k in ingredient_lower for k in acid_keys):
        return "acid"
    if any(k in ingredient_lower for k in herb_keys):
        return "herb"
    if any(k in ingredient_lower for k in spice_keys):
        return "spice"
    if any(k in ingredient_lower for k in thickener_keys):
        return "thickener"
    return "general"


def substitute_ingredient(question):
    ingredient = extract_ingredient_name(question)
    if not ingredient:
        return "Please enter an ingredient you want to substitute."

    rng = random.SystemRandom()

    alias_map = {
        "bell pepper": "pepper",
        "capsicum": "pepper",
        "scallion": "green onion",
        "green onion": "onion",
        "spring onion": "onion",
        "chicken breast": "chicken",
        "chicken thigh": "chicken",
        "ground beef": "beef",
        "minced beef": "beef",
        "ground pork": "pork"
    }
    key = alias_map.get(ingredient, ingredient)

    subs_catalog = {
        "egg": ["1/4 cup applesauce", "1 mashed banana", "1 tbsp flaxseed + 3 tbsp water", "Aquafaba (3 tbsp)", "Silken tofu"],
        "milk": ["Almond milk", "Soy milk", "Oat milk", "Coconut milk", "Half-and-half + water"],
        "butter": ["Olive oil", "Coconut oil", "Ghee", "Avocado oil", "Plant-based butter"],
        "sugar": ["Honey", "Maple syrup", "Agave nectar", "Brown sugar", "Coconut sugar"],
        "flour": ["Oat flour", "Almond flour", "Rice flour", "Coconut flour", "All-purpose flour"],
        "cream": ["Coconut cream", "Greek yogurt", "Half-and-half", "Cashew cream"],
        "yogurt": ["Sour cream", "Greek yogurt", "Coconut yogurt", "Buttermilk"],
        "cheese": ["Nutritional yeast", "Vegan cheese", "Feta", "Parmesan"],
        "soy sauce": ["Tamari", "Coconut aminos", "Worcestershire", "Fish sauce (use less)"],
        "garlic": ["Garlic powder", "Shallot", "Onion", "Chive"],
        "onion": ["Shallot", "Leek", "Scallion", "Onion powder"],
        "tomato": ["Crushed tomatoes", "Tomato paste + water", "Roasted red pepper", "Salsa"],
        "lemon": ["Lime", "Vinegar", "White wine", "Yuzu"],
        "lime": ["Lemon", "Vinegar", "Rice vinegar", "Yuzu"],
        "vinegar": ["Lemon juice", "Lime juice", "Apple cider vinegar", "White wine vinegar"],
        "rice": ["Quinoa", "Cauliflower rice", "Couscous", "Barley"],
        "pasta": ["Zoodles", "Rice noodles", "Spaghetti squash", "Gnocchi"],
        "bread": ["Tortilla", "Pita", "Lettuce wrap", "Rice cakes"],
        "chicken": ["Turkey", "Tofu", "Mushrooms", "Chickpeas"],
        "beef": ["Pork", "Turkey", "Mushrooms", "Lentils"],
        "pork": ["Chicken", "Turkey", "Tofu", "Mushrooms"],
        "fish": ["Shrimp", "Chicken", "Tofu", "Mushrooms"],
        "shrimp": ["Chicken", "Tofu", "Scallops", "Mushrooms"],
        "tofu": ["Tempeh", "Chickpeas", "Mushrooms", "Eggs"],
        "mushroom": ["Eggplant", "Zucchini", "Bell pepper", "Tofu"],
        "spinach": ["Kale", "Chard", "Arugula", "Bok choy"],
        "broccoli": ["Cauliflower", "Green beans", "Asparagus", "Brussels sprouts"],
        "carrot": ["Parsnip", "Sweet potato", "Pumpkin", "Zucchini"],
        "potato": ["Sweet potato", "Cauliflower", "Parsnip", "Turnip"],
        "oil": ["Olive oil", "Avocado oil", "Canola oil", "Ghee"],
        "olive oil": ["Avocado oil", "Canola oil", "Ghee", "Butter"]
    }

    category_subs = {
        "protein": ["Tofu", "Tempeh", "Chickpeas", "Lentils", "Mushrooms"],
        "dairy": ["Coconut milk", "Cashew cream", "Plant-based yogurt", "Evaporated milk"],
        "grain": ["Rice", "Quinoa", "Potatoes", "Cauliflower rice"],
        "vegetable": ["Zucchini", "Eggplant", "Bell pepper", "Cauliflower"],
        "sweetener": ["Honey", "Maple syrup", "Agave", "Brown sugar"],
        "fat": ["Olive oil", "Avocado oil", "Butter", "Ghee"],
        "acid": ["Lemon juice", "Lime juice", "Apple cider vinegar", "White wine vinegar"],
        "herb": ["Parsley", "Cilantro", "Basil", "Dill"],
        "spice": ["Cumin", "Paprika", "Chili flakes", "Coriander"],
        "thickener": ["Cornstarch", "Arrowroot", "Flour", "Potato starch"],
        "general": ["Shallot", "Garlic", "Leek", "Bell pepper"]
    }

    options = subs_catalog.get(key)
    category = detect_category(key)
    if not options:
        options = category_subs.get(category, category_subs["general"])

    options = [item for item in options if item.lower() != key.lower()]
    options = list(dict.fromkeys(options))
    pick_count = min(4, len(options)) if options else 0
    if pick_count == 0:
        options = category_subs["general"]
        pick_count = min(4, len(options))

    picks = rng.sample(options, pick_count)
    substitutes_text = "\n".join(f"- {item}" for item in picks)

    idea_templates = {
        "protein": [
            "Skillet {ingredient} with garlic and herbs",
            "{ingredient} stir-fry with vegetables",
            "{ingredient} grain bowl with a quick sauce",
            "Roasted {ingredient} with lemon and olive oil"
        ],
        "vegetable": [
            "Roasted {ingredient} with olive oil and herbs",
            "{ingredient} stir-fry with garlic and soy sauce",
            "Sheet-pan {ingredient} with potatoes",
            "{ingredient} soup with onions and broth"
        ],
        "grain": [
            "{ingredient} bowl with vegetables and sauce",
            "{ingredient} fried rice with eggs or tofu",
            "Warm {ingredient} salad with herbs",
            "One-pan {ingredient} and veggies"
        ],
        "dairy": [
            "Creamy pasta using {ingredient}",
            "Baked casserole with {ingredient}",
            "Smoothie with {ingredient} and fruit",
            "Dip or sauce using {ingredient}"
        ],
        "sweetener": [
            "Stir {ingredient} into oatmeal or yogurt",
            "Bake {ingredient} into muffins or cookies",
            "Use {ingredient} in a simple vinaigrette",
            "Sweeten a fruit compote with {ingredient}"
        ],
        "spice": [
            "Season roasted vegetables with {ingredient}",
            "Mix {ingredient} into a quick marinade",
            "Stir {ingredient} into soup or stew",
            "Sprinkle {ingredient} over eggs or tofu"
        ],
        "herb": [
            "Finish a salad with {ingredient}",
            "Blend {ingredient} into a simple sauce",
            "Add {ingredient} to pasta or grain bowls",
            "Top roasted vegetables with {ingredient}"
        ],
        "fat": [
            "Saute aromatics in {ingredient}",
            "Use {ingredient} for a quick dressing",
            "Roast vegetables with {ingredient}",
            "Finish a soup with a drizzle of {ingredient}"
        ],
        "acid": [
            "Make a bright vinaigrette with {ingredient}",
            "Add {ingredient} to soups for balance",
            "Marinate proteins with {ingredient}",
            "Finish roasted vegetables with {ingredient}"
        ],
        "general": [
            "Quick skillet with {ingredient} and vegetables",
            "Roasted {ingredient} with olive oil and herbs",
            "Simple bowl with {ingredient} and rice",
            "{ingredient} soup with garlic and broth"
        ]
    }

    templates = idea_templates.get(category, idea_templates["general"])
    idea_count = 2 if len(templates) >= 2 else len(templates)
    ideas = rng.sample(templates, idea_count)
    ingredient_title = ingredient.title()
    ideas_text = "\n".join(f"- {tmpl.format(ingredient=ingredient_title)}" for tmpl in ideas)

    return (
        f"Substitutes for {ingredient_title}\n\n"
        f"{substitutes_text}\n\n"
        f"Quick recipe ideas\n"
        f"{ideas_text}"
    )

# -------------------------
# Weekly Meal Plan
# -------------------------
def meal_plan():
    rng = random.SystemRandom()

    base_pool = [
        "Garlic Lemon Chicken",
        "Veggie Stir-Fry",
        "Tomato Basil Pasta",
        "Beef and Broccoli Bowl",
        "Shrimp Rice Bowl",
        "Sheet-Pan Sausage and Veg",
        "Turkey Chili",
        "Tofu Grain Bowl",
        "Salmon with Roasted Veg",
        "Chicken Fajita Wraps",
        "Veggie Fried Rice",
        "Greek Salad with Pita",
        "Chickpea Curry",
        "BBQ Chicken Bowl",
        "Roasted Veggie Pasta",
        "Bean and Cheese Quesadillas",
        "Chicken Soup",
        "Stir-Fry Noodles",
        "Stuffed Peppers",
        "Veggie Burrito Bowl"
    ]

    vegan_pool = [
        "Chickpea Curry",
        "Tofu Stir-Fry",
        "Lentil Stew",
        "Veggie Buddha Bowl",
        "Roasted Veggie Pasta",
        "Black Bean Tacos",
        "Mushroom Fried Rice",
        "Sweet Potato Chili",
        "Quinoa Veggie Bowl",
        "Coconut Veggie Soup",
        "Sesame Noodle Bowl",
        "Veggie Burrito Bowl"
    ]

    vegetarian_pool = [
        "Caprese Pasta",
        "Veggie Omelet",
        "Spinach and Feta Wrap",
        "Mushroom Risotto",
        "Cheese Quesadillas",
        "Tomato Basil Pasta",
        "Greek Salad with Pita",
        "Veggie Fried Rice",
        "Paneer Stir-Fry",
        "Eggplant Parmesan",
        "Veggie Burrito Bowl",
        "Potato and Pepper Skillet"
    ]

    keto_pool = [
        "Garlic Butter Chicken",
        "Zucchini Noodles with Pesto",
        "Beef Stir-Fry",
        "Salmon with Asparagus",
        "Cauliflower Fried Rice",
        "Egg and Spinach Skillet",
        "Chicken Salad Lettuce Wraps",
        "Pork Chop with Greens",
        "Shrimp and Broccoli",
        "Turkey Lettuce Wraps",
        "Cheesy Cauliflower Bake",
        "Zucchini Beef Skillet"
    ]

    gluten_free_pool = [
        "Grilled Chicken with Rice",
        "Shrimp Rice Bowl",
        "Salmon with Roasted Veg",
        "Beef and Broccoli Bowl",
        "Stuffed Peppers",
        "Veggie Fried Rice",
        "Turkey Chili",
        "Chicken Soup",
        "Quinoa Veggie Bowl",
        "Cauliflower Fried Rice",
        "Potato and Pepper Skillet",
        "Chickpea Curry"
    ]

    pool = base_pool
    if "Vegan" in diet:
        pool = vegan_pool
    elif "Vegetarian" in diet:
        pool = vegetarian_pool
    elif "Keto" in diet:
        pool = keto_pool
    elif "Gluten Free" in diet:
        pool = gluten_free_pool

    if len(pool) < 7:
        pool = base_pool

    picks = rng.sample(pool, 7) if len(pool) >= 7 else [rng.choice(pool) for _ in range(7)]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    header = "Simple Weekly Meal Plan"
    if diet:
        header += f" ({', '.join(diet)})"

    lines = "\n".join(f"- {day}: {meal}" for day, meal in zip(days, picks))
    return f"""
{header}

{lines}
"""

# -------------------------
# Recipe Image
# -------------------------
def get_recipe_image(recipe_name):
    if not recipe_name:
        return "https://images.unsplash.com/photo-1495195134817-aeb325a55b65"
    images = {
        "chicken": "https://images.unsplash.com/photo-1604908177522-040cbe7c5a67",
        "pasta": "https://images.unsplash.com/photo-1551183053-bf91a1d81141",
        "stir fry": "https://images.unsplash.com/photo-1604908177261-8f3ec5d5b3c2",
        "salad": "https://images.unsplash.com/photo-1546069901-ba9599a7e63",
        "beef": "https://images.unsplash.com/photo-1544025162-d76694265947",
        "pork": "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
        "shrimp": "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
        "fish": "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
        "tofu": "https://images.unsplash.com/photo-1473093226795-af9932fe5856",
        "rice": "https://images.unsplash.com/photo-1604908177261-8f3ec5d5b3c2"
    }
    name = recipe_name.lower()
    for key in images:
        if key in name:
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
    ingredients = st.text_input(
        "Ingredients",
        help="Separate items with commas. Example: chicken, garlic, rice, broccoli."
    )
    if st.button("Generate Recipe"):
        recipe_text, signature, recipe_name = generate_recipe(ingredients)
        last_signature = st.session_state.get("last_recipe_signature")
        attempts = 0
        while signature and signature == last_signature and attempts < 2:
            recipe_text, signature, recipe_name = generate_recipe(ingredients)
            attempts += 1
        st.session_state.last_recipe_signature = signature

        if not signature:
            st.warning(recipe_text)
        else:
            image = get_recipe_image(recipe_name or ingredients)
            st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
            st.image(image, use_container_width=True, caption="Your Dish Preview")
            st.markdown(recipe_text)
            st.markdown(nutrition_estimate(ingredients))
            st.markdown(grocery_list(ingredients))
            st.markdown('</div>', unsafe_allow_html=True)
            st.success("Recipe generated by Cook de Staku!")

elif mode == "Ingredient Substitute":
    st.write("## 🔄 Ingredient Substitute")
    question = st.text_input(
        "Ingredient to substitute",
        help="Example: What can I use instead of eggs?"
    )
    if st.button("Find Substitute"):
        response = substitute_ingredient(question)
        st.markdown('<div class="botbox">', unsafe_allow_html=True)
        st.write("👨‍🍳 Cook de Staku AI:")
        st.markdown(response)
        st.markdown('</div>', unsafe_allow_html=True)

elif mode == "Meal Planner":
    st.write("## 📅 Weekly Meal Planner")
    if st.button("Generate Meal Plan"):
        plan = meal_plan()
        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
        st.markdown(plan)
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
        recipe_text, signature, _ = generate_recipe(user_chat)
        last_chat_signature = st.session_state.get("last_chat_signature")
        attempts = 0
        while signature and signature == last_chat_signature and attempts < 2:
            recipe_text, signature, _ = generate_recipe(user_chat)
            attempts += 1
        st.session_state.last_chat_signature = signature
        response = recipe_text

    st.session_state.chat_history.append(("assistant", persona_name, persona_icon, response))

for message in st.session_state.chat_history:
    if message[0] == "user":
        with st.chat_message("user"):
            st.write(message[1])
    else:
        _, persona_name, persona_icon, text = message
        with st.chat_message("assistant"):
            st.markdown(f"**{persona_icon} {persona_name}:**\n\n{text}")
