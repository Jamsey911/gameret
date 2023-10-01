"""
Imports
"""
from django.test import TestCase, Client
from .views import about
from .forms import ContactForm


class TestContactView(TestCase):
    """
    Test to check if contact form is displayed
    """
    def test_template_used(self):
        """
        Test to check if contact form is displayed
        """
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'about/about.html')

    def test_message_sent(self):
        """
        Test to check if message is sent
        """
        response = self.client.post('/about/', data={
            'inquiry_purpose ': 'PRODUCT',
            'name': 'tester',
            'email': 'test@net.com',
            'phone': '12456',
            'message': 'test message'
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_mail_not_sent(self):
        """
        user inputs invalid e mail address
        """
        response = self.client.post('/about/', data={
            'inquiry_purpose ': 'PRODUCT',
            'name': 'tester',
            'email': 'testnet.com',
            'phone': '12456',
            'message': 'test message'
        }, follow=True)
        self.assertContains(response, 'An error occured please check the form')
