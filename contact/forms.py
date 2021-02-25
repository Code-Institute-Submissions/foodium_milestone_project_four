from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Contact form"""
    class Meta:
        model = Contact
        fields = [
            'name',
            'subject',
            'email',
            'message'
        ]

    name = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name here'
        })
    )
    subject = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your subject here'
        })
    )
    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address here'
        })
    )
    message = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message here'
        })
    )
