"""
Imports
"""
from django.urls import reverse
from django.test import TestCase
from products.models import Product, Category


class TestViews(TestCase):
    """
    Testing views in bag app
    """
    def setUp(self):
        """
        Create test data, such as products and categories,
        to use in the tests
        """
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            price=9.99
        )

    def tearDown(self):
        """Clean up test data after each test method runs"""
        self.product.delete()
        self.category.delete()

    def test_view_bag_view(self):
        """
        Test that the view_bag view is accessible and displays
        the correct template
        """
        url = reverse('view_bag')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')