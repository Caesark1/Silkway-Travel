from django.urls import path
from .views import *


urlpatterns = [
    path("", PartnerListView.as_view(), name = "partners_list"),
]