# Generated by Django 3.1.1 on 2020-10-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_auto_20201017_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_first_job',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]