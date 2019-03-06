from django.db import models

# Create your models here.
class Movie(models.Model):
    redate=models.DateField()
    moviename=models.CharField(max_length=64)
    hero=models.CharField(max_length=64)
    heroine=models.CharField(max_length=64)
    rating=models.IntegerField()


