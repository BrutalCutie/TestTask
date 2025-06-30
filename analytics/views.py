from django.shortcuts import render
from django.db.models import Count, Avg, F, ExpressionWrapper, FloatField, Max, Case, When, Value
from django.db.models.functions import Round
from mainapp.models import Product


def product_analytics(request):
    # Получаем параметры фильтрации
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 100000)
    min_rating = request.GET.get('min_rating', 0)
    min_reviews = request.GET.get('min_reviews', 0)
    sort_by = request.GET.get('sort_by', 'name')
    sort_order = request.GET.get('sort_order', 'asc')

    # Фильтрация товаров
    products = Product.objects.filter(
        price__gte=min_price,
        price__lte=max_price,
        rating__gte=min_rating,
        reviews_count__gte=min_reviews
    )

    # Сортировка
    if sort_order == 'desc':
        sort_by = f'-{sort_by}'
    products = products.order_by(sort_by)

    max_price_val = products.aggregate(max_price=Max('price'))['max_price']
    if max_price_val is None:
        max_price_val = 10000
    else:
        max_price_val = float(max_price_val)

    bucket_size = max(1000, max_price_val // 10)
    price_buckets = []
    current = 0
    while current <= max_price_val + bucket_size:
        price_buckets.append(current)
        current += bucket_size

    price_data = []
    for i in range(len(price_buckets) - 1):
        min_val = price_buckets[i]
        max_val = price_buckets[i + 1]
        count = products.filter(price__gte=min_val, price__lt=max_val).count()
        price_data.append({
            'range': f"{min_val:.0f}-{max_val:.0f}",
            'count': count
        })

    # Группируем товары по округленному рейтингу и вычисляем среднюю скидку
    discount_data = products.annotate(
        rounded_rating=Round('rating', 1)  # Округляем рейтинг до 0.1
    ).values('rounded_rating').annotate(
        avg_discount=ExpressionWrapper(
            Avg(
                Case(
                    # Вычисляем скидку только если price > 0
                    When(price__gt=0,
                         then=ExpressionWrapper(
                             (F('price') - F('sale_price')) * 100.0 / F('price'),
                             output_field=FloatField()
                         )
                         ),
                    # Если price=0, устанавливаем скидку 0
                    default=Value(0.0),
                    output_field=FloatField()
                )
            ),
            output_field=FloatField()
        ),
        product_count=Count('id')
    ).order_by('rounded_rating')

    discount_data_list = [
        {
            'rating': float(item['rounded_rating']),
            'discount': float(item['avg_discount']) if item['avg_discount'] is not None else 0.0
        }
        for item in discount_data
    ]

    context = {
        'products': products,
        'price_data': price_data,
        'discount_data': discount_data_list,
        'filters': {
            'min_price': min_price,
            'max_price': max_price,
            'min_rating': min_rating,
            'min_reviews': min_reviews
        },
        'sort': {
            'by': sort_by.lstrip('-'),
            'order': sort_order
        }
    }
    return render(request, 'analytics/analytics.html', context)
