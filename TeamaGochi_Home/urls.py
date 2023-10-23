from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('term-cond/',views.term_and_condition),
    path('creators/',views.creators),
    path('logout/', views.exit),
    path('settings/', views.settings),
    path('info/', views.info),
    path('buscar/', views.buscar),
    path("formulario/", views.formulario),
]