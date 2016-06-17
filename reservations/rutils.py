from django.utils import timezone, dateparse
from datetime import datetime, timedelta

from .models import Reservation, Field

'''
kind of utils for django-reservations
'''


class ReservationExist(Exception):
    pass


def create_reservation(field_id, res_date, reservation_time, user):
    field = Field.objects.get(id=field_id)
    today = dateparse.parse_date(res_date) if res_date else timezone.now()
    time = timezone.datetime(today.year, today.month, today.day, int(reservation_time), tzinfo=timezone.now().tzinfo)
    Reservation.objects.create(name="Reservation", field=field, user=user, time=time)
    pass


def get_reservations(field_id, res_date):
    field = Field.objects.get(id=field_id)
    today = dateparse.parse_date(res_date)if res_date else timezone.now()
    time = timezone.datetime(today.year, today.month, today.day, 0)
    return Reservation.objects.filter(time__range=[time, time+timedelta(days=1)])

