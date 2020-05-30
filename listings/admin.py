from django.contrib import admin
from .models import Listing

#adds info to the listing table in the admin area
#list display shows listing info below, filter allows you to filter by realtor
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'price')
    list_per_page = 25
#register listings for admin area
admin.site.register(Listing, ListingAdmin)