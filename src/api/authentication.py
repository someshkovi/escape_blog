from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 


class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening