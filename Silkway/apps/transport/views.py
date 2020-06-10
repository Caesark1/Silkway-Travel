from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Transport

class Car_list(ListView):
    model = Transport
    template_name = "transport/car_list.html"
    context_object_name = "Cars"
    
    
class Car_detail(DetailView):
    queryset = Transport.objects.all()
    template_name = "transport/detail_car.html"    


