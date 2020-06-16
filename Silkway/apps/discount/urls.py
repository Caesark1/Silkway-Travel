from django.urls import path
from .views import DiscountListView

urlpatterns = [
    path("", DiscountListView.as_view(), name = "discount"),
]