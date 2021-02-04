from django.db import models

# Create your models here.


class Reservation(models.Model):
    '''
     Fields guests will need to fill to make a reservation
    '''
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
