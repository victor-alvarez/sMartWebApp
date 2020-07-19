from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "prerelease/home.html")


def about(request):
    return render(request, "prerelease/about.html")
