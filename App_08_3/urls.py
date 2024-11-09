# App_08_3/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_view, name='resume'),
    path('photo.jpg/', views.photo_view, name='photo'), 
]
