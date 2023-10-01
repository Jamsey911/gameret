"""
Imports
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Contact


class TestContactModel(TestCase):
    """
    Test for contact model in about section
    """
    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_string_method_return(self):
        """
        Testing the message turning to string
        """
        self.contact = Contact.objects.create(
            inquiry_purpose='ORDER',
            name=self.user.username,
            email='test@user.com',
            phone='122445',
            message='test message'

        )
        self.assertEqual(str(self.contact),
                         'Contact MyTestUser and message created')
