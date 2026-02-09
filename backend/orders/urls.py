"""
URL configuration for orders app.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderStatusViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r'order-statuses', OrderStatusViewSet, basename='order-status')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='order-item')

urlpatterns = [
    path('', include(router.urls)),
]
