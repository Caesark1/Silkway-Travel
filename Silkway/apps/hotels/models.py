from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse


class Country(models.Model):
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to="CountryMedia/")
    slug = models.SlugField(max_length = 100, blank = True)


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("region_list", kwargs={"slug":self.slug})

    

class Region(models.Model):
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to="RegionMedia/")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="regions")
    slug = models.SlugField(max_length = 100, blank = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("hotel_list", kwargs={"slug":self.slug})
    
class Hotel(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    img = models.ImageField(upload_to="HotelMedia/")
    slug = models.SlugField(max_length = 100, blank = True)
    stars = models.SmallIntegerField(default = 0)
    region = models.ForeignKey(Region, on_delete = models.CASCADE, related_name = "hotels")

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("hotel_detail", kwargs={"slug":self.slug})

class HotelOrder(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField(default=0)
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
# def unique_slug_generator(instance):
#     constant_slug = slugify(instance.title, allow_unicode=True)
#     slug = constant_slug
#     num = 0
#     Klass = instance.__class__
#     while Klass.objects.filter(slug=slug).exists():
#         num += 1
#         slug = "{slug}-{num}".format(slug=constant_slug, num=num)
#     return slug

# def pre_save_reciever(sender, instance, *args, **kwargs):
#     if not instance.slug or instance.title != Region.objects.filter(slug=instance.slug):
#         instance.slug = unique_slug_generator(instance)

# pre_save.connect(pre_save_reciever, sender=Region)
