# Generated by Django 4.2.1 on 2023-06-09 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shops', '0003_alter_shop_latitude_alter_shop_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]