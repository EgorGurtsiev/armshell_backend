from .wot_api import RequestToAPI


class ClanReserves(RequestToAPI):
    def __init__(self, access_token, fields='', language=''):
        super(ClanReserves, self).__init__(access_token=access_token, fields=fields, language=language)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/stronghold/clanreserves/")


class ActivateClanReserve(RequestToAPI):
    def __init__(self, access_token, reserve_level, reserve_type, fields='', language='ru'):
        super(ActivateClanReserve, self).__init__(access_token=access_token, reserve_level=reserve_level,
                                                  reserve_type=reserve_type, fields=fields, language=language)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/stronghold/activateclanreserve/")
