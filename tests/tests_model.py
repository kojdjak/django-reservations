from django.test import TestCase
from reservations.models import Venue, Field, Reservation
from django.contrib.auth.models import User


class VenueModelTest(TestCase):
    def setUp(self):
        pass

    def test_create_basic(self):
        print("Running VenueModelTest.test_create_basic")
        Venue.objects.create(name="Venue01")
        venue = Venue.objects.get(name="Venue01")
        self.assertEqual(venue.name, "Venue01")


class FieldModelTest(TestCase):
    def setUp(self):
        Venue.objects.create(name="VenueFieldTest01")
        pass

    def test_create_basic(self):
        print("Running FieldModelTest.test_create_basic")
        venue01 = Venue.objects.get(name="VenueFieldTest01")
        Field.objects.create(name="Field01", venue=venue01)
        field = Field.objects.get(name="Field01")
        self.assertEqual(field.name, "Field01")


class ReservationModelTest(TestCase):
    def setUp(self):
        venue01 = Venue.objects.create(name="VenueFieldTest01")
        Field.objects.create(name="FieldReservationdTest01", venue=venue01)
        User.objects.create_user(username="user01", email="email01", password="pass01")
        pass

    def test_create_basic(self):
        print("Running ReservationModelTest.test_create_basic")
        field01 = Field.objects.get(name="FieldReservationdTest01")
        user01 = User.objects.get(username="user01")
        Reservation.objects.create(name="Reservation01", field=field01, user=user01)
        reservation = Reservation.objects.get(name="Reservation01")
        self.assertEqual(reservation.name, "Reservation01")

    def test_create_anonymous(self):
        print("Running ReservationModelTest.test_create_basic")
        field01 = Field.objects.get(name="FieldReservationdTest01")
        user01 = None
        Reservation.objects.create(name="ReservationAnonymous", field=field01, user=user01)
        reservation = Reservation.objects.get(name="ReservationAnonymous")
        self.assertEqual(reservation.name, "ReservationAnonymous")
