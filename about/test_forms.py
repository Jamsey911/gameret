"""
Imports
"""
from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """
    A class to test the ContactForm
    """
    def test_empty_form(self):
        """
        To test empty the form
        """
        form = ContactForm()
        self.assertIn("name", form.fields)
        self.assertIn("phone", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("message", form.fields)
