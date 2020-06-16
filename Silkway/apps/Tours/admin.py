from django.contrib import admin
from .models import Tour, TourOrder
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class HotelAdminForm(forms.ModelForm):
    text = forms.CharField(label="Описание",widget=CKEditorUploadingWidget())
    class Meta:
        model = Tour
        fields = '__all__'

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("title",)
    form = HotelAdminForm


@admin.register(TourOrder)
class TourAddAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "tour", "id")
    readonly_fields = ("first_name", "last_name", "email", "phone_number", "tour")
    search_fields = ("tour","first_name", "last_name")
    list_filter = ("tour",)