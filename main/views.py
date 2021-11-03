from django.shortcuts import render

# from django.http import HttpResponse


def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html", {"title": "About"})


def recipe(request):
    return render(request, "main/recipe.html", {"title": "Recipe"})


def search(request):
    return render(request, "main/search.html", {"title": "Search"})
