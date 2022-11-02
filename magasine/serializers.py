from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, OrderProduct, Category, UserFavoriteProduct
from customuser.serializers import CustomUserListSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'modelname', 'image', 'price']


class ChangePriceSerializer(serializers.Serializer):
    price = serializers.FloatField(required=True)


class ProductDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderProductListSerializers(serializers.ModelSerializer):
    author = CustomUserListSerializer(read_only=True)
    product = ProductListSerializers(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['id', 'author', 'product', 'quantity']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['totlal'] = instance.product.price * instance.quantity
        return representation


class OrderProductPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id', 'author', 'product', 'quantity']

    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError("quantity 0 dan kop bolishi kerak")
        return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['totlal'] = instance.product.price * instance.quantity
        return representation


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
