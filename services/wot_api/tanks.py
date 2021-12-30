from .wot_api import RequestToAPI


class TanksStats(RequestToAPI):
    def __init__(self, account_id, access_token=None, extra=[], fields=[], in_garage=None, language='', tank_id=[]):
        super(TanksStats, self).__init__(account_id=account_id, access_token=access_token, fields=fields,
                                         language=language, extra=extra, tank_id=tank_id)
        if in_garage is not None:
            self.data['in_garage'] = in_garage

    def get_response(self):
        return self.request_to_api(url="https://api.worldoftanks.ru/wot/tanks/stats/")
