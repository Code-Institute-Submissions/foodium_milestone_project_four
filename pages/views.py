from django.shortcuts import render


def faq_view(request, *args, **kwargs):
    """
    A view to render frequently asked questions' template
    """
    return render(request, "pages/faq.html")


def about_us(request, *args, **kwargs):
    """
    A view to render about_us template
    """
    return render(request, "pages/about_us.html")
