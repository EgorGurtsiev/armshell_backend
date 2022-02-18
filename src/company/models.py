from django.db import models


class Company(models.Model):
    name = models.CharField('Наименование роты', max_length=16, unique=True)

