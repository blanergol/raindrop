from django.contrib import admin
from .models import Service, Inventory, HistoryGames, Billing, BillingHistory, ShopStuff, ShopStuffFavorites


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'exchange_link']


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'stuff_id']


class HistoryGamesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id']


class BillingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'money', 'score', 'coins']


class BillingHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'money', 'score', 'date']
    list_filter = ['date']


class ShopStuffAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'stuff_id']


class ShopStuffFavoritesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'stuff_id']


admin.site.register(Service, ServiceAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(HistoryGames, HistoryGamesAdmin)
admin.site.register(Billing, BillingAdmin)
admin.site.register(BillingHistory, BillingHistoryAdmin)
admin.site.register(ShopStuff, ShopStuffAdmin)
admin.site.register(ShopStuffFavorites, ShopStuffFavoritesAdmin)
