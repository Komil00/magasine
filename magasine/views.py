from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from magasine.models import Product, OrderProduct, Category, UserFavoriteProduct
from .serializers import (
    ProductListSerializers,
    OrderProductListSerializers,
    OrderProductPutSerializers, UserFavoriteProductListSerializers, UserFavoriteProductPostSerializers,
    OrderProductPostSerializers
)
from rest_framework.viewsets import ViewSet, ModelViewSet


# Create your views here.

class ProductViewSet(ViewSet):
    queryset = Product.objects.all()

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductListSerializers(queryset, many=True)
        return Response(serializer.data)


# class OrderProductViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = OrderProduct.objects.all()
#
#     def get_serializer_class(self):
#         if self.action in ['list']:
#             return OrderProductListSerializers
#         else:
#             return OrderProductPutSerializers

# def get_serializer_class(self):
#     if self.request.method == 'GET':
#         return OrderProductListSerializers
#     if self.request.method == 'PUT':
#         return OrderProductPutSerializers
# def list(self, request):
#     queryset = OrderProduct.objects.all()
#     serializer = OrderProductListSerializers(queryset, many=True)
#     return Response(serializer.data)
#
# def update(self, request, *args, **kwargs):
#     serializer = OrderProductPutSerializers(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     return Response(serializer.data)

# def create(self, request, *args, **kwargs):
#     serializer = OrderProductPutSerializers(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
# def get_serializer_class(self):
#     if self.action == 'list':
#         return OrderProductListSerializers
#     if self.action == 'retrieve':
#         return OrderProductPutSerializers
# @action(detail=True, methods=['put'])
# def update_quantity(self, request):
#     queryset = OrderProduct.objects.create()
#     serializer = OrderProductPutSerializers(queryset, many=True)
#     return Response(serializer.data)

class OrderProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderProduct.objects.all()
    http_allowed_methods = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return OrderProduct.objects.all()
        return OrderProduct.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list']:
            return OrderProductListSerializers
        if self.action in ['create']:
            return OrderProductPostSerializers
        return OrderProductPutSerializers


class UserFavoriteProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserFavoriteProduct.objects.all()
    http_allowed_methods = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserFavoriteProduct.objects.all()
        return UserFavoriteProduct.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list']:
            return UserFavoriteProductListSerializers
        return UserFavoriteProductPostSerializers
