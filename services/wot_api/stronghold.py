from .wot_api import RequestToAPI


class ClanReserves(RequestToAPI):
    def __init__(self, access_token, fields='', language=''):
        super(ClanReserves, self).__init__(access_token=access_token, fields=fields, language=language)

    def get_response(self):
        return self.request_to_api(url="https://api.worldoftanks.ru/wot/stronghold/clanreserves/")


