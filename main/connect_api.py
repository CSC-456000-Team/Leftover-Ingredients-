from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests


API_KEY = "9f97e9f457aa4379ba2cb4c32072aec4"

# Gets the id's of recipes containing the searched ingredients, ingredients must be a comma-separated list
def get_recipes_ids(ingredients):
    search_url = f"https://api.spoonacular.com/recipes/findByIngredients?{ingredients}&number=5&apiKey={API_KEY}"

    recipe_ids = []

    r = requests.get(search_url)

    if r.status_code == 200:
        r_dict = r.json()
        for recipe in r_dict:
            recipe_ids.append(recipe["id"])

    return recipe_ids


# Gets the names, images, and URLs of the sources of each recipe
def get_recipes(recipe_ids):
    recipes = []

    for recipe_id in recipe_ids:
        results_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information&apiKey={API_KEY}"

        r = requests.get(results_url)

        if r.status_code == 200:
            r_dict = r.json()
            for recipe in r_dict:
                name = recipe["title"]
                image = recipe["image"]
                source_url = recipe["sourceUrl"]
                recipe_info = {"name": name, "image": image, "source_url": source_url}
                recipes.append(recipe_info)

    return recipes
