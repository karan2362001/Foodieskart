from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('hotel_owner', 'Hotel Owner'),
        ('delivery_partner', 'Delivery Partner'),
        ('supplier', 'Supplier'),
        ('captain', 'Captain'),
        ('chef', 'Chef'),
        ('receptionist', 'Receptionist'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)