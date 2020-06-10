from django.urls import path
from .views import *

urlpatterns = [
    path('', CountryListView.as_view(), name="country_list"),
    path('<str:slug>/', CountryDetailView.as_view(), name = "country_detail"),
    path('regions/<str:slug>/', RegionDetailView.as_view(), name = "region_detail"),
    path('regions/hotels/<str:slug>', HotelDetailView.as_view(), name = "hotel_detail" ),
    path('apply/<int:pk>/', HotelOrderView.as_view(), name = "hotelorder"),
]