from django.db import models

# Product model represents items available in the store
class Product(models.Model):
    # Name of the product
    name = models.CharField(max_length = 255)

    # Detailed description
    description = models.TextField()

    # Price of product
    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    # Available stack quantity
    stock = models.IntegerField()

    # Automatically set when product is created
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        # Helps in admin panel readability
        return self.name
        
