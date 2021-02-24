from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_slug(self):
        return self.slug


class Meal(models.Model):
    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    description = models.TextField()
    people = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preparation_time = models.IntegerField()
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = models.ImageField(upload_to='meals', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
