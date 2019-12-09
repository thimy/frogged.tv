from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("users", views.users, name="users"),
    path("users/edit/<int:pk>/", views.user_edit, name="user_edit"),
]
