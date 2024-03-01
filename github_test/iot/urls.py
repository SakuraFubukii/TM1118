from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('W311a/', views.W311a),
    path('W311b/', views.W311b),
    path('W311-H1/', views.W311_H1),
    path('W311-H2/', views.W311_H2),
    path('W311-H3/', views.W311_H3),
    path('W311d-Z1/', views.W311d_Z1),
    path('W311d-Z2/', views.W311d_Z2)
]