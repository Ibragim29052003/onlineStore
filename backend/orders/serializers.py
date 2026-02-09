"""
Serializers for orders app.
"""
from rest_framework import serializers
from .models import OrderStatus, Order, OrderItem
from users.serializers import UserSerializer


class OrderStatusSerializer(serializers.ModelSerializer):
    """Serializer for OrderStatus model."""
    
    class Meta:
        model = OrderStatus
        fields = ['id', 'name', 'description', 'is_final', 'created_at']
        read_only_fields = ['created_at']


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for OrderItem model."""
    
    class Meta:
        model = OrderItem
        fields = [
            'id', 'product', 'product_name', 'product_sku',
            'price', 'quantity', 'get_total_price', 'created_at'
        ]
        read_only_fields = ['created_at']


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""
    items = OrderItemSerializer(many=True, read_only=True)
    status_info = OrderStatusSerializer(source='status', read_only=True)
    user = UserSerializer(read_only=True)
    total_display = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'status', 'status_info', 'total', 'total_display',
            'shipping_address', 'notes', 'items', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'user', 'total']
    
    def get_total_display(self, obj):
        """Get total price as string."""
        return str(obj.total)


class OrderCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating orders."""
    
    class Meta:
        model = Order
        fields = ['status', 'shipping_address', 'notes']
    
    def create(self, validated_data):
        """Create order from cart."""
        user = self.context['request'].user
        from carts.models import Cart
        from django.db import transaction
        
        with transaction.atomic():
            cart = Cart.objects.get(user=user)
            order = Order.objects.create(user=user, **validated_data)
            
            # Create order items
            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    product_name=cart_item.product.name,
                    product_sku=cart_item.product.sku,
                    price=cart_item.product.price,
                    quantity=cart_item.quantity
                )
            
            # Calculate total
            order.calculate_total()
            
            # Clear cart
            cart.items.all().delete()
            
            return order
