from django.utils import timezone, dateparse
from datetime import datetime, timedelta

from .models import Reservation, Field

'''
kind of utils for django-reservations
'''


class ReservationExist(Exception):
    pass


def create_reservation(field_id, res_date, reservation_time, user):
    '''
    Create reservation.

    :param field_id: id of field for which to create reservations
    :param res_date: date on which to create reservation. None -> today
    :param reservation_time: time of reservation
    :param user: actual user or None
    :return:
    '''
    field = Field.objects.get(id=field_id)
    today = dateparse.parse_date(res_date) if res_date else timezone.now()
    time = timezone.datetime(today.year, today.month, today.day, int(reservation_time), tzinfo=timezone.now().tzinfo)
    return Reservation.objects.create(name="Reservation", field=field, user=user, time=time)


def get_reservations(field_id, res_date):
    field = Field.objects.get(id=field_id)
    today = dateparse.parse_date(res_date)if res_date else timezone.now()
    time = timezone.datetime(today.year, today.month, today.day, 0)
    return Reservation.objects.filter(time__range=[time, time+timedelta(days=1)])

