from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from magasine.models import OrderProduct, UserFavoriteProduct, Product
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


class OrderProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderProduct.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['product__price']
    search_fields = ['product__modelname', 'product__category__name']
    authentication_classes = [SessionAuthentication]
    http_allowed_methods = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = OrderProductPostSerializers(data=request.data)
        product = Product.objects.get(id=request.data['product'])
        orderproduct = Product.objects.get(id=request.data['product'])
        if product.productquantity < int(request.data['quantity']):
            return Response("buncha mahsulot yo'q", status=status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        product.productquantity -= int(request.data['quantity'])
        product.save()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        serializer = OrderProductPutSerializers(data=request.data)
        print(serializer.is_valid())
        set_order = set()
        try:
            order = get_object_or_404(self.queryset, pk=pk)
            set_order.add(order)
        except OrderProduct.DoesNotExist:
            return Response({"error": 'order does not exist'}, status=status.HTTP_404_NOT_FOUND)
        prod = None
        ord = set_order.pop()
        if order.product:
            prod = ord.product
        if serializer.validated_data['quantity'] > ord.quantity:
            prod.productquantity -= int(serializer.validated_data['quantity'] - ord.quantity)
            prod.save()
        if serializer.validated_data['quantity'] < ord.quantity:
            prod.productquantity += int(ord.quantity - serializer.validated_data['quantity'])
            prod.save()
        ord.quantity = serializer.validated_data['quantity']
        ord.save()
        return Response({"success": "mahsulotingiz soni muvafaqiyatli o'zgartirildi"})

    def get_queryset(self):
        return OrderProduct.objects.filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list']:
            return OrderProductListSerializers
        if self.action in ['create']:
            return OrderProductPostSerializers
        return OrderProductPutSerializers


class UserFavoriteProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserFavoriteProduct.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['product__price']
    search_fields = ['product__modelname', 'product__category__name']
    authentication_classes = [SessionAuthentication]
    http_allowed_methods = ['get', 'post', 'put', 'delete']
    serializer_class = UserFavoriteProductPostSerializers

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.filter(author=self.request.user)
        return self.queryset.filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list']:
            return UserFavoriteProductListSerializers
        return UserFavoriteProductPostSerializers
