from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='наименование',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='цена'
    )
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="цена со скидкой"
    )
    rating = models.FloatField(
        verbose_name="рейтинг товара",
    )
    reviews_count = models.IntegerField(
        verbose_name='количество отзывов'
    )
    # для будущей возможной отладки.
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.pk=} | {self.name=}"

    def __repr__(self):
        return f"< {self.__class__.__name__} {self.pk=} | {self.name=} >"
