from django.shortcuts import render
from django.http import HttpResponse
from .import models

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def signUp(response):
    if response.method == "POST":
        name = response.POST.get("name")
        email = response.POST.get("email")
        contact = response.POST.get("contact")
        organization = response.POST.get("organization")
        age = response.POST.get("age")
        password = response.POST.get("pwd")

        newUser = models.User(name, email, contact,
                              organization, age, password)
        form = newUser

        return HttpResponse("<h1>SignUp Successful</h1><br>%s" % form)
    else:
        return render(response, "main/signup.html", {})


def login(response):
    return render(response, "main/login.html", {})


def about(response):
    return render(response, "main/about.html", {})


def documentation(response):
    return render(response, "main/document.html", {})
