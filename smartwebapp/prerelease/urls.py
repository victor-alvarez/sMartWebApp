from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="prerelease-home"),
    path('about/', views.about, name="prerelease-about")
]
