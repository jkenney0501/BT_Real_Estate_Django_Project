from django.contrib import admin
from .models import Listing

#register listings for admin area
admin.site.register(Listing)