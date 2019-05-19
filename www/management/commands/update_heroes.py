from ...models import Hero
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests
import logging


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


class Command(BaseCommand):
    help = "Update heroes in database"

    def handle(self, *args, **kwargs):
        update_heroes()
