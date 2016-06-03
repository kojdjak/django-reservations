from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField(max_length=255)


class Field(models.Model):
    name = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue)


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    field = models.ForeignKey(Field)

