from django.shortcuts import render
from .forms import UserCreationForm
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

