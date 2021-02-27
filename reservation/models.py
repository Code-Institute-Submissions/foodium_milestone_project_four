from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Reservation(models.Model):
    '''
     Fields guests will need to fill to make a reservation
    '''
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    contact_date = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
