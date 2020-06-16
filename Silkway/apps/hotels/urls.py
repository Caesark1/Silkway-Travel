from django.urls import path
from .views import *

urlpatterns = [
    path('', CountryListView.as_view(), name="country_list"),
    path('<str:slug>/', RegionListView.as_view(), name = "region_list"),
    path('regions/<str:slug>/', HotelListView.as_view(), name = "hotel_list"),
    path('regions/hotels/<str:slug>', HotelDetailView.as_view(), name = "hotel_detail" ),
    path('apply/<int:pk>/', HotelOrderView.as_view(), name = "hotelorder"),
]       
