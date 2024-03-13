from django.db import models

class BaseCategory(models.Model):
    name = models.CharField(
                max_length=30,
                verbose_name='категория'
                )

    description = models.CharField(
                    max_length=200,
                    null=True,
                    blank=True,
                    verbose_name='описание'
                    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table = 'category'
