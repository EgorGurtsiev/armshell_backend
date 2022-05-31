from services.wot_api.stronghold import ClanReserves


def get_dict_reserves(access_token):
    reserves = ClanReserves(access_token,
                            fields='disposable, name, type, in_stock.action_time, '
                                   'in_stock.activated_at, in_stock.active_till, in_stock.amount,	'
                                   'in_stock.level, in_stock.bonus_values.value, '
                                   'in_stock.bonus_values.battle_type, in_stock.x_level_only'
                            ).get_response()['data']
    return reserves


def formatting_for_issue(data):
    dict_img = {
        'ADDITIONAL_BRIEFING': "img/reserves/ADDITIONAL_BRIEFING.png",
        'BATTLE_PAYMENTS': "img/reserves/BATTLE_PAYMENTS.png",
        'MILITARY_MANEUVERS': "img/reserves/MILITARY_MANEUVERS.png",
        'TACTICAL_TRAINING': "img/reserves/TACTICAL_TRAINING.png",
    }
    for temp_type in data:
        if temp_type['disposable']:
            continue
        for img in dict_img.keys():
            if temp_type['type'] == img:
                temp_type['img'] = dict_img[img]
                break
        for temp_reserve in temp_type['in_stock']:
            action_time = temp_reserve['action_time']
            temp_reserve['action_time'] = int(action_time / 3600)
            for temp_bonus in temp_reserve['bonus_values']:
                temp_bonus['value'] = int(float(temp_bonus['value']) * 100)
    return data
