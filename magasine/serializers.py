from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
    class Meta:
        model = OrderProduct
        fields = ['id', 'author', 'product', 'quantity']

    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError("quantity 0 dan kop bolishi kerak")
        return value

    def to_representation(self, instance):
        return model_to_dict(instance)


class OrderProductPutSerializers(serializers.ModelSerializer):
    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError("quantity 0 dan kop bolishi kerak")
        return value

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
