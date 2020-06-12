from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, CreateView
from .models import Tour
from .forms import TourOrderForm

class TourList(ListView):
    model = Tour
    template_name = "tours/tours_list.html"
    context_object_name = "tours"
    paginate_by = 1

class TourDetail(DetailView):
    template_name = "tours/tour_detail.html"
    queryset = Tour.objects.all()
    form_class = TourOrderForm

    def get_context_data(self, **kwargs):
        context = super(TourDetail, self).get_context_data(**kwargs)
        context['form'] = TourOrderForm()
        return context


class TourApply(View):
    def post(self, request, pk):
        print(request)
        form = TourOrderForm(request.POST)
        print(form)
        tour = Tour.objects.get(id=pk)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"] 
            form = form.save(commit=False)
            form.tour = tour
            form.save()
        return redirect(tour.get_absolute_url())