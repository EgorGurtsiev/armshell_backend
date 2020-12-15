from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    access_token = models.CharField(max_length=40)
    expires_at = models.DateTimeField(blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', null=True, on_delete=models.SET_NULL)


class Stats(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    obj907 = models.IntegerField('Объект 907')
    Chieftain = models.IntegerField('T95/FV4201 Chieftain')
