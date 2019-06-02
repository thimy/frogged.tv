import os
import json
import uuid
import logging

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import (
    Post,
    Emission,
    EmissionSubmission,
    VingtkmmrSubmission,
    TaymaputeSubmission,
)

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from martor.utils import LazyEncoder


logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {"format": "%(name)-12s %(levelname)-8s %(message)s"},
            "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "console"},
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": "/tmp/debug.log",
            },
        },
        "loggers": {"": {"level": "DEBUG", "handlers": ["console", "file"]}},
    }
)

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
        else:
            form = SignUpForm(request.POST)
            logger.info("fail")
    else:
        form = SignUpForm()
    return render(request, "pages/signup.html", {"form": form})


@login_required
def logout_page(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required
def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    if request.method == "POST" and request.is_ajax():
        if "markdown-image-upload" in request.FILES:
            image = request.FILES["markdown-image-upload"]
            image_types = [
                "image/png",
                "image/jpg",
                "image/jpeg",
                "image/pjpeg",
                "image/gif",
            ]
            if image.content_type not in image_types:
                data = json.dumps(
                    {"status": 405, "error": _("Bad image format.")}, cls=LazyEncoder
                )
                return HttpResponse(data, content_type="application/json", status=405)

            print(settings)
            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps(
                    {
                        "status": 405,
                        "error": _("Maximum image file is %(size) MB.")
                        % {"size": to_MB},
                    },
                    cls=LazyEncoder,
                )
                return HttpResponse(data, content_type="application/json", status=405)

            img_uuid = "{0}-{1}".format(
                uuid.uuid4().hex[:10], image.name.replace(" ", "-")
            )
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL, def_path)

            data = json.dumps({"status": 200, "link": img_url, "name": image.name})
            return HttpResponse(data, content_type="application/json")
        return HttpResponse(_("Invalid request!"))
    return HttpResponse(_("Invalid request!"))


def home(request):
    user = request.user
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )[:5]
    return render(request, "pages/home.html", {"posts": posts, "user": user})


def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    return render(request, "pages/posts.html", {"posts": posts})


def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "pages/post.html", {"post": post})


def emissions(request):
    emissions = Emission.objects.all()
    return render(request, "pages/emissions.html", {"emissions": emissions})


def emission(request, pk):
    emission = Emission.objects.get(pk=pk)
    submissions = EmissionSubmission.objects.all()
    subpage = "pages/submissions.html"
    if emission.title == "20k mmr sous les mers":
        subpage = "partials/vingtkmmr.html"
        submissions = VingtkmmrSubmission.objects.all()
    return render(
        request,
        "pages/emission.html",
        {"emission": emission, "submissions": submissions, "subpage": subpage},
    )
