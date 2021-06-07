from django.shortcuts import render
from . import loginDAO as dao
# Create your views here.


def login(response):
    """
    Vaildates Login and directs to User Space if validated
    Or 
    back to login.
    """
    if response.method == "POST":
        email = response.POST.get("email")
        password = response.POST.get("pwd")
        result = dao.authUser(email, password)

        if result[0] == True:
            # print(result[1])
            result[1]["auth"] = True
            return render(response, "login/setCookies.html", result[1])
            # return render(response, "login/userSpace.html", result[1])
        else:
            return render(response, "login/login.html", {"result": result})
    else:
        return render(response, "login/login.html")


def userSpace(response):
    return render(response, "login/userSpace.html")


def addUser(response):
    return render(response, "login/addUser.html")


def deleteAccount(response):
    return render(response, "login/deleteAccount.html")


def deleteUser(response):
    return render(response, "login/deleteUser.html")


def shareLink(response):
    return render(response, "login/shareLink.html")


def updateUser(response):
    return render(response, "login/updateUser.html")


def viewAttendance(response):
    return render(response, "login/viewAttendance.html")
