from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from milk_collection_app.views import MilkCollectionViewSet, CollectionCenterViewSet, FarmerViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'milk-collections', MilkCollectionViewSet)  # Register MilkCollectionViewSet
router.register(r'collection-centers', CollectionCenterViewSet)
router.register(r'farmers', FarmerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include API endpoints
]
