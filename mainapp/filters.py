from django_filters import rest_framework as filters
from mainapp.models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_sale_price = filters.NumberFilter(field_name="sale_price", lookup_expr='gte')
    max_sale_price = filters.NumberFilter(field_name="sale_price", lookup_expr='lte')
    min_rating = filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = filters.NumberFilter(field_name="rating", lookup_expr='lte')
    min_reviews = filters.NumberFilter(field_name="reviews_count", lookup_expr='gte')

    class Meta:
        model = Product
        fields = []
