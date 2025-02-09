from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=300, default= None)
    year = models.IntegerField(default= 1900)
    cert = models.CharField(max_length=10,  default= None)
    runtime = models.IntegerField(default= 0)
    genre = models.CharField(max_length=300,  default= None)
    imdb = models.FloatField(default= 0.0)
    overview = models.CharField(max_length=1000, default= None)
    meta = models.IntegerField()
    director = models.CharField(max_length=100,  default= None)
    stara = models.CharField(max_length=300,  default= None)
    starb = models.CharField(max_length=300,  default= None)
    starc = models.CharField(max_length=300,  default= None)
    stard = models.CharField(max_length=300, default= None)
    votes = models.IntegerField(default= 0)
    gross = models.IntegerField(default= 0)
    match = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.pk)