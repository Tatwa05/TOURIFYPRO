# Generated by Django 4.2.6 on 2023-11-03 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providerapp', '0007_hotel_hotel_ref_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='hotelRefId',
            field=models.CharField(default='REF123', max_length=20),
            preserve_default=False,
        ),
    ]
