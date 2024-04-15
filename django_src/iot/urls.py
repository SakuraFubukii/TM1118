from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('transfer/', views.transfer),
    path('welcome/', views.welcome),
]