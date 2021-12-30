from .wot_api import RequestToAPI


class AccountList(RequestToAPI):
    def __init__(self, search, fields=[], language='ru', limit=0, type_=""):
        super(AccountList, self).__init__(search=search, fields=fields, language=language, limit=limit, type=type_)

    def get_response(self):
        return self.request_to_api(url="https://api.worldoftanks.ru/wot/account/list/")
