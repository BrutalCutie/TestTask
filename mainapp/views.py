from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from mainapp.models import Product
from mainapp.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'price': ['gte', 'lte'],
        'sale_price': ['gte', 'lte'],
        'rating': ['gte'],
        'reviews_count': ['gte'],
    }
    ordering_fields = ['name', 'price', 'rating', 'reviews_count']
