from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from restaurant.serializers import MenuItemSerializer,BookingSerializer
from rest_framework import status
from restaurant.models import MenuItem,Booking
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class MenuItemsViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(Title="MilkShake",Price=10,Inventory=20)
        MenuItem.objects.create(Title="IceCream",Price=80,Inventory=100)
        MenuItem.objects.create(Title="Soup",Price=50,Inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('restaurant:menu'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items,many=True)
        self.assertEqual(response.data,serializer.data)

class BookingViewSetTest(TestCase):
    def setUp(self):
        Booking.objects.create(Name="Booking 1",No_of_guests=10,BookingDate=timezone.make_aware(datetime(2023, 10, 26, 15, 30, 0)))
        Booking.objects.create(Name="Booking 2",No_of_guests=20,BookingDate=timezone.make_aware(datetime(2023, 10, 26, 16, 30, 0)))
        Booking.objects.create(Name="Booking 3",No_of_guests=30,BookingDate=timezone.make_aware(datetime(2023, 10, 26, 17, 30, 0)))

    def test_getall(self):
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        client = APIClient()
        client.force_authenticate(user=test_user)

        response = client.get(reverse('booking-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        booking_items = Booking.objects.all()
        serializer = BookingSerializer(booking_items,many=True)
        self.assertEqual(response.data,serializer.data)