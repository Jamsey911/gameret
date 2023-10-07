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
        """
        Comment form for users wishing to comment on a post
        """
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and class to textfield
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'body': 'Body',
        }

        for field in self.fields:
            self.fields[field].widget.attrs['aria-label'] = placeholders[
                        field]
