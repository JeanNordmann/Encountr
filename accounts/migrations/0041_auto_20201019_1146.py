# Generated by Django 3.1.1 on 2020-10-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_customuser_is_first_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_first_job',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]