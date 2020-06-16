from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Transport

class Car_list(ListView):
    model = Transport
    template_name = "transport/cars_list.html"
    context_object_name = "cars"
    
   


