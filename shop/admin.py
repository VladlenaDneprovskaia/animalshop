from django.contrib import admin

from shop.models import Animal, Brand, ProductImage, Product

admin.site.register(Animal)
admin.site.register(Brand)


class ProductImageAdminInline(admin.TabularInline):
    model = ProductImage
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageAdminInline,)
