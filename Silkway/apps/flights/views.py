from django.shortcuts import render

from .models import Flights
from django.views.generic import ListView

class FlightsView(ListView):
    model = Flights
    template_name = "flights/list_flights.html"
    context_object_name = "flights"