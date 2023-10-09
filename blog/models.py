"""
Imports for blog modles
"""
from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'), (1, 'Posted'))


class Post(models.Model):
    """
    Imports for blog modles
    """
    title = models.CharField(
        max_length=200,
        unique=True
        )
    slug = models.SlugField(
        max_length=200,
        unique=True
        )
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
        )
    created_date = models.DateTimeField(blank=True)
    updated_date = models.DateTimeField()
    content = models.TextField()
    featured_image = models.ImageField(
        null=True,
        blank=True
        )
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Returns order based on date the post was created
        """
        ordering = ['-created_date']

    def __str__(self):
        """
        Returns the title as a string
        """
        return self.title


class Comment(models.Model):
    """
    Model to add comment to blog
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField(
        max_length=50
        )
    email = models.EmailField()
    body = models.TextField(verbose_name="")
    created_date = models.DateTimeField(
        auto_now_add=True
        )
    approved = models.BooleanField(
        default=False
        )

    class Meta:
        """
        Returns order based on date the comment was created
        """
        ordering = ['created_date']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
