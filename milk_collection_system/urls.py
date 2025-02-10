from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views  # Import JWT views
from milk_collection_app import views

# Set up the router for your viewsets
router = DefaultRouter()
router.register(r'farmers', views.FarmerViewSet)
router.register(r'collection-centers', views.CollectionCenterViewSet)
router.register(r'milk-collection', views.MilkCollectionEntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('api/', include(router.urls)),  # Include the app URLs for viewsets

    # JWT Token Endpoints
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
]
