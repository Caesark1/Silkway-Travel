from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "id")

@admin.register(UserDocs)
class DocsAdmin(admin.ModelAdmin):
	list_display = ("user_name", "id")




# {% url 'logout' %}
