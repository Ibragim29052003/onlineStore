"""
модели приложения отзывов
"""
from django.db import models
from django.utils import timezone
from django.contrib.admin import display
from simple_history.models import HistoricalRecords


class Review(models.Model):
    # модель отзыва и оценки товара
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='пользователь'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='товар'
    )
    rating = models.PositiveIntegerField(
        'оценка',
        choices=[(i, i) for i in range(1, 6)]
    )
    comment = models.TextField('комментарий', blank=True)
    is_moderated = models.BooleanField('промодерирован', default=False)
    is_verified_purchase = models.BooleanField('подтвержденная покупка', default=False)
    created_at = models.DateTimeField('дата создания', default=timezone.now)
    updated_at = models.DateTimeField('дата обновления', auto_now=True)
    
    # отслеживание истории изменений через simple_history
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['-created_at']
        unique_together = ('user', 'product')
    
    def __str__(self):
        return f'{self.user.email} - {self.product.name} ({self.rating}★)'
    
    @display(description='оценка')
    def get_rating_stars(self):
        # отображение оценки в виде звёзд
        from django.utils.html import format_html
        stars = '★' * self.rating + '☆' * (5 - self.rating)
        return format_html('<span style="color: gold;">{}</span>', stars)
    
    @display(description='оценка')
    def get_rating_with_label(self):
        # отображение оценки с подписью
        labels = {1: 'плохо', 2: 'неудовлетворительно', 3: 'средне', 4: 'хорошо', 5: 'отлично'}
        return f'{self.rating} - {labels.get(self.rating, "")}'
    
    @display(description='статус')
    def get_moderation_status(self):
        # отображение статуса модерации
        from django.utils.html import format_html
        if self.is_moderated:
            return format_html('<span style="color: green;">✓ промодерирован</span>')
        return format_html('<span style="color: orange;">⏳ на модерации</span>')
