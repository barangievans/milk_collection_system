from django.db import models
from django.contrib.auth.models import AbstractUser

# Updated Customer model to include Farmer-related fields
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Updated Order model to include relationship with Farmer (Customer) and Collection Center
class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

# Updated Farmer model, now without customer relationship
class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    id_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Updated Collection Center model
class CollectionCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Updated Milk Collection Entry model
class MilkCollectionEntry(models.Model):
    # Existing fields
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    collection_center = models.ForeignKey(CollectionCenter, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    # New fields
    collection_date = models.DateField(auto_now_add=True)  # Auto-fills date when entry is created
    collection_time = models.TimeField(auto_now_add=True)  # Auto-fills time when entry is created

    def __str__(self):
        return f"Milk collected from {self.farmer} on {self.collection_date} at {self.collection_time}"

# Staff model, using AbstractUser for authentication
class Staff(AbstractUser):
    employee_id = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50)
    # password field is inherited from AbstractUser
