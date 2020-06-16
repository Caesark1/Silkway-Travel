from django.contrib import admin
from .models import Country, Region, Hotel, HotelOrder, HotelShot, HotelService, HotelRoom
from django.utils.safestring import mark_safe




@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("title", "country")


class HotelServices(admin.TabularInline):
    model = HotelService
    
class HotelRooms(admin.TabularInline):
    model = HotelRoom

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelServices, HotelRooms]
    list_display = ("title", "region")

    class Meta:
        model = Hotel

@admin.register(HotelOrder)
class HotelOrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "hotel", "id")
    readonly_fields = ("first_name", "last_name", "email", "phone_number", "hotel", "check_in", "check_out")
    search_fields = ("hotel","first_name", "last_name")
    list_filter = ("hotel",)


@admin.register(HotelShot)
class HotelShotsAdmin(admin.ModelAdmin):
    list_display = ("headers", "hotel", "get_image")

    def get_image(self,obj):
        return mark_safe(f'<img src = {obj.img.url} width = "50" heigth = "60"')

    get_image.short_description = "Изображение"