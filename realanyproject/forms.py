from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserRegistrationForm, CustomUserLoginForm, ProfileForm
from django.contrib.auth import logout

class SearchForm(forms.Form):
    search_bar = forms.CharField(max_length = 256)

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2', 'age')



class CustomUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

class ProfileForm(UserCreationForm):
    class Meta:
        model = User
        field = ('username', 'phone_number')

def profile(request):
    user = request.user
    form = ProfileForm(instance=user)
    return render(request, 'profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('logout/')
