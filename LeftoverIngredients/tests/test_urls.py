from django.contrib.auth.views import LoginView, LogoutView
from django.test import SimpleTestCase
from django.urls import resolve, reverse

from main.views import about, home
from recipe.views import recipe, search
from users.views import profile, register


class TestUrls(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func, register)

    def test_profile_url_resolves(self):
        url = reverse("profile")
        self.assertEquals(resolve(url).func, profile)

    def test_login_url_resolves(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_resolves(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_home_url_resolves(self):
        url = reverse("main-home")
        self.assertEquals(resolve(url).func, home)

    def test_about_url_resolves(self):
        url = reverse("main-about")
        self.assertEquals(resolve(url).func, about)

    def test_recipe_url_resolves(self):
        url = reverse("recipe-home")
        self.assertEquals(resolve(url).func, recipe)

    def test_search_url_resolves(self):
        url = reverse("recipe-search")
        self.assertEquals(resolve(url).func, search)
