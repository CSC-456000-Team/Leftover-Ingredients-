from django.shortcuts import render
from .connect_api import get_recipe_ids, get_recipes

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
