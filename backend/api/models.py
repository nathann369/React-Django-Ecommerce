from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# category model
class Category(models.Model):
    title = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# product model
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name

# address model
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    address = models.TextField() 
    phone = models.CharField(max_length=100)
    country = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


# cart model
class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart")
    quantity = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name