from django.contrib import admin

from .models import Reservation, Field, Venue


# Register your models here.
admin.site.register(Reservation)
admin.site.register(Field)
admin.site.register(Venue)
