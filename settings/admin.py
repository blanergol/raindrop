from django.contrib import admin
from .models import Settings


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'email', 'count_posts', 'count_video', 'vk_link', 'sales_margin', 'enable_rdcase',
                    'enable_dotabox', 'enable_magick_ball', 'enable_techies', 'enable_shop']
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Settings, SettingsAdmin)
