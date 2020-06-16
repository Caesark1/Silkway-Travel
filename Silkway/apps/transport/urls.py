from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Car_list.as_view(), name="car_list"),
]