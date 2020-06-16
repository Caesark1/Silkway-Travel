from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse
from apps.discount.models import Discount


class Country(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Название")
    img = models.ImageField(upload_to="CountryMedia/", verbose_name = "Фотография")
    slug = models.SlugField(max_length = 100, blank = True)


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("region_list", kwargs={"slug":self.slug})

    

class Region(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Название")
    img = models.ImageField(upload_to="RegionMedia/", verbose_name = "Фотография")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="regions", verbose_name = "Страна")
    slug = models.SlugField(max_length = 100, blank = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("hotel_list", kwargs={"slug":self.slug})
    
class Hotel(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Название")
    text = models.TextField(verbose_name = "Описание")
    img = models.ImageField(upload_to="HotelMedia/", verbose_name = "Фотография")
    slug = models.SlugField(max_length = 100, blank = True)
    stars = models.SmallIntegerField(default = 0, verbose_name = "Звезды")
    discount = models.ForeignKey(Discount, related_name="hotel_discount", on_delete = models.CASCADE, blank=True, null=True, verbose_name = "Скидки")
    region = models.ForeignKey(Region, on_delete = models.CASCADE, related_name = "hotels", verbose_name = "Регион или Город")

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("hotel_detail", kwargs={"slug":self.slug})

class HotelService(models.Model):
    service = models.CharField(max_length = 100, blank=True, verbose_name = "Услуги отеля")
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, related_name = "hotelservices")

class HotelRoom(models.Model):
    type_of_room = models.CharField(max_length = 100, blank=True, verbose_name = "Тип комнат")
    description = models.TextField(max_length=100, blank = True, verbose_name = "Описание комнат")
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, related_name = "hotelrooms")


class HotelShot(models.Model):
    headers = models.CharField(max_length = 100)
    description = models.TextField()
    img = models.ImageField(upload_to = "HotelShotsMedia/")
    hotel = models.ForeignKey(Hotel, verbose_name = "Фотографии Отеля", on_delete= models.CASCADE, related_name="hotel_shots")


    def __str__(self):
        return self.headers
        
    


class HotelOrder(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}---{self.hotel}'



# class ProjectaAnalytics(models.Model):
#     class Meta:
#         db_table = "ProjectaAnalytics"

#     # внешний ключ на статью
#     project = models.ForeignKey(Project, on_delete = models.CASCADE ) 

#     # количество просмотров в эту дату
#     views = models.IntegerField('Просмотры', default=0) 

#     def str(self):
#         return self.project.project_name
# obj, created = ProjectaAnalytics.objects.get_or_create(
#         defaults={
#             "project": projects[0],
#         }, 
#             project = projects[0],
#         )
#     obj.views += 1  # Увелечение счётчика при каждом посещении 
#     obj.save(update_fields=['views']) #Обнавление поля просмотров

#     views = ProjectaAnalytics.objects.filter(project = projects[0]) #Вывод Кол-во просмотров проекта








# utils
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
    if not instance.slug or instance.title != Country.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=Country)



def unique_slug_generator_region(instance):
    constant_slug = slugify(instance.title, allow_unicode=True)
    slug = constant_slug
    num = 0
    Klass = instance.__class__
    while Klass.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug

def pre_save_reciever_region(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title != Region.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator_region(instance)

pre_save.connect(pre_save_reciever_region, sender=Region)



def unique_slug_generator_hotel(instance):
    constant_slug = slugify(instance.title, allow_unicode=True)
    slug = constant_slug
    num = 0
    Klass = instance.__class__
    while Klass.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug

def pre_save_reciever_hotel(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title != Hotel.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator_hotel(instance)

pre_save.connect(pre_save_reciever_hotel, sender=Hotel)