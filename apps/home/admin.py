from django.contrib import admin
from .models import MarketProduct


class MarketProductAdmin(admin.ModelAdmin):
    list_display = ('pk_product', 'product_description', 'product_stock')
    list_filter = ('pk_product', 'product_description', 'product_stock')
    search_fields = ('pk_product', 'product_description')


admin.site.register(MarketProduct, MarketProductAdmin)

