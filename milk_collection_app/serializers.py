from rest_framework import serializers
from .models import Farmer, CollectionCenter, MilkCollectionEntry

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class CollectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionCenter
        fields = '__all__'

class MilkCollectionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCollectionEntry
        fields = '__all__'