from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import AutoField
# Create your models here.


class Contact(models.Model):
    yourName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobilenumber = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.yourName



class turfBooking(models.Model):
    time_slot = models.CharField(max_length=12)
    isBooked = models.BooleanField(default=False)
    days = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.time_slot


class bookslot(models.Model):
    week = ArrayField(
        ArrayField(
            models.IntegerField(default=0),
            size=20,
        ),
        size=7,
    )


class Time(models.Model):
    name = models.CharField(max_length=200, default="")
    week = ArrayField(
        ArrayField(
            models.IntegerField(default=0),
            size=20,
        ),
        size=7,
    )

class TurfBooked(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    amount = models.IntegerField()
    selected_date = models.CharField(max_length=200)
    current_date = models.CharField(max_length=200)
    booking_time = models.CharField(max_length=200, default="")
    slots = ArrayField(
        models.CharField(max_length=200, default=""),
        size=20,
    )
    
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
