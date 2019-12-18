from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required

from www.models import Post, Category, User
from .forms import PostForm, UserForm

from django.db import IntegrityError


@login_required
def dashboard(request):
    return render(request, "pages/index.html")


@login_required
def posts(request):
    messages = get_messages(request)
    posts = reversed(Post.objects.all())
    return render(request, "posts/index.html", {"posts": posts, "messages": messages})


@login_required
def post_new(request):
    user = request.user
    messages = get_messages(request)
    form = PostForm(request.POST or None, request.FILES)

    if request.method == "GET":
        return render(request, "posts/new.html", {"form": form, "messages": messages})
    else:
        if form.is_valid():
            form.author = user
            form.save()
            messages.success(request, "L’article a été créé avec succès !")
            return redirect("posts_index")
        else:
            return render(request, "posts/new.html", {"form": form})
    return render(request, "posts/new.html", {"form": form, "messages": messages})


@login_required
def post_edit(request, pk):
    messages = get_messages(request)
    post = Post.objects.get(pk=pk)
    print(post)
    form = PostForm(request.POST or None, request.FILES, instance=post)

    if request.method == "GET":
        return render(request, "posts/edit.html", {"form": form, "messages": messages})
    else:
        if form.is_valid():
            form.save()
            return redirect("posts_index")
        else:
            return render(request, "posts/edit.html", {"form": form})
    return render(request, "posts/edit.html", {"form": form, "messages": messages})


@login_required
def categories(request):
    messages = get_messages(request)
    categories = reversed(Category.objects.all())
    return render(
        request,
        "posts/categories.html",
        {"categories": categories, "messages": messages},
    )


@login_required
def users(request):
    messages = get_messages(request)
    users = User.objects.all()
    return render(request, "users/index.html", {"users": users, "messages": messages})


@login_required
def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    form = UserForm(request.POST or None, instance=user)

    if request.method == "GET":
        return render(request, "users/edit.html", {"user": user, "form": form})

    else:
        if form.is_valid():
            form.save()
            messages.success(request, "L’utilisateur a été modifié avec succès !")
            return redirect("users")

    return render(request, "users/edit.html", {"user": user})
