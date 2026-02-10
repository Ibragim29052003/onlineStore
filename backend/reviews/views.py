"""
Views for reviews app.
"""
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for Review model."""
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Get reviews for a specific product or user."""
        product_id = self.kwargs.get('product_pk')
        if product_id:
            return Review.objects.filter(product_id=product_id)
        return Review.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Create review for product."""
        product_id = self.kwargs.get('product_pk')
        if product_id:
            serializer.save(
                user=self.request.user,
                product_id=product_id
            )
        else:
            serializer.save(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        """Update review - only own reviews."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Check if user owns this review
        if instance.user != request.user:
            return Response(
                {'detail': 'Вы можете редактировать только свои отзывы.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """Delete review - only own reviews."""
        instance = self.get_object()
        
        if instance.user != request.user:
            return Response(
                {'detail': 'Вы можете удалять только свои отзывы.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
