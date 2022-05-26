from django.contrib import admin

from products.models import Product, Websites, ProductCategory

admin.site.register(Product)

admin.site.register(Websites)

admin.site.register(ProductCategory)
