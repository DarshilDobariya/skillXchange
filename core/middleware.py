# core/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class LogoutRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # If they are trying to access a page that requires login
            if request.path not in [reverse('login'), reverse('signup'), '/']:
                return redirect('home')  # Redirect to home if not logged in
        return self.get_response(request)
