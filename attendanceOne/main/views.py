from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from .import models

# Create your views here.


def home(response):
    return render(response, "main/home.html", {})


def login(response):
    return render(response, "main/login.html", {})


def about(response):
    return render(response, "main/about.html", {})


def documentation(response):
    return render(response, "main/document.html", {})


def page_not_found(request, exception):
    return render(request, 'main/404.html')
