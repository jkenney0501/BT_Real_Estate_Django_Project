#accounts app-urls.py
from django.urls import path

from . import views

urlpatterns = [
    #the name is the page link we use {% urls '' %}
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]