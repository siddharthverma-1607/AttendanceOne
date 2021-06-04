from django.urls import path

from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.login, name="login"),
    path("about/", views.about, name="about"),
    path("documentation/", views.documentation, name="documentation"),
]
