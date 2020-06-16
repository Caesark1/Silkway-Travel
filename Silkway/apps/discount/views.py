from django.shortcuts import render
from .models import Discount
from django.views.generic import ListView
from apps.hotels.models import Hotel
from apps.Tours.models import Tour

class DiscountListView(ListView):
    model = Discount
    template_name = "discount_list.html"
    paginate_by = 6
    context_object_name = "discounts"
    

