from django.contrib import admin
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class HotelAdminForm(forms.ModelForm):
    text = forms.CharField(label="Описание",widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = '__all__'

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ("title", "date")
    form = HotelAdminForm