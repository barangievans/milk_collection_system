from rest_framework import viewsets
from .models import CollectionCenter  # Keep only CollectionCenter
from .serializers import CollectionCenterSerializer  # Keep only CollectionCenter serializer

# Commenting out everything else
# from django.http import JsonResponse
# from django.utils.dateparse import parse_date
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from .models import Farmer, MilkCollectionEntry
# from .serializers import FarmerSerializer, MilkCollectionEntrySerializer

# API Viewset for Collection Centers Only
class CollectionCenterViewSet(viewsets.ModelViewSet):
    queryset = CollectionCenter.objects.all()
    serializer_class = CollectionCenterSerializer

# Commenting out all other viewsets
# class FarmerViewSet(viewsets.ModelViewSet):
#     queryset = Farmer.objects.all()
#     serializer_class = FarmerSerializer

# class MilkCollectionEntryViewSet(viewsets.ModelViewSet):
#     queryset = MilkCollectionEntry.objects.all()
#     serializer_class = MilkCollectionEntrySerializer

# Commenting out report generation functions
# def generate_daily_report(request):
#     date = parse_date(request.GET.get('date', ''))
#     entries = MilkCollectionEntry.objects.filter(collection_date=date)
#     total_milk = sum(entry.quantity for entry in entries)
#     return JsonResponse({
#         'date': date,
#         'total_milk_collected': total_milk,
#         'entries': list(entries.values('farmer', 'collection_center', 'quantity'))
#     })

# def generate_pdf_report(request):
#     date = parse_date(request.GET.get('date', ''))
#     entries = MilkCollectionEntry.objects.filter(collection_date=date)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="milk_collection_report_{date}.pdf"'
#     pdf = canvas.Canvas(response)
#     pdf.drawString(100, 800, f"Milk Collection Report for {date}")
#     y_position = 780
#     for entry in entries:
#         pdf.drawString(100, y_position, f"Farmer: {entry.farmer.first_name} {entry.farmer.last_name}, Quantity: {entry.quantity} liters")
#         y_position -= 20
#     pdf.showPage()
#     pdf.save()
#     return response
