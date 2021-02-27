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
        if request.user.is_authenticated:
            create_reservation_form = Reservation(
                name=request.POST.get('name'),
                phone_number=request.POST.get('phone_number'),
                email=request.POST.get('email'),
                number_of_persons=request.POST.get('number_of_persons'),
                date=request.POST.get('date'),
                time=request.POST.get('time'),
                user_id=request.user
            )
            create_reservation_form.save()
        else:
            create_reservation_form = Reservation(
                name=request.POST.get('name'),
                phone_number=request.POST.get('phone_number'),
                email=request.POST.get('email'),
                number_of_persons=request.POST.get('number_of_persons'),
                date=request.POST.get('date'),
                time=request.POST.get('time'),
            )
            create_reservation_form.save()

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

        messages.success(request, 'Contact form successfully submitted.\
                                    We will be in touch!')
        return redirect(reverse('contact_success'))

    context = {
        'form': TableReservationForm
    }
    return render(request, 'reservation/reservation.html', context)
