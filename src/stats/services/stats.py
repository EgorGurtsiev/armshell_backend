from django.conf import settings
import requests
from ..models import Tanks


def tank_name(tank_id):
    tank = Tanks.objects.get(id=tank_id)
    return tank.full_name


def tanks_stats(account_id, tank_id):
    """"Возвращает кол-во боев, % побед, ср. урон, ср. асист, ср. кол-во убийств в наступлениях."""

    def request_to_api():
        api_url = "https://api.worldoftanks.ru/wot/tanks/stats/"
        req_data = {
            "application_id": settings.APPLICATION_ID,
            "account_id": account_id,
            "tank_id": tank_id,
            "fields": "tank_id, stronghold_defense.battles, stronghold_defense.wins, stronghold_defense.frags, "
                      "stronghold_defense.damage_dealt"
        }
        res_json = requests.post(api_url, req_data).json()
        if res_json["status"] == "ok":
            if res_json["data"][str(account_id)] is None:
                return "Игрок не проводил боев в наступлениях"
            else:
                return res_json["data"][str(account_id)]
        else:
            return "Серверная ошибка"

    result = {}
    stats = request_to_api()
    if isinstance(stats, str):
        result['status'] = "error"
        result['error'] = stats
    else:
        result['status'] = "ок"
        result['data'] = []
        for item in stats:
            if item['stronghold_defense']['battles'] == 0:
                continue
            temp = dict.fromkeys(['tank_name', 'battles', 'pct_wins', 'avg_dmg', 'avg_asst'])
            temp['tank_name'] = tank_name(item['tank_id'])
            temp['battles'] = item['stronghold_defense']['battles']
            temp['pct_wins'] = '%.2f' % (item['stronghold_defense']['wins']/(item['stronghold_defense']['battles']/100))
            temp['avg_dmg'] = '%.0f' % (item['stronghold_defense']['damage_dealt']/item['stronghold_defense']['battles'])
            temp['avg_frags'] = '%.2f' % (item['stronghold_defense']['frags']/item['stronghold_defense']['battles'])

            result['data'].append(temp)
    return result


def account_search(nickname):
    api_url = "https://api.worldoftanks.ru/wot/account/list/"
    data = {
        "application_id": settings.APPLICATION_ID,
        "search": nickname,
        "limit": 1,
    }
    res_json = requests.post(api_url, data).json()
    if res_json['status'] == "ok":
        if res_json['meta']['count']:
            account_id = res_json["data"][0]["account_id"]
            return account_id
        else:
            return "Аккаунт не найден"
    else:
        return "Серверная ошабка"
