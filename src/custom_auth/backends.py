import datetime

from django.contrib.auth.backends import BaseBackend

from services.wot_api.auth import AuthProlongate
from services.wot_api.clan import ClanInfo
from services.wot_api.account import AccountList, AccountInfo
from services.wot_api.wot_api import ExceptionAPI
from src.player.models import Player as User
from src.clan.models import Clan


class WGOpenIDBackend(BaseBackend):
    def authenticate(self, request, nickname=None, account_id=None, access_token=None):
        nickname = nickname or request.GET['nickname']
        account_id = account_id or request.GET['account_id']
        access_token = access_token or request.GET['access_token']

        try:
            temp = self._check_com_access_token_account_id(access_token, account_id)
            self._check_com_nickname_account_id(nickname, account_id)
        except ExceptionAPI:
            return None

        access_token = temp['access_token']
        expires_at = datetime.datetime.fromtimestamp(temp['expires_at']).strftime('%Y-%m-%d %H:%M:%S')

        try:
            user = User.objects.get(id=account_id)
            user.access_token = access_token
            user.expires_at = expires_at
        except User.DoesNotExist:
            user = User(
                username=nickname,
                id=account_id,
                access_token=access_token,
                expires_at=expires_at
            )

        user.clan = self._get_user_clan(user)
        user.save()
        return user

    def get_user(self, account_id):
        try:
            return User.objects.get(id=account_id)
        except User.DoesNotExist:
            return None

    def _check_com_access_token_account_id(self, access_token, account_id):
        res = AuthProlongate(access_token, expires_at=1209600).get_response()
        if res['status'] == 'ok':
            access_token = res['data']['access_token']
            expires_at = res['data']['expires_at']
            if str(res['data']['account_id']) == account_id:
                return {
                    'access_token': access_token,
                    'expires_at': expires_at,
                }
            else:
                print('Некорректный account_id')
                raise ExceptionAPI('Некорректный account_id')
        else:
            print('Некорректный access token')
            raise ExceptionAPI('Некорректный access token')

    def _check_com_nickname_account_id(self, nickname, account_id):
        res = AccountList(search=nickname).get_response()
        if res['status'] == 'ok':
            if res['data'][0]['nickname'] == nickname:
                if str(res['data'][0]['account_id']) == account_id:
                    return
                else:
                    raise ExceptionAPI(f'Найдено несоответствие: account id "{account_id}" не принадлежит "{nickname}"!')
            else:
                raise ExceptionAPI(f'Аккаунт "{nickname}" не найден!')
        else:
            raise ExceptionAPI('Серверная ошибка на стороне Wargaming!')

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

    def get_clan_id(self, account_id):
        res = AccountInfo(account_id=account_id).get_response()
        if res['status'] == 'ok':
            return res['data'][account_id]['clan_id']
        else:
            raise ExceptionAPI('Серверная ошибка на стороне Wargaming!')

    def _add_clan_to_db(self, clan_id):
        res = ClanInfo(clan_id=clan_id).get_response()
        if res['status'] == 'ok':
            clan = Clan(
                clan_id=clan_id,
                clan_tag=res['data'][clan_id]['tag'],
                clan_name=res['data'][clan_id]['name']
            )
            clan.save()
            return clan
        else:
            raise ExceptionAPI('Серверная ошибка на стороне Wargaming!')
