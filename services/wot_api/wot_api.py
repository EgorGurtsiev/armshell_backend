from config import settings
import requests


class APISession:
    session = requests.Session()


class ExceptionAPI(Exception):
    """"Класс исключения при запросе к API"""


class RequestToAPI:
    def __init__(self, **kwargs):
        self.data = {'application_id': settings.APPLICATION_ID}
        for key, value in kwargs.items():
            self.data[key] = value

    def set_application_id(self, application_id):
        self.data['application_id'] = int(application_id)

    def get_application_id(self):
        return self.data['application_id']

    def _request_to_api(self, url, session=None):
        session = session if session else APISession.session
        data = {}
        for key, value in self.data.items():
            if isinstance(value, list):
                value = [str(i) for i in value]
                value = ", ".join(value)
            data[key] = value
        res_dict = session.post(url, data).json()
        return res_dict

    def _multiple_request_to_api(self, url, multiple_field, limit):
        if len(self.data[multiple_field]) <= limit:
            return self._request_to_api(url=url)
        else:
            r = requests.Session()
            res_dict = []
            multiple_field_data = self.data[multiple_field]
            for i in range(0, len(multiple_field_data), limit):
                sl = multiple_field_data[i:i+limit]
                self.data[multiple_field] = sl
                if res_dict:
                    temp = self._request_to_api(url, session=r)
                    res_dict['meta']['count'] += temp['meta']['count']
                    res_dict['data'] = {**res_dict['data'], **temp['data']}
                else:
                    res_dict = self._request_to_api(url, session=r)
            return res_dict

    def _multiple_response_from_api(self, url, iterator_field):
        session = APISession.session
        result = self._request_to_api(url=url, session=session)
        if result['meta']['count'] != result['meta']['total']:
            while result['meta']['count'] != result['meta']['total']:
                self.data[iterator_field] += 1
                res = self._request_to_api(url=url, session=session)
                result['data'] += res['data']
                result['meta']['count'] += res['meta']['count']
        return result
