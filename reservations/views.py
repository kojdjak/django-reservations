from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Reservation, Field
from datetime import datetime


def index(request):
    fields = Field.objects.all()
    return render(request, 'reservations/index.html', {'fields': fields, })


def field_detail(request, field_id):
    field = Field.objects.get(id=field_id)
    return render(request, 'reservations/field_detail.html', {'field_id': field_id, 'field': field, 'hours': range(24), })


def field_reserve(request, field_id, reservation_time):
    field = Field.objects.get(id=field_id)
    user = None if request.user.is_anonymous() else request.user
    today = datetime.today()
    time = datetime(today.year, today.month, today.day, int(reservation_time))
    Reservation.objects.create(name="Reservation", field=field, user=user, time=time)
    return HttpResponseRedirect(reverse('reservations:field.detail', kwargs={'field_id': field_id}))

