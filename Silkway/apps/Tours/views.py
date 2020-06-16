from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, View
from .forms import TourOrderForm
from django.db.models import Q


class TourList(ListView):
    model = Tour
    template_name = "tours/tours_list copy.html"
    context_object_name = "tours"
    paginate_by = 6

    def get_queryset(self):
        if self.request.GET.get("search"):
            query = self.request.GET.get("search")
            print(f"====================={query}-----------------------")
            object_list = Tour.objects.filter(
                Q(title__icontains = query))
            print(object_list)
            return object_list
        return Tour.objects.all()




class TourDetail(DetailView):
    queryset = Tour.objects.all()
    template_name = "tours/tour_detail copy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TourOrderForm
        return context    

    # def get_object(self, **kwargs):
    #     hotel_slug = self.kwargs["slug"]
    #     print(hotel_slug)
    #     return get_object_or_404(Hotel, slug = "garden-hotel")

class TourOrderView(View):
    def post(self, request, pk):
        form = TourOrderForm(request.POST)
        print(form)
        tour = Tour.objects.get(id=pk)    
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"] 
            print(f'{first_name}------------------------------------------- {last_name}')
            form = form.save(commit=False)
            form.tour = tour
            form.save()
        return redirect(tour.get_absolute_url())