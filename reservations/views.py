from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Reservation, Field


def index(request):
    return render(request, 'reservations/index.html', {})


def field_detail(request, field_id):
    return render(request, 'reservations/field_detail.html', {'field_id':field_id, 'hours':range(24),})


def field_reserve(request, field_id, time):
    field = Field.objects.get(id=field_id)
    user = None if request.user.is_anonymous() else request.user
    Reservation.objects.create(name="Reservation", field=field, user=user)
    return HttpResponseRedirect(reverse('reservations:field.detail', kwargs={'field_id':field_id}))

