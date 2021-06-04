from hashlib import new
from django.shortcuts import render
from django.http import HttpResponse
from main import models
from . import registerDAO as dao
# Create your views here.


def register(response):

    if response.method == "POST":
        name = response.POST.get("name")
        email = response.POST.get("email")
        contact = response.POST.get("contact")
        organization = response.POST.get("organization")
        age = response.POST.get("age")
        password = response.POST.get("pwd")

        newUser = models.User(name, email, contact,
                              organization, age, password)

        if(dao.searchUser(newUser)):
            dao.addNewUser(newUser)
            return HttpResponse("<h1>Registeration Successful for </h1><br>")
            # return render(response,"login/login.html",form)

        else:
            form = {"result": "**User with entered email already exists!"}
            return render(response, "register/register.html", form)

    else:

        return render(response, "register/register.html")
