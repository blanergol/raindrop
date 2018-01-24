from django.contrib import admin
from .models import Video, About, Contact


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'video_link', 'created_date']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'img']
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Video, VideoAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
