from django.urls import path
from django.conf.urls import url
from . import views
from .views import markdown_uploader


urlpatterns = [
    path("", views.home, name="home"),
    path("posts", views.posts, name="posts"),
    url(r"^api/uploader/$", markdown_uploader, name="markdown_uploader_page"),
]
