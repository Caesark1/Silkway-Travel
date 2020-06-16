from django.contrib import admin
from .models import Employer, Director

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ("name",)
