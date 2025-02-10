from django.db import models
from django.contrib.auth.models import AbstractUser

# Staff model using AbstractUser for authentication
class Staff(AbstractUser):
    employee_id = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Operator', 'Operator')])

    def __str__(self):
        return self.username


# Customer model (Not related to Staff, but for storing farmer details)
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Order model with a relationship to Customer (Farmer) and Collection Center
class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"


# Farmer model for storing farmer details
class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    id_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Collection Center model for storing collection center details
class CollectionCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Milk Collection Entry model with updated fields
class MilkCollectionEntry(models.Model):
    # Relationships
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)  # Linked to Farmer
    collection_center = models.ForeignKey(CollectionCenter, on_delete=models.CASCADE)  # Linked to Collection Center

    # Milk collection data
    quantity = models.DecimalField(max_digits=5, decimal_places=2)  # Quantity in Liters
    
    # New fields to track the date and time of collection
    collection_date = models.DateField(auto_now_add=True)  # Automatically sets the date when entry is created
    collection_time = models.TimeField(auto_now_add=True)  # Automatically sets the time when entry is created

    def __str__(self):
        return f"Milk collected from {self.farmer} at {self.collection_center} on {self.collection_date} at {self.collection_time}"
