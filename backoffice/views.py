from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required

from www.models import User
from .forms import UserForm


@login_required
def dashboard(request):
    return render(request, "pages/index.html")


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
