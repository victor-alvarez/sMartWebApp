from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="web-homepage"),
    path('marketplace/', views.marketplace, name="web-marketplace"),
    path('student-sign-up/', views.student_sign_up, name="web-student-sign-up"),
    path('mentor-profile/', views.mentor_profile, name="web-mentor-profile"),
    path('profile-student/', views.profile_student_dashboard, name="student-dashboard"),
    path('profile-mentor/', views.profile_mentor_dashboard, name="mentor-dashboard"),
    path('register_student_ajax/', views.register_student_ajax, name="register_student_ajax"),

    path('logout/', views.logout_view, name="logout"),
]

# <app>/<model>_<viewtype).html
