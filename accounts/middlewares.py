from django.conf import settings
from django.shortcuts import redirect

class DevMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if request.path == '/accounts/locked':
            pass
        elif settings.DEBUG and not request.session.get('unlocked'):

            return redirect('locked')
        # Code to be executed for each request/response after
        # the view is called.

        return response