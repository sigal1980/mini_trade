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
    slug = models.SlugField(
                max_length=60
                )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'еденица'
        verbose_name_plural = 'еденицы'
        db_table = 'unit'
        abstract = True
        managed = False


