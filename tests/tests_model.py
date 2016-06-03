from django.test import TestCase
from reservations.models import Venue, Field, Reservation


class VenueModelTest(TestCase):
    def setUp(self):
        pass

    def test_create_basic(self):
        print("Running VenueModelTest.test_create_basic")
        Venue.objects.create(name="Venue01")
        venue = Venue.objects.get(name="Venue01")
        self.assertEqual(venue.name, "Venue01")