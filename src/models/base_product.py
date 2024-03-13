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
                BaseUnit,
                on_delete=models.PROTECT,
                verbose_name='ед.'
                )
    category = models.ForeignKey(
                    BaseCategory,
                    on_delete=models.PROTECT,
                    verbose_name='category'
                    )
    price = models.OneToOneField(
                BasePrice,
                on_delete=models.CASCADE,
                verbose_name='цена'
                )
    quantity = models.OneToOneField(
                    BaseQuantity,
                    on_delete=models.CASCADE,
                    verbose_name='кол-во'
                    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'product'

