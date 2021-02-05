from django import forms
from .models import Reservation


class TableReservationForm(forms.ModelForm):
    '''
    Form that allows guests/users to reserve a table
    '''
    class meta:
        model = Reservation
        fields = '__all__'
