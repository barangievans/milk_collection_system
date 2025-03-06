from rest_framework import generics
from .models import SMSNotification
from .serializers import SMSNotificationSerializer

class SMSNotificationListCreateView(generics.ListCreateAPIView):
    queryset = SMSNotification.objects.all()
    serializer_class = SMSNotificationSerializer

class SMSNotificationDetailView(generics.RetrieveDestroyAPIView):
    queryset = SMSNotification.objects.all()
    serializer_class = SMSNotificationSerializer
