from django.urls import path

from . import views

urlpatterns = [
    path("recipe/", views.recipe, name="recipe-home"),
    path("search/", views.search, name="recipe-search"),
]
