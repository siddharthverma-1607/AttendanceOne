from django.shortcuts import render
from . import loginDAO as dao
# Create your views here.


def login(response):
    if response.method == "POST":
        email = response.POST.get("email")
        password = response.POST.get("pwd")
        result = dao.authUser(email, password)

        if result[0] == True:
            # print(result[1])
            result[1]["auth"] = True
            return render(response, "login/userSpace.html", result[1])
        else:
            return render(response, "login/login.html", {"result": result})
    else:
        return render(response, "login/login.html")


def userSpace(response):
    return render(response, "login/userSpace.html")
