from django.db import models

class BaseQuantity(models.Model):
    quantity = models.DecimalField(
                    max_digits=12,
                    decimal_places=3,
                    default=0.0,
                    blank=True,
                    verbose_name='кол-во'
                    )

    class Meta:
        verbose_name = 'количество'
        verbose_name_plural = 'количество'
        db_table = 'quantity'
        abstract = True


