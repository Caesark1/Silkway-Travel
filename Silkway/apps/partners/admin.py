from django.contrib import admin
from .models import Partner
from django.utils.safestring import mark_safe


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image")

    def get_image(self,obj):
        return mark_safe(f'<img src = {obj.img.url} width = "50" heigth = "60"')

    get_image.short_description = "Изображение"