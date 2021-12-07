from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.user = {
            "email": "testuser@gmail.com",
            "username": "testuser",
            "password": "password",
        }
        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format="text/html")
        self.assertEqual(response.status_code, 302)
