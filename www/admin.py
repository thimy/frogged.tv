from django.contrib import admin
from django.db import models
from .models import (
    User,
    Post,
    Hero,
    Item,
    PatchVersion,
    Emission,
    VingtkmmrSubmission,
    TaymaputeSubmission,
    Player,
    Team,
    Season,
    Division,
    Match,
    Game,
    Standings,
)
from martor.widgets import AdminMartorWidget


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": AdminMartorWidget}}


class EmissionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


#
# class VingtkmmrSubmissionAdmin(admin.ModelAdmin):
#     prepopulated_fields = {
#         "patch_version": PatchVersion.objects.latest("id").version_number
#     }


admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Hero)
admin.site.register(Item)
admin.site.register(PatchVersion)
admin.site.register(Emission, EmissionAdmin)
admin.site.register(VingtkmmrSubmission)
admin.site.register(TaymaputeSubmission)


admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Season)
admin.site.register(Division)
admin.site.register(Match)
admin.site.register(Game)
admin.site.register(Standings)
