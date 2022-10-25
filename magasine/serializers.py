from rest_framework import serializers
from .models import Product, OrderProduct, Category, UserFavoriteProduct
from customuser.serializers import CustomUserSerializers, CustomUserListSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductListSerializers(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'modelname', 'category', 'image', 'price', 'productquantity', 'mode']


# class OrderProductListSerializers(serializers.ModelSerializer):
#     user = CustomUserListSerializer(read_only=True)
#     product = ProductListSerializers(read_only=True)
#     quantity = serializers.FloatField(read_only=True)
#
#     class Meta:
#         model = OrderProduct
#         fields = ['user', 'product', 'quantity']


# class OrderProductPutSerializers(serializers.ModelSerializer):
#     quantity = serializers.FloatField()
#
#     class Meta:
#         model = OrderProduct
#         fields = ['quantity']


class OrderProductListSerializers(serializers.ModelSerializer):
    author = CustomUserListSerializer(read_only=True)
    product = ProductListSerializers(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['id', 'author', 'product', 'quantity']


class OrderProductPostSerializers(serializers.ModelSerializer):
    quantity = serializers.FloatField()

    class Meta:
        model = OrderProduct
        fields = ['id', 'author', 'product', 'quantity']


class OrderProductPutSerializers(serializers.ModelSerializer):
    quantity = serializers.FloatField()

    class Meta:
        model = OrderProduct
        fields = '__all__'


class UserFavoriteProductListSerializers(serializers.ModelSerializer):
    author = CustomUserListSerializer(read_only=True)
    product = ProductListSerializers(read_only=True)

    class Meta:
        model = UserFavoriteProduct
        fields = ['id', 'author', 'product']


class UserFavoriteProductPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFavoriteProduct
        fields = ['id', 'author', 'product']
