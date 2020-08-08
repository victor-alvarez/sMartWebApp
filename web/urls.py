from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="web-homepage")
]

# <app>/<model>_<viewtype).html
