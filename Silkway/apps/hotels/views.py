from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView, View
from .forms import HotelOrderForm

class CountryListView(ListView):
    model = Country
    template_name = "hotels/country_list.html"
    context_object_name = "countries"



class CountryDetailView(DetailView):
    queryset = Country.objects.all()
    template_name = "hotels/region_list.html"



class RegionDetailView(DetailView):
    model = Region
    template_name = "hotels/hotels_list.html"
    # context_object_name = "region"
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hotels"] = Hotel.objects.all()
        return context

    # def get_object(self, **kwargs):
    #     region_slug = self.kwargs["slug"]
    #     print(region_slug)
    #     return get_object_or_404(Region, slug = "hey")



class HotelDetailView(DetailView):
    queryset = Hotel.objects.all()
    template_name = "hotels/hotel_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = HotelOrderForm
        return context    

    # def get_object(self, **kwargs):
    #     hotel_slug = self.kwargs["slug"]
    #     print(hotel_slug)
    #     return get_object_or_404(Hotel, slug = "garden-hotel")

class HotelOrderView(View):
    def post(self, request, pk):
        form = HotelOrderForm(request.POST)
        print(form)
        hotel = Hotel.objects.get(id=pk)    
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"] 
            print(f'{first_name}------------------------------------------- {last_name}')
            form = form.save(commit=False)
            form.hotel = hotel
            form.save()
        return redirect(hotel.get_absolute_url())