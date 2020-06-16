from django.shortcuts import render
from .models import Partner
from django.views.generic import ListView

class PartnerListView(ListView):
    model = Partner
    template_name = "partners/partners_list.html"
    context_object_name = "partners"
    

