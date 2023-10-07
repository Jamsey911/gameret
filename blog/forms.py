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
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'body': '',
        }

        for field in self.fields:
            if field != 'country':
                self.fields[field].widget.attrs['aria-label'] = placeholders[
                    field]
