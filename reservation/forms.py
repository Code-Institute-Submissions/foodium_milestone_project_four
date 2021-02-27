from django import forms
from .models import Reservation


class TableReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = [
            'name',
            'phone_number',
            'email',
            'number_of_persons',
            'date',
            'time',
        ]

    name = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control border-dark rounded-0',
            'placeholder': 'Enter  name'
        })
    )
    phone_number = forms.IntegerField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control border-dark rounded-0',
            'placeholder': 'Enter phone number'
        })
    )
    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control border-dark rounded-0',
            'placeholder': 'Enter email'
        })
    )
    number_of_persons = forms.IntegerField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control border-dark rounded-0',
            'placeholder': 'Enter number of persons'
        })
    )
    date = forms.IntegerField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control border-dark rounded-0',
            'placeholder': 'Enter Date'
        })
    )
    time = forms.TimeField(
        required=True,
        label='',
        widget=forms.TimeInput(attrs={
            'class': 'form-control border-dark rounded-0',
            'placeholder': 'Enter Time'
        })
    )
