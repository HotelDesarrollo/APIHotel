from urllib.parse import parse_qs

from channels.auth import AuthMiddlewareStack
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from rest_framework_simplejwt.tokens import Token
# from rest_framework.authtoken.models import Token
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class WSTokenAuthMiddleware:
    """
    Token [Querystring/Header] authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        # Used for querystring token url auth
        query_string = parse_qs(scope['query_string'])
        headers = dict(scope['headers'])  # Used for headers token url auth
        # print('las cossas que llegan son: ', query_string)
        if b'token' in query_string:
            try:
                print('entro al inf/try1')
                token_key = query_string[b'token'][0].decode()
                print('values', token_key)
                data = {'token': token_key}
                valid_data = VerifyJSONWebTokenSerializer().validate(data)
                user = valid_data['user']
                scope['user'] = user
                close_old_connections()
            except:
                scope['user'] = AnonymousUser()
        elif b'authorization' in headers:
            try:
                print('entro al inf/try2')
                token_name, token_key = headers[b'authorization'].decode(
                ).split()
                print(token_name, token_key)
                if token_name == 'Token':
                    token = Token.objects.get(key=token_key)
                    scope['user'] = token.user
                    close_old_connections()
            except:
                scope['user'] = AnonymousUser()
        else:
            pass  # Session auth or anonymus

        return self.inner(scope)


def UniversalAuthMiddlewareStack(
    inner): return WSTokenAuthMiddleware(AuthMiddlewareStack(inner))
