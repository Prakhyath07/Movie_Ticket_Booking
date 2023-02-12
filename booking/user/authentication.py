from rest_framework.authentication import TokenAuthentication as BaseAuthentication

## to used keyword as Bearer instead of token
class TokenAuthentication(BaseAuthentication):
    keyword = "Bearer"