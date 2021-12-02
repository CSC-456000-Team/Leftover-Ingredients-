from django.shortcuts import render
from .connect_api import get_recipes

# from django.http import HttpResponse


def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html", {"title": "About"})


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        recipes = get_recipes(searched)
        return render(
            request, "main/search.html", {"searched": searched, "recipes": recipes}
        )
    else:
        return render(request, "main/search.html", {})
