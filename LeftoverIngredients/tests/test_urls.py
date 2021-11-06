from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, profile
from django.contrib.auth.views import LoginView, LogoutView
from main.views import home, about, recipe, search


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
        url = reverse("main-recipe")
        self.assertEquals(resolve(url).func, recipe)

    def test_search_url_resolves(self):
        url = reverse("main-search")
        self.assertEquals(resolve(url).func, search)
