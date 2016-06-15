from django.utils import timezone
from datetime import datetime, timedelta

from .models import Reservation, Field

'''
kind of utils for django-reservations
'''


class ReservationExist(Exception):
    pass


def createReservation(field_id, reservation_time, user):
    field = Field.objects.get(id=field_id)
    today = timezone.now()
    time = datetime(today.year, today.month, today.day, int(reservation_time), tzinfo=today.tzinfo)
    Reservation.objects.create(name="Reservation", field=field, user=user, time=time)
    pass


def getReservations(field_id):
    field = Field.objects.get(id=field_id)
    today = timezone.now()
    time = datetime(today.year, today.month, today.day, 0)
    return Reservation.objects.filter(time__range=[time, time+timedelta(days=1)])

