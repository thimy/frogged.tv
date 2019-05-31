import time

from django.db import models
from .static import Hero, Item


class PatchVersion(models.Model):
    version_number = models.CharField(max_length=5)

    def __str__(self):
        return self.version_number


class EmissionSubmission(models.Model):
    title = models.CharField(max_length=60)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    done = models.BooleanField(default="FALSE")
    patch_version = models.ForeignKey(
        PatchVersion,
        on_delete=models.CASCADE,
        # default=PatchVersion.objects.latest("id"),
    )

    def __str__(self):
        return self.title


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
    item_1 = models.ForeignKey(Hero, related_name="item_1", on_delete=models.CASCADE)
    item_2 = models.ForeignKey(Hero, related_name="item_2", on_delete=models.CASCADE)
    item_3 = models.ForeignKey(Hero, related_name="item_3", on_delete=models.CASCADE)
    item_4 = models.ForeignKey(Hero, related_name="item_4", on_delete=models.CASCADE)
    item_5 = models.ForeignKey(Hero, related_name="item_5", on_delete=models.CASCADE)
    item_6 = models.ForeignKey(Hero, related_name="item_6", on_delete=models.CASCADE)


emissions = ((0, "standard"), (1, "20k mmr sous les mers"), (2, "Taymapute"))


class Emission(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    cover = models.ImageField(
        upload_to="uploads/images/{}".format(time.strftime("%Y/%m/%d/")), null=True
    )
    submission_type = models.CharField(max_length=2, choices=emissions, default="0")

    def __str__(self):
        return self.title
