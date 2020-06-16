from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, View
from .forms import HotelOrderForm
from django.db.models import Q
from .tasks import send_userdata


class CountryListView(ListView):
    model = Country
    template_name = "hotels/country_list copy.html"
    context_object_name = "countries"
    paginate_by = 6

    # def get_queryset(self):
    #     if self.request.GET.get("search"):
    #         query = self.request.GET.get("search")
    #         print(f"====================={query}-----------------------")
    #         object_list = Country.objects.filter(
    #             Q(title__icontains = query) |
    #             Q(regions__title__icontains = query))
    #         print(object_list)
    #         return object_list
    #     return Country.objects.all()




class RegionListView(ListView):
    model = Region
    template_name = "hotels/region_list copy.html"
    context_object_name = "regions"
    paginate_by = 6
    
   


    def get_queryset(self):
        self.country = get_object_or_404(Country, slug = self.kwargs["slug"])
        return Region.objects.filter(country=self.country)



        


# class PostDetailView(DetailView):

#     model = Post

#     context_object_name = 'news'

#     template_name = 'blog/post_detail.html'

#     def get_queryset(self):

#         category = self.kwargs.get('category_slug', '')

#         q = super().get_queryset()

#         return q.filter(category__slug=category).select_related('category')

#     def get_context_data(self, *, object_list=None, kwargs):

#         context = super().get_context_data(kwargs)

#         self.object.views = F('views') + 1

#         self.object.save()

#         self.object.refresh_from_db()

#         return context


class HotelListView(ListView):
    queryset = Hotel.objects.all().order_by("stars")
    template_name = "hotels/hotels_list copy.html"
    paginate_by = 6 
    context_object_name = "hotels"
    

    def get_queryset(self):
        self.regions = get_object_or_404(Region, slug=self.kwargs["slug"])
        return Hotel.objects.filter(region=self.regions)
    




class HotelDetailView(DetailView):
    queryset = Hotel.objects.all()
    template_name = "hotels/hotel_detail copy.html"

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
        hotel = Hotel.objects.get(id=pk)    
        if form.is_valid():
            user_data = {}
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            check_in = form.cleaned_data["check_in"]
            check_out = form.cleaned_data["check_out"] 
            form = form.save(commit=False)
            user_data["first_name"] = first_name
            user_data["last_name"] = last_name
            user_data["email"] = email
            user_data["phone_number"] = phone_number
            user_data["check_in"] = check_in
            user_data["check_out"] = check_out
            send_userdata.delay(user_data)
            form.hotel = hotel
            form.save()
        return redirect(hotel.get_absolute_url())


