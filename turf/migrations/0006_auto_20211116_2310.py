# Generated by Django 3.2.8 on 2021-11-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf', '0005_auto_20211012_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfbooked',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turfbooked',
            name='payment_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
