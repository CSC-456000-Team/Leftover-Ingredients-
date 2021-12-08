from django.shortcuts import render

from .connect_api import get_recipe_ids, get_recipes, get_random_recipes
import csv

# from django.http import HttpResponse


def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html", {"title": "About"})


def search(request):
    top_ingredients = []
    with open('top-1k-ingredients.csv', 'r') as f:
        reader = csv.reader(f)
        top_ingredients = [line[0] for line in reader]

    if request.method == "POST":
        searched = request.POST["searched"]
        recipe_ids = get_recipe_ids(searched)
        recipes = get_recipes(recipe_ids)
        return render(
            request, "main/search.html", {"searched": searched, "recipes": recipes, "top_ingredients": top_ingredients}
        )
    else:
        return render(request, "main/search.html", {"top_ingredients": top_ingredients})

def recipe(request):
    recipes = get_random_recipes("breakfast")
    main_course = get_random_recipes("main+course")
    snack = get_random_recipes("snack")

    return render(request, "main/recipe.html", {"recipes": recipes, "main_courses": main_course, "snack": snack})
