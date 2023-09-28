from django.test import TestCase
from shortener.service import shortcode


class ShortcodeTestCase(TestCase):
    def test_shortcode(self):
        # Call the shortcode function
        result = shortcode()

        # Assert that the result is a string
        self.assertIsInstance(result, str)

        # Assert that the length of the result is 5
        self.assertEqual(len(result), 5)
