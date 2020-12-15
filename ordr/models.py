from django.db import models


class Ordr(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_username = models.TextField(blank=True, null=True)
    order_usercontacts = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordr'
