# Generated by Django 4.2.1 on 2023-06-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_shop_address_shop_contact_shop_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='shop',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
