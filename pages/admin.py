from django.contrib import admin
from .models import Pages


class PagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'show_status', 'comments_status']
    search_fields = ['title', 'text']


admin.site.register(Pages, PagesAdmin)
