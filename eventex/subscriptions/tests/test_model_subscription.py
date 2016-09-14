from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelsTest(TestCase):
    def setUp(self):

        self.obj = Subscription(
            name='Murilo Sandiego',
            cpf='1234568901',
            email='murilosandiego1@gmail.com',
            phone='991712891',
        )

        self.obj.save()

    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Murilo Sandiego', str(self.obj))