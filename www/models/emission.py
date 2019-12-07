import time

from django.db import models
from .user import User
from .static import Hero, Item
from .patch import PatchVersion
from django.utils import timezone


class Emission(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    description = models.CharField(max_length=500)
    cover = models.ImageField(
        upload_to="uploads/images/{}".format(time.strftime("%Y/%m/%d/")), null=True
    )

    def __str__(self):
        return self.title


class EmissionSubmission(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=0, blank=False, null=True
    )
    title = models.CharField(max_length=60)
    done = models.BooleanField(default="FALSE")
    patch_version = models.ForeignKey(PatchVersion, on_delete=models.CASCADE)
    emission = models.ForeignKey(Emission, on_delete=models.CASCADE, default=0)
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    upvotes = models.ManyToManyField(User, related_name="user_up+")
    downvotes = models.ManyToManyField(User, related_name="user_down+")

    def __str__(self):
        return self.title

    def vote(self, type, user):
        print(self.upvotes.all())
        print(type)
        if type == "UP":
            if user in self.upvotes.all():
                self.upvotes.remove(user)
            else:
                if user in self.downvotes.all():
                    self.downvotes.remove(user)
                self.upvotes.add(user)
        elif type == "DOWN":
            if user in self.downvotes.all():
                self.downvotes.remove(user)
            else:
                if user in self.upvotes.all():
                    self.upvotes.remove(user)
                self.downvotes.add(user)
        else:
            print("Cannot apply vote")
        return self.get_score()

    def get_score(self):
        up = self.upvotes.count() or 0
        down = self.downvotes.count() or 0
        return up - down


class VingtkmmrSubmission(EmissionSubmission):
    hero_1 = models.ForeignKey(Hero, related_name="hero_1", on_delete=models.CASCADE)
    hero_2 = models.ForeignKey(Hero, related_name="hero_2", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.hero_1 == self.hero_2:
            raise Exception(
                "Le premier héros ne peut pas être similaire au deuxième héros"
            )
        super(VingtkmmrSubmission, self).save(*args, **kwargs)


class TaymaputeSubmission(EmissionSubmission):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    item_1 = models.ForeignKey(Item, related_name="item_1", on_delete=models.CASCADE)
    item_2 = models.ForeignKey(Item, related_name="item_2", on_delete=models.CASCADE)
    item_3 = models.ForeignKey(Item, related_name="item_3", on_delete=models.CASCADE)
    item_4 = models.ForeignKey(Item, related_name="item_4", on_delete=models.CASCADE)
    item_5 = models.ForeignKey(Item, related_name="item_5", on_delete=models.CASCADE)
    item_6 = models.ForeignKey(Item, related_name="item_6", on_delete=models.CASCADE)
