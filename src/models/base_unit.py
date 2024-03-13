from django.db import models

class BaseUnit(models.Model):
    name = models.CharField(
                max_length=3,
                verbose_name='ед.'
                )
    description = models.CharField(
                    max_length=30,
                    null=True,
                    blank=True,
                    verbose_name='описание'
                    )

    class Meta:
        verbose_name = 'еденица'
        verbose_name_plural = 'еденицы'
        db_table = 'unit'
        abstract = True


