""" Forms models of users to send the information. """

# Django
from django.contrib.auth.models import User

# Django_Forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Models
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """ Register login form. """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):
    """ Update User form. """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """ Update Profile form. """
    class Meta:
        model = Profile
        fields = ['image']
