from django.shortcuts import render
from .models import Meal

# Create your views here


def all_meals(request):
    """ A view to display all meals, including seach queries """

    meals = Meal.objects.all()

    context = {
        'meals': meals,
    }

    return render(request, 'meals/meals.html', context)
