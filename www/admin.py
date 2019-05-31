from django.contrib import admin
from django.db import models
from .models import (
    Post,
    Hero,
    Item,
    PatchVersion,
    Emission,
    VingtkmmrSubmission,
    TaymaputeSubmission,
)
from martor.widgets import AdminMartorWidget


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": AdminMartorWidget}}


admin.site.register(Post, PostAdmin)
admin.site.register(Hero)
admin.site.register(Item)
admin.site.register(PatchVersion)
admin.site.register(Emission)
admin.site.register(VingtkmmrSubmission)
admin.site.register(TaymaputeSubmission)
