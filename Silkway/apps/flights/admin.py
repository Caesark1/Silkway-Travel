from django.contrib import admin
from .models import Flights

@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ("title",)