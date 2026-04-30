from django.db import models
from users.models import User
from products.models import Product


# Order represents a purchase made by a user
class Order(models.Model):

    # Which user made the order
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    # Total price of all item
    total_price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)

    # Order creation timestamp
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

# Each item inside an order
class OrderItem(models.Model):

    # Link to order 
    order = models.ForeignKey(Order, related_name = 'items', on_delete = models.CASCADE)

    # Product being ordered
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    # Quantity of product
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} * {self.quantity}"
