from django.db import models

class BasePrice(models.Model):
    price = models.DecimalField(
                max_digits=10,
                decimal_places=2,
                default=0.0,
                blank = True,
                verbose_name='цена'
                )

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'цена'
        verbose_name_plural = 'цены'
        db_table = 'price'
        abstract = True
        managed = False


