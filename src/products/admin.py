from django.contrib import admin
from import_export.admin import ImportExportMixin

from products.models import Product, Websites, ProductCategory, ProductSearchResult, ProductPriceChange

@admin.register(Product)
class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'site', 'price', 'target_price', 'availability')
    ordering = ('site', 'name')
    list_filter = ('availability_message',)
    search_fields = ('url', 'name')

admin.site.register(Websites)

admin.site.register(ProductCategory)

@admin.register(ProductSearchResult)
class ProductSearchResultAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'site', 'price', 'category', 'rating')
    ordering = ('-rating', 'name')
    list_filter = ('search_keyword',)
    search_fields = ('name',)

@admin.register(ProductPriceChange)
class ProductPriceChangeAdmin(admin.ModelAdmin):
    list_display = ('product', 'date')
    ordering = ('-date', 'product')
    list_filter = ('date', 'product')