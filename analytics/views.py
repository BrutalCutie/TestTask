from django.shortcuts import render

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

    # Подготовка данных для графиков
    price_buckets = [
        (0, 1000), (1001, 5000), (5001, 10000),
        (10001, 20000), (20001, 50000), (50001, 100000)
    ]

    price_data = []
    for min_val, max_val in price_buckets:
        count = products.filter(price__gte=min_val, price__lte=max_val).count()
        price_data.append({
            'range': f"{min_val}-{max_val}",
            'count': count
        })

    # Данные для графика скидок
    discount_data = []
    for product in products[:50]:  # Ограничиваем количество точек
        discount = (product.price - product.sale_price) / product.price * 100
        discount_data.append({
            'rating': product.rating,
            'discount': discount
        })

    context = {
        'products': products,
        'price_data': price_data,
        'discount_data': discount_data,
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
