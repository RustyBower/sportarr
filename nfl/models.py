from django.db import models


class File(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.path


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    KIND_CHOICES = [
        ('HOF', 'Hall of Fame'),
        ('PRE', 'Preseason'),
        ('REG', 'Regular Season'),
        ('WC', 'Wild Card'),
        ('DIV', 'Divisional Playoff'),
        ('CON', 'Conference Championship'),
        ('SB', 'Super Bowl'),
    ]

    id = models.AutoField(primary_key=True)
    season = models.IntegerField()
    week = models.IntegerField()
    gametype = models.CharField(
        max_length=4,
        choices=KIND_CHOICES
    )
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home', blank=False, null=False)
    away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away', blank=False, null=False)
    date = models.DateTimeField('date')
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='file', blank=True, null=True)

    def __str__(self):
        return f'{self.away.name} @ {self.home.name}'
