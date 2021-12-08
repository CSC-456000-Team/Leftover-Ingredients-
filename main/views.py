from django.shortcuts import render
from django.utils import html

from .connect_api import get_recipe_ids, get_recipes, get_random_recipes, get_recipe_details

# from django.http import HttpResponse


def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html", {"title": "About"})


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        recipe_ids = get_recipe_ids(searched)
        recipes = get_recipes(recipe_ids)

        return render(
            request, "main/search.html", {"searched": searched, "recipes": recipes}
        )
    else:
        return render(request, "main/search.html", {})

def recipe(request):
    recipes = get_random_recipes("main+course")
    # main_course = get_random_recipes("main+course")
    # snack = get_random_recipes("snack")

    return render(request, "main/recipe.html", {"recipes": recipes})

def single_recipe(request, recipe_id):
    details = get_recipe_details(recipe_id)
    info = details["info"]
    summary = html.format_html(details["info"]["summary"])
    steps = details["steps"]
    equipment = details["equipment"]
    ingredients = details["ingredients"]
    return render(request, "main/single-recipe.html", {"info": info, "summary": summary, "steps": steps, "equipment": equipment, "ingredients": ingredients})