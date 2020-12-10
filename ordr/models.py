from django.db import models


class Ordr(models.Model):
    order_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ordr'

