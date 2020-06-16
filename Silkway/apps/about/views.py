from django.shortcuts import render
from django.views.generic import ListView
from .models import Employer, Director

class DirectorListView(ListView):
    model = Director
    template_name = "about/about.html"
    context_object_name = "directors"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["employers"] = Employer.objects.all()
        return context
        

    
    
