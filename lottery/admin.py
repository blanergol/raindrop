from django.contrib import admin
from .models import Briefcases, Stuff, DotaboxModes, StuffAttributes, StuffAttributesType


class BriefcasesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'score', 'img', 'created_date']


class StuffAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'img', 'show_status', 'show_shop_status']

class StuffAttributesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class StuffAttributesTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class DotaboxModesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'score', 'enable']


admin.site.register(Briefcases, BriefcasesAdmin)
admin.site.register(Stuff, StuffAdmin)
admin.site.register(StuffAttributes, StuffAttributesAdmin)
admin.site.register(StuffAttributesType, StuffAttributesTypeAdmin)
admin.site.register(DotaboxModes, DotaboxModesAdmin)
