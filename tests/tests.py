from django.test import TestCase
from django.core.urlresolvers import reverse
from reservations.models import Venue, Field, Reservation


class IndexViewTests(TestCase):
    def test_index_view_basic(self):
        """
        Basic test index view.
        """
        response = self.client.get(reverse('reservations:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Reservations")


class FieldViewTests(TestCase):
    def setUp(self):
        venue01 = Venue.objects.create(name="VenueFieldTest01")
        Field.objects.create(name="FieldReservationdTest01", venue=venue01)

    def test_field_detail(self):
        response = self.client.get(reverse('reservations:field.detail', kwargs={'field_id':1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Reservations")
