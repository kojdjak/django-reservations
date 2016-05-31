##########
django-reservations
##########

.. image:: https://travis-ci.org/kojdjak/django-reservations.svg?branch=master
    :target: http://travis-ci.org/kojdjak/django-reservations

Django app for managing reservations

##########
Prerequisites
##########

 - Python 3.x
 - Django is the only prerequisite at this moment. It's being tested with latest trunk version.

##########
Installation
##########

Activate your virtualenv and install django-reservations from sources. ::

    pip install -e $PATH\django-reservations

##########
Usage
##########

In your django application's settings.py add django-reservations in INSTALLED_APPS. ::

    INSTALLED_APPS = [
        'reservations.apps.ReservationsConfig',
        ...
    ]

Add urls in your django application's urls.py. ::

    urlpatterns = [
        url(r'^reservations/', include('reservations.urls')),
        url(r'^admin/', admin.site.urls),
    ]


#Tests

Simply run: ::

python runtests.py

