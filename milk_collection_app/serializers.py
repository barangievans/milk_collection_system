# milk_collection_app/serializers.py

from rest_framework import serializers
from .models import CollectionCenter

# Commenting out FarmerSerializer
# class FarmerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Farmer
#         fields = '__all__'  # Include all fields for the Farmer model

class CollectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionCenter
        fields = '__all__'  # Include all fields for the CollectionCenter model

# Commenting out MilkCollectionEntrySerializer
# class MilkCollectionEntrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MilkCollectionEntry
#         fields = ['farmer', 'collection_center', 'quantity', 'collection_date', 'collection_time']
