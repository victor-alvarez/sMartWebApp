from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q
from backend_usermanagement.models import Student, Mentor
from django.db import transaction

User = get_user_model()

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password_confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username']

    def cleaned_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValueError('Passwords do not match')
        return password1

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
            Q(username__iexact = query) |
            Q(email__iexact = query)
        ).distinct()

        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError('Invalid credentials - user does not exist')
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError('Invalid credentials')
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)

class StudentRegistrationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['program', 'year']

    # @transaction.atomic
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_student = True
    #     user.save()
    #     student = Student.objects.create(user=user)
    #     student.program = self.cleaned_data.get('program')
    #     return user
        # user = super(StudentRegistrationForm, self).save(commit=False)
        # user.set_password(self.cleaned_data['password1'])
        # user.is_student = True
        #
        # if commit:
        #     user.save()
        #
        # student = Student.objects.create(user=user)
        # student.username = user.username
        # student.email = user.email
        #
        # student.save()

        # return user

class MentorRegistrationForm(UserCreationForm):

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_teacher = True


        if commit:
            user.save()

        mentor = Mentor.objects.create(user=user)
        mentor.username = user.username
        mentor.email = user.email
        mentor.save()

        return user