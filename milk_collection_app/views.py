from rest_framework.decorators import action 
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CollectionCenter, Farmer, MilkCollection  # ✅ Import models
from .serializers import CollectionCenterSerializer, FarmerSerializer, MilkCollectionSerializer  # ✅ Import serializers

class CollectionCenterViewSet(viewsets.ModelViewSet):
    queryset = CollectionCenter.objects.all()
    serializer_class = CollectionCenterSerializer

    @action(detail=False, methods=['get'], url_path='find-by-number')
    def find_by_number(self, request):
        number = request.query_params.get('number')
        if not number:
            return Response({"error": "Number parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            collection_center = CollectionCenter.objects.get(number=number)
            serializer = self.get_serializer(collection_center)
            return Response(serializer.data)
        except CollectionCenter.DoesNotExist:
            return Response({"error": "Collection Center not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path='all')
    def get_collection_center_list(self, request):
        queryset = CollectionCenter.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'], url_path='remove')
    def delete_by_id(self, request, pk=None):
        try:
            collection_center = self.get_object()
            collection_center.delete()
            return Response({"message": "Collection Center deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except CollectionCenter.DoesNotExist:
            return Response({"error": "Collection Center not found"}, status=status.HTTP_404_NOT_FOUND)

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    @action(detail=False, methods=['get'], url_path='find-by-phone')
    def find_by_phone(self, request):
        phone = request.query_params.get('phone')
        if not phone:
            return Response({"error": "Phone parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            farmer = Farmer.objects.get(phone=phone)
            serializer = self.get_serializer(farmer)
            return Response(serializer.data)
        except Farmer.DoesNotExist:
            return Response({"error": "Farmer not found"}, status=status.HTTP_404_NOT_FOUND)


class MilkCollectionViewSet(viewsets.ModelViewSet):
    queryset = MilkCollection.objects.all().order_by('-collected_at')
    serializer_class = MilkCollectionSerializer