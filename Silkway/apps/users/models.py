from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.shortcuts import reverse
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)


    def __str__(self):
        return f"Profile for user {self.user.first_name}"


class UserDocs(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, null=True, related_name = "profile")
    user_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, verbose_name = "Описание(не обязательно)")
    file = models.FileField(verbose_name = "Документ", null=True, upload_to = "FileMedia/")

    def __str__(self):
        return self.user_name


def post_save_reciever(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

post_save.connect(post_save_reciever, sender = User)

