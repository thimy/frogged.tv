from ...models import (
    Hero,
    Emission,
    PatchVersion,
    VingtkmmrSubmission,
    TaymaputeSubmission,
)
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
    vinkgtkmmrSubmissions = [
        {
            "id": 0,
            "title": "Poison",
            "patch_version": PatchVersion.objects.get(version_number="7.22"),
            "emission": Emission.objects.get(id=0),
            "hero_1": Hero.objects.get(name="npc_dota_hero_viper"),
            "hero_2": Hero.objects.get(name="npc_dota_hero_venomancer"),
        },
        {
            "id": 1,
            "title": "Birds",
            "patch_version": PatchVersion.objects.get(version_number="7.22"),
            "emission": Emission.objects.get(id=0),
            "hero_1": Hero.objects.get(name="npc_dota_hero_phoenix"),
            "hero_2": Hero.objects.get(name="npc_dota_hero_winter_wyvern"),
        },
        {
            "id": 2,
            "title": "Birds",
            "patch_version": PatchVersion.objects.get(version_number="7.22"),
            "emission": Emission.objects.get(id=0),
            "hero_1": Hero.objects.get(name="npc_dota_hero_phoenix"),
            "hero_2": Hero.objects.get(name="npc_dota_hero_winter_wyvern"),
        },
        {
            "id": 3,
            "title": "Love",
            "patch_version": PatchVersion.objects.get(version_number="7.22"),
            "emission": Emission.objects.get(id=0),
            "hero_1": Hero.objects.get(name="npc_dota_hero_vengefulspirit"),
            "hero_2": Hero.objects.get(name="npc_dota_hero_skywrath_mage"),
        },
        {
            "id": 4,
            "title": "Invisible",
            "patch_version": PatchVersion.objects.get(version_number="7.22"),
            "emission": Emission.objects.get(id=0),
            "hero_1": Hero.objects.get(name="npc_dota_hero_riki"),
            "hero_2": Hero.objects.get(name="npc_dota_hero_bounty_hunter"),
        },
        {
            "id": 5,
            "title": "Zap",
            "patch_version": PatchVersion.objects.get(version_number="7.22"),
            "emission": Emission.objects.get(id=0),
            "hero_1": Hero.objects.get(name="npc_dota_hero_lion"),
            "hero_2": Hero.objects.get(name="npc_dota_hero_lina"),
        },
    ]
    print(vinkgtkmmrSubmissions)
    for v in vinkgtkmmrSubmissions:
        obj, created = VingtkmmrSubmission.objects.update_or_create(
            id=int(v["id"]),
            defaults={
                "title": v["title"],
                "patch_version": v["patch_version"],
                "emission": v["emission"],
                "hero_1": v["hero_1"],
                "hero_2": v["hero_2"],
            },
        )


class Command(BaseCommand):
    help = "Create emissions in base"

    def handle(self, *args, **kwargs):
        create_emissions()
        create_submissions()
