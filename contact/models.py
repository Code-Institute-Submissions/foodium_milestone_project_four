from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=200, blank=True)
    contact_date = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
