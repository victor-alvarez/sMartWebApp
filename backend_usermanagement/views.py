from django.contrib.auth import login, logout
from django.shortcuts import render
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect

# Create your views here.



def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
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
    content = {'user' : request.user}
    return render(request, 'backend_usermanagement/profile.html', content)



