from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    access_token = models.CharField(max_length=40)
    expires_at = models.DateTimeField(blank=True, null=True)
    account_id = models.CharField(max_length=8, null=True, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', null=True, on_delete=models.SET_NULL)


class Stats(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    tanks_in_garage = models.JSONField('Танки в ангаре', null=True)
    all_stats = models.JSONField('Вся статистика', null=True)
    # {
    #     tank_id{
    #         name,
    #         class, (artillery or carton or lightweight_wagon or heavy_station_wagon or)
    #         date{
    #
    #             random{
    #
    #
    #             }
    #
    #         }
    #     }
    # }
