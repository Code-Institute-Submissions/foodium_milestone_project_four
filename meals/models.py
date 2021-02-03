from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
