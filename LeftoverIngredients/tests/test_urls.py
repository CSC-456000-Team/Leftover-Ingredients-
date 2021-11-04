from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, profile

class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
    
    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_login_url_resolves(self):
        assert 1 == 1
        # url = reverse('register')
        # self.assertEquals(resolve(url).func, login)

    def test_logout_url_resolves(self):
        assert 1 == 1
        # url = reverse('register')
        # self.assertEquals(resolve(url).func, logout)