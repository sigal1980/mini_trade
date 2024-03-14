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
    slug = models.SlugField(
                max_length=60
                )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table = 'category'
        abstract = True


