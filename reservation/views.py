from django.shortcuts import render
from .models import Reservation
from .forms import TableReservationForm
from reservation.models import Reservation

# Create your views here.


def reserve_a_table(request):
    reserve_form = TableReservationForm()

    if request.method == 'POST':
        reserve_form = TableReservationForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {
        'form': reserve_form
    }

    return render(request, 'reservation/reservation.html', context)
