from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="web-home"),
    path('events/', views.events, name="web-events")
]

# <app>/<model>_<viewtype).html
