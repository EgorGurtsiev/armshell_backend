from services.wot_api.account import AccountList
from services.wot_api.tanks import TanksStats
from services.wot_api.encyclopedia import EncyclopediaVehicles
from services.wot_api.wot_api import ExceptionAPI


def tanks_stats(account_id, tank_id):
    """"Возвращает кол-во боев, % побед, ср. урон, ср. асист, ср. кол-во убийств в наступлениях."""
    fields = "tank_id, stronghold_defense.battles, stronghold_defense.wins, stronghold_defense.frags, " \
             "stronghold_defense.damage_dealt"
    res = TanksStats(account_id=account_id, tank_id=tank_id, fields=fields).get_response()
    if res['status'] == 'ok':
        if res["data"][str(account_id)] is None:
            return "Игрок не проводил боевв наступлениях"
    else:
        return "Серверная ошибка"

    result = {}
    stats = res['data'][str(account_id)]
    if isinstance(stats, str):
        result['status'] = "error"
        result['error'] = stats
    else:
        result['status'] = "ок"
        result['data'] = []
        for item in stats:
            if item['stronghold_defense']['battles'] == 0:
                continue
            temp = dict.fromkeys({'tank_name', 'battles', 'pct_wins', 'avg_dmg', 'avg_asst'})
            temp['tank_name'] = tank_name(item['tank_id'])
            temp['battles'] = item['stronghold_defense']['battles']
            temp['pct_wins'] = '%.2f' % (item['stronghold_defense']['wins']/(item['stronghold_defense']['battles']/100))
            temp['avg_dmg'] = '%.0f' % (item['stronghold_defense']['damage_dealt']/item['stronghold_defense']['battles'])
            temp['avg_frags'] = '%.2f' % (item['stronghold_defense']['frags']/item['stronghold_defense']['battles'])
            result['data'].append(temp)
    return result


def account_search(nickname):
    res = AccountList(search=nickname, limit=1,).get_response()
    if res['status'] == 'ok':
        if res['meta']['count']:
            account_id = res["data"][0]["account_id"]
            return account_id
        else:
            raise ExceptionAPI("Аккаунт не найден")
    else:
        raise ExceptionAPI("Серверная ошибка")


def tank_name(tank_id):
    tank = EncyclopediaVehicles(tank_id=tank_id, fields="tag").get_response()
    return tank['data'][str(tank_id)]['tag']
