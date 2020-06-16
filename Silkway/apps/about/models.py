from django.db import models

class Director(models.Model):
    name = models.CharField(max_length = 100)
    post = models.CharField(max_length = 100)
    qoute = models.CharField(max_length = 100)
    img = models.ImageField(upload_to="EmployersMedia/")

    def __str__(self):
        return self.name
        

class Employer(models.Model):
    name = models.CharField(max_length = 100)
    post = models.CharField(max_length = 100)
    qoute = models.CharField(max_length = 100)
    img = models.ImageField(upload_to="EmployersMedia/")

    def __str__(self):
        return self.name
