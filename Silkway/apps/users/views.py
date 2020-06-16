from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth
from django.contrib import messages



def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')

    else:
        return render(request,'base.html') 

class FileListProfileView(LoginRequiredMixin,ListView):
	model = UserDocs
	template_name = 'user/user_profile.html'
	context_object_name = "files"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["user"] = self.request.user
		print(context)
		return context

	def get_queryset(self):
		self.profile = get_object_or_404(Profile, id = self.kwargs["id"])
		return UserDocs.objects.filter(profile = self.profile)


def logout(request):
	auth.logout(request)
	return redirect("/")
	