from django.db import models



class Discount(models.Model):
    discount_title = models.CharField(max_length = 100, verbose_name = "Наименование Акции")


    def __str__(self):
        return self.discount_title

    