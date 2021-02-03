from django.shortcuts import render, get_object_or_404
from .models import Meal

# Create your views here


def all_meals(request):
    """ A view to display all meals, including seach queries """

    meals = Meal.objects.all()

    context = {
        'meals': meals,
    }

    return render(request, 'meals/meals.html', context)


def meal_detail(request, meal_id):
    """ A view to display individual meal details """

    meal = get_object_or_404(Meal, pk=meal_id)

    context = {
        'meals': meal,
    }

    return render(request, 'mealss/meal_detail.html', context)
