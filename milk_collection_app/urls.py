from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectionCenterViewSet  # Keep only CollectionCenterViewSet

# Set up router for CollectionCenter only
router = DefaultRouter()
router.register(r'collection-centers', CollectionCenterViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include only CollectionCenter router
]
