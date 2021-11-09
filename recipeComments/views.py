from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "recipeComments/index.html")


def about(request):
    return render(request, "recipeComments/about.html")
