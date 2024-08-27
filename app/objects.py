from pydantic import BaseModel, Field, conlist, constr
from typing import List, Optional

class Material(BaseModel):
    name: str
    amount: float
    color: str
    weight: float



class RecipeRule(BaseModel):
    materials: conlist(str, min_items=2)  # A list of material names (at least 2)
    weight_relation: Optional[constr(regex=r'^\w+ > \w+$')] = None  # e.g., "flour > sugar"
    color_options: Optional[List[str]] = None  # e.g., ["red", "blue"]

class Recipe(BaseModel):
    name: str
    rules: List[RecipeRule]  # Each recipe can have multiple rules


def recognize_recipes(materials: List[Material], recipes: List[Recipe]) -> List[str]:
    recognized_recipes = []

    for recipe in recipes:
        match = True
        for rule in recipe.rules:
            # Check if all materials in the rule are present
            material_names = [material.name for material in materials]
            if not all(mat in material_names for mat in rule.materials):
                match = False
                break

            # Check weight relations if provided
            if rule.weight_relation:
                material1, material2 = rule.weight_relation.split(" > ")
                weight1 = next((material.weight for material in materials if material.name == material1), None)
                weight2 = next((material.weight for material in materials if material.name == material2), None)
                if weight1 is None or weight2 is None or weight1 <= weight2:
                    match = False
                    break

            # Check color options if provided
            if rule.color_options:
                if not any(material.color in rule.color_options for material in materials if
                           material.name in rule.materials):
                    match = False
                    break

        if match:
            recognized_recipes.append(recipe.name)

    return recognized_recipes

# Define materials used that day
materials_used = [
    Material(name="flour", amount=200, color="white", weight=200),
    Material(name="sugar", amount=100, color="brown", weight=100),
    Material(name="butter", amount=50, color="yellow", weight=50),
]

# Define recipes
recipes = [
    Recipe(
        name="Cake",
        rules=[
            RecipeRule(
                materials=["flour", "sugar"],
                weight_relation="flour > sugar",
                color_options=["white", "brown"]
            ),
            RecipeRule(
                materials=["butter"]
            )
        ]
    ),
    Recipe(
        name="Pastry",
        rules=[
            RecipeRule(
                materials=["flour", "butter"],
                weight_relation="flour > butter",
                color_options=["white", "yellow"]
            )
        ]
    )
]

# Recognize recipes
recognized = recognize_recipes(materials_used, recipes)
print(recognized)  # Output will be ['Cake', 'Pastry']


