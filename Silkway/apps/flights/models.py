from django.db import models
from django.shortcuts import reverse


class Flights(models.Model):
    title = models.CharField(max_length = 250)
    text = models.TextField()
    img = models.ImageField(upload_to = "MediaFlights/")

    def __str__(self):
        return self.title
