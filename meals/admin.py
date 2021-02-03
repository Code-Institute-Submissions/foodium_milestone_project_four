from django.contrib import admin
from .models import Category, Meal

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )


class MealAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'category',
        'price',
        'description'
        'people'
        'preparation_time'
        'rating',
        'image',
        'stock',
        'available'
    )


admin.site.register(Category)
admin.site.register(Meal)
