from django.contrib import admin
from .models import *


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['id', 'title']


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['title']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')
    list_display_links = ('id', 'title', 'created')
    search_fields = ['title']
    filter_horizontal = ['tags']


admin.site.register(About, AboutAdmin)

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Awards)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Blog)
admin.site.register(Categories)
admin.site.register(Projects)

