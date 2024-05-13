from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length = 15)
    team_id = models.IntegerField(default= 0)
    score = models.IntegerField()
    def __str__(self):
        return self.team_name

class Quset(models.Model):
    quest_name = models.CharField(max_length = 20)
    quset_id = models.IntegerField(default= 0)
    ans = models.CharField(default= '', max_length = 25)
    def __str__(self):
        return self.quest_name

class Rounds(models.Model):
    round_name = models.CharField(max_length = 20)
    round_id = models.IntegerField(default= 0)
    points = models.IntegerField()
    quests = models.ManyToManyField(Quset)
    def __str__(self):
        return self.round_name

