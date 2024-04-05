from django.http import HttpResponseForbidden
import jwt

class VerifyToken:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the token from the request
        token = request.COOKIES.get('ene')

        # Validate the token
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

            # Add the user ID to the request for further processing
            request.userId = payload['id']
            print(request.userId)
        except jwt.ExpiredSignatureError:
            return HttpResponseForbidden('Token expired')
        except jwt.InvalidTokenError:
            return HttpResponseForbidden('Invalid token')

        return self.get_response(request)