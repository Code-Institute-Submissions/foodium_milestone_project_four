from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_meals, name='meals'),
    path('<meal_id>', views.meal_detail, name='meal_detail'),
]
