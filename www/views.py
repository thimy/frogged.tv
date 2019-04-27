from django.shortcuts import render
from django.utils import timezone
from .models import Post


def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )[:5]
    return render(request, "posts/home.html", {"posts": posts})


def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "posts/posts.html", {"posts": posts})
