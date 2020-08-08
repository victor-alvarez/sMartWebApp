from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import MyUser
# Register your models here.
class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_admin', 'is_staff')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields':('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff')})
    )

    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    # filter_vertical = ()
    filter_horizontal = ()

admin.site.register(MyUser, MyUserAdmin)


# admin.site.unregister(Group)