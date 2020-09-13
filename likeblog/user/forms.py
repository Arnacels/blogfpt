from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2',)
