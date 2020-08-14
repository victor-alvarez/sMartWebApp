from django.shortcuts import render
from django.http import HttpResponseRedirect
from backend_usermanagement.forms import UserCreationForm, UserLoginForm
from django.contrib.auth import login, logout

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



def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login/')
    context = {
        'form': form
    }
    return render(request, "backend_usermanagement/register.html", context)

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)

        return HttpResponseRedirect('/profile/')
    return render(request, "backend_usermanagement/login.html", {"form" : form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile_dashboard(request):
    if (request.user.is_authenticated):
        content = {'user' : request.user}
        return render(request, 'backend_usermanagement/profile.html', content)
    else:
        return HttpResponseRedirect('/')
