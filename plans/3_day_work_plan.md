# План работы на 3 дня

## День 1: Users + Products

### Файлы для изменения:

#### 1.1 users/models.py - добавить методы модели
```python
# Добавить методы в User модель:
- get_full_name()
- get_short_name()
- email_domain()
```
**Commit:** `git commit -m "feat(users): добавить методы модели User"`

#### 1.2 users/serializers.py - улучшить сериализаторы
```python
# Улучшить UserSerializer:
- добавить поле role
- добавить поле last_login_formatted
```
**Commit:** `git commit -m "feat(users): улучшить UserSerializer"`

#### 1.3 users/views.py - добавить пагинацию/фильтрацию
```python
# Добавить пагинацию в UserViewSet
# Добавить фильтрацию по is_active
```
**Commit:** `git commit -m "feat(users): добавить пагинацию и фильтрацию"`

#### 1.4 products/models.py - добавить методы Product
```python
# Добавить в Product:
- get_discount_price(percent)
- is_in_stock()
- get_absolute_url()
```
**Commit:** `git commit -m "feat(products): добавить методы модели Product"`

#### 1.5 products/serializers.py - добавить поле со скидкой
```python
# Добавить в ProductSerializer:
- discounted_price (если есть скидка)
- is_available
```
**Commit:** `git commit -m "feat(products): добавить поле скидки в сериализатор"`

---

## День 2: Cart + Orders

### Файлы для изменения:

#### 2.1 carts/models.py - методы Cart
```python
# Добавить в Cart:
- is_empty()
- clear()
- get_item_count()
```
**Commit:** `git commit -m "feat(carts): добавить методы модели Cart"`

#### 2.2 carts/serializers.py - улучшить сериализацию
```python
# Улучшить CartItemSerializer:
- добавить product_thumbnail
- добавить item_total
```
**Commit:** `git commit -m "feat(carts): улучшить сериализацию CartItem"`

#### 2.3 orders/models.py - методы Order
```python
# Добавить в Order:
- can_cancel()
- get_status_display_colored()  # уже есть get_status_display
- is_paid()
```
**Commit:** `git commit -m "feat(orders): добавить методы модели Order"`

#### 2.4 orders/serializers.py - улучшить сериализацию
```python
# Улучшить OrderSerializer:
- добавить items_count
- добавить formatted_status
- добавить can_be_cancelled
```
**Commit:** `git commit -m "feat(orders): добавить поля для отмены заказа"`

#### 2.5 orders/views.py - добавить действия
```python
# Добавить action в OrderViewSet:
- cancel_order
- confirm_order
```
**Commit:** `git commit -m "feat(orders): добавить экшены для управления заказом"`

---

## День 3: Reviews + API + Admin

### Файлы для изменения:

#### 3.1 reviews/models.py - методы Review
```python
# Добавить в Review:
- get_rating_stars()  # уже есть
- is_recent()
- helpful_count()
```
**Commit:** `git commit -m "feat(reviews): добавить методы модели Review"`

#### 3.2 reviews/serializers.py - улучшить отзывы
```python
# Улучшить ReviewSerializer:
- добавить user_name
- добавить helpful_count
- добавить is_verified
```
**Commit:** `git commit -m "feat(reviews): улучшить сериализатор отзывов"`

#### 3.3 reviews/views.py - добавить лайки отзывов
```python
# Добавить action:
- like_review
- unlike_review
```
**Commit:** `git commit -m "feat(reviews): добавить систему лайков отзывов"`

#### 3.4 products/admin.py - улучшить отображение
```python
# Улучшить ProductAdmin:
- добавить list_display улучшения
- добавить actions (deactivate_products)
```
**Commit:** `git commit -m "feat(admin): добавить actions для управления товарами"`

#### 3.5 users/admin.py - улучшить отображение
```python
# Улучшить UserAdmin:
- добавить custom list_display
- добавить actions (activate_users, deactivate_users)
```
**Commit:** `git commit -m "feat(admin): добавить actions для управления пользователями"`

---

## Дополнительные идеи для коммитов:

### Файлы для удаления (если не используются):
- ? Спросить какие файлы не нужны

### Файлы для добавления:
- `backend/core/permissions.py` - кастомные разрешения
- `backend/core/throttling.py` - Rate limiting
- `backend/products/tasks.py` - Celery задачи
- `backend/orders/signals.py` - сигналы для заказов

---

## Формат коммитов:
- `feat()` - новая функциональность
- `fix()` - исправление багов
- `refactor()` - рефакторинг кода
- `docs()` - документация
- `admin()` - изменения в админке
- `api()` - изменения API
