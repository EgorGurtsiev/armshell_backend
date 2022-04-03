from .wot_api import RequestToAPI


class AuthLogin(RequestToAPI):
    def __init__(self, redirect_uri, display="", expires_at=1209600, nofollow=1):
        super(AuthLogin, self).__init__(display=display, expires_at=expires_at, nofollow=nofollow,
                                        redirect_uri=redirect_uri)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/auth/login/")


class AuthProlongate(RequestToAPI):
    def __init__(self, access_token, expires_at=1209600):
        super(AuthProlongate, self).__init__(access_token=access_token, expires_at=expires_at)

    def get_response(self):
        return self._request_to_api(url="https://api.worldoftanks.ru/wot/auth/prolongate/")
