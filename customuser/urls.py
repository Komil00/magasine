from django.urls import path, include
from .views import UsersViewList
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'', UsersViewSet)
urlpatterns = [
    path('', UsersViewList.as_view()),
]


