from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import MyUser, Student, Mentor
# Register your models here.
class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_admin', 'is_staff', 'is_active')
    list_filter = ('is_admin', 'is_student', 'is_teacher')

    fieldsets = (
        (None, {'fields':('username', 'email', 'password')}),
        ('Type of User', {'fields' : ('is_student', 'is_teacher')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')})
    )

    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    # filter_vertical = ()
    filter_horizontal = ()

admin.site.register(MyUser,MyUserAdmin)
admin.site.register(Student)
admin.site.register(Mentor)



# admin.site.unregister(Group)