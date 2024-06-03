# Updated /mnt/data/mbm-main/mbm-main/realanyproject/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class CustomUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(UserChangeForm):  # Use UserChangeForm for profile updates
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class SearchForm:
    pass