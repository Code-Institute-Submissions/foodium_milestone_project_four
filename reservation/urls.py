from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserve_a_table, name='reserve_a_table'),
    path('success/', views.reserve_a_table_success,
         name='reserve_a_table_success'),
]
