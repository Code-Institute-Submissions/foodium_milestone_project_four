from django.shortcuts import render, redirect, reverse
from .models import Reservation
from .forms import TableReservationForm
from django.contrib import messages
from django.core.mail import send_mail


import os
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')


def reserve_a_table(request):
    """
    A view to render reservation form
    """

    if request.method == 'POST':
        reservation_form = TableReservationForm(request.POST)
        if not reservation_form.is_valid():
            return render(
                request, 'reservation/reservation.html',
                {"form": reservation_form})

        reservation = reservation_form.save()
        if request.user.is_authenticated:
            reservation.user_id = request.user
            reservation.save()

        # Send Email
        send_mail(
            'New Form Submission',
            'Hi Admin,\n\nYou have a new reservation message. Sign '
            'into the admin panel to view.\n\nRegards,'
            'n\nFOODIUM',
            'takaforyannick30@gmail.com',
            [EMAIL_HOST_USER],
            fail_silently=True
        )

        messages.success(request, 'Reservation form successfully submitted.\
                                    We will be in touch!')
        return redirect(reverse('reserve_a_table_success'))

    context = {
        'form': TableReservationForm
    }
    return render(request, 'reservation/reservation.html', context)


def reserve_a_table_success(request):
    """
    A view to render reservation success template
    """
    return render(request, "reservation/reservation_success.html")
