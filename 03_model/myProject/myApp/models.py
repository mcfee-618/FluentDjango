from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400, null=False)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
