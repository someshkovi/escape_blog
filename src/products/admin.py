from django.contrib import admin

from products.models import Product, Websites, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'price', 'target_price', 'availabity')
    ordering = ('site', 'name')
    list_filter = ('availabity_messsage',)
    search_fields = ('url', 'name')

admin.site.register(Websites)

admin.site.register(ProductCategory)
