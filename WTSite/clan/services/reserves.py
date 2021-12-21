from .Stronghold import ClanReserves
from django.conf import settings


def get_dict_reserves(access_token):
    reserves = ClanReserves(settings.APPLICATION_ID, access_token)
    reserves = reserves.get_dictionary_reserves()['data']
    return reserves


def formatting_for_issue(data):
    for temp_type in data:
        dict_img = {
            'ADDITIONAL_BRIEFING': "https://ru-wotp.wgcdn.co/dcont/fb/image/military_maneuvers_(2)_KBiZ3DF.png",
            'BATTLE_PAYMENTS': "https://ru-wotp.wgcdn.co/dcont/fb/image/battle_payments_dn0kgqb.png",
            'MILITARY_MANEUVERS': "https://ru-wotp.wgcdn.co/dcont/fb/image/additional_briefing_(2)_EUordU9.png",
            'TACTICAL_TRAINING': "https://ru-wotp.wgcdn.co/dcont/fb/image/tactical_training_(2)_utNaHIo.png",
        }
        for img in dict_img.keys():
            if temp_type['type'] == img:
                temp_type['img'] = dict_img[img]
                break
        if temp_type['disposable']:
            continue
        for temp_reserve in temp_type['in_stock']:
            action_time = temp_reserve['action_time']
            temp_reserve['action_time'] = int(action_time / 3600)
            for temp_bonus in temp_reserve['bonus_values']:
                temp_bonus['value'] = int(float(temp_bonus['value']) * 100)
    return data
