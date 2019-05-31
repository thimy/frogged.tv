import time

from django.conf import settings
from django.db import models
from django.utils import timezone
from martor.models import MartorField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = MartorField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=50, null=True)
    cover = models.ImageField(
        upload_to="uploads/images/{}".format(time.strftime("%Y/%m/%d/")), null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Hero(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    portrait = models.CharField(max_length=100)
    portrait_lg = models.CharField(max_length=100)
    portrait_full = models.CharField(max_length=100)
    portrait_vert = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    cost = models.IntegerField()
    secret_shop = models.BooleanField()
    recipe = models.BooleanField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name
