from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone
from django.test import TestCase
from checkout.models import Order, OrderLineItem


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test123')
        test_order_main = Order.objects.create(full_name='test user', purchaser=cls.user, phone_number='01111222333',
                                               country='Mars', town_or_city='The Pits', street_address1='1 Legend St',
                                               county='Legendville', date=timezone.now())

    def test_create_order_and_date_today(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.date, date.today())
