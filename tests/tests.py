from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexViewTests(TestCase):
    def test_index_view_basic(self):
        """
        Basic test index view.
        """
        response = self.client.get(reverse('reservations:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Reservations")
