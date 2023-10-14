from django.test import TestCase
from restaurant.models import MenuItem,Booking
from django.utils import timezone
from datetime import datetime

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title="IceCream",Price=80,Inventory=100)
        self.assertEqual(str(item),"IceCream : 80")

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(Name="Booking 1",No_of_guests=10,BookingDate=timezone.make_aware(datetime(2023, 10, 26, 15, 30, 0)))
        self.assertEqual(str(item),f"Booking 1 : 10 : {timezone.make_aware(datetime(2023, 10, 26, 15, 30, 0))}")