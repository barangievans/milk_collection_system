# milk_collection_app/serializers.py

from rest_framework import serializers
from .models import Farmer, CollectionCenter, MilkCollectionEntry

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'  # Include all fields for the Farmer model

class CollectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionCenter
        fields = '__all__'  # Include all fields for the CollectionCenter model

class MilkCollectionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCollectionEntry
        fields = ['farmer', 'collection_center', 'quantity', 'collection_date', 'collection_time']
