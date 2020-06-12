from django.urls import path
from .views import ContentMainView

urlpatterns = [
    path('', ContentMainView.as_view(), name = 'index')
]