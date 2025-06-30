from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from config import settings
from mainapp.views import ProductViewSet, product_analytics


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', product_analytics, name='product_analytics'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
