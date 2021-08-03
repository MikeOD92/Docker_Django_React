from django.urls import path
from .views import login, users, register

urlpatterns = [
    path('users', users),
    path('register', register),
    path('login', login),
]
