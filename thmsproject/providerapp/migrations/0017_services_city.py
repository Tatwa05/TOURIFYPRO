# Generated by Django 4.2.6 on 2023-11-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providerapp', '0016_services_nameofhotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='City',
            field=models.CharField(default='Guntur', max_length=20),
            preserve_default=False,
        ),
    ]
