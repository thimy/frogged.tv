from django.db import models


class PatchVersion(models.Model):
    version_number = models.CharField(max_length=5)

    def __str__(self):
        return self.version_number
