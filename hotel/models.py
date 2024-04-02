from django.db import models

from account.models import CustomUser


# Create your models here.
class hotel(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile_no=models.BigIntegerField(null=True)
    address = models.TextField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    
    def __str__(self):
        return self.name

    '''
class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)

class Menu(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    chef = models.ForeignKey(Staff, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer_id = models.IntegerField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class OrderUpdate(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Order.STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)'''