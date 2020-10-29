""" Forms models of comments to send the information. """

# Forms
from django import forms

# Models
from .models import Comment


class NewCommentForm(forms.ModelForm):
    """ New comment form."""
    class Meta:
        model = Comment
        fields = ['content']
