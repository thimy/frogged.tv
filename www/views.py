import os
import json
import uuid
import logging

from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )[:5]
    return render(request, "pages/home.html", {"posts": posts})


def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    return render(request, "pages/posts.html", {"posts": posts})


def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "pages/post.html", {"post": post})
