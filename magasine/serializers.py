from rest_framework import serializers
from .models import Product, OrderProduct, Category
from customuser.serializers import CustomUserSerializers, CustomUserListSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductListSerializers(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['modelname', 'category', 'image', 'price', 'productquantity', 'mode']


class OrderProductListSerializers(serializers.ModelSerializer):
    user = CustomUserListSerializer(read_only=True)
    product = ProductListSerializers(read_only=True)
    quantity = serializers.FloatField(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['user', 'product', 'quantity']


class OrderProductPutSerializers(serializers.ModelSerializer):
    quantity = serializers.FloatField()

    class Meta:
        model = OrderProduct
        fields = ['quantity']
