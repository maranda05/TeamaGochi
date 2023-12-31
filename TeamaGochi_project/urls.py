"""
URL configuration for TeamaGochi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from TeamaGochi_Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TeamaGochi_Home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
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
    
