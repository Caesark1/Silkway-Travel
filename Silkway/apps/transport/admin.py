from django.contrib import admin
from .models import Transport

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ("title", "about")
