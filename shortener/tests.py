from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User
from shortener.service import shortcode
from shortener.models import Shorturl


class ShortcodeTestCase(TestCase):
    def test_shortcode(self):
        # Call the shortcode function
        result = shortcode()

        # Assert that the result is a string
        self.assertIsInstance(result, str)

        # Assert that the length of the result is 5
        self.assertEqual(len(result), 5)


class ShorturlDetailTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.shorturl = Shorturl.objects.create(
            user=self.user, url="https://www.example.com"
        )
        self.url = reverse(
            "shorturl_detail", kwargs={"identifier": self.shorturl.identifier}
        )

    def test_shorturl_detail(self):
        request = HttpRequest()
        request.user = self.user
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.shorturl.url)
