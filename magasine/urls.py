from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, OrderProductViewSet, UserFavoriteProductViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'order-product', OrderProductViewSet)
router.register(r'favorite-product', UserFavoriteProductViewSet)


# router.register(r'',)


urlpatterns = [
    path('', include(router.urls))
]
