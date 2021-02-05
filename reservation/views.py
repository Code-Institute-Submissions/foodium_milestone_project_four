from django.shortcuts import render
from .models import Reservation

# Create your views here.


def reserve_a_table(request):

    context = {}

    return render(request, 'reservation/reservation.html', context)
