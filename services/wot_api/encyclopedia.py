from .wot_api import RequestToAPI


class EncyclopediaVehicles(RequestToAPI):
    def __init__(self, fields="", language="", limit=0, nation="", page_no=1, tank_id="", tier="", type=""):
        super(EncyclopediaVehicles, self).__init__(fields=fields, language=language, limit=limit, nation=nation,
                                                   page_no=page_no, tank_id=tank_id, tier=tier, type=type)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/encyclopedia/vehicles/")
