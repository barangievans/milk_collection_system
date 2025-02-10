# milk_collection_app/views.py

from rest_framework import viewsets
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Farmer, CollectionCenter, MilkCollectionEntry
from .serializers import FarmerSerializer, CollectionCenterSerializer, MilkCollectionEntrySerializer

# API Viewsets for Farmers, Collection Centers, and Milk Collection Entries

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class CollectionCenterViewSet(viewsets.ModelViewSet):
    queryset = CollectionCenter.objects.all()
    serializer_class = CollectionCenterSerializer

class MilkCollectionEntryViewSet(viewsets.ModelViewSet):
    queryset = MilkCollectionEntry.objects.all()  # Get all milk collection entries
    serializer_class = MilkCollectionEntrySerializer  # Use the corresponding serializer

    # You can add additional functionality here if needed, e.g., filtering or permission checks

# API to Generate Reports:

def generate_daily_report(request):
    # Parse date from query parameters (e.g., '2025-02-10')
    date = parse_date(request.GET.get('date', ''))
    
    # Filter the milk collection entries based on the date
    entries = MilkCollectionEntry.objects.filter(collection_date=date)
    
    # Generate a simple response with total collected milk
    total_milk = sum(entry.quantity for entry in entries)
    
    return JsonResponse({
        'date': date,
        'total_milk_collected': total_milk,
        'entries': list(entries.values('farmer', 'collection_center', 'quantity'))  # Convert queryset to list
    })

def generate_pdf_report(request):
    # Get date from the query parameter
    date = parse_date(request.GET.get('date', ''))
    
    # Filter the milk collection entries based on the date
    entries = MilkCollectionEntry.objects.filter(collection_date=date)
    
    # Create the HTTP response with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="milk_collection_report_{date}.pdf"'
    
    # Create a new PDF document
    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, f"Milk Collection Report for {date}")
    
    y_position = 780  # Start position for the first entry
    for entry in entries:
        pdf.drawString(100, y_position, f"Farmer: {entry.farmer.first_name} {entry.farmer.last_name}, Quantity: {entry.quantity} liters")
        y_position -= 20  # Move to the next line
    
    pdf.showPage()
    pdf.save()  # Save the PDF
    
    return response
