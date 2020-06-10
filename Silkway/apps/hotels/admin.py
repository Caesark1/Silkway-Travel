from django.contrib import admin
from .models import Country, Region, Hotel, HotelOrder

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("title", "country")


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("title", "region")


@admin.register(HotelOrder)
class HotelOrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "hotel", "id")
    readonly_fields = ("first_name", "last_name", "email", "phone_number", "hotel")
    search_fields = ("hotel","first_name", "last_name")
    list_filter = ("hotel",)