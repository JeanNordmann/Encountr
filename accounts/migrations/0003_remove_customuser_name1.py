# Generated by Django 3.1.3 on 2020-11-19 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_name1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name1',
        ),
    ]