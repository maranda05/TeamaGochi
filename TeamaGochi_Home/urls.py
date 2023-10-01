from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('term-cond/',views.term_and_condition),
    path('creators/',views.creators)
]