from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('program', views.program, name='program'),
    path('fasilitas', views.fasilitas, name='fasilitas')
]