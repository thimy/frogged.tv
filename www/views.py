from django.shortcuts import render


def home(request):
    return render(request, "posts/home.html", {})


def posts(request):
    return render(request, "posts/posts.html", {})
