from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
    AuthenticationForm
)
from .forms import RegistrationForm


def login_view(request):

    if (request.method == 'POST'):

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('posts:post_list'))
        else:
            form = AuthenticationForm()
            error_message = "Invalid username or password. Please try again."
            return render(request, 'account2/login.html', {'error_message': error_message, 'form': form})

    else:

        form = AuthenticationForm()
        if request.user.is_authenticated:
            return redirect(reverse('posts:post_list'))
            pass

    return render(request, 'account2/login.html', {'form': form})


def signup_view(request):

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('posts:post_list'))

    else:
        form = RegistrationForm()
        if request.user.is_authenticated:
            return redirect(reverse('posts:post_list'))
            pass
    return render(request, 'account2/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('posts:post_list'))


def home_view(request):
    return render(request, 'account2/home.html')
