from django.db import models


# Create your models here.
class Org(models.Model):
    class Meta:
        db_table = 'table1'

    id = models.IntegerField(primary_key=True, db_column='id')
    title = models.CharField(max_length=100, verbose_name='Source Title', db_column='Source Title')
