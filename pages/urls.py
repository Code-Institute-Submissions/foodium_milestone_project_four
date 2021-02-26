from django.urls import path
from .views import faq_view, about_us


urlpatterns = [
    path('faq/', faq_view, name="faq"),
    path('about/', about_us, name="about_us"),
]
