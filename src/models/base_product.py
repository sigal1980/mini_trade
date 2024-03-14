from django.db import models

from src.models import BaseUnit
from src.models import BaseCategory
from src.models import BasePrice
from src.models import BaseQuantity


class BaseProduct(models.Model):
    name = models.CharField(
                max_length=30,
                verbose_name='наименование'
                )
    description = models.CharField(
                    max_length=200,
                    null=True,
                    blank=True,
                    verbose_name='описание'
                    )
    unit = models.ForeignKey(
                'Unit',
                on_delete=models.PROTECT,
                verbose_name='ед.'
                )
    category = models.ForeignKey(
                    'Category',
                    on_delete=models.PROTECT,
                    verbose_name='категория'
                    )
    price = models.OneToOneField(
                'Price',
                on_delete=models.CASCADE,
                verbose_name='цена'
                )
    quantity = models.OneToOneField(
                    'Quantity',
                    on_delete=models.CASCADE,
                    verbose_name='кол-во'
                    )
    slug = models.SlugField(
                max_length=60,
                null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'product'
        abstract = True


