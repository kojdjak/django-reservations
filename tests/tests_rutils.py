from django.test import TestCase
from reservations.models import Venue, Field, Reservation
from django.contrib.auth.models import User
from reservations import rutils


class CreateReservationTest(TestCase):
    def setUp(self):
        venue01 = Venue.objects.create(name="VenueFieldTest01")
        Field.objects.create(name="FieldReservationdTest01", venue=venue01)
        User.objects.create_user(username="user01", email="email01", password="pass01")
        pass

    def test_create_basic(self):
        field01 = Field.objects.get(name="FieldReservationdTest01")
        user01 = User.objects.get(username="user01")
        rutils.create_reservation(field_id=field01.id, res_date="2016-06-21", reservation_time=1, user=user01)
        reservation = Reservation.objects.get(id=1)
        self.assertIsNotNone(reservation.user)

class GetReservationsTest(TestCase):
    def setUp(self):
        venue01 = Venue.objects.create(name="VenueFieldTest01")
        field1 = Field.objects.create(name="FieldReservationdTest01", venue=venue01)
        field2 = Field.objects.create(name="FieldReservationdTest02", venue=venue01)
        user = User.objects.create_user(username="user01", email="email01", password="pass01")
        rutils.create_reservation(field_id=field1.id, res_date="2016-06-21", reservation_time=1, user=user)
        pass

    def test_g_basic(self):
        field1 = Field.objects.get(name="FieldReservationdTest01")
        reservations_field1 = rutils.get_reservations(field_id=field1.id, res_date="2016-06-21")
        self.assertEqual(len(reservations_field1), 1)
        field2 = Field.objects.get(name="FieldReservationdTest02")
        reservations_field1 = rutils.get_reservations(field_id=field2.id, res_date="2016-06-21")
        self.assertEqual(len(reservations_field1), 0)
