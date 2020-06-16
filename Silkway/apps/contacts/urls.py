from django.urls import path
from .views import view_map

urlpatterns = [
    path('', view_map, name = "contact"),
]