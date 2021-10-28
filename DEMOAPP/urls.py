from django.urls import path
from . import views

urlpatterns = [
    path('Hi', views.hi, name='home-page'),
    path('Home', views.home, name='home-page2'),
]
