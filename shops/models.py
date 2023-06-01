from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    address = models.CharField(max_length=200, default='')
    contact = models.CharField(max_length=20, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
