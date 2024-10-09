# core/models.py
from django.db import models
from django.contrib.auth.models import User

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is created
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # To store the user's IP address

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"
