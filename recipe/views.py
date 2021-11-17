from django.shortcuts import render

from .models import Recipe

# dummy data which wiil replace by database
recipeDummies = [
    {
        "author": "David",
        "title": " Avocado Toast",
        "content": "First recipe content",
        "date_posted": "October 31, 2021",
    },
    {
        "author": "Jinho",
        "title": "Pumpkin Pie",
        "content": "Second recipe content",
        "date_posted": "November 1, 2021",
    },
]


def recipe(request):
    context = {
        "title": "Recipe",
        "recipeDummies": recipeDummies
        # Recipe.objects.all()
    }
    return render(request, "main/recipe.html", context)


# -------------------------- DB need to be setup for testing -------------------
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        # recipes = Recipe.objects.filter(name__contains=searched)
        return render(
            request,
            "main/search.html",
            {
                "searched": searched
                # ,
                # "recipes": recipes
            },
        )
    else:
        return render(request, "main/search.html", {"title": "Search"})
