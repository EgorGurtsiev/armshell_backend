from config import settings
import requests


class RequestToAPI:
    def __init__(self, **kwargs):
        self.data = {'application_id': settings.APPLICATION_ID}
        for key, value in kwargs.items():
            if value:
                self.data[key] = value

    def request_to_api(self, url):
        res_dict = requests.post(url, self.data).json()
        return res_dict


class ExceptionAPI(Exception):
    """"Класс исключения при запросе к API"""
