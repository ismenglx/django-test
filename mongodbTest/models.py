from django.db import models


# Create your models here.

class Authors(models.Model):
    class Meta:
        app_label = 'mongodbTest'
        db_table = 'a_authors'

    _id = models.CharField(db_column='_id', max_length=30, primary_key=True)
    # id = models.CharField(db_column='id', max_length=30, primary_key=False)
    name = models.CharField(db_column='name', max_length=30)
    h_index = models.IntegerField(db_column='h_index')
