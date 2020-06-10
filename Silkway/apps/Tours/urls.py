from django.urls import path

from .views import *

urlpatterns = [
    path('', TourList.as_view(), name="tour_list"),
    path('<str:slug>/', TourDetail.as_view(), name = "tour_detail"),
    path('apply/<int:pk>/', TourApply.as_view(), name = "apply"),
]