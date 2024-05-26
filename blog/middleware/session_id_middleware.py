from django.http import HttpResponse
import uuid

class SessionIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Add a cookie to the response
        if 'session_id' not in request.COOKIES:
            response.set_cookie('session_id', uuid.uuid4())

        return response