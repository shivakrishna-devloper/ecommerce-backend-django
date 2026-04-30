from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model to support roles (Admin / Customer)
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )

    # Role field to differentiate users
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='customer'
    )

    def __str__(self):
        return self.username