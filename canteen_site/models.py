from django.db import models

class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email


class MenuItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.title

class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart item for {self.user.username}: {self.item.title} - {self.quantity} units"


from django.db import models
from .models import UserInfo

class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )

    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order #{self.order_id} - {self.user.username} - {self.created_at}"



class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # Storing the title directly
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()  # Assuming image_url will be stored directly

    def __str__(self):
        return f"Order {self.order.order_id}: {self.title} - {self.quantity} units"

class FavoriteItem(models.Model):
    favorite_item_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.item.title}"
