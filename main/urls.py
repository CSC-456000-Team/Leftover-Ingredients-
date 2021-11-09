from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="main-home"),
    path("about/", views.about, name="main-about"),
    path("recipe/", views.recipe, name="main-recipe"),
    path("search/", views.search, name="main-search"),
]
