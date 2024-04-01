from django.db import models

from account.models import CustomUser

# Create your models here.
'''
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)'''