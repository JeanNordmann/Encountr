# Generated by Django 3.1.1 on 2020-10-13 06:51

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20201012_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=mapbox_location_field.models.LocationField(default='Lyon, France', map_attrs={}),
        ),
    ]