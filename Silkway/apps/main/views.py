from django.shortcuts import render
from django.views.generic import ListView
from apps.hotels.models import Country
from apps.Tours.models import Tour
from apps.blog.models import Blog
from django.db.models import Q
from apps.hotels.models import Country, Region, Hotel
from apps.partners.models import Partner
from apps.discount.models import Discount

class ContentMainView(ListView):
    model = Country
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["discounts"] = Discount.objects.all()[:3]
        context["tours"] = Tour.objects.all()[:3]
        context["partners"] = Partner.objects.all()
        # print(context)
        return context

    # def get_queryset(self):
    #     if self.request.GET.get("search"):
    #         query = self.request.GET.get("search")
    #         print(f"====================={query}-----------------------")
    #         object_list = Country.objects.filter(
    #             Q(title__icontains = query))
    #         return object_list
    #     return Country.objects.all()
    
class SearchList(ListView):
    template_name = "base copy.html"

    def get_queryset(self):
        query = self.request.GET.get("S")
        object_list = [
            Country.objects.filter(Q(title__icontains = query)),
            Region.objects.filter(Q(title__icontains = query)),
            Hotel.objects.filter(Q(title__icontains = query)),
            ]
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("S")
        context["countries"] = Country.objects.filter(Q(title__icontains = query)),
        context["regions"] = Region.objects.filter(Q(title__icontains = query)),
        context["hotels"] = Hotel.objects.filter(Q(title__icontains = query)),
        return context


    