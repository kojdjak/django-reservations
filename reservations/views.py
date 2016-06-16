from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Reservation, Field
from reservations import rutils
from datetime import datetime, timedelta


def index(request):
    fields = Field.objects.all()
    return render(request, 'reservations/index.html', {'fields': fields, })


def field_detail(request, field_id):
    field = Field.objects.get(id=field_id)
    reservations = rutils.getReservations(field_id)
    hours2res = dict.fromkeys(range(24))
    for reservation in reservations:
        hours2res[reservation.time.hour] = reservation
        print(reservation.name + str(reservation.time.hour) )
    return render(request, 'reservations/field_detail.html', {'field_id': field_id, 'field': field, 'hours': range(24), 'hours2res':hours2res })


def field_reserve(request, field_id, reservation_time):
    rutils.createReservation(field_id, reservation_time, None if request.user.is_anonymous() else request.user)
    return HttpResponseRedirect(reverse('reservations:field.detail', kwargs={'field_id': field_id}))

