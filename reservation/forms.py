from django import forms
from .models import Reservation


class TableReservationForm(forms.ModelForm):
    '''
    Form that allows guests/users to reserve a table
    '''
    class Meta:
        model = Reservation
        fields = '__all__'
