from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "prerelease/home.html")

def about_us(request):
    return render(request, "prerelease/about_us.html")
