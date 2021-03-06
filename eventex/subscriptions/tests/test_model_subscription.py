from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Andre Marcos Gelhen',
            cpf = '12345678901',
            email = 'gelhen@gmail.com',
            phone = '49-123456789'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)


    def test_str(self):
        self.assertEqual('Andre Marcos Gelhen', str(self.obj))


    def test_paid_default_to_false(self):
        """By default paid must be False"""
        self.assertEqual(False, self.obj.paid)