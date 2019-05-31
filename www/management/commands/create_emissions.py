from ...models import Emission, PatchVersion, VingtkmmrSubmission, TaymaputeSubmission
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests
import logging


def create_patches():
    PatchVersion.objects.update_or_create(
        "version_number": "7.22"
    )


def create_emissions():
    emissions = [
        {
            "id": 0,
            "title": "20k mmr sous les mers",
            "description": "Choisissez le prochain duo pour YouYou et v0ja !",
            "submission_type": "1",
        },
        {
            "id": 1,
            "title": "Taymapute",
            "description": "Créez des builds sur des héros que devra jouer YouYou dans son émission",
            "submission_type": "2",
        },
    ]
    print(emissions)
    for e in emissions:
        obj, created = Emission.objects.update_or_create(
            id=int(e["id"]),
            defaults={
                "title": e["title"],
                "description": e["description"],
                "submission_type": e["submission_type"],
            },
        )


class Command(BaseCommand):
    help = "Create emissions in base"

    def handle(self, *args, **kwargs):
        create_emissions()
