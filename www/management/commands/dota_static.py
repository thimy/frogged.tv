from ...models import Hero, Item, PatchVersion
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests
import logging


def create_patches():
    PatchVersion.objects.update_or_create(id=0, defaults={"version_number": "7.22"})


def update_heroes():
    response = requests.get(
        "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1?key="
        + settings.STEAM_API_KEY
    )
    heroes = response.json()["result"]["heroes"]
    print(heroes)
    for h in heroes:
        obj, created = Hero.objects.update_or_create(
            id=int(h["id"]),
            defaults={
                "name": h["name"],
                "portrait": "http://cdn.dota2.com/apps/dota2/images/heroes/"
                + h["name"].replace("npc_dota_hero_", "")
                + "_sb.png",
                "portrait_lg": "http://cdn.dota2.com/apps/dota2/images/heroes/"
                + h["name"].replace("npc_dota_hero_", "")
                + "_lg.png",
                "portrait_full": "http://cdn.dota2.com/apps/dota2/images/heroes/"
                + h["name"].replace("npc_dota_hero_", "")
                + "_full.png",
                "portrait_vert": "http://cdn.dota2.com/apps/dota2/images/heroes/"
                + h["name"].replace("npc_dota_hero_", "")
                + "_vert.jpg",
            },
        )


def update_items():
    response = requests.get(
        "https://api.steampowered.com/IEconDOTA2_570/GetGameItems/V001/?key="
        + settings.STEAM_API_KEY
    )
    items = response.json()["result"]["items"]
    print(items)
    for i in items:
        obj, created = Item.objects.update_or_create(
            id=int(i["id"]),
            defaults={
                "name": i["name"],
                "cost": i["cost"],
                "secret_shop": i["secret_shop"],
                "recipe": i["recipe"],
                "image": "http://cdn.dota2.com/apps/dota2/images/items/"
                + i["name"].replace("item_", "")
                + "_lg.png",
            },
        )


class Command(BaseCommand):
    help = "Update heroes in database"

    def handle(self, *args, **kwargs):
        create_patches()
        update_heroes()
        update_items()
