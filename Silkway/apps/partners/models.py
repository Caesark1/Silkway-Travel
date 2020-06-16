from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Наименование компании партнера")
    img = models.ImageField(upload_to="PartnersMedia", verbose_name = "Логотип компании")

    def __str__(self):
        return self.name
        
    