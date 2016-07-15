from django.conf.urls import url
from . import views


app_name = 'reservations'
urlpatterns = [
    url(r'^$', views.index, name='index'),  #index
    url(r'^(?P<field_id>[0-9]+)/$',
        views.field_detail, name='field.detail'),   #detail of field without date specified, it means for today.
    url(r'^(?P<field_id>[0-9]+)/(?P<res_date>\d{4}-\d{2}-\d{2})/$',
        views.field_detail_date, name='field.detail.date'),   #detail of field for specific date.
    url(r'^(?P<field_id>[0-9]+)/reserve/(?P<reservation_time>[0-9]+)/$',
        views.field_reserve, name='field.reserve'),    #reserve field with hour without date (=today)
    url(r'^(?P<field_id>[0-9]+)/reserve/(?P<res_date>\d{4}-\d{2}-\d{2})/(?P<reservation_time>[0-9]+)/$',
        views.field_reserve_date, name='field.reserve.date'),  #reserve field with hour with date
    url(r'^reservations/$',
        views.reservations, name='reservations'),    #list reservations. if logged in -> list users reservations
    url(r'^reservations/(?P<reservation_id>[0-9]+)/$',
        views.reservation_detail, name='reservation.detail'),    #detail of reservation
    url(r'^reservations/(?P<reservation_id>[0-9]+)/delete/$',
        views.reservation_delete, name='reservation.delete')  # delete reservation
]