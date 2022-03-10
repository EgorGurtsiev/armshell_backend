from django.db import models
from src.player.models import Player


class Company(models.Model):
    tag = models.CharField('Тэг. Название роты', max_length=16, unique=True)
    description = models.CharField('Описание роты', max_length=256, null=True)
    captain = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='captain')


class Recruiter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    player = models.OneToOneField(Player, on_delete=models.CASCADE)


class Invitation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.SET_NULL, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
