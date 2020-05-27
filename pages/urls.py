#Pages app-urls.py
from django.urls import path

from . import views

urlpatterns = [
    #the name is the page link we use {% urls '' %}
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]