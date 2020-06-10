from django.urls import path
from .views import FlightsView


urlpatterns = [
    path('',  FlightsView.as_view(), name = "flights_list"),
]
