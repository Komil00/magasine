from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, OrderProduct, Category, UserFavoriteProduct, ProductImage

# Register your models here.
admin.site.register(ProductImage)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display
    search_fields = ('name',)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['modelname', 'category', 'price']
    list_display_links = list_display
    search_fields = ('modelname',)
    inlines = [ProductImageInline]


@admin.register(OrderProduct)
class OrderProductModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'quantity']
    list_display_links = list_display
    search_fields = ('product__modelname',)

    # def image_tag(self, obj):
    #     if obj.product.image.url:
    #         return mark_safe(f'<img src="{obj.product.image.url}" width="50" height="50" />')
    #
    # image_tag.short_description = 'Image'


@admin.register(UserFavoriteProduct)
class UserFavoriteProductModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'product']
    search_fields = ['product__modelname']
    list_display_links = ['author', 'product']

    # def image_tag(self, obj):
    #     if obj.product.image.url:
    #         return mark_safe(f'<img src="{obj.product.image.url}" width="50" height="50" />')
    #
    # image_tag.short_description = 'Image'
