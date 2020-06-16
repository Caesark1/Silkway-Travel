from django.urls import path
from .views import ContentMainView, SearchList

urlpatterns = [
    path('', ContentMainView.as_view(), name = 'index'),
    path('search/', SearchList.as_view(), name = "search"),
]