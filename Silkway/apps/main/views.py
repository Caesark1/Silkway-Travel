from django.shortcuts import render
from django.views.generic import ListView
from apps.hotels.models import Country
from apps.Tours.models import Tour
from apps.blog.models import Blog
from django.db.models import Q


class ContentMainView(ListView):
    model = Country
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["countries"] = Country.objects.all()
        context["tours"] = Tour.objects.all()
        context["blogs"] = Blog.objects.all().order_by("-date")[:3]
        
        return context
        
    def get_queryset(self):
        if self.request.GET.get("search"):
            query = self.request.GET.get("search")
            print(f"====================={query}-----------------------")
            object_list = Country.objects.filter(
                Q(title__icontains = query))
            return object_list
        return Country.objects.all()
    