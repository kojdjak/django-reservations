from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    """
    Model for Venue, which contains more fields.

    Venue could not be reserved.
    """
    name = models.CharField(max_length=255)


class Field(models.Model):
    """
    Model for Field, which could be reserved. It have to be part of Venue
    """
    name = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue)


class Reservation(models.Model):
    """
    Reservation itself.

    user: user who does the reservation. could be anonymous
    field: field which is being reserved
    time: datetime of reservations. At this moment it's on hour granularity.
    """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank = True, null = True)
    field = models.ForeignKey(Field)
    time = models.DateTimeField(default=None, blank=True, null=True)

