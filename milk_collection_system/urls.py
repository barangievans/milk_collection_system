from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from milk_collection_app import views

router = DefaultRouter()
router.register(r'farmers', views.FarmerViewSet)
router.register(r'collection-centers', views.CollectionCenterViewSet)
router.register(r'milk-collection', views.MilkCollectionEntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Ensure this is correctly registered
]
