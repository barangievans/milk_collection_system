from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from milk_collection_app import views

# Set up the router for only CollectionCenterViewSet
router = DefaultRouter()
router.register(r'collection-centers', views.CollectionCenterViewSet)  # Keep only this

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('api/', include(router.urls)),  # Include only collection center URLs
]
