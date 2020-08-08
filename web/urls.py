from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="web-homepage"),
    path('marketplace/', views.marketplace, name="web-marketplace")
]

# <app>/<model>_<viewtype).html
