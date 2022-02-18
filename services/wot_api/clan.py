from .wot_api import RequestToAPI


class ClanInfo(RequestToAPI):
    def __init__(self, clan_id, access_token="", extra=[], fields=[], language='ru', members_key=None):
        super(ClanInfo, self).__init__(clan_id=clan_id, access_token=access_token, extra=extra,
                                       fields=fields, language=language, members_key=members_key)

    def get_response(self):
        return self.request_to_api(url="https://api.worldoftanks.ru/wot/clans/info/")
