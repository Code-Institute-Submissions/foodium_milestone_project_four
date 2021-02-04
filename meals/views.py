from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Meal

# Create your views here


def all_meals(request):
    """ A view to display all meals, including seach queries """

    meals = Meal.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You have not enter any search criteria!")
                return redirect(reverse('meals'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            meals = meals.filter(queries)

    context = {
        'meals': meals,
        'search_term': query
    }

    return render(request, 'meals/meals.html', context)


def meal_detail(request, meal_id):
    """ A view to display individual meal details """

    meal = get_object_or_404(Meal, pk=meal_id)

    context = {
        'meal': meal,
    }

    return render(request, 'meals/meal_detail.html', context)
