from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "recipeComments/index.html")


def about(request):
    return render(request, "recipeComments/about.html")
