from django.contrib import admin
from .models import Tour, TourOrder

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(TourOrder)
class TourAddAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "tour", "id")
    readonly_fields = ("first_name", "last_name", "email", "phone_number", "tour")
    search_fields = ("tour","first_name", "last_name")
    list_filter = ("tour",)