from django.test import TestCase
from .models import Farmer

class FarmerModelTest(TestCase):
    def setUp(self):
        Farmer.objects.create(first_name="John", last_name="Doe", id_number="123456789", phone_number="0987654321")

    def test_farmer_creation(self):
        farmer = Farmer.objects.get(id=1)
        self.assertEqual(farmer.first_name, "John")
        self.assertEqual(farmer.last_name, "Doe")