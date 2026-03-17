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
- **Live Gemini LLM integration** (optional)
- **Lakers dark-mode** appearance theme

---

## How the AI Works

This app supports live LLM responses via Gemini and falls back to local logic when disabled:

- Gemini handles recipes, substitutes, meal plans, and chat when `GEMINI_API_KEY` is set
- Local rules handle everything when Gemini is off
- Diet swaps apply for Vegan, Vegetarian, Keto, and Gluten Free
- Responses are styled with Anthony Edwards or LeBron James personas

### Gemini Setup

1. Get a Gemini API key from Google AI Studio.
2. Set `GEMINI_API_KEY` in your environment or `.env`.
3. (Optional) Set `GEMINI_MODEL` (default: `gemini-3-flash-preview`).


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
3. Adjust settings in the sidebar for servings, skill level, diet, persona, and AI engine.
4. Use **Regenerate** for a fresh recipe with the same ingredients.

---

## 💬 Chat Personas

The chat is now powered by two special personas:

- **Anthony Edwards**
- **LeBron James**

Each response is tagged with a persona for a fun, lively feel.

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

- Gemini tool expansion (images, pantry memory, shopping links)
- Personalized dietary recommendations
- Multi-language support
- Voice cooking assistant
- Grocery delivery integration


