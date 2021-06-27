"""attendanceOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as registerView
from markAttendance import views as markAttendanceView
from upgrade import views as upgradeView
from viewattendance import views as attendanceView

from django.conf import settings
from django.conf.urls.static import static

#from login import views as loginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", registerView.register, name="register"),
    path("login/", include("login.urls")),
    path("login/viewattendance/", attendanceView.attendance, name="viewattendance"),
    path("attendance/<userid>/", markAttendanceView.attendance, name="attendance"),
    path('', include("main.urls")),
    path('upgrade/', upgradeView.upgrade, name="upgrade"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "main.views.page_not_found"
