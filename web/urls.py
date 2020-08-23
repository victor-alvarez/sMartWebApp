from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="web-homepage"),
    path('marketplace/', views.marketplace, name="web-marketplace"),
    path('mentor-profile/', views.mentor_profile, name="web-mentor-profile"),
    path('profile-student/', views.profile_student_dashboard, name="student-dashboard"),
    path('logout/', views.logout_view, name="logout"),
]

# <app>/<model>_<viewtype).html
