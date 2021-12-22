import requests


class ClanReserves:
    def __init__(self, application_id, access_token, fields='', language='ru'):
        self.application_id = application_id
        self.access_token = access_token
        self.fields = fields
        self.language = language

    def get_dictionary_reserves(self):
        """Отдает python dict со всеми полями полученными от запроса в wg api"""
        api_url = "https://api.worldoftanks.ru/wot/stronghold/clanreserves/"
        data = {
            "application_id": self.application_id,
            "access_token": self.access_token,
            "language": self.language,
        }
        if self.fields == '':
            data["fields"] = 'disposable, name, type, in_stock.action_time, in_stock.activated_at, ' \
                             'in_stock.active_till, ' \
                             'in_stock.amount,	in_stock.level, in_stock.bonus_values.value'

        res_dict = requests.post(api_url, data).json()
        return res_dict

