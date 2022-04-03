from .wot_api import RequestToAPI


class AccountList(RequestToAPI):
    def __init__(self, search, fields=[], language='ru', limit=0, type_=""):
        super(AccountList, self).__init__(search=search, fields=fields, language=language, limit=limit, type=type_)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/account/list/")


class AccountInfo(RequestToAPI):
    def __init__(self, account_id, access_token=None, extra=[], fields=[], language='ru'):
        super(AccountInfo, self).__init__(account_id=account_id, access_token=access_token, extra=extra, fields=fields,
                                          language=language)

    def get_response(self):
        return self._multiple_request_to_api(url="https://api.worldoftanks.ru/wot/account/info/",
                                             multiple_field='account_id', limit=100)
