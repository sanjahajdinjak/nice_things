"""
DIRECT COPY (generated by Django)

Authors: Tyler Amos, Alexander Tyan
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

