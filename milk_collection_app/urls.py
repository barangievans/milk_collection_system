from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views  # Import JWT views
from .views import FarmerViewSet, CollectionCenterViewSet, MilkCollectionEntryViewSet
from . import views  # Import views for report generation

# Set up router for viewsets
router = DefaultRouter()
router.register(r'farmers', FarmerViewSet)
router.register(r'collection-centers', CollectionCenterViewSet)
router.register(r'milk-collection', MilkCollectionEntryViewSet)

urlpatterns = [
    # JWT Token Endpoints
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    
    # Report Generation Endpoints
    path('daily-report/', views.generate_daily_report, name='daily_report'),
    path('pdf-report/', views.generate_pdf_report, name='pdf_report'),
    
    # Other URLs
    path('', include(router.urls)),  # Include the router URLs for the other views
]
