#listings app-urls.py
from django.urls import path

from . import views

urlpatterns = [
    #the name is the page link we use {% urls '' %}
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]