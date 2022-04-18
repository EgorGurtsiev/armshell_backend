import time

from services.wot_api.account import AccountInfo
from services.wot_api.clan import ClanList, ClanInfo
from services.wot_api.tanks import TanksStats
from services.wot_api.wot_api import APISession


class SearchPlayerInClans:
    """
    Player_list = [
    {
        account_id = int
        clan_tag = str
        last_battle_time = int (unix time)
        battles_in_clan_wars = int
        stats = [
            {
                tank_id = int
                random = {
                    avg_damage = int
                    battles = int
                    percent_win = int
                }
                stronghold_skirmish = {...}
                stronghold_defense = {...}
                globalmap_absolute = {...}
            },
            ...
        ]
    },
    ...
    ]
    """
    def __init__(self, search,
                 count_players_in_clan=60,
                 last_battle=7,
                 avg_bamage=None,
                 battles_in_clan_wars=500):

        if not avg_bamage:
            avg_bamage = {'57937': 3400, '15617': 3000, '46849': 3500}
        tanks_list = avg_bamage.keys()

        self.clan_list = self._get_clan_list(search)
        self._clan_filter(count_players_in_clan)

        self.players_list = self._get_players_in_clans()

        self._get_last_battle_time_and_count_battles()
        self._last_battle_filter(last_battle)
        self._count_battles_filter(battles_in_clan_wars)

        self._get_detail_account_stats(tanks_list)
        self._stats_filter(avg_bamage)

    def _get_clan_list(self, search):
        fields = 'name, tag, members_count, clan_id'
        r = ClanList(search=search, fields=fields).get_full_response()
        r_clan_list = {'count': r['meta']['total'],
                       'data': r['data']}
        return r_clan_list

    def _clan_filter(self, count_players_in_clan):
        temp_clan_list_data = self.clan_list['data'][:]
        self.clan_list['data'] = []
        self.clan_list['count'] = 0
        for clan in temp_clan_list_data:
            if clan['members_count'] > count_players_in_clan:
                self.clan_list['data'].append(clan)
                self.clan_list['count'] += 1

    def _get_players_in_clans(self):
        clan_id_list = list(map(lambda clan: clan['clan_id'], self.clan_list['data']))
        i = 0
        players_list = []
        while i < len(clan_id_list):
            r = ClanInfo(clan_id=clan_id_list[i:i+100]).get_response()
            i += 100
            for clan_id, value in r['data'].items():
                for member in r['data'][clan_id]['members']:
                    player = {
                        'account_id': member['account_id'],
                        'role': member['role'],
                        'clan_tag': value['tag'],
                        'clan_id': value['clan_id']
                    }
                    players_list.append(player)
        return players_list

    def _get_last_battle_time_and_count_battles(self):
        account_id_list = list(map(lambda account: account['account_id'], self.players_list))
        extra = 'statistics.globalmap_absolute'
        fields = ['statistics.stronghold_skirmish.battles',
                  'statistics.stronghold_defense.battles',
                  'statistics.globalmap_absolute.battles',
                  'last_battle_time',
                  'nickname']
        r = AccountInfo(account_id=account_id_list, extra=extra, fields=fields).get_response()
        for player in self.players_list:
            player['last_battle_time'] = r['data'][str(player['account_id'])]['last_battle_time']
            player['battles_in_clan_wars'] = int(r['data'][str(player['account_id'])]['statistics']['stronghold_skirmish']['battles']) + \
                                             int(r['data'][str(player['account_id'])]['statistics']['stronghold_defense']['battles']) + \
                                             int(r['data'][str(player['account_id'])]['statistics']['globalmap_absolute']['battles'])
            player['nickname'] = r['data'][str(player['account_id'])]['nickname']

    def _last_battle_filter(self, day_delta):
        for player in self.players_list:
            if int(player['last_battle_time']) + day_delta * 86400 < int(time.time()):
                self.players_list.remove(player)

    def _count_battles_filter(self, battles):
        temp_player_list = self.players_list[:]
        self.players_list = []
        for player in temp_player_list:
            if player['battles_in_clan_wars'] >= battles:
                self.players_list.append(player)

    def _get_detail_account_stats(self, tank_id=["57937", "15617", "46849"]):
        fields = ['random', 'stronghold_defense', 'stronghold_skirmish', 'globalmap', 'tank_id']
        extra = 'random'
        session = APISession.session
        for player in self.players_list:
            r = TanksStats(account_id=player['account_id'], extra=extra, fields=fields, tank_id=tank_id)\
                .get_response(session)
            player['stats'] = []
            if r.get('error'):
                print(r['error']['message'])
            if r['data'][str(player['account_id'])]:
                for tank in r['data'][str(player['account_id'])]:
                    tank_stats = {'tank_id': tank['tank_id']}
                    if tank['random']['battles']:
                        tank_stats['random'] = {
                            'avg_damage': tank['random']['damage_dealt'] / tank['random']['battles'],
                            'battles': tank['random']['battles'],
                            'percent_win': tank['random']['wins'] / tank['random']['battles'] * 100,
                        }
                    if tank['stronghold_skirmish']['battles']:
                        tank_stats['stronghold_skirmish'] = {
                            'avg_damage': tank['stronghold_skirmish']['damage_dealt'] / tank['stronghold_skirmish']['battles'],
                            'battles': tank['stronghold_skirmish']['battles'],
                            'percent_win': tank['stronghold_skirmish']['wins'] / tank['stronghold_skirmish']['battles'] * 100,
                        }
                    if tank['stronghold_defense']['battles']:
                        tank_stats['stronghold_defense'] = {
                            'avg_damage': tank['stronghold_defense']['damage_dealt'] / tank['stronghold_defense']['battles'],
                            'battles': tank['stronghold_defense']['battles'],
                            'percent_win': tank['stronghold_defense']['wins'] / tank['stronghold_defense']['battles'] * 100,
                        },
                    if tank['globalmap']['battles']:
                        tank_stats['globalmap'] = {
                            'avg_damage': tank['globalmap']['damage_dealt'] / tank['globalmap']['battles'],
                            'battles': tank['globalmap']['battles'],
                            'percent_win': tank['globalmap']['wins'] / tank['globalmap']['battles'] * 100,
                        }
                    player['stats'].append(tank_stats)

    def _stats_filter(self, avg_bamage):
        temp_players_list = self.players_list
        self.players_list = []
        for player in temp_players_list:
            suit = False
            if player['stats']:
                for tank in player['stats']:
                    if tank.get('random'):
                        if tank['random']['avg_damage'] >= avg_bamage[str(tank['tank_id'])]:
                            suit = True
                            break
            if suit:
                self.players_list.append(player)

    def get_clan_list(self):
        return self.clan_list

    def get_players_list(self):
        return self.players_list
