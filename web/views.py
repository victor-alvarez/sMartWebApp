from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "web/homepage.html", {
        'title': 'Homepage',
        'root': 'homepage'
    })


def marketplace(request):
    return render(request, "web/marketplace.html", {
        'title': 'Marketplace',
        'root': 'marketplace'
    })


def mentor_profile(request):
    return render(request, "web/mentor_profile.html", {
        'title': 'Mentor Profile',
        'root': 'mentor_profile'
    })
