from django.db import models

# Create your models here.
class Games(models.Model):

    gname=models.CharField(max_length=30)
    gsize=models.IntegerField()
    gtype=models.CharField(max_length=30)
    gstyle=models.CharField(max_length=10)
    gos=models.CharField(max_length=30)
