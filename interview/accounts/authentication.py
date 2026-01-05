from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import Token

class SimpleTokenAuthentication(BaseAuthentication):
    keyword = 'Token'

    def authenticate(self, request):
        auth = request.headers.get('Authorization')
        if not auth:
            return None
        parts = auth.split()
        if len(parts) != 2 or parts[0] != self.keyword:
            return None
        key = parts[1]
        try:
            token = Token.objects.select_related('user').get(key=key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')
        return (token.user, token)
