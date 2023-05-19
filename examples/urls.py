from django.urls import path
from . import views
from .views import index, profile 

urlpatterns =[
    path('', views.index),
    path('profile', views.profile, name='profile'),
]