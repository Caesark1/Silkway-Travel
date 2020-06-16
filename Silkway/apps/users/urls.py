from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login/", login, name = "login"),
    path("profile/<int:id>/", FileListProfileView.as_view(), name = "user_profile"),
    path("logout/", logout, name = "logout"),
]