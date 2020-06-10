from django.urls import path
from .views import BlogView, BlogDetail


urlpatterns = [
    path('', BlogView.as_view(), name = "blog_view"),
    path('<str:slug>/', BlogDetail.as_view(), name = "blog_detail"),
]

