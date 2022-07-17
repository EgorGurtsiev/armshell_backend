from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomAuthentication(JWTAuthentication):
    def __init__(self, *args, **kwargs):
        super(JWTAuthentication, self).__init__(*args, **kwargs)
