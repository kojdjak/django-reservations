# django-reservations
Django app for managing reservations

#Installation

Activate your virtualenv and install django-reservations from sources.

```bash
pip install -e $PATH\django-reservations
```

#Usage

In your django application's settings.py add django-reservations in INSTALLED_APPS:
```python
INSTALLED_APPS = [
    'reservations.apps.ReservationsConfig',
    ...
]
```

Add urls in your django application's urls.py:
```python
urlpatterns = [
    url(r'^reservations/', include('reservations.urls')),
    url(r'^admin/', admin.site.urls),
]
```
