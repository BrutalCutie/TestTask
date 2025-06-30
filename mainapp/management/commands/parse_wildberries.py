import requests
from django.core.management.base import BaseCommand
from mainapp.models import Product


class Command(BaseCommand):
    help = 'Парсинг товаров с Wildberries'

    def add_arguments(self, parser):
        parser.add_argument('query', type=str)

    def handle(self, *args, **options):
        query = options['query']
        url = f"https://search.wb.ru/exactmatch/ru/common/v4/search"
        params = {
            'query': query,
            'resultset': 'catalog',
            'sort': 'popular',
            'page': 1
        }
        response = requests.get(url, params=params)
        data = response.json()['data']['products']

        for item in data:
            Product.objects.update_or_create(
                id=item['id'],
                defaults={
                    'name': item['name'],
                    'price': item['priceU'] / 100,
                    'sale_price': item['salePriceU'] / 100,
                    'rating': item['reviewRating'],
                    'reviews_count': item['feedbacks']
                }
            )
        self.stdout.write(f"Добавлено товаров: {len(data)}")