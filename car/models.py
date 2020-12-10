from django.db import models

class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_name = models.CharField(max_length=50, blank=True, null=True)
    car_number = models.IntegerField(blank=True, null=True)
    car_trans = models.CharField(max_length=50, blank=True, null=True)
    car_price = models.IntegerField(blank=True, null=True)
    car_year = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey('Ordr', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Usr', models.DO_NOTHING, blank=True, null=True)
    park = models.ForeignKey('Park', models.DO_NOTHING, blank=True, null=True)
    station = models.ForeignKey('Station', models.DO_NOTHING, blank=True, null=True)
    car_img = models.TextField(blank=True, null=True)
    car_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class Park(models.Model):
    park_id = models.IntegerField(primary_key=True)
    park_block = models.CharField(max_length=50, blank=True, null=True)
    park_address = models.CharField(max_length=50, blank=True, null=True)


class Ordr(models.Model):
    order_id = models.IntegerField(primary_key=True)


class Usr(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_contact = models.TextField(blank=True, null=True)


class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    station_address = models.CharField(max_length=50, blank=True, null=True)
    station_type = models.CharField(max_length=50, blank=True, null=True)

