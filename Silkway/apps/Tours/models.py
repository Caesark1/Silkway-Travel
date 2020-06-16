from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from apps.discount.models import Discount


class Tour(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Название")
    text = models.TextField(verbose_name = "Описание")
    img = models.ImageField(upload_to = "MediaTours/", verbose_name = "Фотография")
    slug = models.SlugField(max_length = 100, blank = True)
    discount = models.ForeignKey(Discount, on_delete = models.CASCADE, related_name="tour_discount", verbose_name = "Скидки", blank = True,null=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("tour_detail", kwargs={"slug":self.slug})



class TourOrder(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=35)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}---{self.tour}'



def unique_slug_generator(instance):
    constant_slug = slugify(instance.title, allow_unicode=True)
    slug = constant_slug
    num = 0
    Klass = instance.__class__
    while Klass.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug

def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title != Tour.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=Tour)