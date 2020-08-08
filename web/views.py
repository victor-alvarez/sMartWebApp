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
