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

    def test_field_reserve(self):
        url_reserve_5 = reverse('reservations:field.reserve', kwargs={'field_id': 1, 'reservation_time': 5,})
        url_reserve_6 = reverse('reservations:field.reserve', kwargs={'field_id': 1, 'reservation_time': 6,})
        #get field detail. both links should be present
        response = self.client.get(reverse('reservations:field.detail', kwargs={'field_id':1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, url_reserve_5)
        self.assertContains(response, url_reserve_6)
        #reserve hour 5, links to 5 should not be present anymore in response
        response = self.client.get(reverse('reservations:field.reserve', kwargs={'field_id': 1, 'reservation_time': 5,}))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('reservations:field.detail', kwargs={'field_id':1}))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, url_reserve_5)
        self.assertContains(response, url_reserve_6)
