# Generated by Django 3.2.8 on 2021-10-11 19:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=20), size=7)),
            ],
        ),
    ]