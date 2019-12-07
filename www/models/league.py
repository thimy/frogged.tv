from django.db import models
from .user import User
from django.utils import timezone


def time_delta(weeks):
    return timezone.now() + timezone.timedelta(weeks=weeks)


class Team(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=6, blank=True)
    status = models.BooleanField(default=True)
    captain = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    creation_date = models.DateTimeField(default=timezone.now)
    recruiting = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    steam_id = models.IntegerField(null=True)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=True)


class Season(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    starting_date = models.DateTimeField(default=timezone.now)
    ending_date = models.DateTimeField(default=time_delta(10))
    # logo = models.ImageField(upload_to="uploads/images/teams/" + name, null=True)
    victory_points = models.IntegerField(default=2)
    draw_points = models.IntegerField(default=1)
    loss_points = models.IntegerField(default=0)


class Division(models.Model):
    name = models.CharField(max_length=30)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, default=0)
    team = models.ManyToManyField(Team)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Week(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=time_delta(1))


class Match(models.Model):
    team_1 = models.ForeignKey(Team, related_name="team_1", on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, related_name="team_2", on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    play_date = models.DateTimeField(null=True)
    suggested_date_1 = models.DateTimeField(null=True)
    suggested_date_2 = models.DateTimeField(null=True)
    played = models.BooleanField(default=False)
    games = models.IntegerField(default=2)
    winner = models.ForeignKey(
        Team, related_name="winner", on_delete=models.CASCADE, null=True
    )


class Game(models.Model):
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)


class Standings(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.IntegerField(
        null=True, blank=True, default=1, verbose_name="Position"
    )
    matches = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="Matches"
    )
    win = models.IntegerField(null=True, blank=False, default=0, verbose_name="Won")
    draw = models.IntegerField(null=True, blank=False, default=0, verbose_name="Draw")
    lost = models.IntegerField(null=True, blank=False, default=0, verbose_name="Lost")
    points = models.IntegerField(
        null=True, blank=False, default=0, verbose_name="Points"
    )
