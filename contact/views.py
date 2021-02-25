from django.shortcuts import render, redirect, reverse
from .models import Contact
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail

import os
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')


def contact(request):
    """
    A view to render contact form/template
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            create_contact_form = Contact(
                name=request.POST.get('name'),
                subject=request.POST.get('subject'),
                email=request.POST.get('email'),
                message=request.POST.get('message'),
                user_id=request.user
            )
            create_contact_form.save()
        else:
            create_contact_form = Contact(
                name=request.POST.get('name'),
                subject=request.POST.get('subject'),
                email=request.POST.get('email'),
                message=request.POST.get('message'),
            )
            create_contact_form.save()

        # Send Email
        send_mail(
            'New Form Submission',
            'Hi Admin,\n\nYou have a new contact message. Sign '
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
        'form': ContactForm
    }
    return render(request, 'contact/contact.html', context)
