from django.shortcuts import render


def faq_view(request, *args, **kwargs):
    """
    A view to render frequently asked questions' template
    """
    return render(request, "pages/faq.html")
