% Midterm Project Report Slides
% Cook de Staku
% March 17, 2026

---

# Cook de Staku
Midterm Project Report

Team: ChefDaze AI  
Course: Midterm Project  
Date: March 17, 2026

---

# Agenda
1. Project Overview
2. Problem and Objectives
3. Features and UX
4. System Design
5. Implementation Highlights
6. Progress and Challenges
7. Future Work

---

# Project Overview
Cook de Staku is a Streamlit-based cooking assistant that helps users:
1. Generate recipes from ingredients
2. Find ingredient substitutes
3. Build weekly meal plans
4. Explore a playful, themed UI experience

---

# Problem Statement
Home cooks often struggle with:
1. Deciding what to cook using available ingredients
2. Replacing missing ingredients without losing flavor
3. Planning meals efficiently across the week

---

# Project Objectives
1. Provide fast recipe ideas from simple inputs
2. Offer practical substitutions for common ingredients
3. Generate flexible, repeatable meal plans
4. Deliver a polished, fun UI to improve engagement

---

# Target Users and Use Cases
1. Students and busy professionals with limited time
2. Home cooks with pantry-only ingredient lists
3. Users following dietary preferences

Example Use Cases:
1. "What can I cook with chicken and rice?"
2. "Substitute for eggs in baking?"
3. "Plan dinners for the week"

---

# Core Features
                                                   1. Recipe Generator with step-by-step instructions
                                                   2. Regenerate button for fresh recipes using the same ingredients
                                                   3. Diet-aware adjustments (Vegan, Vegetarian, Keto, Gluten Free)
                                                   4. Ingredient Substitute suggestions for most foods
                                                   5. Weekly Meal Planner with random variety
                                                   6. Nutrition estimate and grocery list
                                                   7. Chat with two personas for fun guidance

---

# UI and UX Design
1. Lakers Light and Lakers Dark appearance themes
2. Clear card-based layout for readability
3. Consistent typography and spacing
4. Quick actions in sidebar for easy resets

---

# System Design (High Level)
1. Streamlit front end
2. Rule-based recipe generation engine
3. Ingredient parsing and categorization
4. Diet replacement and filtering logic
5. Session state for history and regenerate logic

---

# Data and Logic Flow
1. User inputs ingredients
2. Parse and clean input
3. Apply diet-aware replacements
4. Select a recipe profile
5. Generate ingredients, steps, tips
6. Render card with recipe, nutrition, grocery list

---

# Implementation Highlights
1. Unique recipe regeneration using signature history
2. Diet-aware replacements for ingredients and steps
3. Context-aware substitutions with recipe ideas
4. Consistent UI theming through CSS variables

---

# Progress to Date
1. Full feature set implemented
2. UI polish and theming completed
3. Chat personas updated to Anthony Edwards and LeBron James
4. README and project documentation updated

---

# Challenges and Solutions
1. Preventing repeated recipes
   Solution: signature history with regeneration loop
2. Diet filtering without breaking recipes
   Solution: replace ingredients and adjust steps dynamically
3. UI consistency across modes
   Solution: shared CSS and reusable components

---

# Evaluation and Testing
1. Manual scenario tests for major flows
2. Multiple ingredient combinations for variety
3. Diet preference testing for replacements

---

# Future Work
1. LLM-based recipe generation
2. Pantry management and saved favorites
3. User accounts and personalization
4. Mobile-first layout refinements

---

# Demo Plan
1. Show recipe generation and regenerate
2. Demonstrate diet-aware filtering
3. Run ingredient substitute examples
4. Generate a weekly meal plan

---

# Q and A
Thank you
