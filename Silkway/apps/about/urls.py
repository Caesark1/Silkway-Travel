from django.urls import path
from .views import *

urlpatterns = [
    path("", DirectorListView.as_view(), name="about"),
]