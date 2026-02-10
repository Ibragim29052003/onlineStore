"""
Serializers for reviews app.
"""
from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer
from products.serializers import ProductSerializer


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model."""
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    rating_stars = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = [
            'id', 'user', 'product', 'rating', 'rating_stars',
            'comment', 'is_moderated', 'is_verified_purchase',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'user', 'product', 'is_moderated', 
            'is_verified_purchase', 'created_at', 'updated_at'
        ]
    
    def get_rating_stars(self, obj):
        """Get rating as stars string."""
        return '★' * obj.rating + '☆' * (5 - obj.rating)


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating reviews."""
    
    class Meta:
        model = Review
        fields = ['rating', 'comment']
    
    def validate_rating(self, value):
        """Validate rating value."""
        if not 1 <= value <= 5:
            raise serializers.ValidationError('Рейтинг должен быть от 1 до 5.')
        return value
    
    def create(self, validated_data):
        """Create review for product."""
        user = self.context['request'].user
        product = self.context['product']
        
        # Check if user already reviewed this product
        if Review.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError(
                {'detail': 'Вы уже оставили отзыв на этот товар.'}
            )
        
        return Review.objects.create(user=user, product=product, **validated_data)


class ReviewUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating reviews."""
    
    class Meta:
        model = Review
        fields = ['rating', 'comment']
    
    def validate_rating(self, value):
        """Validate rating value."""
        if not 1 <= value <= 5:
            raise serializers.ValidationError('Рейтинг должен быть от 1 до 5.')
        return value
