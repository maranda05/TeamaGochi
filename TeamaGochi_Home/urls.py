from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio),
    path('index/', views.index),
    path('creators/',views.creators),
    path('term-cond/',views.term_and_condition),
    path('logout/', views.exit),
    path('settings/', views.settings),
    path('info/', views.info),
    path('buscar/', views.buscar),
    path("formulario/", views.formulario),
    
]