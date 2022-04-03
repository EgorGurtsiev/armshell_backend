from .wot_api import RequestToAPI


class ClanInfo(RequestToAPI):
    def __init__(self, clan_id, access_token="", extra=[], fields=[], language='ru', members_key=None):
        super(ClanInfo, self).__init__(clan_id=clan_id, access_token=access_token, extra=extra,
                                       fields=fields, language=language, members_key=members_key)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/clans/info/")


class ClanList(RequestToAPI):
    def __init__(self, fields=[], language='ru', limit=100, page_no=1, search=''):
        super(ClanList, self).__init__(fields=fields, language=language, limit=limit, page_no=page_no, search=search)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/clans/list/")

    def get_full_response(self):
        return self._multiple_response_from_api(url="https://api.worldoftanks.ru/wot/clans/list/",
                                                iterator_field='page_no')


class AccountInfo(RequestToAPI):
    def __init__(self, account_id, fields=[], language='ru'):
        super(AccountInfo, self).__init__(account_id=account_id, fields=fields, language=language)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/clans/accountinfo/")
