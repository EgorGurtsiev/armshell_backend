from datetime import datetime

from django.utils import timezone
from django.urls import reverse
from django.db import models

from services.wot_api.clan import AccountInfo
from src.clan.models import Clan


class PlayerManager(models.Manager):
    def create_user(self, nickname, account_id, access_token, expires_at):
        user = self.model(
            nickname=nickname,
            id=account_id,
            access_token=access_token,
            expires_at=datetime.fromtimestamp(int(expires_at))
        )
        user.clan = self._get_user_clan(user)
        user.save(using=self._db)
        return user

    def _get_user_clan(self, user):
        clan_id = self.get_clan_id(str(user.id))
        if clan_id:
            try:
                clan = Clan.objects.get(clan_id=str(clan_id))
                return clan
            except Clan.DoesNotExist:
                clan = self._add_clan_to_db(clan_id=str(clan_id))
                return clan
        else:
            return None

class Player(models.Model):
    username = models.CharField(verbose_name='Имя в игре', max_length=25, unique=True)
    id = models.CharField(verbose_name='ID в БД wargaming', max_length=8, unique=True, primary_key=True)
    access_token = models.CharField(verbose_name='Токен доступа к данным игрока', max_length=40)
    expires_at = models.DateTimeField(verbose_name='Дата истечения токена')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'id', 'access_token', 'expires_at']

    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='player')
    clan = models.ForeignKey('clan.Clan', on_delete=models.SET_NULL, null=True, blank=True, related_name='player')
    objects = PlayerManager()

    date_joined = models.DateTimeField('date joined', default=timezone.now)
    last_login = models.DateTimeField('last login', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    @property
    def is_officer(self):
        rank_list = ['personnel_officer', 'combat_officer', 'executive_officer', 'commander']
        if AccountInfo(self.id, fields=['role']).get_response()['data'][self.id]['role'] in rank_list:
            return True
        else:
            return False

    @property
    def is_senior_officer(self):
        rank_list = ['executive_officer', 'commander']
        if AccountInfo(self.id, fields=['role']).get_response()['data'][self.id]['role'] in rank_list:
            return True
        else:
            return False

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    @property
    def is_staff(self):
        return False

    def has_perm(self, perm, obj=None):
        return False

    def has_module_perms(self, app_label):
        return False

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"

    def __str__(self):
        return f"{self.username}"

    def get_username(self):
        return getattr(self, self.USERNAME_FIELD)

    def get_full_name(self):
        full_name = '%s' % (self.username)
        return full_name.strip()

    def get_short_name(self):
        return self.username

    def get_absolute_url(self):
        return reverse('stats', args=str(self.username))
