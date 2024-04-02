from django.db import models

from account.models import CustomUser

from hotel.models import hotel
# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact = models.BigIntegerField()
    address=models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Product(models.Model):
    CATEGORY = [
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('dairy', 'Dairy'),
        ('spices', 'Spices'),
    ]
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}_{self.supplier.name}"

    
    

    
    

class product_order(models.Model):
    STATUS_CHOICES = [
        ('placed', 'Placed'),
        ('in_warehouse', 'In Warehouse'),
        ('packed', 'Order Packed'),
        ('out_of_delivery', 'Out Of Delivery'),
    ]
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Placed')
    total_amount = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return self.hotel.name

class OrderItem(models.Model):
    order = models.ForeignKey(product_order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.order.hotel.name}_{self.order.id}_{self.product.name}"