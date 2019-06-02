from ...models import Emission, PatchVersion, VingtkmmrSubmission, TaymaputeSubmission
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests
import logging


def create_emissions():
    emissions = [
        {
            "id": 0,
            "title": "20k mmr sous les mers",
            "slug": "20kmmr",
            "description": "Choisissez le prochain duo pour YouYou et v0ja !",
            "cover": "",
        },
        {
            "id": 1,
            "title": "Taymapute",
            "slug": "taymapute",
            "description": "Créez des builds sur des héros que devra jouer YouYou dans son émission",
            "cover": "",
        },
    ]
    print(emissions)
    for e in emissions:
        obj, created = Emission.objects.update_or_create(
            id=int(e["id"]),
            defaults={"title": e["title"], "description": e["description"]},
        )


def create_submissions():
    submissions = [
        {
            "id": 0,
            "title": "Poison",
            "patch_version": "7.22",
            "emission": 0,
            "hero_1": "npc_dota_hero_viper",
            "hero_2": "npc_dota_hero_venomancer",
        }
    ]


class Command(BaseCommand):
    help = "Create emissions in base"

    def handle(self, *args, **kwargs):
        create_emissions()
