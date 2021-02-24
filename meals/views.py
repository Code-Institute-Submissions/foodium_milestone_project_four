from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Meal, Category
from .forms import MealForm

# Create your views here


def all_meals(request):
    """ A view to display all meals, including seach queries """

    meals = Meal.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            meals = meals.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'meals/meals.html', context)


def meal_detail(request, meal_id):
    """ A view to display individual meal details """

    meal = get_object_or_404(Meal, pk=meal_id)

    context = {
        'meal': meal,
    }

    return render(request, 'meals/meal_detail.html', context)


def add_meal(request):
    """ Add a meal to the store """
    form = MealForm()
    template = 'meals/add_meal.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
