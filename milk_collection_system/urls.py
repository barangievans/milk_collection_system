from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from milk_collection_app.views import (
    MilkCollectionViewSet, 
    CollectionCenterViewSet, 
    FarmerViewSet
)
from milk_collection_app.sms_notifications import (
    SMSNotificationListCreateView, 
    SMSNotificationDetailView
)  # ✅ Import SMS notification views correctly

# Initialize the router
router = DefaultRouter()
router.register(r'milk-collections', MilkCollectionViewSet)
router.register(r'collection-centers', CollectionCenterViewSet)
router.register(r'farmers', FarmerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include API endpoints from the router
    path('api/sms_notifications/', SMSNotificationListCreateView.as_view(), name='sms-notifications-list'),
    path('api/sms_notifications/<int:pk>/', SMSNotificationDetailView.as_view(), name='sms-notification-detail'),
]
