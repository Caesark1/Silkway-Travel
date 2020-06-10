from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Transport(models.Model):
    title = models.CharField(max_length = 100)
    about = models.TextField()
    img = models.ImageField(upload_to="MediaCar/")
    slug = models.SlugField(max_length = 100,blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"slug":self.slug})


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
    if not instance.slug or instance.title != Transport.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=Transport)