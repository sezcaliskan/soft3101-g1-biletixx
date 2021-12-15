from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    eventtype = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


   


     






    




