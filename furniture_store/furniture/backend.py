# backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import UserProfile

class PhoneAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # We treat the incoming 'username' as the phone number
            profile = UserProfile.objects.get(ph_no=username)
            user = profile.user
            
            # Check if the standard Django password matches
            if user.check_password(password):
                return user
        except UserProfile.DoesNotExist:
            return None