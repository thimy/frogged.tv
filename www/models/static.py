from django.db import models


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
