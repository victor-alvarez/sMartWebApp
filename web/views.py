
from django.shortcuts import render
from django.http import HttpResponseRedirect
from backend_usermanagement.forms import UserCreationForm, UserLoginForm, StudentRegistrationForm, MentorRegistrationForm
from django.contrib.auth import login, logout

# Create your views here.


def homepage(request):
    return render(request, "web/homepage.html", {
        'title': 'Homepage',
        'name': 'homepages'
    })


def marketplace(request):
    return render(request, "web/marketplace.html", {
        'title': 'Marketplace',
        'name': 'marketplaces'
    })


def student_sign_up(request):
    return render(request, "web/student_sign_up.html", {
        'title': 'Student Sign Up',
        'name': 'student_sign_ups'
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

def register_student(request):
    user_form = UserCreationForm(request.POST or None)
    student_form = StudentRegistrationForm(request.POST or None)
    if user_form.is_valid() and student_form.is_valid():
        user = user_form.save(commit=False)
        user.is_student = True
        user.save()
        student = student_form.save(commit=False)
        student.user = user
        student.username = user.username
        student.email = user.email
        student.save()
        return HttpResponseRedirect('/login/')
    context = {
        'form' : user_form, 'form_student' : student_form
    }
    return render(request, "backend_usermanagement/register.html", context)

def register_mentor(request):
    form = MentorRegistrationForm(request.POST or None)
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
        if user_obj.is_student :
            return HttpResponseRedirect('/profile-student/')
        else :
            return HttpResponseRedirect('/profile-mentor/')


    return render(request, "backend_usermanagement/login.html", {"form" : form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def profile_student_dashboard(request):
    if (request.user.is_authenticated and request.user.is_student):
        content = {'user' : request.user}
        return render(request, 'web/student_dashboard.html', content)
    else:

        return HttpResponseRedirect('/login/')


def profile_mentor_dashboard(request):
    if (request.user.is_authenticated and request.user.is_teacher):
        content = {'user' : request.user}
        return render(request, 'web/student_dashboard.html', content)
    else:

        return HttpResponseRedirect('/login/')