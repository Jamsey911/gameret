"""
Imports for testing Blog models
"""
from datetime import date
from django.test import TestCase
from .models import Comment, Post


# Test blog comment Form model

class TestCommentModel(TestCase):
    """
    Imports for testing Comment model
    """
    def setUp(self):
        self.comment = Comment(
            name="Tester",
            email="test@mail.com",
            body="Test message",
            created_date="2024-06-15",
            approved=False,
        )

    def test_comment_form(self):
        """
        Comment test results defiend by the below elements
        """
        self.assertEqual(self.comment.name, "Tester")
        self.assertEqual(self.comment.email, "test@mail.com")
        self.assertEqual(self.comment.body, "Test message")
        self.assertEqual(self.comment.created_date, "2024-06-15")
        self.assertEqual(self.comment.approved, False)


class TestPostModel(TestCase):
    """
    Setup for testing Post model testing
    """
    def setUp(self):
        self.post = Post(
            title="Test Title",
            excerpt=6,
            updated_date="2023-06-05",
            content="Test Content",
            created_date="2023-06-05",
        )

    def test_blog_post_model(self):
        """
        Post test results defiend by the below elements
        """
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(self.post.excerpt, 6)
        self.assertEqual(self.post.updated_date, "2023-06-05")
        self.assertEqual(self.post.content, "Test Content")
        self.assertEqual(self.post.created_date, "2023-06-05")
