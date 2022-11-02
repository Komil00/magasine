from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, OrderProduct, Category, UserFavoriteProduct


# Register your models here.


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display
    search_fields = ('name',)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['modelname', 'category', 'price', 'image_tag']
    fields = ['modelname', 'category', 'price', 'image']
    list_display_links = list_display
    search_fields = ('modelname',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')

    image_tag.short_description = 'Image'


@admin.register(OrderProduct)
class OrderProductModelAdmin(admin.ModelAdmin):
    fields = ['author', 'product', 'quantity']
    list_display = ['product', 'author', 'quantity', 'image_tag']
    list_display_links = list_display
    search_fields = ('product__modelname',)

    def image_tag(self, obj):
        if obj.product.image.url:
            return mark_safe(f'<img src="{obj.product.image.url}" width="50" height="50" />')

    image_tag.short_description = 'Image'


@admin.register(UserFavoriteProduct)
class UserFavoriteProductModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'image_tag']
    search_fields = ['product__modelname']
    list_display_links = ['author', 'product', 'image_tag']

    def image_tag(self, obj):
        if obj.product.image.url:
            return mark_safe(f'<img src="{obj.product.image.url}" width="50" height="50" />')

    image_tag.short_description = 'Image'
