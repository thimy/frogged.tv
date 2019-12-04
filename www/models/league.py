from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def season_average_duration():
    return timezone.now() + timezone.timedelta(weeks=10)


class Player(User):
    steam_id = models.IntegerField()


class Team(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=6, blank="TRUE")
    status = models.BooleanField(default="TRUE")
    captain = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=timezone.now)
    recruiting = models.BooleanField(default="FALSE")

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default="FALSE")
    starting_date = models.DateTimeField(default=timezone.now)
    ending_date = models.DateTimeField(default=season_average_duration)
    # logo = models.ImageField(upload_to="uploads/images/teams/" + name, null=True)
    victory_points = models.IntegerField(default=2)
    draw_points = models.IntegerField(default=1)
    loss_points = models.IntegerField(default=0)


class Division(models.Model):
    name = models.CharField(max_length=30)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, default=0)
    team = models.ManyToManyField(Team)


class Match(models.Model):
    team_1 = models.ForeignKey(Team, related_name="team_1", on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, related_name="team_2", on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    play_date = models.DateTimeField()
    suggested_date_1 = models.DateTimeField()
    suggested_date_2 = models.DateTimeField()


class Game(models.Model):
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
