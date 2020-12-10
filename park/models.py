from django.db import models


class Park(models.Model):
    park_id = models.IntegerField(primary_key=True)
    park_block = models.CharField(max_length=50, blank=True, null=True)
    park_address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'park'

