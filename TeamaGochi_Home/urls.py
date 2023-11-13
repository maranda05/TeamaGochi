from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio),
    path("register/", views.register),
    path('index/', views.index),
    path('register/index/', views.index),   
    path('creators/',views.creators),
    path('index/creators/',views.creators),
    path('register/term-cond/',views.term_and_condition),
    path('index/logout/', views.exit),
    path('index/settings/', views.settings),
    path('index/info/', views.info),
    path('buscar/', views.buscar),
    path("formulario/", views.formulario),
    
]