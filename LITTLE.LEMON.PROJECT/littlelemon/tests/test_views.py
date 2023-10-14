from django.test import TestCase
from django.urls import reverse
from restaurant.serializers import MenuItemSerializer
from rest_framework import status
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
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