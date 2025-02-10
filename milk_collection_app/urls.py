from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet, CollectionCenterViewSet, MilkCollectionEntryViewSet

router = DefaultRouter()
router.register(r'farmers', FarmerViewSet)
router.register(r'collection-centers', CollectionCenterViewSet)
router.register(r'milk-collection', MilkCollectionEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Make sure the URLs are included here
]
