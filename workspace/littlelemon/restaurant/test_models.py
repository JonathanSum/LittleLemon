from django.test import TestCase
from .models import MenuItem
from django.db import models
import datetime

class MenuItemTest(TestCase):
    def test_get_item(self):
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        d = datetime.date(1997, 10, 19)

        item = MenuItem.objects.create(title="IceCream", bookingDate = d, price=80, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")
    # title = models.CharField(max_length=255, db_index=True)
    # bookingDate =  models.DateField(db_index=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    # inventory = models.SmallIntegerField()