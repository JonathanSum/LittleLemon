# Generated by Django 4.2.3 on 2023-07-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('bookingDate', models.DateField(db_index=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('inventory', models.SmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='BookingDate',
            new_name='bookingDate',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='No_of_guests',
            new_name='no_of_guests',
        ),
    ]