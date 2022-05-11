from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('simple_fetch', views.simple_fetch)
]