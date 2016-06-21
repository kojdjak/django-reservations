from django.conf.urls import url
from . import views


app_name = 'reservations'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<field_id>[0-9]+)/$', views.field_detail, name='field.detail'),
    url(r'^(?P<field_id>[0-9]+)/(?P<res_date>\d{4}-\d{2}-\d{2})/$', views.field_detail_date, name='field.detail.date'),
    url(r'^(?P<field_id>[0-9]+)/reserve/(?P<reservation_time>[0-9]+)/$', views.field_reserve, name='field.reserve'),
    url(r'^(?P<field_id>[0-9]+)/reserve/(?P<res_date>\d{4}-\d{2}-\d{2})/(?P<reservation_time>[0-9]+)/$', views.field_reserve_date, name='field.reserve.date'),
]