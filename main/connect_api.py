import json
import os

import requests

# from dotenv import find_dotenv, load_dotenv

# # BASE_DIR = Path(__file__).resolve().parent.parent
# # dotenv_path = os.path.join(BASE_DIR(__file__), '.env')
# load_dotenv(find_dotenv)

API_KEY = str(os.environ.get("API_KEY_SPOONACULAR"))


# Gets the id's of recipes containing the searched ingredients, ingredients must be a comma-separated list
def get_recipe_ids(ingredients):
    search_url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=3&apiKey={API_KEY}"

    r = requests.get(search_url)

    results = json.loads(r.text)

    recipe_ids = []

    for recipe in results:
        recipe_ids.append(recipe["id"])

    return recipe_ids


# Gets the names, images, and URLs of the sources of each recipe
def get_recipes(recipe_ids):
    recipes = []

    for recipe_id in recipe_ids:
        info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
        r = requests.get(info_url)
        results = json.loads(r.text)

        title = results["title"]
        image = results["image"]
        recipe_url = results["sourceUrl"]

        recipe = {"title": title, "image": image, "recipe_url": recipe_url}

        recipes.append(recipe)

    return recipes
