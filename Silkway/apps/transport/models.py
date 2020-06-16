from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Transport(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Тип авто")
    price = models.CharField(max_length=100, verbose_name = "Средняя цена")
    about = models.TextField(verbose_name = "Краткое описание")
    img = models.ImageField(upload_to="MediaCar/",verbose_name = "Фотография")

    def __str__(self):
        return self.title



