# milk_collection_app/serializers.py

from rest_framework import serializers
from .models import CollectionCenter, Farmer,MilkCollection  # ✅ Import models

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'  # Or list specific fields if needed

class CollectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionCenter
        fields = '__all__'  # Include all fields for the CollectionCenter model

class MilkCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCollection
        fields = '__all__'
