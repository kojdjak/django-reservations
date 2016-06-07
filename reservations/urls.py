from django.conf.urls import url
from . import views


app_name = 'reservations'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<field_id>[0-9]+)/$', views.field_detail, name='field.detail'),
    url(r'^(?P<field_id>[0-9]+)/reserve/(?P<time>[0-9]+)$', views.field_reserve, name='field.reserve'),
]