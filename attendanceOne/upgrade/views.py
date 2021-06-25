from django.shortcuts import render

# Create your views here.


def upgrade(response):
    if response.method == "POST":
        pass
    else:
        return render(response, "upgrade/upgrade.html")
