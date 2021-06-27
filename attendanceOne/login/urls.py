from django.urls import path

from .import views

urlpatterns = [
    path("", views.login, name="login"),
    path("userSpace/", views.userSpace, name="userSpace"),
    path("addUser/", views.addUser, name="addUser"),
    path("deleteAccount/", views.deleteAccount, name="deleteAccount"),
    path("deleteUser/", views.deleteUser, name="deleteUser"),
    path("shareLink/", views.shareLink, name="shareLink"),
    path("updateUser/", views.updateUser, name="updateUser"),
    # path("viewAttendance/", views.viewAttendance, name="viewAttendance"),

]
