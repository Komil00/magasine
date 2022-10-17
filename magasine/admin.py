from django.contrib import admin
from .models import Product, OrderProduct, Category, UserFavoriteProduct

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(UserFavoriteProduct)
