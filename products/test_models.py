"""
import
"""
from django.contrib.auth.models import User
from django.test import TestCase

from products.models import Category, Product


class TestCategoryModel(TestCase):
    """
    Testing category model
    """
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            friendly_name='Test Category'
        )

    def tearDown(self):
        self.category.delete()

    def test_str_method(self):
        """
        Checks if category comes back as string
        """
        self.assertEqual(str(self.category), self.category.name)

    def test_get_friendly_name(self):
        """
        import
        """
        self.assertEqual(
            self.category.get_friendly_name(),
            self.category.friendly_name
            )


class TestProductModel(TestCase):
    """
    Testing product model
    """
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            friendly_name='Test Category'
        )
        self.product = Product.objects.create(
            sku='test',
            description='Test description',
            price=99.99,
            category=self.category,
            rating=4.3,
        )

    def tearDown(self):
        self.product.delete()
        self.category.delete()

    def test_str_method(self):
        """
        Checks if product comes back as string
        """
        self.assertEqual(str(self.product), self.product.name)
