# Generated by Django 4.2.3 on 2023-07-15 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_booking_bookingdate_alter_booking_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='bookingDate',
        ),
    ]
