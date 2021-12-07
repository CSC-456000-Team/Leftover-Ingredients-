from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="main-home"),
    path("about/", views.about, name="main-about"),
    path("search/", views.search, name="main-search"),
]
