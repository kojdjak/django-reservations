from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField(max_length=255)


class Field(models.Model):
    name = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue)


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank = True, null = True)
    field = models.ForeignKey(Field)
    time = models.DateTimeField(default=None, blank=True, null=True)

