from django.db import models


class Clan(models.Model):
    clan_name = models.CharField(verbose_name='Навание клана', max_length=256)
    clan_tag = models.CharField(verbose_name='Тэг клана', max_length=5, unique=True)
    clan_id = models.CharField(verbose_name='ID в БД wargaming', max_length=8, unique=True, primary_key=True)

    def __str__(self):
        return f'[{self.clan_tag}]'
