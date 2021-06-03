from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse("<h1>tech with Master God Siddhart</h1>")


def v1(response, id):
    return HttpResponse("<h1>View-%s !</h1>" % id)


def home(response):
    return render(response, "main/home.html", {})
