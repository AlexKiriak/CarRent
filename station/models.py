from django.db import models


class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    station_address = models.CharField(max_length=50, blank=True, null=True)
    station_type = models.CharField(max_length=50, blank=True, null=True)
