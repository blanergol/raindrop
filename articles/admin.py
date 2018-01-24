from django.contrib import admin
from .models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'text', 'created_date', 'img', 'comments_status']
    list_filter = ['created_date']
    search_fields = ['title', 'text']


admin.site.register(Articles, ArticlesAdmin)
