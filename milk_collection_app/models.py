from django.db import models

# Commenting out everything except CollectionCenter

# Customer model (For storing farmer details)
# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.name

# Order model with a relationship to Customer (Farmer) and Collection Center
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=100)
#     quantity = models.IntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Order #{self.id} by {self.customer.name}"

# Farmer model for storing farmer details
class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)  # Allow NULL for optional fields
    id_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.id_number})"


# Collection Center model (Updated from CollectionCentre to CollectionCenter)
class CollectionCenter(models.Model):
    collection_center_number = models.CharField(max_length=50, unique=True)  # Unique identifier for the center
    name = models.CharField(max_length=100)  # Collection center name
    contact_number = models.CharField(max_length=15, unique=True)  # Contact number for the center

    def __str__(self):
        return f"{self.collection_center_number} - {self.name}"


class MilkCollection(models.Model):
    farmer = models.ForeignKey('Farmer', on_delete=models.CASCADE, related_name='milk_collections')  # Links to Farmer
    collection_center = models.ForeignKey('CollectionCenter', on_delete=models.CASCADE, related_name='milk_collections')  # Links to Collection Center
    quantity_liters = models.DecimalField(max_digits=5, decimal_places=2)  # Milk quantity in liters
    collected_at = models.DateTimeField(auto_now_add=True)  # Timestamp for collection

    def __str__(self):
        return f"{self.farmer.first_name} {self.farmer.last_name} - {self.quantity_liters}L"
    

class SMSNotification(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SMS to {self.farmer.phone_number} at {self.sent_at}"
