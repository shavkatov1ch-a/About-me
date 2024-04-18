from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_display_links = ['name', 'email', 'message']
    search_fields = ('name', 'email', 'phone', 'message')


admin.site.register(Contact, ContactAdmin)