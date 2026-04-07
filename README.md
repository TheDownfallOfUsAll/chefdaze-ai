# 🍳 Recipe de SUCKERPUNCH – AI-Powered Smart Recipe Assistant

**Recipe de SUCKERPUNCH** is a modern, interactive cooking assistant built with **Streamlit**. It helps home cooks generate recipes, plan meals, substitute ingredients, and receive smart cooking guidance with a bold Lakers-inspired dark-mode UI.

---

## 🌟 Features

- **Recipe Generator** with step-by-step instructions
- **Regenerate** button to create a fresh recipe using the same ingredients
- **Diet-aware recipe adjustments** for Vegan, Vegetarian, Keto, and Gluten Free
- **Ingredient Substitute** suggestions for almost any food
- **Weekly Meal Planner** with varied meals each time
- **Nutrition estimates** (calories and protein)
- **Auto grocery list** from your ingredients
- **Chat with Anthony Edwards & LeBron James** personas
- **Prompt Hacking Defenses demo** with before/after outputs
- **Any Foods Quick Picks** for fast demo inputs
- **Lakers dark-mode** appearance theme

---

## How the AI Works

This app uses AI-style logic (no live LLM calls):

- Parses ingredients with lightweight rules
- Chooses recipe profiles and methods from curated templates
- Applies diet swaps for Vegan, Vegetarian, Keto, and Gluten Free
- Suggests substitutions from a curated ingredient catalog
- Adds randomized variations for freshness
- Styles responses with Anthony Edwards or LeBron James personas
- Includes prompt-hacking defenses (refusal + redirect) for unsafe requests

## 🚀 Installation

```bash
git clone https://github.com/yourusername/recipe-de-suckerpunch.git
cd recipe-de-suckerpunch
```

Create and activate a virtual environment (recommended).

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

## 🧑‍🍳 Usage

1. Choose a mode: Recipe Generator, Ingredient Substitute, or Meal Planner.
2. Enter ingredients or a question.
3. Adjust settings in the sidebar for servings, skill level, diet, and persona.
4. Use **Regenerate** for a fresh recipe with the same ingredients.
5. In the **AI Chatbot Demo**, compare the **before vs after** prompt outputs.
6. Use **Any Foods Quick Picks** to auto-fill sample inputs.

---

## 💬 Chat Personas

The chat is now powered by two special personas:

- **Anthony Edwards**
- **LeBron James**

Each response is tagged with a persona for a fun, lively feel.

---

## 🛡️ Prompt Hacking Defenses

The app includes a **before/after** demo that shows how prompt-hacking defenses work:

- **Before:** midterm prompt with no defenses
- **After:** defended prompt that refuses prompt injection and redirects to cooking help

Defenses include:
- Instruction hierarchy (system > developer > user)
- Untrusted input framing (user input is data, not instructions)
- Prompt injection / data exfiltration refusal
- Role and output-format lock
- Capability limits (no web/tool claims)
- Safe redirect to cooking tasks

---

## 🖼️ Screenshots

Add screenshots here:

- `screenshots/recipe.png`
- `screenshots/chat.png`
- `screenshots/mealplanner.png`

---

## 🤝 Contribution

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🔮 Future Ideas

- Optional LLM integration (if desired)
- Personalized dietary recommendations
- Multi-language support
- Voice cooking assistant
- Grocery delivery integration


