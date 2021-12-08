import requests
import json
import os

import requests

from dotenv import load_dotenv

# BASE_DIR = Path(__file__).resolve().parent.parent
# dotenv_path = os.path.join(BASE_DIR(__file__), '.env')
load_dotenv()

API_KEY = str(os.environ.get("API_KEY_SPOONACULAR"))


# Gets the id's of recipes containing the searched ingredients, ingredients must be a comma-separated list
def get_recipe_ids(ingredients):
    search_url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=6&apiKey={API_KEY}"

    r = requests.get(search_url)

    results = json.loads(r.text)

    recipe_ids = []

    for recipe in results:
        recipe_ids.append(recipe["id"])

    return recipe_ids


# Gets the names, images, and URLs of the sources of each recipe
def get_recipe(recipe_id):

    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
    r = requests.get(info_url)
    results = json.loads(r.text)

    title = results["title"]
    image = results["image"]
    servings = results["servings"]
    time = results["readyInMinutes"]


    recipe = {"title": title, "image": image, "servings": servings, "time": time}

    return recipe

def get_recipes(recipe_ids):
    recipes = []
    for recipe_id in recipe_ids:
        recipes.append(get_recipe(recipe_id))
    return recipes


# Meal types: breakfast, dessert, main course, snack (?)
def get_random_recipes(category):
    random_recipes = []

    url = f"https://api.spoonacular.com/recipes/random?number=9&tags={category}&apiKey={API_KEY}"
    r = requests.get(url)
    results = json.loads(r.text)

    for random in results["recipes"]:
        recipe_id = random["id"]
        title = random["title"]
        servings = random["servings"]
        time = random["readyInMinutes"]
        image = random["image"]

        random = {"recipe_id": recipe_id, "title": title, "servings": servings, "time": time, "image": image}
        random_recipes.append(random)

    return random_recipes

def get_recipe_details(recipe_id):
    steps = []
    equipment = []

    url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey={API_KEY}"
    r = requests.get(url)
    results = json.loads(r.text)

    for step in results[0]["steps"]:
        number = step["number"]
        s = step["step"]
        steps.append({"number": number, "step": s})
        for e in step["equipment"]:
            if e["name"] not in equipment:
                equipment.append(e["name"])

    # url = 

    details = {"steps": steps, "equipment": equipment}
    return details


# def get_recipe_details(recipe_id):
#     details = {}
    
#     url = f""

# print (get_recipe_details(651389))
