from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView, DetailView

class BlogView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"


class BlogDetail(DetailView):
    template_name = "blog/blog_detail.html"
    queryset = Blog.objects.all()