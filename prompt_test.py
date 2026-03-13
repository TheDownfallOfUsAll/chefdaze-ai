# ChefDaze AI Prompt Testing Script
# Team Summer Daze

def chef_daze_prompt(ingredients_input):

    system_prompt = """
You are ChefDaze AI, a smart recipe coach for home cooks.

Your responsibilities:
- Suggest recipes based on ingredients
- Provide structured cooking instructions
- Suggest ingredient substitutions
- Encourage safe cooking practices
- Keep recipes varied so different inputs do not produce the same output
- Add optional add-ons and variation ideas

Output Format:

Recipe Name
Serving Size
Prep Time
Cook Time

Ingredients:
- item

Instructions:
1. step

Optional Tips
"""

    user_prompt = f"Give me a recipe for {ingredients_input}."

    # Simulated responses for testing
    if "pasta" in ingredients_input.lower():
        response = """
Recipe Name: Garlic Butter Pasta

Serving Size: 2
Prep Time: 5 minutes
Cook Time: 10 minutes

Ingredients:
- Pasta
- Garlic
- Butter
- Parmesan Cheese
- Salt
- Black Pepper

Instructions:
1. Boil pasta in salted water until al dente.
2. Melt butter in a pan over medium heat.
3. Add minced garlic and saute until fragrant.
4. Drain pasta and add it to the pan.
5. Toss with parmesan cheese and pepper.
6. Serve hot.

Tips:
Add chili flakes if you want a spicy version.
"""

    elif "chicken" in ingredients_input.lower():
        response = """
Recipe Name: Soy Garlic Chicken

Serving Size: 3
Prep Time: 10 minutes
Cook Time: 20 minutes

Ingredients:
- Chicken breast
- Garlic
- Soy sauce
- Brown sugar
- Cooking oil

Instructions:
1. Heat oil in a frying pan.
2. Add minced garlic and saute briefly.
3. Add chicken pieces and cook until browned.
4. Pour soy sauce and a small amount of brown sugar.
5. Simmer until chicken is fully cooked.

Tips:
Serve with steamed rice and vegetables.
"""

    elif "substitute egg" in ingredients_input.lower():
        response = """
Ingredient Substitution Guide:

You can replace eggs with the following:

- 1/4 cup applesauce
- 1 mashed banana
- 1 tablespoon flaxseed + 3 tablespoons water
- Yogurt

Best used for:
- Baking
- Pancakes
- Muffins
"""

    else:
        response = """
ChefDaze AI Suggestion:

Try entering ingredients like:
- chicken, garlic, rice
- pasta, tomato, cheese
- eggs, milk, flour

I will generate a recipe for you.
"""

    return f"""
===============================
ChefDaze AI Prompt Simulation
===============================

SYSTEM PROMPT:
{system_prompt}

USER INPUT:
{ingredients_input}

PROMPT:
{user_prompt}

AI RESPONSE:
{response}
"""


# -------------------------------
# Test Cases
# -------------------------------

tests = [
    "I have pasta, garlic, and butter. What can I cook?",
    "I have chicken and soy sauce",
    "What can I substitute egg with?",
    "Give me recipe ideas"
]


print("\n====== CHEFDAZE AI PROMPT TESTS ======\n")

for i, test in enumerate(tests, 1):

    print(f"\n--- Test Case {i} ---")
    print(chef_daze_prompt(test))
