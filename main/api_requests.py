from django.conf import settings
import requests
import json


i = "apples, bananas, grapes"

API_KEY = "9f97e9f457aa4379ba2cb4c32072aec4"

url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={i}&number=3&apiKey={API_KEY}"

r = requests.get(url)

results = json.loads(r.text)

recipe_ids = []

for recipe in results:
    recipe_ids.append(recipe['id'])

recipes = []

for recipe_id in recipe_ids:
    info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
    r = requests.get(info_url)
    results = json.loads(r.text)

    title = results['title']
    image = results['image']
    recipe_url = results['sourceUrl']

    recipe = {
        'title': title,
        'image': image,
        'recipe_url': recipe_url 
    }

    recipes.append(recipe)

print(recipes)