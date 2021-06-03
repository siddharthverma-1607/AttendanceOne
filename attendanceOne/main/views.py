from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def signUp(response):
    form = SignUpForm()
    return render(response, "main/signup.html", {"form": form})
