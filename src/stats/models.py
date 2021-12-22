from django.db import models


class Tanks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=10)
