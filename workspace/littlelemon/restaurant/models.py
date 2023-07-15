from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.SmallIntegerField()
    bookingDate =  models.DateField(db_index=True)

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    bookingDate =  models.DateField(db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    def get_item(self):
        return self.__str__()
