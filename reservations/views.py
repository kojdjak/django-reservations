from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone, dateparse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Reservation, Field, Venue
from reservations import rutils


def index(request):
    """
    Index view shows all fields in system for now.
    """
    return render(request, 'reservations/index.html', {'fields': Field.objects.all(), })


class FieldDetailViewModel:
    """
    UI View Model for detail of field.
    """
    def __init__(self, res_date):
        self.res_date = res_date
        self.today = dateparse.parse_date(res_date) if res_date else timezone.now()
        self.res_date_previous = timezone.datetime(self.today.year, self.today.month, self.today.day-1, 0).strftime("%Y-%m-%d")
        self.res_date_next = timezone.datetime(self.today.year, self.today.month, self.today.day+1, 0).strftime("%Y-%m-%d")


def field_detail(request, field_id):
    """
    Detail of field without date (=today).
    """
    return field_detail_date(request, field_id, None)


def field_detail_date(request, field_id, res_date):
    """
    Detail of field with date specified.
    """
    field = Field.objects.get(id=field_id)
    reservations = rutils.get_reservations(field_id, res_date)
    fdvm = FieldDetailViewModel(res_date if res_date else timezone.now().strftime("%Y-%m-%d"))
    hours2res = dict.fromkeys(range(24))
    for reservation in reservations:
        hours2res[reservation.time.hour] = reservation
    return render(request, 'reservations/field_detail.html', {'field_id': field_id, 'field': field,
                                                              'hours2res': hours2res, 'fdvm': fdvm })


def field_reserve(request, field_id, reservation_time):
    """
    Reserve field for time without date (=today).
    """
    return field_reserve_date(request, field_id, None, reservation_time)


def field_reserve_date(request, field_id, res_date, reservation_time):
    """
    Reserve field for time with date. Redirect to detail of field afterwards.
    """
    rutils.create_reservation(field_id, res_date, reservation_time, None if request.user.is_anonymous() else request.user)
    if res_date:
        return HttpResponseRedirect(reverse('reservations:field.detail.date', kwargs={'field_id': field_id, 'res_date':res_date}))
    else:
        return HttpResponseRedirect(reverse('reservations:field.detail', kwargs={'field_id': field_id}))


def reservations(request):
    """
    List reservations.

    if user is logged in, list only user's reservations.
    """
    ress = rutils.get_reservations_user(None if request.user.is_anonymous() else request.user)
    return render(request, 'reservations/reservations.html', {'ress':ress,})


def reservation_detail(request, reservation_id):
    """
    Detail of reservations.

    """
    res = Reservation.objects.get(id=reservation_id)
    return render(request, 'reservations/reservation_detail.html', {'res':res,})


def reservation_delete(request, reservation_id):
    """
    Delete reservation.

    Redirect to list of reservations.
    """
    Reservation.objects.get(id=reservation_id).delete()
    return HttpResponseRedirect(reverse('reservations:reservations', kwargs={}))


class VenuesListView(ListView):
    model = Venue
    template_name = "reservations/venues.html"


class VenueDetailView(DetailView):
    model = Venue
    template_name = "reservations/venue_detail.html"


class VenueAllFieldsView(DetailView):
    model = Venue
    template_name = "reservations/venue_detail_fields.html"

    def get_context_data(self, **kwargs):
        venueid = self.kwargs['pk']
        venue = self.get_object()
        res_date = timezone.now().strftime("%Y-%m-%d")
        all_fdvm = {}
        for field in venue.field_set.all():
            reservations = rutils.get_reservations(field.id, res_date)
            fdvm = FieldDetailViewModel(res_date if res_date else timezone.now().strftime("%Y-%m-%d"))
            hours2res = dict.fromkeys(range(24))
            for reservation in reservations:
                hours2res[reservation.time.hour] = reservation
            all_fdvm[field.id] = hours2res
        context = super(VenueAllFieldsView, self).get_context_data(**kwargs)
        context['all_fdvm'] = all_fdvm
        return context


