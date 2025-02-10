# milk_collection_app/views.py

from rest_framework import viewsets
from .models import Farmer, CollectionCenter, MilkCollectionEntry
from .serializers import FarmerSerializer, CollectionCenterSerializer, MilkCollectionEntrySerializer

# API Viewsets
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class CollectionCenterViewSet(viewsets.ModelViewSet):
    queryset = CollectionCenter.objects.all()
    serializer_class = CollectionCenterSerializer

class MilkCollectionEntryViewSet(viewsets.ModelViewSet):
    queryset = MilkCollectionEntry.objects.all()
    serializer_class = MilkCollectionEntrySerializer
