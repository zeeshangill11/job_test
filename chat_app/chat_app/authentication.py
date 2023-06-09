from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            raise AuthenticationFailed('Token missing')

        try:
            username, token = token.split(':')
            user = User.objects.get(username=username)
            if user.auth_token.key != token:
                raise AuthenticationFailed('Invalid token')
        except (ValueError, User.DoesNotExist):
            raise AuthenticationFailed('Invalid token')

        return user, None