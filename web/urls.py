from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="web-homepage"),
    path('marketplace/', views.marketplace, name="web-marketplace"),
    path('mentor-profile/', views.mentor_profile, name="web-mentor-profile")
]

# <app>/<model>_<viewtype).html
