"""
Imports for the blog commentform
"""
from django import forms
from . models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form for users wishing to comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)
